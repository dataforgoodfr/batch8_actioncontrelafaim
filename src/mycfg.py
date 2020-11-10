# RUN WITH FROM REPOSITORY ROOT TO CONVERT NOTEBOOKS TO SCRIPTS
# jupyter nbconvert --config "./src/mycfg.py" --to script --output-dir "./src/scripts/collection/"

import os, fnmatch
from pathlib import Path

notebooks_path = './src/notebooks/collection/'
# Configuration
c = get_config()
# List notebooks to convert
listOfFiles = os.listdir(notebooks_path)
pattern = "*.ipynb"
notebooks = []
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        path_str = str(Path(notebooks_path) / entry)
        notebooks.append(path_str)

[print("Converting: " + str(nb)) for nb in notebooks]

c.TagRemovePreprocessor.remove_cell_tags = ("dev",)
c.NbConvertApp.notebooks = notebooks
# Cells marked with the tag "dev" will be ignored from conversion to script.
# Go to  "View - Cell Toolbar - Tags" to activate tags
