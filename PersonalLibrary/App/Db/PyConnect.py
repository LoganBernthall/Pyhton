import sqlite3
import streamlit as st

@st.cache_resource
def get_connection():
    return sqlite3.connect("Books.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        genre TEXT,
        year INTEGER,
        status TEXT
    )
    """)

    conn.commit()

def add_book(title, author, genre, year, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, genre, year, status) VALUES (?, ?, ?, ?, ?)",
        (title, author, genre, year, status)
    )
    conn.commit()

def get_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()