import pandas as pd

def load_data():

    books = pd.read_csv(
        "data/raw/books.csv",
        sep=";",
        on_bad_lines="skip",
        encoding="latin-1"
    )

    users = pd.read_csv(
        "data/raw/users.csv",
        sep=";",
        encoding="latin-1"
    )

    ratings = pd.read_csv(
        "data/raw/ratings.csv",
        sep=";",
        encoding="latin-1"
    )

    return books, users, ratings


def clean_data():

    books, users, ratings = load_data()

    books = books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-M']]

    books.rename(columns={
        "Book-Title":"title",
        "Book-Author":"author",
        "Year-Of-Publication":"year",
        "Publisher":"publisher",
        "Image-URL-M":"image_url"
    }, inplace=True)

    ratings.rename(columns={"Book-Rating":"rating"}, inplace=True)

    return books, users, ratings


if __name__ == "__main__":

    books, users, ratings = clean_data()

    books.to_csv("data/processed/books_cleaned.csv",index=False)
    users.to_csv("data/processed/users_cleaned.csv",index=False)
    ratings.to_csv("data/processed/ratings_cleaned.csv",index=False)

    print("Cleaned datasets saved.")