from PIL import Image
from os import listdir
from os.path import isfile, join
from pathlib import Path


class folderContainer:
    def __init__(self, folder):
        self.folder = folder
        self.extensions = ('.jpg', '.jpeg', '.png', '.ico', ".gif", ".webp", ".tiff")
        self.images = [f for f in listdir(self.folder) if
                       f.lower().endswith(self.extensions) and isfile(join(self.folder, f))]

        assert len(listdir(self.folder)) != 0, "Le dossier est vide, aucune image ne peut être convertie"

    def get_indexes(self):
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
            end = len(self.images)

        for image in self.images[start:end]:
            image_name = image.split('.')[0]
            image = Image.open(join(self.folder, image))
            print(image.format)
            image.convert('RGB')
            new_path = join(self.folder, image_name)
            print(new_path)
            image.save(new_path + f'.{destination_format.lower()}', destination_format)

        print("Les nouvelles images sont dans le dossier.")

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

