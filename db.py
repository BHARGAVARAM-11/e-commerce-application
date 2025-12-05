import sqlite3

conn = sqlite3.connect("products.db")
c = conn.cursor()

c.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    image TEXT
)
""")

products = [
    ("Laptop", 50000, ""),
    ("Mobile", 20000, ""),
    ("Headphones", 2500, ""),
    ("Keyboard", 1500, "")
]

c.executemany("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", products)

conn.commit()
conn.close()

print("Database created successfully!")

