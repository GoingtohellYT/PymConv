from PIL import Image
from pillow_heif import HeifImagePlugin
from os import listdir
from os.path import isfile, join


class FolderContainer:
    def __init__(self, folder):
        self.folder = folder
        self.extensions = ('.jpg', '.jpeg', '.png', '.ico', ".gif", ".webp", ".tiff", ".heic")  # conteneurs que l'on peut lire
        self.images = [f for f in listdir(self.folder) if
                       f.lower().endswith(self.extensions) and isfile(join(self.folder, f))]

        assert len(listdir(self.folder)) != 0, "Le dossier est vide, aucune image ne peut être convertie"

    def get_indexes(self):
        """
        Cette fonction renvoie les index des images du dossier plus 1

        Retourne :
            Une liste d'entiers allant de 0 à la taille de la liste
        Pré-conditions :
            Aucune
        Post-condition :
            L'élément retourné est une liste d'entiers allant de 0 au nombre d'images supportées dans le dossier
        """
        indexes = [i for i in range(len(self.images) + 1)]
        return indexes

    def to_format(self, destination_format, start=0, end=None):
        """
        Cette fonction convertit une liste d'image en dans le format spécifié

        Retourne :
            Rien
        Pré-conditions :
            Le dossier passé en argument de la classe n'est pas vide et existe
        Post-conditions :
            Le dossier passé en argument de la classe contient de nouveaux éléments (les images au format spécifié)
        """
        if end is None:
            end = len(self.images)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            image_name = image.split('.')[0]  # sépare la chaîne de caractères au niveau du '.' pour séparer le nom de l'extension du fichier
            image = Image.open(join(self.folder, image))
            image = image.convert('RGB')  # convertir l'image en RGB assure une meilleure compatibilité --> il faudrait tester cette compatibilité avec RGBA afin de garder la transparence entre deux formats qui le supporte (PNG et ICO par exemple)
            new_path = join(self.folder, image_name)
            image.save(new_path + f'.{destination_format.lower()}', destination_format)

        # print("Les nouvelles images sont dans le dossier.")

    def see_images(self, start=0, end=None):
        """
        Cette fonction affiche les images les unes après les autres

        Retourne :
             Rien
        Pré-conditions :
            Le dossier passé en argument de la classe n'est pas vide et existe
        Post-conditions :
            Les images s'affichent à l'écran
        """
        if end is None:
            end = len(self.images)

        for image in self.images[start:end]:
            image = Image.open(join(self.folder, image))
            image.show()
