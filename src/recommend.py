import pickle
import numpy as np

pt = pickle.load(open("models/pivot.pkl","rb"))
similarity = pickle.load(open("models/similarity.pkl","rb"))
books = pickle.load(open("models/books.pkl","rb"))


def recommend(book_name):

    index = np.where(pt.index == book_name)[0][0]

    similar_items = sorted(
        list(enumerate(similarity[index])),
        key=lambda x:x[1],
        reverse=True
    )[1:5]

    data = []

    for i in similar_items:

        item = []
        temp = books[books["title"] == pt.index[i[0]]]

        item.append(list(temp["title"])[0])
        item.append(list(temp["author"])[0])

        data.append(item)

    return data