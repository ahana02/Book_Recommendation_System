# 📚 Book Recommendation System

A machine learning project that builds a **Book Recommendation System** using:

- Popularity-Based Filtering
- Collaborative Filtering (Item-Based)
- Streamlit Web App

---

## 🚀 Project Overview

This project recommends books to users based on:

1. **Popularity-Based Recommendation**
   - Top-rated books (minimum 200 ratings)
   - Same recommendations for all users

2. **Collaborative Filtering**
   - Item-based similarity using cosine similarity
   - Personalized recommendations based on user behavior

---

## 📂 Dataset

Dataset used:

👉 Books Dataset from Kaggle  
https://www.kaggle.com/datasets/saurabhbagchi/books-dataset

### Data Files

- **Books.csv**
  - ISBN, Title, Author, Year, Publisher, Image URLs

- **Users.csv**
  - User-ID, Location, Age

- **Ratings.csv**
  - User-ID, ISBN, Book-Rating

---


## 📁 Project Structure

```
book-recommendation-system
│
├── data
│ ├── raw
│ └── processed
│
├── models
│ ├── similarity.pkl
│ ├── pivot.pkl
│ └── popular_books.pkl
│
├── notebooks
│ └── eda.ipynb
│
├── src
│ ├── download_data.py
│ ├── data_preprocessing.py
│ ├── popularity_model.py
│ ├── collaborative_filtering.py
│ └── recommend.py
│
├── app
│ └── streamlit_app.py
│
├── requirements.txt
└── README.md
```


---

## ▶️ How to Run

### 1. Install Dependencies
```
pip install -r requirements.txt
``

---

### 2. Download Dataset
```
python src/download_data.py
``


---

### 3. Run Pipeline
```
python src/data_preprocessing.py
python src/popularity_model.py
python src/collaborative_filtering.py
```

---

### 4. Run Streamlit App
```
streamlit run app/streamlit_app.py
```