import os

def make_folder(path):
    if not os.path.exists(f"{path}/Figure"):
        os.makedirs(f"{path}/Figure")