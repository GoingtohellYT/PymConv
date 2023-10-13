from PIL import Image
import os
from pathlib import Path


class img_modifier:

    def __init__(self, paths):
        self.paths = paths  # on modifie le chemin d'accès pour qu'il soit relatif
        self.image = Image.open(self.paths).convert("RGB")  # image ouverte sur laquelle on va travailler
        self.image_modifier = Image.open(self.paths).convert("RGB")  # image ouverte sur laquelle on va travailler

    def get_image(self):
        return self.image

    def show_image(self):
        return self.image.show()

    def rotate_img(self, degre):
        """methode qui fait pivoter l'image"""
        self.image_modifier = self.image_modifier.rotate(degre).show()
        return self.image_modifier

    def filter_img(self, filter):
        self.image_modifier = self.image_modifier.filter(filter).show()
        return self.image_modifier

    def resize_img(self, size):
        """parametre : size est un tuple avec largeur, hauteur"""
        self.image_modifier = self.image_modifier.resize(size).show()
        return self.image_modifier

    def save_img(self):  # format de conversion sous forme str
        new_path = os.path.splitext(self.paths)[0]
        self.image.save(new_path, "jpeg")


img1 = img_modifier(Path(r"C:\Users\Mat\Desktop\projet_bis\image_modifier\V5.gif"))
img1.resize_img((1280,720))
img1.rotate_img(45)