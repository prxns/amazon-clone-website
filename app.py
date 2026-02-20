from flask import Flask, render_template, send_from_directory, jsonify
import sqlite3

app = Flask(__name__)

# function to connect database
def get_db_connection():
    conn = sqlite3.connect("amazon_clone.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

@app.route("/category/<category>")
def category_page(category):

    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products WHERE category = ?",
        (category,)
    ).fetchall()

    conn.close()

    return render_template(
        "category.html",
        products=products,
        category_name=category.capitalize()
    )

@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory("images", filename)

# route to get products from database
@app.route("/products")
def get_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    # convert to list of dictionaries
    product_list = [dict(product) for product in products]

    return jsonify(product_list)

if __name__ == "__main__":
    app.run(debug=True)