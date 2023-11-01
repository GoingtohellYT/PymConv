from PIL import Image
from pillow_heif import HeifImagePlugin


class ImgModifier:

    def __init__(self, path):
        self.paths = path  # on modifie le chemin d'accès pour qu'il soit relatif
        assert len(path) != 0, "Le chemin donné est vide"
        if self.paths.split(".")[1] == "ico" or self.paths.split(".")[1] == "png" or self.paths.split('.')[1] == "tiff" or self.paths.split('.')[1] == "webp" or self.paths.split('.')[1] == "gif":
            self.image = Image.open(self.paths).convert("RGBA")  # image ouverte sur laquelle on va travailler
        else:
            self.image = Image.open(self.paths).convert("RGB")
        self.width, self.height = self.image.size

    def preview_rotate_img(self, degre):
        """Méthode qui fait montre l'image pivoter l'image.
        Prend en paramètre le nombre de degrés sur lequel il faut pivoter"""
        self.image.rotate(degre, expand=True).show()

    def rotate_img(self, degre):
        """Méthode qui fait pivoter l'image et la sauvegarde.
        Prend en paramètre le nombre de degrés sur lequel il faut pivote"""
        return self.image.rotate(degre, expand=True)

    def preview_filter_img(self, filtre):
        """Methode qui montre le filtre sur l'image que l'utilisateur veut mettre.
        Prend en paramètre une instance du filtre (ex: ImageFilter.BLUR)"""
        self.image.filter(filtre).show()

    def filter_img(self, filtre):
        """Methode qui sauvegarde le filtre sur l'image que l'utilisateur veut mettre.
        Prend en paramètre une instance du filtre (ex: ImageFilter.BLUR)"""
        return self.image.filter(filtre)

    def preview_resize_img(self, size):
        """Fonction qui montre la modification de taille.
        Paramètre : size est un tuple avec largeur, hauteur des entiers"""
        if size[0] <= self.width and size[1] <= self.height:
            self.image.resize(size).show()

    def resize_img(self, size):
        """Fonction qui sauvegarde la modification de taille
        paramètre : size est un tuple avec largeur, hauteur des entiers"""
        if size[0] <= self.width and size[1] <= self.height:
            return self.image.resize(size)
