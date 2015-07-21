#! /usr/bin/python
# -*- coding:utf-8 -*-

from lignes import *
from time import localtime, strftime

def recup_list_ville_kivy():
    '''recupère la liste des villes et la renvoi sous forme de tableau'''
    ville_aller = []
    ville_retour = []

    for i in range(len(Le_Cheylard_Valence[0])):
        if Le_Cheylard_Valence[0][i][0] not in ville_aller:
            ville_aller.append('Ville : '+Le_Cheylard_Valence[0][i][0]+' Arret : '+Le_Cheylard_Valence[0][i][1])

    for i in range(len(Valence_le_cheylard[0])):
        if Valence_le_cheylard[0][i][0] not in ville_retour:
            ville_retour.append('Ville : '+Valence_le_cheylard[0][i][0]+' Arret : '+Valence_le_cheylard[0][i][1])

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
'''valeur d'entrée'''
periode = 'scol'
aujourdhui = 'M'
ville_depart = 'LE CHEYLARD'
ville_arriver = 'CHARMES'
heure = strftime("%H:%M", localtime())

index_jour = []

ville_aller, ville_retour = recup_list_ville()
print(ville_aller)
'''recup le sens voulu grace a la position des ville dans la liste'''
if ville_depart in ville_aller and ville_arriver in ville_aller:
    if ville_aller.index(ville_depart) < ville_aller.index(ville_arriver):
        fiche_horaire = Le_Cheylard_Valence
    else:
        fiche_horaire = Valence_le_cheylard

'''recup la fiche horaire pour la periode voulue'''
for i in range(2):
    if fiche_horaire[i][0][0] == periode:
        fiche_horaire = fiche_horaire[i]

'''recup l'index des colonnes voulue (jour) pour selectionner les bons horaires'''
for jour in fiche_horaire[0]:
    if aujourdhui in jour:
        index_jour.append(fiche_horaire[0].index(jour))

'''recup lignes contenant depart et arriver'''
depart = []
arriver = []
index_jour.reverse()
index_jour.append(1)
index_jour.append(0)
index_jour.reverse()
for row in fiche_horaire:
    if row[0] == ville_depart:
        for index in index_jour:
            depart.append(row[index])
    elif row[0] == ville_arriver:
        for index in index_jour:
            arriver.append(row[index])

print(depart)
print(arriver)



