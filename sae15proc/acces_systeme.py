"""
.. module:: acces_systeme
  :platform: Unix, windows
  :synopsis: module de lecture d'informations du système, nottamment la version du kernel Linux et son architecture (/proc/version)

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import re

def extraire_info_linux(chemin_fichier):
    """ Fonction qui permets d'extraire la version du kernel Linux et son architecture
    
    :param chemin_fichier: chemin du fichier /proc/version
    :type chemin_fichier: str
    :returns: la version du kernel Linux et son architecture.
    :rtype: str
    :raises: TypeError
    :example:
    
    .. code-block:: python
     
     systeme_version = extraire_info_linux("/proc/version")

    """
    try:
        with open(chemin_fichier, 'r') as f:
            version_info = f.read()

            version_recherche = re.compile(r'Linux version ([^\s]+) .*?\((.*?)\)')
            """
            Le premier groupe de capture corresponds a la version du noyeau Linux qui correspond a une sequence de caractere qui ne sont
            pas des espaces ([^\s]+) suivi d'un point, jusqu'au second groupe qui correspond a l'architecture qui est entre parentheses. 
            (l'utilisation des barres obliques corresponds exprime que nous cherchons ce qui est "litteralement" entre parentheses)
            """
            correspondance = version_recherche.search(version_info)

            if correspondance:
              # Extraire la version et l'architecture à de la correspondance effectuée
              linux_version = correspondance.group(1)
              architecture = correspondance.group(2)
              return f"Version Linux: {linux_version}, Architecture: {architecture}"
            else:
              return "Impossible d'extraire la version de Linux et son architecture."

    except FileNotFoundError:
        return "Le fichier /proc/info n'a pas été trouvé."
