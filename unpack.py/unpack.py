import os
import shutil

def ffs(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist")

    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} is not a directory")

    for root, _, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            os.makedirs(os.path.join(os.path.dirname(path), filename), exist_ok=True)
            shutil.copy(filepath, os.path.join(os.path.dirname(path), filename))

if __name__ == "__main__":
    path = input("Enter the path to the directory to unpack: ")
    ffs(path)