"""
Using the tinify API to compress an image
"""
import tinify
import os
from decouple import config
import logging

DATA_DIR = "./opt/"
API_KEY = config("API_KEY", default=None, cast=str)
tinify.key = API_KEY

def check_file_exists(filename: str) -> bool:
    return os.path.exists(file_path)

def optimize_image(image_filename: str, output_filename: str):
    # Check if the image exists
    if not check_file_exists(image_filename):
        logging.debug(f"Image {image_filename} does not exist")
        return

    # get the image
    source = tinify.from_file(image_filename)
    
    if(not os.path.exists(DATA_DIR)):
        os.mkdir(DATA_DIR)

    image_dir = os.path.join(DATA_DIR, output_filename)

    # optimized image
    source.to_file(image_dir)

if __name__ == "__main__":
    optimize_image("image.png", "opt.png") 