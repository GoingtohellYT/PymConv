from folderConverter import folderContainer
from pathlib import Path


test1 = folderContainer(Path('images'))
# test1.see_images(end=1)
test1.to_format('TIFF', 1)

