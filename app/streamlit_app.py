import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pickle
from src.recommend import recommend

popular_books = pickle.load(open("models/popular_books.pkl","rb"))
pt = pickle.load(open("models/pivot.pkl","rb"))

st.title("Book Recommendation System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Popular Books","Book Recommendation"]
)

if menu == "Popular Books":

    st.header("Top 50 Popular Books")

    for i in range(50):

        st.write(popular_books.iloc[i]["title"])
        st.write(popular_books.iloc[i]["author"])
        st.write(popular_books.iloc[i]["avg_rating"])
        st.write("---")


elif menu == "Book Recommendation":

    book_list = pt.index.values

    selected_book = st.selectbox(
        "Select a book",
        book_list
    )

    if st.button("Recommend"):

        recommendations = recommend(selected_book)

        for book in recommendations:
            st.write(book[0])
            st.write(book[1])
            st.write("---")