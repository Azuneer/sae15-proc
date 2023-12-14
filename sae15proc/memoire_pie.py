"""
.. module:: memoire_pie
  :platform: Unix, windows
  :synopsis: script de génération du graphique de la mémoire

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import sae15_biblio
import matplotlib.pyplot as plt

def memoire_pie():
    """ Fonction qui permets de calculer les pourcentages et de générer le graphique camembert qui est sauvegardé dans le répertoire plots/

    :returns: affiche le diagramme
    :example:

    .. code-block:: python

    memoire_pie()

    """
    # On calcule les grandeurs en premier lieu
    memoire = sae15_biblio.acces_memoire.extraire_info_memoire("/proc/meminfo") # la variable memoire est un couple
    memoire_totale = memoire[0] * 1024 # On transforme en MB pour avoir les mêmes dimensions
    memoire_libre = memoire[1]
    memoire_util = memoire_totale - memoire_libre # valeur de la memoire utilisée en MB
    pourcentage_util = (memoire_util/memoire_totale) * 100 # pourcentage de la mémoire utilisée 
    pourcentage_total = 100 - pourcentage_util
    
    # On passe à l'établissement des paramètres du graphique camembert
    titres = ["Mémoire utilisée", "Mémoire totale"] # les titres des grandeurs
    grandeurs = [pourcentage_total, pourcentage_util] # association des grandeurs au titres
    couleurs = ['#ff9999', '#66b3ff'] # les couleurs des grandeurs
    explode = (0.1,0) #permets de mettre en valeur la première slice du graphique, séparant bien les deux grandeurs
    
    # On génère le graphique camembert
    plt.pie(grandeurs, explode=explode, labels=titres, colors=couleurs, autopct='%1.1f%%', startangle=90) #les paramètres autocpt et startangle permettent d'assurer le bon affichage des grandeurs de pourcentage et l'angle initial
    plt.axis('equal') # assure que le ratio d'affichage corresponde bien à celui d'un cercle
    plt.title("Utilisation de la mémoire") # titre du graphique
    
    # On sauvegarde la figure et on l'affiche à l'écran (test)
    plt.savefig("plots/camembert_memoire.png") #sauvegarde dans le dossier plots
