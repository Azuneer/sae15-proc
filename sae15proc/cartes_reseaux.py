"""
.. module:: cartes_reseaux
  :platform: Unix, windows
  :synopsis: module de lecture d'informations des interfaces réseaux (/proc/net/dev)

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import re

def obtenir_interfaces_reseau():
    """ Fonction qui permets d'extraire les interfaces réseaux présentes sur le système
    
    :param chemin_fichier: chemin du fichier /proc/net/dev
    :returns: les interfaces réseaux présentes sur le système
    :rtype: str
    :raises: TypeError
    :example:
    
    .. code-block:: python
     
     interfaces_reseau = obtenir_interfaces_reseau("/proc/net/dev)

    """
    interfaces = []
    try:
        with open('/proc/net/dev', 'r') as f:
            network_info = f.read()

        interfaces_match = re.findall(r'(\w+):\s+\d+', network_info)

        for interface in interfaces_match:
            if interface != 'lo':
                interfaces.append(interface)

    except FileNotFoundError:
        print("Le fichier /proc/net/dev n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

    return interfaces
