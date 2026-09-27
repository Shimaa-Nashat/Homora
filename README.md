# Homora

Homora is a responsive furniture storefront built with Flask, SQLite, Jinja and plain CSS. Browse room collections, create an account, save pieces to a session-based bag, and send the team a message.

## Run locally

1. Install Python 3.9 or later.
2. Create and activate a virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Start the app with `python app.py`.
5. Visit `http://127.0.0.1:8080`.

The included `database.db` contains the product catalogue. If it is missing, the app creates an empty SQLite database and the required tables on startup. Set `HOMORA_DATABASE` to use a different database file and set `SECRET_KEY` to a private random value when deploying. The built-in contact form currently displays a confirmation; connect it to an email or support service to deliver messages.

## Project structure

```text
app.py                 Flask routes and SQLite access
database.db            Product catalogue and user accounts
templates/             Shared layout and page templates
static/style.css       Responsive storefront styling
static/site.js         Mobile navigation and notices
static/*_photos/       Furniture and home photography
```

## Features

- Five room collections with product imagery and pricing
- Responsive navigation and product layouts
- Account registration with hashed passwords
- Session-based shopping bag
- Contact form validation and confirmation
- SQLite database path configurable through the environment

Checkout and message delivery are not connected to payment or email providers yet.
