from folderConverter import folderContainer
from pathlib import Path
import tkinter
import tkinter.filedialog

path = ""


def open_folder():
    """
    Fonction qui ouvre un dossier avec tkinter.filedialog

    Returns :
        Le chemin de l'élément
    Pré-condition :
        Rien
    Post-condition :
        Affiche une interface pour sélectionner l'élément voulu et renvoie son chemin
    """
    global path = Path(tkinter.filedialog.askdirectory(mustexist=True))


def open_file():
    """
    Fonction qui ouvre un fichier avec tkinter.filedialog

    Returns :
        Le chemin de l'élément
    Pré-condition :
        Rien
    Post-condition :
        Affiche une interface pour sélectionner l'élément voulu et renvoie son chemin
    """
    return Path(tkinter.filedialog.askopenfilename())


def ui_window():
    """
     Fonction qui créé une interface graphique Tkinter pour l'application

     Returns :
        Rien
     Pré-condition :
        Aucune
     Post-condition :
        Une fenêtre s'affiche à l'écran
    """
    window = tkinter.Tk()
    window.title("PymConv")
    window.geometry("1080x720")
    window.config(background="#B2BABB")

    folder_button = tkinter.Button(window, text="Ouvrir un dossier", font=("Arial", 12), bg='white', command=open_folder)
    folder_button.pack()

    file_button = tkinter.Button(window, text="Ouvrir un fichier", font=("Arial", 12), bg='white', command=open_file)
    file_button.pack()

    window.mainloop()


ui_window()
