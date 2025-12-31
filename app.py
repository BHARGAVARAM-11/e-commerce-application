from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mysecretkey"   # Required for session

# Product List with working image URLs
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80"
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 20000,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=400&q=80"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2500,
        "image": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=400&q=80"
    },
    {
        "id": 4,
        "name": "Keyboard",
        "price": 1500,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80"
    }
]

# Home page
@app.route("/")
def index():
    return render_template("index.html", products=products)

# Add to cart
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True

    return redirect(url_for("cart"))

# View cart
@app.route("/cart")
def cart():
    cart_items = []
    total = 0

    if "cart" in session:
        for item_id in session["cart"]:
            product = next((p for p in products if p["id"] == item_id), None)
            if product:
                cart_items.append(product)
                total += product["price"]

    return render_template("cart.html", cart_items=cart_items, total=total)


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


