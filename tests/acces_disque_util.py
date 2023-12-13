import psutil

def extraire_info_disque_utilise():
    try:
        informations = psutil.disk_usage('/')
        taille_utilisee = round(informations.used / (1024 * 1024),2)  # Taille utilisée en GB
        
        return taille_utilisee
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        return None

print(extraire_info_disque_utilise())
