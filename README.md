# PymConv

Un programme python simple qui permet de convertir des images et des dossiers d'images ainsi que de faire des retouches rapides.

## Pourquoi avoir créé Pymconv ?

Nous sommes partis d'un constat simple : lorsque l'on souhaite convertir une image, on se dirige souvent vers les sites de conversion en ligne. Et en local ? Malheureusement, peu d'options légères accomplissent cette tâche. La plupart sont des logiciels de retouche d'images complets et ne proposent même pas tous les formats que PymConv propose. 
Photoshop par exemple ne peut qu'enregistrer des images aux formats *jpg, png, gif*. Vous pouvez dire adieu au *ico* pour les icones Windows ou au *webp* qui se démocratise sur le web.

PymConv est un programme qui ne propose que de la conversion et des retouches extrêmement rapides afin de rester rapide, utile et simple d'utilisation que vous souhaitiez convertir une image ou même 100 !


## Formats supportés

PymConv est capable de lire des fichiers de type *jpg, png, ico, gif, webp, tiff, heic*
PymConv est capable d'enregistrer les images dans les formats : *jpeg, png, ico, webp, gif, tiff, pdf*

La transparence est supportée pour les formats *png, ico, gif, webp, tiff*. Si une image avec un partie transparente est convertie dans un format qui ne prend pas en charge la transparence, la zone transparente est remplacée par du noir.

## Modifications possibles

PymConv offre plusieurs types de retouches rapides :
- Rotation (en sens anti-horaire)
- Redimmensionnement (change la hauteur et la largeur de l'image sans rogner les bords)
- Filtres (Tous les filtres sont issus du module pillow, à l'exception de la nuance de gris qui est une convertion dans le mode 'L' --> [Voir les modes](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes) & [Voir les filtres](https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html pour plus d'information)

## Modules utilisés

Pour fonctionner correctement, PymConv utilise plusieurs modules qui sont :
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [pillow](https://pillow.readthedocs.io/en/stable/)
- [pillow_heif](https://github.com/bigcat88/pillow_heif)
- [os](https://docs.python.org/3/library/os.html)
- [pathlib](https://docs.python.org/pl/3.13/library/pathlib.html)
- [gc](https://docs.python.org/3/library/gc.html)
