"""
.. module:: acces_systeme
  :platform: Unix, windows
  :synopsis: module de lecture d'informations du système, nottamment la version du kernel Linux et son architecture (/proc/version)

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import re

def extraire_info_linux():
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
        with open('/proc/version', 'r') as f:
            version_info = f.read()

            version_recherche = re.compile(r'Linux version ([^\s]+) .*?\((.*?)\)')
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
