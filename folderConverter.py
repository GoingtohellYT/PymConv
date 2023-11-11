from PIL import Image
from pillow_heif import HeifImagePlugin
from os import listdir
from os.path import isfile, join
from modifier import ImagesModifier


class FolderContainer(ImagesModifier):
    def __init__(self, folder):
        self.folder = folder
        assert len(listdir(self.folder)) != 0, "Le dossier est vide, aucune image ne peut être convertie"

        self.extensions = ('.jpg', '.jpeg', '.png', '.ico', ".gif", ".webp", ".tiff", ".heic")  # conteneurs que l'on peut lire
        self.rgba_types = ("ico", "png", "tiff", "webp", "gif")  # conteneurs qui supportent un canal alpha
        self.files = [f for f in listdir(self.folder) if
                      f.lower().endswith(self.extensions) and isfile(
                          join(self.folder, f))]  # liste des fichiers de type image
        assert len(self.files) != 0, "Aucune image au format supporté dans le dossier"
        self.images = list()
        for file in self.files:  # On crée des instances de la classe Image pour chaque fichier de type image et on définit son mode sur le plus approprié selon le support de la transparence par le conteneur
            if file.split(".")[1] in self.rgba_types:
                self.images.append(Image.open(join(self.folder, file)).convert("RGBA"))
            else:
                self.images.append(Image.open(join(self.folder, file)).convert("RGB"))
        self.modified = False

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
        return [i for i in range(len(self.files) + 1)]

    def try_rotations(self, angle, start=0, end=None):
        """
        Fonction qui affiche les images tournées en faisant appel à la superclasse ImagesModifier

        Arguments :
            angle est l'angle de la rotation des images dans le sens horaire (float)
            start est un integer qui correspond au premier élément concerné de la liste d'images
            end est un integer qui correspond au dernier élément concerné de la liste d'images
        Post-conditions :
            Les images tournées sont affichées, mais la liste reste inchangée
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            self.preview_image_rotation(angle, image)

    def apply_rotations(self, angle, start=0, end=None):
        """
        Fonction qui applique la rotation aux images concernées en faisant appel à la superclasse ImagesModifier

        Arguments :
            angle est l'angle de la rotation des images dans le sens horaire (float)
            start est un integer qui correspond au premier élément concerné de la liste d'images
            end est un integer qui correspond au dernier élément concerné de la liste d'images
        Post-conditions :
            La liste d'images est modifiée et compte les images tournées
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            self.images[self.images.index(image)] = self.apply_image_rotation(angle, image)

        self.modified = True

    def try_filter(self, filtre, start=0, end=None):
        """
        Fonction qui affiche les images avec le filtre spécifié en faisant appel à la superclasse ImagesModifier

        Arguments :
             filtre est une instance de la classe ImageFilter du module PIL ou 'GRAYSCALE' en str
             start est un integer qui correspond au premier élément concerné de la liste d'images
             end est un integer qui correspond au dernier élément concerné de la liste d'images
        Post-conditions :
            Les images sont affichées avec le filtre activé, mais les changements ne sont pas appliqués
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            self.preview_image_filter(filtre, image)

    def apply_filter(self, filtre, start=0, end=None):
        """
        Fonction qui applique le filtre spécifié sur les images en faisant appel à la superclasse ImagesModifier

        Arguments :
             filtre est une instance de la classe ImageFilter du module PIL
             start est un integer qui correspond au premier élément concerné de la liste d'images
             end est un integer qui correspond au dernier élément concerné de la liste d'images
        Post-conditions :
             Le filtre est appliqué aux images spécifiées
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            self.images[self.images.index(image)] = self.apply_image_filter(filtre, image)

        self.modified = True

    def try_resize(self, size, start=0, end=None):
        """
        Fonction qui affiche les images redimensionnées en faisant appel à la superclasse ImagesModifier

        Arguments :
            size est un tuple d'entiers de la forme (largeur, hauteur) en pixels
            start est un integer qui correspond au premier élément concerné de la liste d'images
            end est un integer qui correspond au dernier élément concerné de la liste d'images
        Pré-conditions :
           size ne peut dépasser la taille de l'image originelle, ni en hauteur, ni en largeur
        Post-conditions :
            Les images redimensionnées sont affichées, mais les changements ne sont pas appliqués
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            self.preview_resized_image(size, image)

    def apply_resize(self, size, start=0, end=None):
        """
        Fonction qui applique le redimensionnement aux images sélectionnées en faisant appel à la superclasse ImagesModifier

        Arguments :
            size est un tuple d'entiers de la forme (largeur, hauteur) en pixels
            start est un integer qui correspond au premier élément concerné de la liste d'images
            end est un integer qui correspond au dernier élément concerné de la liste d'images
        Pré-conditions :
           size ne peut dépasser la taille de l'image originelle, ni en hauteur, ni en largeur ; sans quoi l'image ne sera pas redimensionnée
        Post-conditions :
            Les modifications de dimensions sont appliquées aux images sélectionnées
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for image in self.images[start:end]:
            self.images[self.images.index(image)] = self.apply_resized_image(size, image)

    def to_format(self, destination_format, start=0, end=None):
        """
        Cette fonction convertit une liste d'image dans le format spécifié

        Retourne :
            Rien
        Pré-conditions :
            Le dossier passé en argument de la classe n'est pas vide et existe
        Post-conditions :
            Le dossier passé en argument de la classe contient de nouveaux éléments (les images au format spécifié)
        """
        if end is None:
            end = len(self.files)  # Si aucune valeur de fin n'est spécifiée, on prend la dernière image (une valeur de fin est toujours spécifiée avec l'interface graphique)

        for file in self.files[start:end]:
            image_name = file.split('.')[0]  # sépare la chaîne de caractères au niveau du '.' pour séparer le nom de l'extension du fichier
            image = self.images[self.files.index(file)]  # On récupère l'image correspondante
            if not self.modified:
                if (destination_format.lower() not in self.rgba_types) and image.mode == "RGBA":
                    image = image.convert('RGB')  # convertir l'image en RGB pour les formats qui ne supportent pas la transparence
                else:
                    pass
                new_path = join(self.folder, image_name)
                image.save(new_path + f'.{destination_format.lower()}', destination_format)
            else:
                if (destination_format.lower() not in self.rgba_types) and image.mode == "RGBA":
                    image = image.convert('RGB')  # convertir l'image en RGB pour les formats qui ne supportent pas la transparence
                else:
                    pass
                new_path = join(self.folder, image_name + '_modified')
                image.save(new_path + f'.{destination_format.lower()}', destination_format)

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
            end = len(self.files)

        for image in self.images[start:end]:
            image.show()
