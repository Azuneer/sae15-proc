"""
.. module:: acces_disque_util
  :platform: Unix, windows
  :synopsis: module de lecture de la taille utilisée du disque auquel la racine est montée 

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import psutil

def extraire_info_disque_utilise(chemin_fichier):
    """ Fonction qui permets d'extraire la taille utilisée du disque dur

    :param chemin_fichier: chemin de la racine ou de n'importe quel fichier
    :type chemin_fichier: str
    :returns: la utilisée du disque
    :rtype: float
    :raises: TypeError
    :example:

    .. code-block:: python

     taille_util = extraire_info_disque_utilise("/")

    """
    try:
        informations = psutil.disk_usage(chemin_fichier) # On utilise la fonction disk_usage du module Psutil pour recuperer l'utilisation du disque principal a l'instant T
        taille_utilisee = round(informations.used / (1024**3),2)  # Taille utilisée en GB que l'on arrondie a deux chiffres apres la virgule.
        
        return taille_utilisee
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        return None
