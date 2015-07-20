#! /usr/bin/python
# -*- coding:utf-8 -*-

def lecture_fichier(path):
    '''lit un csv ou un txt et le renvoi sous forme de tableau.'''
    with open(path, 'r') as fichier:
        read_fichier = fichier.read()

    tab_fichier = []
    saut_de_ligne = True

    while saut_de_ligne:
        if '\n' in read_fichier:
            index = read_fichier.index('\n')
            tab_fichier.append([read_fichier[:index]])
            read_fichier = read_fichier[index+1:]
        else:
            saut_de_ligne = False

    for j in range(len(tab_fichier)):
        ligne_tab = ';'.join(tab_fichier[j])
        ligne_tab = ligne_tab.split(';')
        tab_fichier[j] = ligne_tab

    return tab_fichier

def suppr_inutile(tableau):
    '''supprimer les colonnes inutile (contenant ND(non désservi))'''
    index_to_pop = []
    first = True
    for i in range(len(tableau[0])-2):
        if tableau[0][i] == 'ND':
            tableau[0].pop(i)
            index_to_pop.append(i)

    for row in tableau:
        if first == True or len(row) == len(tableau[0]):
            first = False
            continue
        for to_pop in index_to_pop:
            row.pop(to_pop)

    return tableau

'''chemin du fichier a traiter'''
path = 'st sauveur le cheylard.txt'

fichier = lecture_fichier(path)

'''Création de trois tableaux
pour chaque "catégories"
scol = periode scolaire
...'''
scol = [fichier[0]] + fichier[3:]
vac_ete = [fichier[1]] + fichier[3:]
autre_vac = [fichier[2]] + fichier[3:]

scol = suppr_inutile(scol)
autre_vac = suppr_inutile(autre_vac)
vac_ete = suppr_inutile(vac_ete)

'''decoupe du chemin du fichier pour enlever espace et extension'''
path = path.split(' ')
path = path[:len(path)-1]+path[len(path)-1].split('.')
path.pop(len(path)-1)
path = '_'.join(path)

'''inscrit les tableaux dans lignes.py
path fichier + = [ + les trois tableau + ]
avec un saut de ligne après chaque tableaux
'''
with open('lignes.py', 'a') as bd:
    bd.write(path+' = [\n'+str(scol)+',\n'+str(autre_vac)+',\n'+str(vac_ete)+']')
