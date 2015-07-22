#! /usr/bin/python
# -*- coding:utf-8 -*-
'''Pour se servir de ce gestionnaire il suffit de :

################################################################
import gestion_bd

#selectionner les ville et retour sous forme de tableau
villes = select_ville()

#selectionner les bons horaires
depart, arriver = gestion_bd.select(ville_depart, ville_arriver)
################################################################

depart et arriver seront ensuite des tableau sous cette forme :
['VILLE', 'ARRET', 'HORAIRE 1', 'HORAIRE 2', '...']

Les valeur données au select sont sous cette forme :

ville_depart = 'LE CHEYLARD'
ville_arriver = 'CHARMES'

Pour utiliser l'heure actuelle, dans select_depart(),
décommentez les lignes commentées et commentez la ligne de test
'''

from Base_de_donnees import *
from time import localtime, strftime
from datetime import datetime

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
'''section "calendrier" '''

def numjouran(date):
    """Donne le numéro du jour dans l'année de la date [j,m,a]"""
    jour, mois, annee = date
    jour, mois, annee = int(jour), int(mois), int(annee)
    if ((annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0):  # bissextile?
        return (0,31,60,91,121,152,182,213,244,274,305,335,366)[mois-1] + jour
    else:
        return (0,31,59,90,120,151,181,212,243,273,304,334,365)[mois-1] + jour

def numjoursem(date):
    """donne le numéro du jour de la semaine d'une date 'j/m/a'"""
    date = date.split('/')
    annee = int(date[2])-1
    jour = (annee+(annee//4)-(annee//100)+(annee//400)+numjouran(date)) % 7
    if jour == 0 :jour=7
    return jour

def joursem():
    """donne le jour de la semaine d'une date 'j/m/a'"""
    objet_date = datetime.now()
    if len(str(objet_date.month)) == 1:
        mois = '0' + str(objet_date.month)
    else:
        mois = str(objet_date.month)
    date = str(objet_date.day)+'/'+mois+'/'+str(objet_date.year)
    return ('Lundi', 'Mardi', 'mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche')[numjoursem(date)-1]

###############################################################
'''section periode'''

def date_anterieur(premiere_date,seconde_date):
    """date_posterieur(D1,D2): dit si une date D2 'j/m/a' est postérieure ou égale à une autre date D1 'j/m/a'"""
    premiere_date = premiere_date.split('/')
    seconde_date = seconde_date.split('/')
    if premiere_date == seconde_date:
        return 'identique'
    else:
        if int(seconde_date[2]) > int(premiere_date[2]):
            return True
        elif int(seconde_date[2]) == int(premiere_date[2]):
            if int(seconde_date[1]) > int(premiere_date[1]):
                return True
            elif int(seconde_date[1]) == int(premiere_date[1]):
                if int(seconde_date[0]) >= int(premiere_date[0]):
                    return True
        return False

def date_posterieur(premiere_date,seconde_date):
    """date_posterieur(D1,D2): dit si une date D2 'j/m/a' est postérieure ou égale à une autre date D1 'j/m/a'"""
    premiere_date = premiere_date.split('/')
    seconde_date = seconde_date.split('/')
    if premiere_date == seconde_date:
        return 'identique'
    else:
        if int(seconde_date[2]) < int(premiere_date[2]):
            return True
        elif int(seconde_date[2]) == int(premiere_date[2]):
            if int(seconde_date[1]) < int(premiere_date[1]):
                return True
            elif int(seconde_date[1]) == int(premiere_date[1]):
                if int(seconde_date[0]) <= int(premiere_date[0]):
                    return True
        return False

def select_periode(date):
    vacances = {
    'vac_ete' : ['5/07/2015', '1/09/2015'],
    'toussaint' : ['17/10/2015', '2/11/2015'],
    'noel' : ['19/12/2015', '4/01/2016'],
    'hiver' : ['13/02/2016', '29/02/2016'],
    'printemps' : ['9/04/2016', '25/04/2016']
    }
    for vacance in vacances:
        posterieur = date_posterieur(date,vacances[vacance][0])
        anterieur = date_anterieur(date,vacances[vacance][1])

        if posterieur == True and anterieur == True:
            if vacance == 'vac_ete':
                return 'vac_ete'
            else:
                return 'autres_vac'
        elif posterieur == False or anterieur == False:
            retour = 'scol'
    return retour

def select_fiche(fiche_horaire):
    '''recup la fiche horaire pour la periode voulue'''
    date = datetime.now()
    if len(str(date.month)) == 1:
        mois = '0' + str(date.month)
    else:
        mois = str(date.month)
    date = str(date.day)+'/'+str(mois)+'/'+str(date.year)

    periode = select_periode(date)

    for i in range(3):
        if fiche_horaire[i][0][0] == periode:
            fiche_horaire = fiche_horaire[i]

    return fiche_horaire

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

def select_list_ville():
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

def select_jour(fiche_horaire):
    '''recup l'index des colonnes voulue (jour) pour selectionner les bons horaires'''
    index_jour = []
    aujourdhui = joursem()
    aujourdhui = aujourdhui[0]
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

def select_depart(tableau):
    '''renvoi la ville, l'arret et les horaire en fonction de l'heure
    ainsi que les index de la selection'''
    #heure = strftime("%H:%M", localtime())
    #heure = heure.split(':')
    #heure = int(str(heure[0])+str(heure[1]))
    heure = 930 #ligne de test
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
    if index_retour != []:
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

def select(ville_depart, ville_arriver):
    ville_aller, ville_retour = select_list_ville()
    fiche_horaire = select_sens(ville_depart, ville_aller, ville_arriver)
    fiche_horaire = select_fiche(fiche_horaire)
    index_jour = select_jour(fiche_horaire)

    depart, arriver = select_depart_arriver(fiche_horaire, index_jour, ville_depart, ville_arriver)

    depart = depart[1:] #seulement pour la fiche horaire FH012
    depart, index_selection = select_depart(depart)
    arriver = select_arriver(arriver, index_selection)
    return depart, arriver

def main():
    '''valeur d'entrée'''
    ville_depart = 'LE CHEYLARD'
    ville_arriver = 'CHARMES'

    depart, arriver = select(ville_depart, ville_arriver)

    for row in depart:
        print(row)

    for row in arriver:
        print(row)

if __name__ == '__main__':
    main()