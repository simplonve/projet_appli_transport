#! /usr/bin/python
# -*- coding:utf-8 -*-

def lecture_fichier(path):
    '''lit un csv et le renvoi sous forme de tableau.
    decommentez ligne 20-21 pour un visuel
    dans le terminal'''
    with open(path, 'r') as fichier:
        read_fichier = fichier.read()
    tab_fichier = []
    for i in range(len(read_fichier)):
        if '\n' in read_fichier:
            index = read_fichier.index('\n')
            tab_fichier.append([read_fichier[:index]])
            read_fichier = read_fichier[index+1:]
    for j in range(len(tab_fichier)):
        ligne_tab = ';'.join(tab_fichier[j])
        ligne_tab = ligne_tab.split(';')
        tab_fichier[j] = ligne_tab
    #for row in tab_fichier:
    #    print(row)
    return tab_fichier

def supp_inutile(tableau):
    '''supprimer les colonnes inutile (contenant ND(non défini))'''
    index_to_pop = []
    first = True
    for i in range(len(tableau[0])-2):
        if tableau[0][i] == 'ND':
            tableau[0].pop(i)
            index_to_pop.append(i)

    for row in tableau:
        if first == True:
            first = False
            continue
        for to_pop in index_to_pop:
            row.pop(to_pop)

    return tableau

path = 'Le Cheylard - St Sauveur.csv'

fichier = lecture_fichier(path)

'''3 lignes en dessous, crée trois tableaux
pour chaque "catégories"
periode scolaire = scol
les deux autre ça se comprend'''
scol = [fichier[0]] + fichier[3:]
vac_ete = [fichier[1]] + fichier[3:]
autre_vac = [fichier[2]] + fichier[3:]


'''ne supprime rien dans scol = normal
probleme de ce soir : si on les lance un par un
marche niquel
si on lance les trois (ou les deux sans scol)
met pop index out of range car cet abruti
repasse sur la premiere ligne du tableau (qu'il a déjà traiter)
'''
scol = supp_inutile(scol)
autre_vac = supp_inutile(autre_vac)
vac_ete = supp_inutile(vac_ete)
