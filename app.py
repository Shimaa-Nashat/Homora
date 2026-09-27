"""Homora furniture storefront."""

import os
import sqlite3
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = Path(__file__).resolve().parent
DATABASE = Path(os.environ.get("HOMORA_DATABASE", BASE_DIR / "database.db"))
CATEGORIES = {
    "bedroom": ("Bedrooms", "bed", "bedroom_photos", "Thoughtful pieces for a slower, softer start and end to every day."),
    "living": ("Living rooms", "living", "living_photos", "Comfortable, considered pieces made for gathering."),
    "kitchen": ("Kitchens", "kitchen", "kitchen_photos", "Bring warmth and function to the heart of your home."),
    "dressing": ("Dressing rooms", "dressing", "dressing_photos", "A little more order, with a lot more style."),
    "office": ("Home offices", "office", "office_photos", "Create a calm, focused space for your best work."),
}

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "homora-local-development-key")
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            image TEXT,
            category TEXT NOT NULL,
            folder TEXT
        )""")


def normalize_product(row):
    product = dict(row)
    category = product.get("category", "")
    product["folder"] = product.get("folder") or CATEGORIES.get(
        category, (None, None, "Home_photos", None)
    )[2]
    return product


init_db()


@app.context_processor
def shared_template_data():
    cart = session.get("cart", [])
    endpoints = {value[1]: key for key, value in CATEGORIES.items()}
    return {"username": session.get("username"), "cart_count": len(cart), "category_endpoints": endpoints}


@app.route("/")
def index():
    featured = []
    with get_db() as connection:
        featured = [normalize_product(row) for row in connection.execute(
            "SELECT * FROM products ORDER BY id LIMIT 4"
        ).fetchall()]
    return render_template("index.html", categories=CATEGORIES, featured=featured)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with get_db() as connection:
            user = connection.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password"], password):
            session["username"] = user["username"]
            flash("Welcome back.", "success")
            return redirect(url_for("index"))
        flash("That username and password do not match.", "error")
    return render_template("login.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("index"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")
        if not username or not email or not password:
            flash("Please complete every field.", "error")
        elif len(password) < 8:
            flash("Choose a password with at least 8 characters.", "error")
        elif password != confirm:
            flash("Your passwords do not match.", "error")
        else:
            try:
                with get_db() as connection:
                    connection.execute(
                        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                        (username, email, generate_password_hash(password)),
                    )
                session["username"] = username
                flash("Your account is ready. Welcome to Homora.", "success")
                return redirect(url_for("index"))
            except sqlite3.IntegrityError:
                flash("That username or email is already registered.", "error")
    return render_template("signup.html")


def catalog_page(page):
    title, category, folder, description = CATEGORIES[page]
    with get_db() as connection:
        products = [normalize_product(row) for row in connection.execute(
            "SELECT * FROM products WHERE category = ? ORDER BY id", (category,)
        ).fetchall()]
    return render_template(
        "catalog.html", title=title, category=page, description=description,
        products=products, folder=folder,
    )


for page in CATEGORIES:
    app.add_url_rule(f"/{page}", page, lambda page=page: catalog_page(page))


@app.route("/cart")
def cart():
    ids = session.get("cart", [])
    products = {}
    if ids:
        placeholders = ",".join("?" for _ in set(ids))
        with get_db() as connection:
            rows = connection.execute(f"SELECT * FROM products WHERE id IN ({placeholders})", tuple(set(ids))).fetchall()
            products = {row["id"]: dict(row) for row in rows}
    items = []
    total = 0
    for product_id in ids:
        product = products.get(product_id)
        if product:
            product["folder"] = product.get("folder") or CATEGORIES.get(product["category"], (None, None, "Home_photos"))[2]
            items.append(product)
            total += product["price"]
    return render_template("cart.html", cart_items=items, total=total)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    if "username" not in session:
        flash("Sign in to add items to your cart.", "error")
        return redirect(url_for("login"))
    try:
        product_id = int(request.form.get("item_id", ""))
    except ValueError:
        flash("We could not find that product.", "error")
        return redirect(request.referrer or url_for("index"))
    with get_db() as connection:
        exists = connection.execute("SELECT id FROM products WHERE id = ?", (product_id,)).fetchone()
    if not exists:
        flash("We could not find that product.", "error")
    else:
        cart = session.get("cart", [])
        cart.append(product_id)
        session["cart"] = cart
        flash("Added to your cart.", "success")
    return redirect(request.referrer or url_for("cart"))


@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    try:
        product_id = int(request.form.get("item_id", ""))
        cart = session.get("cart", [])
        cart.remove(product_id)
        session["cart"] = cart
        flash("Item removed from your cart.", "success")
    except (ValueError, AttributeError):
        flash("That item was not in your cart.", "error")
    return redirect(url_for("cart"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        fields = [request.form.get(key, "").strip() for key in ("name", "number", "email", "message")]
        if not all(fields):
            flash("Please complete every field before sending.", "error")
        else:
            flash("Thanks for reaching out. We will be in touch soon.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=False)
