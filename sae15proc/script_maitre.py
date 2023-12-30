"""
.. module:: script_maitre
  :platform: Unix, windows
  :synopsis: programme maitre, qui génère la page et récupère les informations du PC grâce au différents modules

.. moduleauthor:: GADONNAUD Ewen <ewen.gadonnaud@etu.univ-poitiers.fr> & BRUNEAU Théo <theo.bruneau@etu.univ-poitiers.fr>
"""

import os
import sys
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
    chemin_gen = sys.argv[1]
    sae15_biblio.disque_pie.disque_pie()
    sae15_biblio.memoire_pie.memoire_pie() # exécute la génération du diagramme à chaque appel de la fonction main()
    titre_page = "Compil page"
    corps = """
            <?xml version=\"1.0\" encoding=\"UTF-8\" ?>
        <!DOCTYPE html>
        <html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">
        <head>
        <title>{titre_page}</title>
        <link rel="stylesheet" type="text/css" href="../css/principale.css" media="screen" />
			<link rel="stylesheet" type="text/css" href="../css/impress.css"media="print"  />
        </head>
        <header>
        <h1>Page de compilation des données contenue dans le dossier /proc de Linux
        </h1>
        </header>
        <body>
        <h3>Information sur le processeur de la machine:</h3>  <p>{infos_cpu}</p>
        <h3>Information sur l'utilisation du disque de la machine :</h3><h4>Taille totale du disque :</h4><p> {infos_disque} Go</p><h4>Utilisation du disque :</h4> <p>{infos_disque_util} Go</p>
        <h3>Information sur l'OS de la machine :</h3><p> {infos_systeme}</p>
        <h3>Information sur la mémoire de la machine:</h3>
        <h4>Mémoire totale :</h4> <p>{infos_memoire[0]} Go</p>
        <h4>Mémoire utilisée :</h4> <p>{infos_memoire[2]} Mo</p>
        <h4>Mémoire libre :</h4> <p>{infos_memoire[1]} Mo</p>
        <h3>Nom de(s) carte(s) réseau(x) de la machine :</h3> <p>{infos_cartes_reseaux[0]}</p>
        <h3>Information sur le(s) carte(s) graphique(s) de la machine : </h3>
        <p>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
        <p> Nombre de processus actifs sur la machine : {processus}<p>
        <p> Temps total depuis que le serveur est lancé : {uptime}<p>
        <p> Ports UDP/TCP ouverts : {ports_ouverts} </p>
        <p>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
        <p> Graphique camembert représentant l'utilisation de la mémoire actuelle : <p>
        <img src="../sae15proc/plots/camembert_memoire.png">
        <p> Graphique camembert représentant l'utilisation du disque <p>
        <img src="../sae15proc/plots/camembert_disque.png">
        </body>
        </html>
    """.format(titre_page=titre_page,infos_cpu=infos_cpu,infos_disque=infos_disque,infos_disque_util=infos_disque_util,infos_systeme=infos_systeme,infos_memoire=infos_memoire,infos_cartes_reseaux=infos_cartes_reseaux,processus=processus,uptime=uptime,ports_ouverts=ports_ouverts)
    genere_page_web(chemin_gen,corps)
    os.system("firefox file://" + os.path.abspath(chemin_gen + "compil-proc.html")) #ouvre la page sur Firefox après la génération de cette dernière

if __name__ == "__main__":
    main()
