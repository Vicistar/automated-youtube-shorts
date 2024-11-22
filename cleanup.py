import os
import shutil

def cleanup_files():
    shutil.rmtree("downloads/")
    shutil.rmtree("compiled/")
