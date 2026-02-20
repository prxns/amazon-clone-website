import sqlite3

conn = sqlite3.connect("amazon_clone.db")
cursor = conn.cursor()

# Drop old table (optional reset)
cursor.execute("DROP TABLE IF EXISTS products")

# Create table
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    image TEXT,
    category TEXT
)
""")

# ELECTRONICS
electronics = [
("iPhone 15 Pro", 134900, "electronics/iphone.jpg", "electronics"),
("Samsung Galaxy S24 Ultra", 129999, "electronics/s24.jpg", "electronics"),
("OnePlus 12", 64999, "electronics/1+.jpg", "electronics"),
("Realme GT 6", 36999, "electronics/realme.jpg", "electronics"),
]

# GAMING
gaming = [
("PlayStation 5", 54990, "gaming/ps5.jpg", "gaming"),
("Xbox Series X", 52999, "gaming/xbox.jpg", "gaming"),
("Gaming PC RTX 4070", 145000, "gaming/pc.jpg", "gaming"),
("Logitech G502 Mouse", 4995, "gaming/logitech.jpg", "gaming"),
]

# CLOTHES
clothes = [
("Nike T-Shirt", 4499, "dress/nike.jpg", "clothes"),
("Adidas Hoodie", 12999, "dress/adidas.jpg", "clothes"),
("Puma Track Pants", 3499, "dress/puma.jpg", "clothes"),
("Zara Jacket", 9999, "dress/zara.jpg", "clothes"),
]

# BIKES
bikes = [
("KTM Duke 390", 310000, "bikes/390.jpg", "bikes"),
("Yamaha R15 V4", 182000, "bikes/r15.jpg", "bikes"),
("Honda CB350", 210000, "bikes/cb350.jpg", "bikes"),
("BMW G310R", 290000, "bikes/g310.jpg", "bikes"),
]

# LAPTOPS
laptops = [
("MacBook Air M2", 114900, "laptops/mac.jpg", "laptop"),
("HP Omen Gaming Laptop", 135000, "laptops/hp.jpg", "laptop"),
("Lenovo Legion 5", 120000, "laptops/legion.jpg", "laptop"),
("ASUS ROG Strix G16", 145000, "laptops/rog.jpg", "laptop"),
]

# BEAUTY
beauty = [
("Minimalist Vitamin C Serum", 699, "beauty/1.jpg", "beauty"),
("Lakme Foundation", 499, "beauty/2.jpg", "beauty"),
("Mamaearth Face Wash", 299, "beauty/3.jpg", "beauty"),
("Neutrogena Sunscreen", 599, "beauty/4.jpg", "beauty"),
]

# FURNITURE
furniture = [
("Office Chair", 5999, "furniture/chair.jpg", "furniture"),
("Study Table", 17999, "furniture/table.jpg", "furniture"),
("Queen Size Bed", 18999, "furniture/bed.jpg", "furniture"),
("Wooden Wardrobe", 25999, "furniture/wardrobe.jpg", "furniture"),
]

# Insert all
all_products = electronics + gaming + clothes + bikes + laptops + beauty + furniture

cursor.executemany(
    "INSERT INTO products (name, price, image, category) VALUES (?, ?, ?, ?)",
    all_products
)

conn.commit()
conn.close()

print("Database created with 28 products.")