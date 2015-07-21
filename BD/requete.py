#! /usr/bin/python
# -*- coding:utf-8 -*-

from lignes import *
from time import localtime, strftime

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

'''valeur d'entrée'''
periode = 'scol'
aujourdhui = 'M'
depart = 'LE CHEYLARD'
arriver = 'CHARMES'
heure = strftime("%H:%M", localtime())

index_jour = []

ville_aller, ville_retour = recup_list_ville()

'''recup le sens voulu'''
if depart in ville_aller and arriver in ville_aller:
    if ville_aller.index(depart) < ville_aller.index(arriver):
        fiche_horaire = Le_Cheylard_Valence
    else:
        fiche_horaire = Valence_le_cheylard

'''recup la fiche horaire pour la bonne periode'''
for i in range(2):
    if fiche_horaire[i][0][0] == periode:
        fiche_horaire = fiche_horaire[i]

'''recup index jour pour selectionner les bons horaires'''
for jour in fiche_horaire[0]:
    if aujourdhui in jour:
        index_jour.append(fiche_horaire[0].index(jour))

'''recup lignes contenant depart et arriver'''
for row in fiche_horaire:
    if row[0] == depart:
        for index in index_jour:
            print(row)
    elif row[0] == arriver:
        print(row)

print(index_jour)



