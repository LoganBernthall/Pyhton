import streamlit as st

from Db.PyConnect import init_db, add_book, get_books, delete_book

init_db()

#Titles
st.title("Welcome To Your Personal Library")
st.caption("Welcome, make this place your personal library!")

# Add book form
with st.form("add_book"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Year", min_value=0, step=1)
    status = st.selectbox("Status", ["Unread", "Reading", "Finished"])

    submitted = st.form_submit_button("Add Book")

    if submitted:
        add_book(title, author, genre, year, status)
        st.success("Book added!")

# Display books
books = get_books()

for book in books:
    st.write(book)
    if st.button(f"Delete {book[0]}"):
        delete_book(book[0])
        st.rerun()