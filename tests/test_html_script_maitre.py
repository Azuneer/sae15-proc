import re 
import os
import sae15_biblio

# On récupère les informations grâce au module créé précedemment.
infos_cpu = sae15_biblio.acces_cpu.extraire_info_cpu("/proc/cpuinfo")
infos_disque = sae15_biblio.acces_disque_total.extraire_info_disque("/proc/partitions")
infos_disque_util = sae15_biblio.acces_disque_util.extraire_info_disque_utilise()
infos_memoire = sae15_biblio.acces_memoire.extraire_info_memoire("/proc/meminfo")
infos_systeme= sae15_biblio.acces_systeme.extraire_info_linux()
infos_cartes_reseaux = sae15_biblio.cartes_reseaux.obtenir_interfaces_reseau()

# On affiche le contenu des variables (test).
print("Informations sur le CPU:")
print(infos_cpu) 

print("\nInformations sur le disque:")
print(infos_disque)

print("\nInformations sur la mémoire:")
print("Mémoire totale :",infos_memoire[0],"Mo","\nMémoire libre :",infos_memoire[1],"Mo")

print("\nInformations sur le système Linux:")
print(infos_systeme)

print("\nInformations sur la carte réseau active:")
print(infos_cartes_reseaux[0])

def genere_page_web(nom_du_fichier,titre_page,corps):
    try:
        f = open(nom_du_fichier,'w',encoding='utf-8')
        f.write(corps)
    except IOError as e:
        print("Erreur dans l\'ouverture du fichier \n", e)
    finally:
        f.close()

def main():
    titre_page = "Compil page"
    corps = """
            <?xml version=\"1.0\" encoding=\"UTF-8\" ?>
        <!DOCTYPE html>
        <html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">
        <style>
        table, th, td {{
        border:1px solid black;
        }}
        </style>
        <head>
        <title>{titre_page}</title>
        </head>
        <body>
        <p>information sur le processeur de la machine:{infos_cpu}</p>
        <p>information sur l'utilisation du disque de la machine:{infos_disque}<br>{infos_disque_util}</p>
        <p>information sur l'OS de la machine:{infos_systeme}</p>
        <p>information sur l'utilisation de la mémoire de la machine:
        <br>Mémoire total:{infos_memoire[0]}Mo
        <br>Mémoire utilisée:{infos_memoire[1]}Mo</p>
        <p>Nom de(s) carte(s) réseau(x) de la machine:{infos_cartes_reseaux}</p>
        <p>information sur le(s) carte(s) graphique(s) de la machine:</p>

        </body>
        </html>
    """.format(titre_page=titre_page,infos_cpu=infos_cpu,infos_disque=infos_disque,infos_disque_util=infos_disque_util,infos_systeme=infos_systeme,infos_memoire=infos_memoire,infos_cartes_reseaux=infos_cartes_reseaux)
    genere_page_web("./html_test/compil-proc.html",titre_page,corps)

main()
