from folderConverter import FolderContainer
from convert_file import FilesContainers
from pathlib import Path
import tkinter
import tkinter.filedialog
from tkinter import ttk
from PIL import ImageFilter
from os.path import isdir, isfile
from os import listdir
from gc import get_objects


class UI:
    def __init__(self):
        self.instance = None

        # --------------- Partie Définition des constantes ----------------- #

        self.types_supportes = ['JPEG', 'PNG', 'ICO', "GIF", "WEBP", "TIFF",
                                "PDF"]  # Types dans lesquels on peut convertir les fichiers
        self.degres = ["0.0", "45.0", "90.0", "135.0", "180.0", "225.0", "270.0",
                       "315.0"]  # Angles de rotation par défaut
        self.filtres = ["NONE", "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS",
                        "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE", "GRAYSCALE"]  # Filtres disponibles

        self.background_color = "#B2BABB"
        self.font = ("Arial", 12)
        self.minimal_y_separation = 4
        self.large_y_separation = 15
        self.usual_x_separation = 20
        self.minimal_x_separation = 10
        self.massive_x_separation = 70

        # --------------- Partie Mise en place de l'UI ----------------- #

        self.window = tkinter.Tk()  # On crée une fenêtre graphique avec tkinter
        self.window.title("PymConv")
        self.window.geometry("1080x500")
        self.window.config(background="#B2BABB")
        self.window.resizable(False, False)

        # On définit des "boîtes" qui vont contenir les éléments du GUI
        self.right_frame = tkinter.Frame(self.window, background=self.background_color)
        self.left_frame = tkinter.Frame(self.window, background=self.background_color)
        self.top_frame = tkinter.Frame(self.window, background=self.background_color)
        self.bottom_frame = tkinter.Frame(self.window, background=self.background_color)

        self.file_button = tkinter.Button(self.top_frame, text="Ouvrir un fichier", font=self.font, bg='white',
                                          command=self.open_file)
        self.file_button.pack(side=tkinter.LEFT, padx=self.usual_x_separation)

        self.folder_button = tkinter.Button(self.top_frame, text="Ouvrir un dossier", font=self.font, bg='white',
                                            command=self.open_folder)
        self.folder_button.pack(side=tkinter.LEFT, padx=self.usual_x_separation)

        self.start_label = tkinter.Label(self.top_frame, text="Agir sur les images : ", font=self.font, fg='black',
                                         bg=self.background_color)
        self.start_label.pack(side=tkinter.LEFT, padx=self.minimal_x_separation)

        self.fo_start_indexes = ttk.Combobox(self.top_frame, state='readonly')
        self.fo_start_indexes.pack(side=tkinter.LEFT, padx=self.minimal_x_separation)

        self.separator_label = tkinter.Label(self.top_frame, text="à", font=self.font, fg="black",
                                             bg=self.background_color)
        self.separator_label.pack(side=tkinter.LEFT, padx=self.minimal_x_separation)

        self.fo_end_indexes = ttk.Combobox(self.top_frame, state='readonly')
        self.fo_end_indexes.pack(side=tkinter.LEFT, padx=self.minimal_x_separation)

        self.see_images_btn = tkinter.Button(self.bottom_frame, text="Voir la ou les images", font=self.font,
                                             bg='white',
                                             command=self.see_images)
        self.see_images_btn.pack(side=tkinter.LEFT)

        # --------------- Partie Modifications ----------------- #

        self.resize_label = tkinter.Label(self.left_frame, font=self.font, bg=self.background_color, fg='black',
                                          text="Changer les dimensions")
        self.resize_label.pack(padx=self.massive_x_separation)

        self.size_entry = tkinter.Entry(self.left_frame, font=self.font, bg='white')
        self.size_entry.insert(0, "Largeur*Hauteur")
        self.size_entry.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.size_try = tkinter.Button(self.left_frame, text="Essayer", font=self.font, bg='white',
                                       command=self.try_crop)
        self.size_try.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.size_confirm = tkinter.Button(self.left_frame, text="Valider", font=self.font, bg='white',
                                           command=self.confirm_crop)
        self.size_confirm.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.rotation_label = tkinter.Label(self.left_frame, text="Tourner la ou les images", font=self.font,
                                            fg="black", bg=self.background_color)
        self.rotation_label.pack(padx=self.massive_x_separation, pady=self.large_y_separation)

        self.rotation_choice = ttk.Combobox(self.left_frame, values=self.degres)
        self.rotation_choice.current(0)
        self.rotation_choice.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.rotation_test = tkinter.Button(self.left_frame, text="Essayer", font=self.font, bg='white',
                                            command=self.try_rotation)
        self.rotation_test.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.rotation_confirm = tkinter.Button(self.left_frame, text="Valider", font=self.font, bg='white',
                                               command=self.confirm_rotation)
        self.rotation_confirm.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.filter_label = tkinter.Label(self.right_frame, text="Appliquer un filtre", font=self.font,
                                          bg=self.background_color, fg="black")
        self.filter_label.pack(padx=self.massive_x_separation)

        self.filter_choice = ttk.Combobox(self.right_frame, values=self.filtres, state='readonly')
        self.filter_choice.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.filter_try = tkinter.Button(self.right_frame, text="Essayer", font=self.font, bg='white',
                                         command=self.try_filter)
        self.filter_try.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.filter_confirm = tkinter.Button(self.right_frame, text="Valider", font=self.font, bg="white",
                                             command=self.confirm_filter)
        self.filter_confirm.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.type_label = tkinter.Label(self.right_frame, text="Choisir le format de destination", font=self.font,
                                        bg=self.background_color, fg="black")
        self.type_label.pack(padx=self.massive_x_separation, pady=self.large_y_separation)

        self.container_choice = ttk.Combobox(self.right_frame, values=self.types_supportes,
                                             state='readonly')  # On crée une combobox avec les conteneurs disponibles
        self.container_choice.current(0)  # On définit l'élément par défaut sur le premier élément de la liste
        self.container_choice.pack(pady=self.minimal_y_separation, padx=self.massive_x_separation)

        self.container_convert = tkinter.Button(self.bottom_frame, text="Convertir la ou les images",
                                                font=self.font, bg='white', command=self.convert_images)
        self.container_convert.pack(side=tkinter.LEFT, padx=self.usual_x_separation)

        # -------------- Partie Affichage des ensembles ----------------- #
        self.menu_bar = tkinter.Menu(self.window)  # création du menu de navigation
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)  # On définit un premier champ

        self.file_menu.add_command(label="Nouvelle instance", command=self.create_new_instance)
        self.file_menu.add_command(label="Fermer la fenêtre", command=self.destroy_instance)
        self.file_menu.add_command(label="Fermer toutes les fenêtres", command=self.destroy_all_instances)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)  # On nomme le premier champ

        self.window.config(menu=self.menu_bar)  # On ajoute le menu de navigation à la fenêtre

        # -------------- Partie Affichage des ensembles ----------------- #
        # On affiche les frames
        self.top_frame.pack(side=tkinter.TOP, pady=20)
        self.left_frame.pack(side=tkinter.LEFT)
        self.right_frame.pack(side=tkinter.RIGHT)
        self.bottom_frame.pack(side=tkinter.BOTTOM, pady=15)
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

        path = tkinter.filedialog.askdirectory(mustexist=True)
        assert isdir(path), "Le dossier n'existe pas"
        path = Path(path)
        assert len(listdir(path)) > 0, "Le dossier est vide"
        self.instance = FolderContainer(path)
        images_indexes = self.instance.get_indexes()

        # On modifie les valeurs possibles et par défaut des combos boxes
        self.fo_start_indexes.config(values=images_indexes[0:-1])
        self.fo_start_indexes.current(0)
        self.fo_end_indexes.config(values=images_indexes[1:])
        self.fo_end_indexes.current(len(images_indexes) - 2)

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
        assert isfile(path), "Aucun chemin sélectionné"
        self.instance = FilesContainers(path)

    def see_images(self):
        """
        Fonction qui permet d'afficher la ou les images voulues en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            L'image/Les images sont affichées
        """
        if type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            self.instance.see_images(start, end)
        elif type(self.instance) == FilesContainers:
            self.instance.show_image()

    def convert_images(self):
        """
        Fonction permet de convertir l'image/les images voulues dans le format voulu en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            L'image/Les images sont enregistrées sur la machine
        """
        if type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            dest_format = str(self.container_choice.get())
            self.instance.to_format(dest_format, start, end)
        elif type(self.instance) == FilesContainers:
            dest_format = str(self.container_choice.get())
            self.instance.convert_img(dest_format)

    def try_rotation(self):
        """
        Fonction qui affiche un aperçu de l'image/les images avec la rotation appliquée en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            L'image/Les images tournées sont affichées
        """
        if type(self.instance) == FilesContainers:
            angle = float(self.rotation_choice.get())
            self.instance.try_rotate_img(angle)
        elif type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            angle = float(self.rotation_choice.get())
            self.instance.try_rotations(angle, start, end)

    def confirm_rotation(self):
        """
        Fonction qui applique la rotation sur l'image/les images en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            La rotation est appliquée
        """
        if type(self.instance) == FilesContainers:
            angle = float(self.rotation_choice.get())
            self.instance.confirm_rotation(angle)
        elif type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            angle = float(self.rotation_choice.get())
            self.instance.apply_rotations(angle, start, end)

    def try_filter(self):
        """
        Fonction qui affiche un aperçu de l'image/les images avec le filtre appliqué en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            L'image/Les images sont affichées avec le filtre
        """
        if type(self.instance) == FilesContainers:
            filtre = str(self.filter_choice.get())
            if filtre == "BLUR":
                self.instance.try_filter(ImageFilter.BLUR)
            elif filtre == "CONTOUR":
                self.instance.try_filter(ImageFilter.CONTOUR)
            elif filtre == "DETAIL":
                self.instance.try_filter(ImageFilter.DETAIL)
            elif filtre == "EDGE_ENHANCE":
                self.instance.try_filter(ImageFilter.EDGE_ENHANCE)
            elif filtre == "EDGE_ENHANCE_MORE":
                self.instance.try_filter(ImageFilter.EDGE_ENHANCE_MORE)
            elif filtre == "EMBOSS":
                self.instance.try_filter(ImageFilter.EMBOSS)
            elif filtre == "FIND_EDGES":
                self.instance.try_filter(ImageFilter.FIND_EDGES)
            elif filtre == "SHARPEN":
                self.instance.try_filter(ImageFilter.SHARPEN)
            elif filtre == "SMOOTH":
                self.instance.try_filter(ImageFilter.SMOOTH)
            elif filtre == "SMOOTH_MORE":
                self.instance.try_filter(ImageFilter.SMOOTH_MORE)
            elif filtre == "GRAYSCALE":
                self.instance.try_filter("GRAYSCALE")
        elif type(self.instance) == FolderContainer:
            filtre = str(self.filter_choice.get())
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            if filtre == "BLUR":
                self.instance.try_filter(ImageFilter.BLUR, start, end)
            elif filtre == "CONTOUR":
                self.instance.try_filter(ImageFilter.CONTOUR, start, end)
            elif filtre == "DETAIL":
                self.instance.try_filter(ImageFilter.DETAIL, start, end)
            elif filtre == "EDGE_ENHANCE":
                self.instance.try_filter(ImageFilter.EDGE_ENHANCE, start, end)
            elif filtre == "EDGE_ENHANCE_MORE":
                self.instance.try_filter(ImageFilter.EDGE_ENHANCE_MORE, start, end)
            elif filtre == "EMBOSS":
                self.instance.try_filter(ImageFilter.EMBOSS, start, end)
            elif filtre == "FIND_EDGES":
                self.instance.try_filter(ImageFilter.FIND_EDGES, start, end)
            elif filtre == "SHARPEN":
                self.instance.try_filter(ImageFilter.SHARPEN, start, end)
            elif filtre == "SMOOTH":
                self.instance.try_filter(ImageFilter.SMOOTH, start, end)
            elif filtre == "SMOOTH_MORE":
                self.instance.try_filter(ImageFilter.SMOOTH_MORE, start, end)
            elif filtre == 'GRAYSCALE':
                self.instance.try_filter("GRAYSCALE", start, end)

    def confirm_filter(self):
        """
        Fonction qui applique le filtre sur l'image/les images en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            Le filtre est appliqué
        """
        if type(self.instance) == FilesContainers:
            filtre = str(self.filter_choice.get())
            if filtre == "BLUR":
                self.instance.confirm_filter(ImageFilter.BLUR)
            elif filtre == "CONTOUR":
                self.instance.confirm_filter(ImageFilter.CONTOUR)
            elif filtre == "DETAIL":
                self.instance.confirm_filter(ImageFilter.DETAIL)
            elif filtre == "EDGE_ENHANCE":
                self.instance.confirm_filter(ImageFilter.EDGE_ENHANCE)
            elif filtre == "EDGE_ENHANCE_MORE":
                self.instance.confirm_filter(ImageFilter.EDGE_ENHANCE_MORE)
            elif filtre == "EMBOSS":
                self.instance.confirm_filter(ImageFilter.EMBOSS)
            elif filtre == "FIND_EDGES":
                self.instance.confirm_filter(ImageFilter.FIND_EDGES)
            elif filtre == "SHARPEN":
                self.instance.confirm_filter(ImageFilter.SHARPEN)
            elif filtre == "SMOOTH":
                self.instance.confirm_filter(ImageFilter.SMOOTH)
            elif filtre == "SMOOTH_MORE":
                self.instance.confirm_filter(ImageFilter.SMOOTH_MORE)
            elif filtre == "GRAYSCALE":
                self.instance.confirm_filter("GRAYSCALE")
        elif type(self.instance) == FolderContainer:
            filtre = str(self.filter_choice.get())
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            if filtre == "BLUR":
                self.instance.apply_filter(ImageFilter.BLUR, start, end)
            elif filtre == "CONTOUR":
                self.instance.apply_filter(ImageFilter.CONTOUR, start, end)
            elif filtre == "DETAIL":
                self.instance.apply_filter(ImageFilter.DETAIL, start, end)
            elif filtre == "EDGE_ENHANCE":
                self.instance.apply_filter(ImageFilter.EDGE_ENHANCE, start, end)
            elif filtre == "EDGE_ENHANCE_MORE":
                self.instance.apply_filter(ImageFilter.EDGE_ENHANCE_MORE, start, end)
            elif filtre == "EMBOSS":
                self.instance.apply_filter(ImageFilter.EMBOSS, start, end)
            elif filtre == "FIND_EDGES":
                self.instance.apply_filter(ImageFilter.FIND_EDGES, start, end)
            elif filtre == "SHARPEN":
                self.instance.apply_filter(ImageFilter.SHARPEN, start, end)
            elif filtre == "SMOOTH":
                self.instance.apply_filter(ImageFilter.SMOOTH, start, end)
            elif filtre == "SMOOTH_MORE":
                self.instance.apply_filter(ImageFilter.SMOOTH_MORE, start, end)
            elif filtre == "GRAYSCALE":
                self.instance.apply_filter("GRAYSCALE", start, end)

    def try_crop(self):
        """
        Fonction qui affiche la version redimensionnée de l'image/les images en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            L'image/Les images sont affichées aux nouvelles dimensions
        """
        if type(self.instance) == FilesContainers:
            try:
                width = int(self.size_entry.get().split("*")[0])
                height = int(self.size_entry.get().split("*")[1])
                self.instance.try_resize((width, height))
            except ValueError:
                return
        elif type(self.instance) == FolderContainer:
            try:
                width = int(self.size_entry.get().split("*")[0])
                height = int(self.size_entry.get().split("*")[1])
                start = int(self.fo_start_indexes.get())
                end = int(self.fo_end_indexes.get())
                self.instance.try_resize((width, height), start, end)
            except ValueError:
                return

    def confirm_crop(self):
        """
        Fonction qui applique le recadrage de l'image/les images en faisant appel à la méthode de l'instance

        Retourne :
            Rien
        Pré-conditions :
            Rien
        Post-conditions :
            Le redimensionnement est appliqué
        """
        if type(self.instance) == FilesContainers:
            try:
                width = int(self.size_entry.get().split("*")[0])
                height = int(self.size_entry.get().split("*")[1])
                self.instance.confirm_resize((width, height))
            except ValueError:
                return
        elif type(self.instance) == FolderContainer:
            try:
                width = int(self.size_entry.get().split("*")[0])
                height = int(self.size_entry.get().split("*")[1])
                start = int(self.fo_start_indexes.get())
                end = int(self.fo_end_indexes.get())
                self.instance.apply_resize((width, height), start, end)
            except ValueError:
                return

    @staticmethod
    def create_new_instance():
        """
        Fonction qui créé une nouvelle instance de la classe UI et ouvre une nouvelle fenêtre.
        Cela permet de travailler sur plusieurs dossiers ou images individuelles en même temps

        Retourne :
            Rien
        Pré-conditions :
            Aucune
        Post-conditions :
            Une nouvelle fenêtre est ouverte et permet de travailler sur d'autres images
        """
        UI()

    def destroy_instance(self):
        """
        Fonction qui ferme la fenêtre actuelle. Le programme s'arrête si aucune autre fenêtre était ouverte

        Retourne :
            Rien
        Pré-conditions :
            Une instance de la classe UI existe
        Post-conditions :
            La fenêtre se ferme
        """
        self.window.destroy()

    @staticmethod
    def destroy_all_instances():
        """
        Fonction qui ferme toutes les fenêtres qui sont des instances de la classe UI
        Le programme est arrêté lors de l'exécution de cette fonction

        Retourne :
            Rien
        Pré-conditions :
            Aucune
        Post-conditions :
            Toutes les fenêtres qui sont des instances de la classe UI sont fermées
        """
        for ob in get_objects():
            if isinstance(ob, UI):
                ob.destroy_instance()


ui = UI()
