import os
from img_modifier import ImgModifier


class FilesContainers(ImgModifier):

    def __init__(self, paths):
        super().__init__(paths)
        self.modified = False

    def get_image(self):
        return self.image

    def show_image(self):
        """ Cette fonction permet d'afficher l'image instancié """
        return self.image.show()

    def try_rotate_img(self, degre):
        """
        Cette fonction affiche l'image tournée sans appliquer la modification en faisant appel à la superclasse ImgModifier

        Argument :
            degre est un nombre flottant
        """
        self.preview_rotate_img(degre)

    def confirm_rotation(self, degre):
        """
        Cette fonction applique la rotation à l'image en faisant appel à la superclasse ImgModifier et défini l'image comme modifiée

        Argument :
            degre est un nombre flottant
        """
        self.image = self.rotate_img(degre)
        self.modified = True

    def try_filter(self, filtre):
        """
         Cette fonction affiche l'image avec le filtre sans appliquer la modification en faisant appel à la superclasse ImgModifier

        Argument :
            filtre est une instance de ImageFilter
        """
        self.preview_filter_img(filtre)

    def confirm_filter(self, filtre):
        """
        Cette fonction applique le filtre à l'image en faisant appel à la superclasse ImgModifier et défini l'image comme modifiée

        Argument :
            filtre est une instance de ImageFilter
        """
        self.image = self.filter_img(filtre)
        self.modified = True

    def try_resize(self, size):
        """
        Cette fonction affiche l'image recadrée sans appliquer la modification en faisant appel à la superclasse ImgModifier

        Argument :
            size est un tuple d'entiers
        """
        self.preview_resize_img(size)

    def confirm_resize(self, size):
        """
        Cette fonction applique le recadrage à l'image en faisant appel à la superclasse ImgModifier et défini l'image comme modifiée

        Argument :
            size est un tuple d'entiers
        """
        start_size = self.image.size
        self.image = self.resize_img(size)
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
            if (format_ == "PNG" or format_ == "TIFF" or format_ == "WEBP" or format_ == "GIF" or format_ == "ICO") and self.image.mode == "RGBA":
                image = self.image
            elif (format_ == "JPEG" or format_ == "PDF") and self.image.mode == "RGBA":
                image = self.image.convert("RGB")
            else:
                image = self.image
            image.save(new_path + f'.{format_.lower()}', format_)
        else:
            if (format_ == "PNG" or format_ == "TIFF" or format_ == "WEBP" or format_ == "GIF" or format_ == "ICO") and self.image.mode == "RGBA":
                image = self.image
            elif (format_ == "JPEG" or format_ == "PDF") and self.image.mode == "RGBA":
                image = self.image.convert("RGB")
            else:
                image = self.image
            image.save(new_path + "_modified" + f'.{format_.lower()}', format_)
