import os
import sae15_biblio

# On récupère les informations grâce au module créé précedemment (partie résumé materiel).
infos_cpu = sae15_biblio.acces_cpu.extraire_info_cpu("/proc/cpuinfo")
infos_disque = sae15_biblio.acces_disque_total.extraire_info_disque("/proc/partitions")
infos_disque_util = sae15_biblio.acces_disque_util.extraire_info_disque_utilise("/")
infos_memoire = sae15_biblio.acces_memoire.extraire_info_memoire("/proc/meminfo")
infos_systeme= sae15_biblio.acces_systeme.extraire_info_linux("/proc/version")
infos_cartes_reseaux = sae15_biblio.cartes_reseaux.obtenir_interfaces_reseau("/proc/net/dev")

#On établit les récapitulatifs divers ainsi que les diagrammes
processus = os.popen('ps aux | wc -l').read() #lecture du nombre de processus
processus = int(processus.strip()) - 1 #on soustrait l'entête
uptime = os.popen('uptime -p').read().strip() #stock l'uptime de la machine dans la variable uptime
ports_ouverts = os.popen('netstat -tuln').read().strip() #stock les ports UDP/TCP ouverts dans la variable ports_ouverts


def genere_page_web(nom_du_fichier,corps):
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
        <p>Information sur le processeur de la machine:  <br>{infos_cpu}</p>
        <p>Information sur l'utilisation du disque de la machine : <br>Taille totale du disque : {infos_disque} Go<br>Utilisation du disque : {infos_disque_util} Go</p>
        <p>Information sur l'OS de la machine : {infos_systeme}</p>
        <p>Information sur la mémoire de la machine:
        <br>Mémoire totale : {infos_memoire[0]} Go
        <br>Mémoire libre : {infos_memoire[1]} Mo</p>
        <p>Nom de(s) carte(s) réseau(x) de la machine : {infos_cartes_reseaux[0]}</p>
        <p>Information sur le(s) carte(s) graphique(s) de la machine : </p>
        <p>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
        <p> Nombre de processus actifs sur la machine : {processus}<p>
        <p> Temps total depuis que le serveur est lancé : {uptime}<p>
        </body>
        </html>
    """.format(titre_page=titre_page,infos_cpu=infos_cpu,infos_disque=infos_disque,infos_disque_util=infos_disque_util,infos_systeme=infos_systeme,infos_memoire=infos_memoire,infos_cartes_reseaux=infos_cartes_reseaux,processus=processus,uptime=uptime)
    genere_page_web("../html/compil-proc.html",corps)
    os.system("firefox file://" + os.path.abspath("../html/compil-proc.html")) #ouvre la page sur Firefox après la génération de cette dernière

if __name__ == "__main__":
    main()