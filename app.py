from flask import Flask, redirect, render_template, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from cs50 import SQL

app = Flask(__name__)
app.secret_key = "your-secret-key"
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)

# ================== Database ==================
db = SQL("sqlite:///database.db")

db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")

db.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        image TEXT,
        category TEXT NOT NULL
    )
""")

# ================== Routes ==================


@app.route("/")
def index():
    return render_template("index.html", username=session.get("username"))

# ---------- Auth ----------


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("login.html", message="Please fill all fields.")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) == 1 and check_password_hash(rows[0]["password"], password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", message="Invalid username or password.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not username or not email or not password or not confirm_password:
            return render_template("signup.html", message="All fields are required.")
        if password != confirm_password:
            return render_template("signup.html", message="Passwords do not match.")

        hashed_password = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                       username, email, hashed_password)
        except Exception as e:
            print(e)  # Debugging purpose
            return render_template("signup.html", message="Username or email already exists.")

        session["username"] = username
        return redirect("/")
    return render_template("signup.html")

# ---------- Product Pages ----------


@app.route("/bedroom")
def bedroom():
    items = db.execute("SELECT * FROM products WHERE category = ?", "bed")
    return render_template("bedroom.html", items=items)


@app.route("/living")
def living():
    items = db.execute("SELECT * FROM products WHERE category = ?", "living")
    return render_template("living.html", items=items)


@app.route("/kitchen")
def kitchen():
    items = db.execute("SELECT * FROM products WHERE category = ?", "kitchen")
    return render_template("kitchen.html", items=items)


@app.route("/dressing")
def dressing():
    items = db.execute("SELECT * FROM products WHERE category = ?", "dressing")
    return render_template("dressing.html", items=items)


@app.route("/office")
def office():
    items = db.execute("SELECT * FROM products WHERE category = ?", "office")
    return render_template("office.html", items=items)

# ---------- Cart ----------


@app.route("/cart")
def cart():
    cart_items = []
    total = 0

    if "cart" in session:
        for item_id in session["cart"]:
            item = db.execute("SELECT * FROM products WHERE id = ?", item_id)
            if item:
                cart_items.append(item[0])
                total += item[0]["price"]

    return render_template("cart.html", cart_items=cart_items, total=total)


@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    item_id = request.form.get("item_id")

    if "cart" in session and item_id:
        session["cart"] = [i for i in session["cart"] if str(i) != str(item_id)]
        session.modified = True

    return redirect("/cart")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    if "username" not in session:
        return redirect("/login")

    try:
        item_id = int(request.form.get("item_id"))
    except (ValueError, TypeError):
        flash("Invalid item.")
        return redirect(request.referrer or "/bedroom")

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(item_id)
    session.modified = True

    return redirect(request.referrer or "/bedroom")

# ---------- Contact ----------


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not number or not email or not message:
            flash("Please fill in all fields.")
            return redirect("/contact")

        flash("Your message has been sent successfully!")
        return redirect("/contact")

    return render_template("contact.html")
