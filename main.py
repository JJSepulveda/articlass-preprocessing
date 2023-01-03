"""
Proccess Notion exports in order to reduce the image size and place the new image in the markdown file.
"""

import os
import logging
from decouple import config

# load environment variables
DEBUG = config("DEBUG", default=False, cast=bool)

# set the logging level
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# FUNCTIONS ----------------------------------------------------------------
def get_zip_files():
    """Returns a list of zip files"""
    zip_files = []
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith(".zip"):
                zip_files.append(os.path.join(root, file))
    
    return zip_files

# ENTRY ----------------------------------------------------------------
def main():
    # find zip files
    zip_files = get_zip_files()
    logging.debug(zip_files)

if __name__ == "__main__":
    main()