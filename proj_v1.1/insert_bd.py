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
    index = None
    IsND = True
    while IsND:
        if 'ND' not in tableau[0]:
            IsND = False
            break
        for row in tableau:
            if len(row) == len(tableau[0]) and len(row) <= 8:
                break
            if row == tableau[0] and 'ND' in row:
                index = tableau[0].index('ND')
                tableau[0].pop(index)
            else:
               row.pop(index)

    return tableau

def main():
    '''chemin du fichier a traiter'''
    path = 'sources/Valence le cheylard.txt'


    '''Création de trois tableaux
    pour chaque "catégories"
    scol = periode scolaire
    ...'''
    fichier = lecture_fichier(path)

    scol = [fichier[0]] + fichier[3:]
    scol = suppr_inutile(scol)

    fichier = lecture_fichier(path)

    autre_vac = [fichier[2]] + fichier[3:]
    autre_vac = suppr_inutile(autre_vac)

    fichier = lecture_fichier(path)

    vac_ete = [fichier[1]] + fichier[3:]
    vac_ete = suppr_inutile(vac_ete)


    '''decoupe du chemin du fichier pour enlever espace et extension'''
    path = path.split(' ')
    path = path[:len(path)-1]+path[len(path)-1].split('.')
    path.pop(len(path)-1)
    path = '_'.join(path)

    '''inscrit les tableaux dans Base_de_donnees.py
    path fichier + = [ + les trois tableau + ]
    avec un saut de ligne après chaque tableaux
    '''
    with open('Base_de_donnees.py', 'a') as bd:
        bd.write(path+' = [\n'+str(scol)+',\n'+str(autre_vac)+',\n'+str(vac_ete)+']\n')

if __name__ == '__main__':
    main()