import os

BASE_DIR = os.getcwd()
image_dir = os.path.join(BASE_DIR,'resources')


def train():
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                path = os.path.join(root,file)
                