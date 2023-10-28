from PIL import Image
from pillow_heif import HeifImagePlugin
import os
from pathlib import Path


class img_modifier:

    def __init__(self, paths):
        self.paths = paths  # on modifie le chemin d'accès pour qu'il soit relatif
        self.image = Image.open(self.paths).convert("RGB")  # image ouverte sur laquelle on va travailler

    def get_image(self):
        return self.image

    def show_image(self):
        return self.image.show()

    def preview_rotate_img(self, degre):
        """methode qui fait montre l'image pivoter l'image.
        Prend en paramètre le nombre de degré sur lequel il faut pivoter"""
        self.image.rotate(degre).show()

    def rotate_img(self, degre):
        """methode qui fait pivoter l'image et la sauvegarde.
        Prend en paramètre le nombre de degré sur lequel il faut pivote"""
        self.image.rotate(degre).save(self.paths)


    def preview_filter_img(self, filter):
        """methode qui montre le filte sur l'image que l'utilisateur veut mettre.
        Prend en paramètre le nom du filtre"""
        self.image.filter(filter).show()

    def filter_img(self, filter):
        """methode qui sauvegarde le filte sur l'image que l'utilisateur veut mettre.
        Prend en paramètre le nom du filtre"""
        self.image.filter(filter).save(self.paths)

    def preview_resize_img(self, size):
        """Focntion qui montre la modification de taille.
        parametre : size est un tuple avec largeur, hauteur"""
        self.image.resize(size).show()

    def resize_img(self, size):
        """Fonctiojn qui sauvegarde la modification de taille
        parametre : size est un tuple avec largeur, hauteur"""
        self.image.resize(size).save(self.paths)

    def save_img(self):  # format de conversion sous forme str
        new_path = os.path.splitext(self.paths)[0]
        self.image.save(new_path, "jpeg")

