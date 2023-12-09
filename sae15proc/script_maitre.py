import re 
import os
import sae15_biblio

# On récupère les informations grâce au module créé précedemment.
infos_cpu = sae15_biblio.acces_cpu.extraire_info_cpu("/proc/cpuinfo")
infos_disque = sae15_biblio.acces_disque_total.extraire_info_disque("/proc/partitions")
infos_memoire = sae15_biblio.acces_memoire.extraire_info_memoire("/proc/meminfo")
infos_systeme= sae15_biblio.acces_systeme.extraire_info_linux("/proc/version")
infos_cartes_reseaux = sae15_biblio.cartes_reseaux.obtenir_interfaces_reseau("/proc/net/dev")

# On affiche le contenu des variables (test).
print("Informations sur le CPU:")
print(infos_cpu)

print("\nInformations sur le disque:")
print(infos_disque)

print("\nInformations sur la mémoire:")
print(infos_memoire)

print("\nInformations sur le système Linux:")
print(infos_systeme)

print("\nInformations sur les cartes réseau:")
print(infos_cartes_reseaux)