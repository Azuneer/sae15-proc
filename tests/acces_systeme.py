import re

def extraire_info_linux():
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

# Tester la fonction
result = extraire_info_linux()
print(result)

