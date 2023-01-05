"""
Proccess Notion exports in order to reduce the image size and place the new image in the markdown file in the correct place.
"""
from typing import List, Dict, Union

import os
import logging
from decouple import config

import zipfile

# My own source file
from utils import delete_nameId
from utils import get_filename
from utils import preprocess_string

# load environment variables
DEBUG = config("DEBUG", default=False, cast=bool)
API_KEY = config("API_KEY", default=None, cast=str)

# CONST VARIABLES
UNZIP_FILES_PATH = "./unzips/"

# set the logging level
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# FUNCTIONS ----------------------------------------------------------------
def get_zip_files() -> List[str]:
    """Returns a list of zip files"""
    zip_files = []
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith(".zip"):
                zip_files.append(os.path.join(root, file))
    
    return zip_files


def unzip_file(zip_file: str):
    """Unzip a zip file"""
    logging.debug(zip_file)
    # unzip the file
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(UNZIP_FILES_PATH)


def get_markdown_filenames() -> List[str]:
    """Returns a list of markdown filename"""
    markdown_filename = []
    for root, dirs, files in os.walk(UNZIP_FILES_PATH):
        for file in files:
            if file.endswith(".md"):
                markdown_filename.append(os.path.join(root, file))
    
    return markdown_filename


def get_image_path_list(filename: str) -> List[str]:
    """Returns a list of images filename of one markdown file"""
    images_filename = []
    # split the filename to remove the extension
    name, _ = os.path.splitext(filename)
    # Obtener la ruta de la carpeta de las imagenes
    file_path = os.path.join(UNZIP_FILES_PATH, name)

    logging.debug("#"*10)
    logging.debug(file_path)
    for root, _, files in os.walk(file_path):
        for file in files:
            if file.endswith(".png"):
                images_filename.append(os.path.join(root, file))
    return images_filename

def make_dictionary_with_all_files_images(markdown_files: List[str]) -> Dict[str, List[str]]:
    """Returns a dictionary with all images"""
    images_dict = {}
    for name in markdown_files:
        # Retorna el nombre del archvio markdown (nombre id.md)
        filename = get_filename(name)
        # No queremos el id asi que se lo vamos a quitar
        filename = delete_nameId(filename)
        # Tampoco queremos la extensión
        filename, _ = os.path.splitext(filename)
        # Ahora la vamos a preprocesar
        filename = preprocess_string(filename[0:-2])
        logging.debug(filename)
        # ahora vamos a crear un diccionario donde almacenemos todas las imagenes de todos los arhcivos
        images_dict[filename] = get_image_path_list(get_filename(name))
    logging.debug(images_dict)
    return images_dict

# Some images don't have title, so I'll make the filename with the title of the directory

# ENTRY ----------------------------------------------------------------
def main():
    # find zip files
    zip_files = get_zip_files()
    logging.debug('# zip files')
    logging.debug(zip_files)

    # Unzip one fiele
    unzip_file(zip_files[0])

    # Get list of markdown files
    markdown_files = get_markdown_filenames()
    logging.debug('# Mark down files')
    logging.debug(markdown_files)

    # The dirname where images are placed is the same as the file name
    logging.debug(get_filename(markdown_files[0]))
    
    # Get list of images of each markdown file
    # image_path_list = get_image_path_list(get_filename(markdown_files[0]))
    # logging.debug('# Image path list')
    # logging.debug(image_path_list)

    print("##"*10)
    images_path_dict = make_dictionary_with_all_files_images(markdown_files)
    

if __name__ == "__main__":
    main()