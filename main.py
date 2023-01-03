"""
Proccess Notion exports in order to reduce the image size and place the new image in the markdown file.
"""
from typing import List

import os
import logging
from decouple import config

import zipfile

# load environment variables
DEBUG = config("DEBUG", default=False, cast=bool)

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


# ENTRY ----------------------------------------------------------------
def main():
    # find zip files
    zip_files = get_zip_files()
    logging.debug(zip_files)

    # Unzip one fiele
    unzip_file(zip_files[0])


if __name__ == "__main__":
    main()