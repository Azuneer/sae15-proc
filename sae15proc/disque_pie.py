

"""
.. module:: disque_pie
  :platform: Unix, windows
  :synopsis: script de génération du graphique du disque système

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import sae15_biblio
import matplotlib.pyplot as plt

def disque_pie():
    """ Fonction qui permets de calculer les pourcentages et de générer le graphique camembert qui est sauvegardé dans le répertoire plots/

    :returns: affiche le diagramme
    :example:

    .. code-block:: python

    disque_pie()

    """
    # On calcule les grandeurs en premier lieu
    taille_totale = sae15_biblio.acces_disque_total.extraire_info_disque("/proc/partitions")
    taille_util = sae15_biblio.acces_disque_util.extraire_info_disque_utilise("/")
    pourcentage_util = (taille_util/taille_totale) * 100 # pourcentage de la mémoire utilisée 
    pourcentage_total = 100 - pourcentage_util
    
    # On passe à l'établissement des paramètres du graphique camembert
    titres = ["Taille utilisée", "Taille totale"] # les titres des grandeurs
    grandeurs = [pourcentage_util, pourcentage_total] # association des grandeurs au titres
    couleurs = ['#ff9999', '#66b3ff'] # les couleurs des grandeurs
    explode = (0.1,0) #permets de mettre en valeur la première slice du graphique, séparant bien les deux grandeurs
    
    # On génère le graphique camembert
    plt.pie(grandeurs, explode=explode, labels=titres, colors=couleurs, autopct='%1.1f%%', startangle=90) #les paramètres autocpt et startangle permettent d'assurer le bon affichage des grandeurs de pourcentage et l'angle initial
    plt.axis('equal') # assure que le ratio d'affichage corresponde bien à celui d'un cercle
    plt.title("Utilisation du disque") # titre du graphique
    
    # On sauvegarde la figure et on l'affiche à l'écran (test)
    plt.savefig("plots/camembert_disque.png") #sauvegarde dans le dossier plots
