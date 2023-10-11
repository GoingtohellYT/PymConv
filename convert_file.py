from PIL import Image
import os


class FilesContainers:

    def __init__(self, paths):
        self.paths = paths  # on modifie le chemin d'accès pour qu'il soit relatif
        self.image = Image.open(self.paths).convert("RGB")  # image ouverte sur laquelle on va travailler

        assert len(self.paths) != 0, "Aucun fichier n'est fournit"

    def get_image(self):
        return self.image

    def show_image(self):
        return self.image.show()

    def convert_img(self, format_):  # format de conversion sous forme str
        """
        Cette fonction permet de convertir l'image séléctionné sous d'autre format

        Prend en paramètre le format dans lequel il faut convertir l'image sous forme string

        Renvoie : rien
        """
        assert len(format_) != 0, "aucun format rentrer"
        new_path = os.path.splitext(self.paths)[0]
        self.image.save(new_path + f'.{format_.lower()}', format_)
