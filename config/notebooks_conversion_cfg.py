# RUN WITH FROM REPOSITORY ROOT TO CONVERT NOTEBOOKS TO SCRIPTS
# jupyter nbconvert --config "config/notebooks_conversion_cfg.py" --to script --output-dir "./src/scripts/collection/"

import os, fnmatch
from pathlib import Path

from config.config import config
notebooks_collection_path = config.notebooks_collection_path

# Configuration
c = get_config()
# List notebooks to convert
listOfFiles = os.listdir(notebooks_collection_path)
pattern = "*.ipynb"
notebooks = []
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        path_str = str(Path(notebooks_collection_path) / entry)
        notebooks.append(path_str)

[print("Converting: " + str(nb)) for nb in notebooks]

c.TagRemovePreprocessor.remove_cell_tags = ("dev",)
c.NbConvertApp.notebooks = notebooks
# Cells marked with the tag "dev" will be ignored from conversion to script.
# Go to  "View - Cell Toolbar - Tags" to activate tags
