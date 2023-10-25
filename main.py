from folderConverter import FolderContainer
from convert_file import FilesContainers
from pathlib import Path
import tkinter
import tkinter.filedialog
from tkinter import ttk


class UI:
    def __init__(self):
        self.instance = None

        self.types_supportes = ['JPEG', 'PNG', 'ICO', "GIF", "WEBP", "TIFF", "PDF"]  # Types dans lesquels on peut convertir les fichiers

        self.window = tkinter.Tk()  # On crée une fenêtre graphique avec tkinter
        self.window.title("PymConv")
        self.window.geometry("1080x720")
        self.window.config(background="#B2BABB")

        # On définit deux "boîtes" qui vont contenir les éléments du GUI
        self.right_frame = tkinter.Frame(self.window, background="#B2BABB")
        self.left_frame = tkinter.Frame(self.window, background="#B2BABB")

        self.folder_button = tkinter.Button(self.window, text="Ouvrir un dossier", font=("Arial", 12), bg='white',
                                            command=self.open_folder)
        self.folder_button.pack(pady=10)

        self.file_button = tkinter.Button(self.window, text="Ouvrir un fichier", font=("Arial", 12), bg='white',
                                          command=self.open_file)
        self.file_button.pack(pady=5)

        self.show_image = tkinter.Button(self.left_frame, text="Voir l'image", font=("Arial", 12), bg='white', command=self.see_image)
        self.show_image.pack(pady=20)

        # --------------- Partie Fichiers --------------- #

        self.fi_container_choice = ttk.Combobox(self.left_frame, values=self.types_supportes, state='readonly')
        self.fi_container_choice.current(0)
        self.fi_container_choice.pack()

        self.convert_file = tkinter.Button(self.left_frame, text="Convertir l'image", font=("Arial", 12), bg='white', command=self.convert_image)
        self.convert_file.pack(pady=20)

        # --------------- Partie Dossiers ----------------- #

        self.fo_start_indexes = ttk.Combobox(self.right_frame, state='readonly')
        self.fo_start_indexes.pack(pady=20)

        self.fo_end_indexes = ttk.Combobox(self.right_frame, state='readonly')
        self.fo_end_indexes.pack()

        self.see_images_btn = tkinter.Button(self.right_frame, text="Voir les images du dossier", font=("Arial", 12),
                                             bg='white',
                                             command=self.see_folder_images)
        self.see_images_btn.pack(pady=20)

        self.fo_container_choice = ttk.Combobox(self.right_frame, values=self.types_supportes,
                                                state='readonly')  # On crée une combobox avec les conteneurs disponibles
        self.fo_container_choice.current(0)  # On définit l'élément par défaut sur le premier élément de la liste
        self.fo_container_choice.pack()

        self.fo_container_convert = tkinter.Button(self.right_frame, text="Convertir les images du dossier",
                                                   font=("Arial", 12), bg='white', command=self.convert_folder_images)
        self.fo_container_convert.pack(pady=20)

        # -------------- Partie Générale ----------------- #
        # On affiche les frames
        self.left_frame.pack(side=tkinter.LEFT, padx=20, pady=20)
        self.right_frame.pack(side=tkinter.RIGHT, padx=20, pady=20)
        # On actualise la fenêtre
        self.window.mainloop()

    def open_folder(self):
        """
        Fonction qui ouvre un dossier avec tkinter.filedialog

        Returns :
            Rien
        Pré-condition :
            Rien
        Post-condition :
            Affiche une interface pour sélectionner l'élément voulu et défini le chemin sur celui l'élément voulu
        """

        path = Path(tkinter.filedialog.askdirectory(mustexist=True))
        self.instance = FolderContainer(path)
        images_indexes = self.instance.get_indexes()

        # On modifie les valeurs possibles et par défaut des combos boxes
        self.fo_start_indexes.config(values=images_indexes[0:-1])
        self.fo_start_indexes.current(0)
        self.fo_end_indexes.config(values=images_indexes[1:])
        self.fo_end_indexes.current(len(images_indexes) - 2)

    def see_folder_images(self):
        """
        Fonction qui appelle FolderContainer.see_images() pour afficher les images voulues du dossier actuel
        """
        if type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            self.instance.see_images(start, end)

    def convert_folder_images(self):
        """
        Fonction appelle FolderContainer.to_format() pour convertir les images voulues du dossier actuel dans le format voulu
        """
        if type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            dest_format = str(self.fo_container_choice.get())
            self.instance.to_format(dest_format, start, end)

    def open_file(self):
        """
        Fonction qui ouvre un fichier avec tkinter.filedialog

        Returns :
            Rien
        Pré-condition :
            Rien
        Post-condition :
            Affiche une interface pour sélectionner l'élément voulu et défini le chemin sur celui l'élément voulu
        """

        path = tkinter.filedialog.askopenfilename()
        self.instance = FilesContainers(path)

    def see_image(self):
        """
        Fonction qui appelle FilesContainers.show_image() pour afficher l'image actuelle
        """
        if type(self.instance) == FilesContainers:
            self.instance.show_image()

    def convert_image(self):
        """
        Fonction qui appelle FilesContainers.convert_img() pour convertir l'image dans le format voulu
        """
        if type(self.instance) == FilesContainers:
            dest_format = str(self.fi_container_choice.get())
            self.instance.convert_img(dest_format)


ui = UI()
