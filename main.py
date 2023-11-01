from folderConverter import FolderContainer
from convert_file import FilesContainers
from pathlib import Path
import tkinter
import tkinter.filedialog
from tkinter import ttk
from PIL import ImageFilter


class UI:
    def __init__(self):
        self.instance = None

        self.types_supportes = ['JPEG', 'PNG', 'ICO', "GIF", "WEBP", "TIFF", "PDF"]  # Types dans lesquels on peut convertir les fichiers
        self.degres = ["0.0", "45.0", "90.0", "135.0", "180.0", "225.0", "270.0", "315.0"]  # Angles de rotation par défaut
        self.filtres = ["NONE", "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]  # Filtres disponibles

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

        # --------------- Partie Fichiers --------------- #

        self.fi_rotations = ttk.Combobox(self.left_frame, values=self.degres)
        self.fi_rotations.current(0)
        self.fi_rotations.pack()

        self.fi_rotate_try = tkinter.Button(self.left_frame, text="Essayer", font=("Arial", 12), bg='white', command=self.try_file_rotation)
        self.fi_rotate_try.pack(pady=2)

        self.fi_rotate_confirm = tkinter.Button(self.left_frame, text="Valider", font=("Arial", 12), bg="white", command=self.confirm_file_rotation)
        self.fi_rotate_confirm.pack(pady=2)

        self.fi_filter_choice = ttk.Combobox(self.left_frame, values=self.filtres, state="readonly")
        self.fi_filter_choice.pack(pady=5)

        self.fi_filter_try = tkinter.Button(self.left_frame, text="Essayer", font=("Arial", 12), bg="white", command=self.try_file_filter)
        self.fi_filter_try.pack(pady=2)

        self.fi_filter_confirm = tkinter.Button(self.left_frame, text="Valider", font=("Arial", 12), bg="white", command=self.confirm_file_filter)
        self.fi_filter_confirm.pack(pady=2)

        self.fi_size_entry = tkinter.Entry(self.left_frame, font=("Arial", 12), bg='white')
        self.fi_size_entry.insert(0, "Largeur*Hauteur")
        self.fi_size_entry.pack(pady=5)

        self.fi_size_try = tkinter.Button(self.left_frame, text="Essayer", font=("Arial", 12), bg="white", command=self.try_file_crop)
        self.fi_size_try.pack(pady=2)

        self.fi_size_confirm = tkinter.Button(self.left_frame, text="Valider", font=("Arial", 12), bg='white', command=self.confirm_file_crop)
        self.fi_size_confirm.pack(pady=2)

        self.show_image = tkinter.Button(self.left_frame, text="Voir l'image", font=("Arial", 12), bg='white',
                                         command=self.see_images)
        self.show_image.pack(pady=20)

        self.fi_container_choice = ttk.Combobox(self.left_frame, values=self.types_supportes, state='readonly')
        self.fi_container_choice.current(0)
        self.fi_container_choice.pack()

        self.convert_file = tkinter.Button(self.left_frame, text="Convertir l'image", font=("Arial", 12), bg='white', command=self.convert_images)
        self.convert_file.pack(pady=20)

        # --------------- Partie Dossiers ----------------- #

        self.fo_start_indexes = ttk.Combobox(self.right_frame, state='readonly')
        self.fo_start_indexes.pack(pady=20)

        self.fo_end_indexes = ttk.Combobox(self.right_frame, state='readonly')
        self.fo_end_indexes.pack()

        self.fo_rotation_choice = ttk.Combobox(self.right_frame, values=self.degres)
        self.fo_rotation_choice.current(0)
        self.fo_rotation_choice.pack(pady=5)

        self.fo_rotation_test = tkinter.Button(self.right_frame, text="Essayer", font=("Arial", 12), bg='white', command=self.try_file_rotation)
        self.fo_rotation_test.pack(pady=2)

        self.fo_rotation_confirm = tkinter.Button(self.right_frame, text="Valider", font=('Arial', 12), bg='white', command=self.confirm_file_rotation)
        self.fo_rotation_confirm.pack(pady=2)

        self.fo_filter_choice = ttk.Combobox(self.right_frame, values=self.filtres, state='readonly')
        self.fo_filter_choice.pack(pady=5)

        self.fo_filter_try = tkinter.Button(self.right_frame, text="Essayer", font=("Arial", 12), bg='white', command=self.try_file_filter)
        self.fo_filter_try.pack(pady=2)

        self.fo_filter_confirm = tkinter.Button(self.right_frame, text="Valider", font=("Arial", 12), bg="white", command=self.confirm_file_filter)
        self.fo_filter_confirm.pack(pady=2)

        self.fo_size_entry = tkinter.Entry(self.right_frame, font=("Arial", 12), bg='white')
        self.fo_size_entry.insert(0, "Largeur*Hauteur")
        self.fo_size_entry.pack(pady=5)

        self.fo_size_try = tkinter.Button(self.right_frame, text="Essayer", font=("Arial", 12), bg='white', command=self.try_file_crop)
        self.fo_size_try.pack(pady=2)

        self.fo_size_confirm = tkinter.Button(self.right_frame, text="Valider", font=("Arial", 12), bg='white', command=self.confirm_file_crop)
        self.fo_size_confirm.pack(pady=2)

        self.see_images_btn = tkinter.Button(self.right_frame, text="Voir les images du dossier", font=("Arial", 12),
                                             bg='white',
                                             command=self.see_images)
        self.see_images_btn.pack(pady=20)

        self.fo_container_choice = ttk.Combobox(self.right_frame, values=self.types_supportes,
                                                state='readonly')  # On crée une combobox avec les conteneurs disponibles
        self.fo_container_choice.current(0)  # On définit l'élément par défaut sur le premier élément de la liste
        self.fo_container_choice.pack()

        self.fo_container_convert = tkinter.Button(self.right_frame, text="Convertir les images du dossier",
                                                   font=("Arial", 12), bg='white', command=self.convert_images)
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

    def see_images(self):
        """
        Fonction qui permet d'afficher les images voulues
        """
        if type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            self.instance.see_images(start, end)
        elif type(self.instance) == FilesContainers:
            self.instance.show_image()

    def convert_images(self):
        """
        Fonction permet de convertir les images voulues dans le format voulu
        """
        if type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            dest_format = str(self.fo_container_choice.get())
            self.instance.to_format(dest_format, start, end)
        elif type(self.instance) == FilesContainers:
            dest_format = str(self.fi_container_choice.get())
            self.instance.convert_img(dest_format)

    def try_file_rotation(self):
        """
        Fonction qui appelle FilesContainers.preview_rotate_img(degre) pour afficher un aperçu de l'image avec la rotation appliquée
        """
        if type(self.instance) == FilesContainers:
            angle = float(self.fi_rotations.get())
            self.instance.try_rotate_img(angle)
        elif type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            angle = float(self.fo_rotation_choice.get())
            self.instance.try_rotations(angle, start, end)

    def confirm_file_rotation(self):
        """
        Fonction qui applique la rotation sur l'image
        """
        if type(self.instance) == FilesContainers:
            angle = float(self.fi_rotations.get())
            self.instance.confirm_rotation(angle)
        elif type(self.instance) == FolderContainer:
            start = int(self.fo_start_indexes.get())
            end = int(self.fo_end_indexes.get())
            angle = float(self.fo_rotation_choice.get())
            self.instance.apply_rotations(angle, start, end)

    def try_file_filter(self):
        """
        Fonction qui affiche un aperçu de l'image avec le filtre appliqué
        """
        if type(self.instance) == FilesContainers:
            filtre = str(self.fi_filter_choice.get())
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
        elif type(self.instance) == FolderContainer:
            filtre = str(self.fo_filter_choice.get())
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

    def confirm_file_filter(self):
        """
        Fonction qui applique le filtre sur l'image
        """
        if type(self.instance) == FilesContainers:
            filtre = str(self.fi_filter_choice.get())
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
        elif type(self.instance) == FolderContainer:
            filtre = str(self.fo_filter_choice.get())
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

    def try_file_crop(self):
        """
        Fonction qui affiche la version redimensionnée de l'image
        """
        if type(self.instance) == FilesContainers:
            try:
                width = int(self.fi_size_entry.get().split("*")[0])
                height = int(self.fi_size_entry.get().split("*")[1])
                self.instance.try_resize((width, height))
            except ValueError:
                return
        elif type(self.instance) == FolderContainer:
            try:
                width = int(self.fo_size_entry.get().split("*")[0])
                height = int(self.fo_size_entry.get().split("*")[1])
                start = int(self.fo_start_indexes.get())
                end = int(self.fo_end_indexes.get())
                self.instance.try_resize((width, height), start, end)
            except ValueError:
                return

    def confirm_file_crop(self):
        """
        Fonction qui applique le recadrage de l'image
        """
        if type(self.instance) == FilesContainers:
            try:
                width = int(self.fi_size_entry.get().split("*")[0])
                height = int(self.fi_size_entry.get().split("*")[1])
                self.instance.confirm_resize((width, height))
            except ValueError:
                return
        elif type(self.instance) == FolderContainer:
            try:
                width = int(self.fo_size_entry.get().split("*")[0])
                height = int(self.fo_size_entry.get().split("*")[1])
                start = int(self.fo_start_indexes.get())
                end = int(self.fo_end_indexes.get())
                self.instance.apply_resize((width, height), start, end)
            except ValueError:
                return


ui = UI()
