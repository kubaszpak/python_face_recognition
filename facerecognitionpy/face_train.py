import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
image_dir = os.path.join(PROJECT_DIR,"resources")

def train():
    print(PROJECT_DIR)
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith(".png") of file.endswith(".jpg"):
                path = os.path.join(root,file)
                print(path)
                # learning os