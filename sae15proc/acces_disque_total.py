"""
.. module:: acces_disque_total
  :platform: Unix, windows
  :synopsis: module de lecture d'informations du disque, nottamment la taille totale du disque (/proc/partitions)

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import re

def extraire_info_disque(chemin_fichier):
    """ Fonction qui permets d'extraire la taille totale du disque dur

    :param chemin_fichier: chemin du fichier /proc/partitions
    :type chemin_fichier: str
    :returns: la taille totale du disque
    :rtype: float
    :raises: TypeError
    :example:

    .. code-block:: python

     taille_totale = extraire_info_disque("/proc/partitions")

    """
    # Le "try" permets d'encapsuler le code dans le cas ou une exception pourrait arriver
    try:
        #Lecture du fichier /proc/partitions
        with open(chemin_fichier, 'r') as f:
            contenu_partitions = f.read()

        #Utilisation des expressions régulières pour faire correspondre les infos recherchées
        correspondance = re.search(r'\s+\d+\s+\d+\s+(\d+)\s+([sh]d[a-z]*)', contenu_partitions)
        """
        L'expression reguliere est un peu plus longue ici car on veux capturer un pattern difficile d'acces

        On recherche ici un pattern qui correspond a un espace (\s+), un ou des chiffres (\d+), ainsi de suite
        jusqu'au premier groupe ou l'on recupere la taille totale qui n'est pas sous une forme lisible.

        La suite de l'expression reguliere permets de specifier le format exact du disque, ici sois un disque commencant par un "s" ou un "h",
        suivi obligatoirement d'un "d" et suivi d'une lettre de l'alphabet de "a" a "z". On utilise pas de chiffres ici, car c'est un disque tout entier
        que l'on souhaite capturer, et non pas une partition. Ainsi, on recupere EXACTEMENT un disque et non pas un autre peripherique.
        """

        if correspondance:
            taille_totale = round(int(correspondance.group(1)) / (1024 * 1024),2) #taille en GB, arrondie avec la fonction round()
            return taille_totale
        else:
            print("Impossible de récupérer la taille totale du disque")
            return None

    # On capture les deux types d'exceptions
    except FileNotFoundError:
        print("Le fichier /proc/partitions n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        return None
