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
            partitions_content = f.read()
        
        #Utilisation des expressions régulières pour faire correspondre les infos recherchées 
        correspondance = re.search(r'\s+\d+\s+\d+\s+(\d+)\s+[sh]d[a-z]', partitions_content)
        print(correspondance)
        
        if correspondance:
            taille_totale = round((int(correspondance.group(1)) / (1024 ** 2)),2) #taille en GB, arrondie avec la fonction round()
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
            
print(extraire_info_disque("/proc/partitions"))
