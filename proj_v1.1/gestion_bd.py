#! /usr/bin/python
# -*- coding:utf-8 -*-
'''Pour se servir de ce gestionnaire il suffit de :

################################################################
import gestion_bd

#selectionner les ville et retour sous forme de tableau
villes = select_ville()

#selectionner les bons horaires
depart, arriver = gestion_bd.select(periode, aujourdhui, ville_depart, ville_arriver, heure)
################################################################

depart et arriver seront ensuite des tableau sous cette forme :
['LE CHEYLARD', 'Av.Saunier/GrpeScol.', '11:45', '17:05']

Les valeur données au select sont sous cette forme :

periode = 'scol' ou 'vac_ete' ou 'autres_vac'
aujourdhui = 'L' ou 'M' ou 'm' ou 'J' ou 'V' ou 'S' ou 'D'
ville_depart = 'LE CHEYLARD'
ville_arriver = 'CHARMES'

L'heure doit être sous cette forme : 1045

Pour arriver à ceci :

################################################################
heure = strftime("%H:%M", localtime())
heure = heure.split(':')
heure = int(str(heure[0])+str(heure[1]))
################################################################
'''

from Base_de_donnees import *
from time import localtime, strftime

###############################################################
'''section insertion'''

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

def insert():
    '''chemin du fichier a traiter'''
    path = input('nom du fichier a inserer')
    path = 'sources/'+path

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

###############################################################
def select_ville():
    '''recupère la liste des villes et la renvoi sous forme de tableau'''
    ville_aller = []
    ville_retour = []

    for i in range(len(Le_Cheylard_Valence[0])):
        if Le_Cheylard_Valence[0][i][0] not in ville_aller:
            ville_aller.append(Le_Cheylard_Valence[0][i][0]+' - '+Le_Cheylard_Valence[0][i][1])

    for i in range(len(Valence_le_cheylard[0])):
        if Valence_le_cheylard[0][i][0] not in ville_retour:
            ville_retour.append(Valence_le_cheylard[0][i][0]+' - '+Valence_le_cheylard[0][i][1])

    ville_aller.pop(0)
    ville_retour.pop(0)
    return ville_aller

def recup_list_ville():
    '''recupère la liste des villes et la renvoi sous forme de tableau'''
    ville_aller = []
    ville_retour = []

    for i in range(len(Le_Cheylard_Valence[0])):
        if Le_Cheylard_Valence[0][i][0] not in ville_aller:
            ville_aller.append(Le_Cheylard_Valence[0][i][0])

    for i in range(len(Valence_le_cheylard[0])):
        if Valence_le_cheylard[0][i][0] not in ville_retour:
            ville_retour.append(Valence_le_cheylard[0][i][0])

    ville_aller.pop(0)
    ville_retour.pop(0)
    return ville_aller, ville_retour

def select_sens(ville_depart, ville_aller, ville_arriver):
    '''recup le sens voulu grace a la position des ville dans la liste'''
    if ville_depart in ville_aller and ville_arriver in ville_aller:
        if ville_aller.index(ville_depart) < ville_aller.index(ville_arriver):
            fiche_horaire = Le_Cheylard_Valence
        else:
            fiche_horaire = Valence_le_cheylard
    return fiche_horaire

def select_periode(fiche_horaire, periode):
    '''recup la fiche horaire pour la periode voulue'''
    for i in range(2):
        if fiche_horaire[i][0][0] == periode:
            fiche_horaire = fiche_horaire[i]
    return fiche_horaire

def select_jour(fiche_horaire, aujourdhui):
    '''recup l'index des colonnes voulue (jour) pour selectionner les bons horaires'''
    index_jour = []
    for jour in fiche_horaire[0]:
        if aujourdhui in jour:
            index_jour.append(fiche_horaire[0].index(jour))
    index_jour.reverse()
    index_jour.append(1)
    index_jour.append(0)
    index_jour.reverse()
    return index_jour

def select_depart_arriver(fiche_horaire, index_jour, ville_depart, ville_arriver):
    '''recup lignes contenant depart et arriver'''
    depart = []
    arriver = []
    for row in fiche_horaire:
        buffer_depart = []
        buffer_arriver = []
        if row[0] == ville_depart:
            for index in index_jour:
                buffer_depart.append(row[index])
        elif row[0] == ville_arriver:
            for index in index_jour:
                buffer_arriver.append(row[index])
        if buffer_arriver != []:
            arriver.append(buffer_arriver)
        if buffer_depart != []:
            depart.append(buffer_depart)
    return depart, arriver

def select_depart(tableau, heure):
    '''renvoi la ville, l'arret et les horaire en fonction de l'heure
    ainsi que les index de la selection'''
    heure = 930#seulement pour les test !
    index_retour = []
    tab_retour = []
    for row in tableau:
        tab_selection = []
        for element in row:
            if element != tableau[0] or element != tableau[1]:
                try:
                    decoupe = element.split(':')
                    decoupe = int(str(decoupe[0])+str(decoupe[1]))
                    if decoupe > heure:
                        tab_selection.append(element)
                        index_retour.append(row.index(element))
                except:
                    index_retour.append(row.index(element))
                    tab_selection.append(element)
        tab_retour.append(tab_selection)
    index_retour = index_retour[:len(tab_retour[0])]
    return tab_retour, index_retour

def select_arriver(tableau, index):
    '''renvoi la ville, l'arret et les horaire en fonction des index'''
    tab_retour = []
    for row in tableau:
        tab_selection = []
        for element in row:
            if row.index(element) in index:
                tab_selection.append(element)
            else:
                continue
        tab_retour.append(tab_selection)
    return tab_retour

def select(periode, aujourdhui, ville_depart, ville_arriver, heure):
    ville_aller, ville_retour = recup_list_ville()
    fiche_horaire = select_sens(ville_depart, ville_aller, ville_arriver)
    fiche_horaire = select_periode(fiche_horaire, periode)
    index_jour = select_jour(fiche_horaire, aujourdhui)
    depart, arriver = select_depart_arriver(fiche_horaire, index_jour, ville_depart, ville_arriver)

    depart = depart[1:] #seulement pour la fiche horaire FH012
    depart, index_selection = select_depart(depart, heure)
    arriver = select_arriver(arriver, index_selection)
    return depart, arriver

def main():
    '''valeur d'entrée'''
    periode = 'scol'
    aujourdhui = 'M'
    ville_depart = 'LE CHEYLARD'
    ville_arriver = 'CHARMES'

    heure = strftime("%H:%M", localtime())
    heure = heure.split(':')
    heure = int(str(heure[0])+str(heure[1]))
    depart, arriver = select(periode, aujourdhui, ville_depart, ville_arriver, heure)

    for row in depart:
        print(row)

    for row in arriver:
        print(row)

if __name__ == '__main__':
    main()