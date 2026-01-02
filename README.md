***My E-Commerce Store***

A simple e-commerce web application built with Flask, featuring product listing, image display, and a shopping cart.

Products use Unsplash image URLs, so no local images are needed. The cart functionality uses Flask sessions (no database required).

**Features**

- Display products with images, names, and prices

- Add products to cart

- View cart with items and total price

- Responsive UI using Bootstrap 5

- Lightweight and easy to extend

**Project Structure**
```
myecommerce-app/
├── app.py              # Main Flask application
├── db.py               # Optional database file (not required for cart)
├── products.db         # Optional database
├── templates/
│   ├── index.html      # Home page showing products
│   ├── cart.html       # Cart page showing selected items
│   └── checkout.html   # Checkout page (optional)
├── venv/               # Python virtual environment
└── README.md           # This file
```
**Setup Instructions**
**1. Clone the repository **
```
git clone <your-repo-url>
cd myecommerce-app
```
**2. Create and activate virtual environment**
```
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

**3. Install dependencies**
```
pip install flask
```
Flask is the only required dependency for this project.

**4. Run the application**
```
python app.py
```
You should see output like:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
**5. Open the application**
```
http://localhost:portnumber 0000/
```
- Browse products
- Add items to the cart
- Click “View Cart” to see selected items

**Notes**
- Product images are loaded via external URLs from Unsplash.
- Cart functionality uses Flask sessions, so cart data persists per browser session.
- To add more products, edit the products list in app.py.

## Architecture

```mermaid
flowchart TB
    U[End User<br/>(Browser)]
    F[Flask Web Server<br/>(app.py / routes & views)<br/><br/>• Product Listing<br/>• Cart Actions<br/>• Checkout Views]
    A[Application Logic Layer<br/>(Flask Business Logic)<br/><br/>• Add to Cart<br/>• Session Handling<br/>• Redirect / Render HTML]
    D[Data Layer<br/>(SQLite - products.db)<br/><br/>• Product Info<br/>• Cart via Sessions]
    I[Deployment / Infrastructure<br/><br/>• Dockerfile<br/>• docker-compose<br/>• GitHub Actions CI/CD<br/>• Docker Hub Registry]

    U -->|HTTP Requests| F
    F -->|Route Handling| A
    A -->|Read / Write| D
    D -->|Data Response| A
    A -->|HTML Response| F
    F -->|HTTP Response| U
    F --> I
```


