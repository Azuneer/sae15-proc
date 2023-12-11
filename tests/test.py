import sae15_biblio

memoire = sae15_biblio.acces_memoire.extraire_info_memoire("/proc/meminfo")
print(memoire[0])
