import os

ROOT_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))  # This is your Project Root


def get_full_path(path):
    return os.path.join(ROOT_DIR, path)
