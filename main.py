from folderConverter import folderContainer
from pathlib import Path
import tkinter
import tkinter.filedialog
from tkinter import ttk


class UI:
    def __init__(self):
        self.instance = None

        self.types_supportes = ['JPEG', 'PNG', 'ICO', "GIF", "WEBP", "TIFF"]

        self.window = tkinter.Tk()  # On crée une fenêtre graphique avec tkinter
        self.window.title("PymConv")
        self.window.geometry("1080x720")
        self.window.config(background="#B2BABB")

        # On définit deux "boîtes" qui vont contenir les éléments du GUI
        self.right_frame = tkinter.Frame(self.window, background="#B2BABB")
        self.left_frame = tkinter.Frame(self.window)

        self.folder_button = tkinter.Button(self.window, text="Ouvrir un dossier", font=("Arial", 12), bg='white',
                                            command=self.open_folder)
        self.folder_button.pack(pady=10)

        self.file_button = tkinter.Button(self.window, text="Ouvrir un fichier", font=("Arial", 12), bg='white',
                                          command=self.open_file)
        self.file_button.pack(pady=5)

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
                                                   font=("Arial", 12),
                                                   bg='white')

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
        self.instance = folderContainer(path)
        images_indexes = self.instance.get_indexes()

        # On modifie les valeurs possibles et par défaut des combos boxes
        self.fo_start_indexes.config(values=images_indexes[0:-1])
        self.fo_start_indexes.current(0)
        self.fo_end_indexes.config(values=images_indexes[1:])
        self.fo_end_indexes.current(len(images_indexes) - 2)

    def see_folder_images(self):
        """
        Fonction qui appelle folderContainer.see_images() pour afficher les images voulues du dossier actuel
        """
        if type(self.instance) == folderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            self.instance.see_images(start, end)

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

        path = Path(tkinter.filedialog.askopenfilename())


ui = UI()
