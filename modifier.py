from PIL import ImageFilter


class ImagesModifier:
    @staticmethod
    def preview_image_rotation(angle, image):
        """
        Fonction qui affiche les différentes images avec une rotation à l'angle spécifié (sens horaire)

        Arguments :
            angle est un float
            image est une instance de la classe Image de PIL
        Post-conditions :
            Les images tournées sont affichées, mais ces changements ne sont pas appliqués
        """
        image.rotate(angle, expand=True).show()

    @staticmethod
    def apply_image_rotation(angle, image):
        """
        Fonction qui applique la rotation aux différentes images

        Arguments :
            angle est un float
            image est une instance de la classe Image du module PIL
        Post-conditions :
            L'image tournée est renvoyée
        """
        return image.rotate(angle, expand=True)

    @staticmethod
    def preview_image_filter(filtre, image):
        """
        Fonction qui affiche les différentes images avec les filtres

        Arguments :
            filter est une instance de la classe ImageFilter du module PIL
            image est une instance de la classe Image du module PIL
        Post-conditions :
            Les images sont affichées avec le filtre appliqué
        """
        if filtre == "GRAYSCALE":
            image.convert("L").show()
        elif issubclass(filtre, ImageFilter.BuiltinFilter):
            image.filter(filtre).show()

    @staticmethod
    def apply_image_filter(filtre, image):
        """
        Fonction qui applique le filtre spécifié aux différentes images

        Arguments :
            filter est une instance de la classe ImageFilter du module PIL ou "GRAYSCALE" en str
            image est une instance de la classe Image du module PIL
        Post-conditions :
            Les images sont renvoyées avec le filtre appliqué
        """
        if filtre == "GRAYSCALE":
            return image.convert("L")
        elif issubclass(filtre, ImageFilter.BuiltinFilter):
            return image.filter(filtre)

    @staticmethod
    def preview_resized_image(size, image):
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

    @staticmethod
    def apply_resized_image(size, image):
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

