from PIL import Image
from pathlib import Path
import os

class FilesContainers:

    def __init__(self, paths):
        self.paths = Path(os.path.realpath(paths))  # on modifie le chemin d'accès pour qu'il soit relatif
        self.image = Image.open(self.paths).convert("RGB")  # image ouverte sur laquelle on va travailler

    def get_image(self):
        return self.image

    def show_image(self):
        return self.image.show()

    def convert_img(self, format_):  # format de conversion sous forme str
        
        new_path = image.split('.')[0]
        self.image.save(new_path + f'.{format_.lower()}', format_)
