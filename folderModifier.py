from PIL import Image
from pillow_heif import HeifImagePlugin
from os import listdir
from os.path import isfile, join


class ImagesModifier:
    def __init__(self, folder):
        self.folder = folder
        assert len(listdir(self.folder)) != 0, "Le dossier est vide, aucune image ne peut être convertie"

        self.extensions = ('.jpg', '.jpeg', '.png', '.ico', ".gif", ".webp", ".tiff", ".heic")  # conteneurs que l'on peut lire
        self.files = [f for f in listdir(self.folder) if
                      f.lower().endswith(self.extensions) and isfile(join(self.folder, f))]  # liste des fichiers de type image
        self.images = list()
        for file in self.files:  # On crée des instances de la classe Image pour chaque fichier de type image et on définit son mode sur le plus approprié selon le support de la transparence par le conteneur
            if file.split(".")[1] == "png" or file.split('.')[1] == "ico" or file.split(".") == "tiff" or file.split('.') == "webp" or file.split('.') == "gif":
                self.images.append(Image.open(join(self.folder, file)).convert("RGBA"))
            else:
                self.images.append(Image.open(join(self.folder, file)).convert("RGB"))

    def preview_images_rotation(self, angle, image):
        """
        Fonction qui affiche les différentes images avec une rotation à l'angle spécifié (sens horaire)

        Arguments :
            angle est un float
            image est une instance de la classe Image de PIL
        Post-conditions :
            Les images tournées sont affichées, mais ces changements ne sont pas appliqués
        """
        image.rotate(angle, expand=True).show()

    def apply_images_rotation(self, angle, image):
        """
        Fonction qui applique la rotation aux différentes images

        Arguments :
            angle est un float
            image est une instance de la classe Image du module PIL
        Post-conditions :
            L'image tournée est renvoyée
        """
        return image.rotate(angle, expand=True)

    def preview_images_filter(self, filtre, image):
        """
        Fonction qui affiche les différentes images avec les filtres

        Arguments :
            filter est une instance de la classe ImageFilter du module PIL
            image est une instance de la classe Image du module PIL
        Post-conditions :
            Les images sont affichées avec le filtre appliqué
        """
        image.filter(filtre).show()

    def apply_images_filter(selfself, filtre, image):
        """
        Fonction qui applique le filtre spécifié aux différentes images

        Arguments :
            filter est une instance de la classe ImageFilter du module PIL
            image est une instance de la classe Image du module PIL
        Post-conditions :
            Les images sont renvoyées avec le filtre appliqué
        """
        return image.filter(filtre)

    def preview_resized_images(self, size, image):
        """
        Fonction qui affiche les différentes images avec la nouvelle taille

        Arguments :
            size est un tuple d'integers (largeur, hauteur)
            image est une instance de la classe Image du module PIL
        Post-conditions :
            Les images sont affichées avec la nouvelle taille
        """
        width, height = image.size
        if size[0] <= width and size[1] <= height:
            image.resize(size).show()

    def apply_resized_images(self, size, image):
        """
        Fonction qui applique la nouvelle taille aux différentes images si possible

        Arguments :
            size est un tuple d'integers (largeur, hauteur)
            image est une instance de la classe Image du module PIL
        Post-conditions :
            Les images sont renvoyées avec la nouvelle taille
        """
        width, height = image.size
        if size[0] <= width and size[1] <= height:
            return image.resize(size)

