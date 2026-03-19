import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity


def build_collaborative_model():

    books = pd.read_csv("data/processed/books_cleaned.csv")
    ratings = pd.read_csv("data/processed/ratings_cleaned.csv")

    merged = ratings.merge(books,on="ISBN")

    x = merged.groupby("User-ID").count()["rating"] > 200
    experienced_users = x[x].index

    filtered = merged[merged["User-ID"].isin(experienced_users)]

    y = filtered.groupby("title").count()["rating"] >= 50
    famous_books = y[y].index

    final = filtered[filtered["title"].isin(famous_books)]

    pt = final.pivot_table(index="title",columns="User-ID",values="rating")

    pt.fillna(0,inplace=True)

    similarity = cosine_similarity(pt)

    pickle.dump(pt,open("models/pivot.pkl","wb"))
    pickle.dump(similarity,open("models/similarity.pkl","wb"))
    pickle.dump(books,open("models/books.pkl","wb"))

    print("Collaborative filtering model saved")


if __name__ == "__main__":
    build_collaborative_model()