"""
.. module:: acces_memoire
  :platform: Unix, windows
  :synopsis: module de lecture d'informations de la mémoire libre (/proc/meminfo)

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import re

def extraire_info_memoire(chemin_fichier):
    """ Fonction qui permets d'extraire la mémoire libre et la mémoire totale du système
    
    :param chemin_fichier: chemin du fichier /proc/meminfo
    :type chemin_fichier: str
    :returns: la mémoire totale et la mémoire libre.
    :rtype: float
    :raises: TypeError
    :example:
    
    .. code-block:: python
     
     memoire = extraire_info_memoire("/proc/meminfo")

    """
    try:
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()

            # Utilisation de expressions régulières pour extraire des lignes spécifiques
            pattern_total = re.compile(r'MemTotal:\s+(\d+) kB') # Cherche dans l'entree brute une ligne commencant par "MemTotal:" suivi d'un ou plusieurs espace (\s+) puis d'un ou plusieurs chiffres (\d+)
            pattern_libre = re.compile(r'MemFree:\s+(\d+) kB') # Pareil ici 

            # Recherche des correspondances dans le contenu
            match_total = pattern_total.search(contenu) 
            match_libre = pattern_libre.search(contenu)

            # Affichage des résultats
            if match_total and match_libre:
                total_memory = int(match_total.group(1)) / 1024  # Convertir en mégaoctets
                free_memory = int(match_libre.group(1)) / 1024  # Convertir en mégaoctets
                return (total_memory,free_memory)

    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'existe pas.")
    except PermissionError:
        print(f"Permission refusée pour accéder au fichier {chemin_fichier}.")

