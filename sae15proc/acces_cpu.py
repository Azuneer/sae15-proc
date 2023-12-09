"""
.. module:: acces_cpu
  :platform: Unix, windows
  :synopsis: module de lecture d'informations sur le/les CPU(s) (modèle du CPU, sa fréquence et la taille de son cache)

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import re

def extraire_info_cpu(chemin_fichier):
    """ Fonction qui permets d'extraire des informations sur le/les CPU(s) (modèle du CPU, sa fréquence et la taille de son cache)
    
    :param chemin_fichier: chemin du fichier /proc/cpuinfo
    :type chemin_fichier: str
    :returns: la mémoire totale et la mémoire libre.
    :rtype: str, int, float
    :raises: TypeError
    :example:
    
    .. code-block:: python
     
     cpu_infos = extraire_info_cpu("/proc/cpuinfo")

    """
    try:
        with open(chemin_fichier, 'r') as f:
            contenu_cpuinfo = f.read()

        # Utilisation des expressions régulières pour faire correspondre les infos recherchées (modèle,fréquence,cache)
        type_correspondance = re.search(r'model name\s+:\s+(.*)', contenu_cpuinfo)
        frequence_correspondance = re.search(r'cpu MHz\s+:\s+([\d.]+)', contenu_cpuinfo)
        cache_correspondance = re.search(r'cache size\s+:\s+(\d+) KB', contenu_cpuinfo)

        if type_correspondance and frequence_correspondance and cache_correspondance:
            cpu_type = type_correspondance.group(1)
            cpu_frequence = float(frequence_correspondance.group(1))
            cache_taille = int(cache_correspondance.group(1))
            return f"CPU Type: {cpu_type}, Fréquence: {cpu_frequence} MHz, Taille du cache: {cache_taille} KB" #Pas besoin de formatter les informations, elles le sont déjà sous le bon format
        else:
            print("Impossible de récupérer les informations sur le CPU.")
            return None

    except FileNotFoundError:
        print("Le fichier /proc/cpuinfo n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        return None