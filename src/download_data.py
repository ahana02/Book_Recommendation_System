import os
import zipfile

def download_kaggle_dataset():

    os.system(
        "kaggle datasets download -d saurabhbagchi/books-dataset -p data/raw"
    )

    zip_path = "data/raw/books-dataset.zip"

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("data/raw")

    print("Dataset downloaded and extracted.")


if __name__ == "__main__":
    download_kaggle_dataset()