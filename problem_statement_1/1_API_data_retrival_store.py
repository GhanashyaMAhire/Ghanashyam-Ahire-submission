#importing requirements
import requests
import sqlite3

# book information api (dummy api created by me with flask and json).
"""GitHub Repository Link: https://github.com/GhanashyaMAhire/Book_api """
API_URL = "https://book-api-frdn.onrender.com/books"

def fetch_book_data():
    response = requests.get(API_URL)
    return response.json()


DB_NAME = 'books.db'

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            title TEXT,
            author TEXT,
            year INTEGER)
        ''')
    
    conn.commit()
    conn.close()

def store_book_data(books):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for book in books:
        cursor.execute('''
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
        ''', (book['title'], book['author'], book['year']))

    conn.commit()
    conn.close()

def display_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, year FROM books")
    rows = cursor.fetchall()

    for title, author, year in rows:
        print(f"{title} by {author} ({year})")

    conn.close()

def main():
    create_database()
    books = fetch_book_data()
    store_book_data(books)
    display_books()

if __name__ == "__main__":
    main()
