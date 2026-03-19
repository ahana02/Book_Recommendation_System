import pandas as pd
import pickle

def build_popularity_model():

    books = pd.read_csv(
        "data/processed/books_cleaned.csv",
        low_memory=False
    )

    ratings = pd.read_csv("data/processed/ratings_cleaned.csv")

    # ensure rating is numeric
    ratings["rating"] = pd.to_numeric(ratings["rating"], errors="coerce")
    ratings = ratings.dropna(subset=["rating"])

    merged = ratings.merge(books, on="ISBN")

    rating_count = merged.groupby("title")["rating"].count().reset_index()
    rating_count.rename(columns={"rating": "num_ratings"}, inplace=True)

    rating_avg = merged.groupby("title")["rating"].mean().reset_index()
    rating_avg.rename(columns={"rating": "avg_rating"}, inplace=True)

    popular = rating_count.merge(rating_avg, on="title")

    popular_books = popular[popular["num_ratings"] >= 200]

    popular_books = popular_books.sort_values("avg_rating", ascending=False)

    popular_books = popular_books.merge(books, on="title").drop_duplicates("title")

    popular_books = popular_books[
        ["title", "author", "image_url", "num_ratings", "avg_rating"]
    ]

    pickle.dump(popular_books, open("models/popular_books.pkl", "wb"))

    print("Popularity model saved")


if __name__ == "__main__":
    build_popularity_model()