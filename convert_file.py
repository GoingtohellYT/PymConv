import os
from modifier import ImagesModifier
from PIL import Image
from pillow_heif import HeifImagePlugin


class FilesContainers(ImagesModifier):
    def __init__(self, paths):
        self.paths = paths  # on modifie le chemin d'accès pour qu'il soit relatif
        assert len(paths) != 0, "Le chemin donné est vide"

        self.rgba_types = ("ico", "png", "tiff", "webp", "gif")
        if self.paths.split(".")[1] in self.rgba_types:
            self.image = Image.open(self.paths).convert("RGBA")  # image ouverte sur laquelle on va travailler
        else:
            self.image = Image.open(self.paths).convert("RGB")

        self.width, self.height = self.image.size
        self.modified = False

    def get_image(self):
        return self.image

    def show_image(self):
        """ Cette fonction permet d'afficher l'image instancié """
        self.image.show()

    def confirm_rotation(self, degre):
        """
        Cette fonction applique la rotation à l'image en faisant appel à la superclasse ImagesModifier et défini l'image comme modifiée

        Argument :
            degre est un nombre flottant
        """
        self.image = self.apply_image_rotation(degre, self.image)
        self.modified = True

    def confirm_filter(self, filtre):
        """
        Cette fonction applique le filtre à l'image en faisant appel à la superclasse ImagesModifier et défini l'image comme modifiée

        Argument :
            filtre est une instance de ImageFilter
        """
        self.image = self.apply_image_filter(filtre, self.image)
        self.modified = True

    def confirm_resize(self, size):
        """
        Cette fonction applique le recadrage à l'image en faisant appel à la superclasse ImagesModifier et défini l'image comme modifiée

        Argument :
            size est un tuple d'entiers
        """
        start_size = self.image.size
        self.image = self.apply_resized_image(size, self.image)
        if start_size != self.image.size:
            self.modified = True

    def convert_img(self, format_):  # format de conversion sous forme str
        """
        Cette fonction permet de convertir l'image sélectionnée sous un autre format

        Prend en paramètre le format dans lequel il faut convertir l'image sous forme de string

        Renvoie : rien
        """
        assert len(format_) != 0, "aucun format rentré"
        new_path = os.path.splitext(self.paths)[0]
        if not self.modified:
            if (format_.lower() not in self.rgba_types) and self.image.mode == "RGBA":
                image = self.image.convert("RGB")
            else:
                image = self.image
            image.save(new_path + f'.{format_.lower()}', format_)
        else:
            if (format_.lower() not in self.rgba_types) and self.image.mode == "RGBA":
                image = self.image.convert("RGB")
            else:
                image = self.image
            image.save(new_path + "_modified" + f'.{format_.lower()}', format_)
