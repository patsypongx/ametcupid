import os

def read_root():
    root_dir = os.getcwd()
    return os.path.abspath(root_dir)
