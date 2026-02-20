import sqlite3

# Connect to database
conn = sqlite3.connect("amazon_clone.db")

cursor = conn.cursor()

# create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT NOT NULL,
    description TEXT
)
""")

# Insert products
cursor.execute("""
INSERT INTO products (name, price, image, description)
VALUES 
('Gaming PC', 59999, 'pc game.jpg', 'Gaming computer'),
('Electronics', 2999, 'box4_image.jpg', 'Electronic gadgets'),
('Furniture', 8999, 'box3_image.jpg', 'Furniture')
""")

conn.commit()
conn.close()

print("Database created successfully")