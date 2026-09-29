import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
)
""")

books = [
    (1, "Data Science Basics", "Technology", 1450, 10),
    (2, "Clean Code", "Technology", 1200, 8),
    (3, "The Silent Patient", "Fiction", 1350, 2),
    (4, "Python Programming", "Technology", 950, 6),
    (5, "The Alchemist", "Fiction", 800, 4),
    (6, "Atomic Habits", "Self-Help", 1100, 7),
    (7, "Harry Potter", "Fiction", 1050, 3),
    (8, "Database Systems", "Technology", 1250, 9)
]

cursor.executemany(
    "INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?, ?)",
    books
)

conn.commit()

print("Part A - Books above Rs.1000 (sorted):")

cursor.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC
""")

for row in cursor.fetchall():
    print(row)

print("\nPart B - Books with renamed title:")

cursor.execute("""
SELECT title AS book_title, price
FROM books
""")

for row in cursor.fetchall():
    print(row)

print("\nPart C - Low-stock Fiction books:")

cursor.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5
""")

for row in cursor.fetchall():
    print(row)

conn.close()