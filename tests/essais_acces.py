import re

def extraire_info_memoire(chemin_fichier):
    try:
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()

            # Utilisation de expressions régulières pour extraire des lignes spécifiques
            pattern_total = re.compile(r'MemTotal:\s+(\d+) kB')
            pattern_libre = re.compile(r'MemFree:\s+(\d+) kB')

            # Recherche des correspondances dans le contenu
            match_total = pattern_total.search(contenu)
            match_libre = pattern_libre.search(contenu)

            # Affichage des résultats
            if match_total:
                total_memory = int(match_total.group(1)) / 1024  # Convertir en mégaoctets
                print(f"Total de mémoire : {total_memory:.2f} Mo")

            if match_libre:
                free_memory = int(match_libre.group(1)) / 1024  # Convertir en mégaoctets
                print(f"Mémoire libre : {free_memory:.2f} Mo")

    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'existe pas.")
    except PermissionError:
        print(f"Permission refusée pour accéder au fichier {chemin_fichier}.")

#utilisation pour le fichier /proc/meminfo
chemin_meminfo = '/proc/meminfo'
extraire_info_memoire(chemin_meminfo)