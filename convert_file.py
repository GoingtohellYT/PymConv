from PIL import Image


class FileContainer:

    def __int__(self, img):
        self.img = img  # nom de l'image et son extension en local avec le programme sous forme str
        self.image = Image.open(self.img).convert("RGB") # image ouverte sur laquelle on va travailler

    def get_image(self):
        return self.image

    def convert_img(self, format): # format de conversion sous forme str
        self.image.save(self.img, format)
        return self.image


"""idées d'ajouts identifiés: 
- gerer les options de qualité etc
-
"""
