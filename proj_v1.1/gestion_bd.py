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

import os
import BDD as bd
from time import localtime, strftime
from datetime import datetime

class Ligne(object):
    '''principe de l'objet : une instance par ligne qu'on testera par la suite'''
    def __init__(self, ligne):
        self.num_ligne = ligne
        self.ville_aller = self.init_ville(self.num_ligne, 'aller')
        self.ville_retour = self.init_ville(self.num_ligne, 'retour')
        self.aller = bd.lignes[ligne]['aller']
        self.retour = bd.lignes[ligne]['retour']
        self.ligne = bd.lignes[ligne]

    def init_ville(self, num_ligne, Sens):
        ville_aller = []
        periode = ['scol', 'vac_ete', 'autres_vac']

        for sens in bd.lignes[num_ligne]:
            if sens == Sens:
                for row in bd.lignes[num_ligne][sens]:
                    for i in range(len(row)):
                        if row[i][0] not in ville_aller and row[i][0] not in periode:
                            ville_aller.append(row[i][0])

        return ville_aller

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
    dossier = os.listdir('sources')

    for i in range(len(dossier)):
        paths = []
        path_dossier = 'sources/' + dossier[i]
        fichier = os.listdir(path_dossier)
        for j in range(len(fichier)):
            path_fichier = path_dossier + '/' + fichier[j]
            paths.append(path_fichier)

        dico_bd = []
        for path in paths:
            '''Création de trois tableaux
            pour chaque "catégories"
            scol = periode scolaire
            ...'''
            fichier = lecture_fichier(path)

            scol = [fichier[1]] + fichier[4:]
            scol = suppr_inutile(scol)

            fichier = lecture_fichier(path)

            vac_ete = [fichier[2]] + fichier[4:]
            vac_ete = suppr_inutile(vac_ete)

            fichier = lecture_fichier(path)

            autre_vac = [fichier[3]] + fichier[4:]
            autre_vac = suppr_inutile(autre_vac)

            if dico_bd == []:
                dico_bd.append(fichier[0][0])
                dico_bd.append(fichier[0][1])
                dico_bd.append(fichier[0][2])
            else:
                dico_bd.append(fichier[0][2])

            '''inscrit les tableaux dans une var'''
            with open('BDD.py', 'a') as bd:
                bd.write(fichier[0][2]+' = [\n'+str(scol)+',\n'+str(autre_vac)+',\n'+str(vac_ete)+']\n')
        with open('BDD.py', 'a') as bd:
            ligne = "lignes = {'"+dico_bd[1]+"' : {'aller' : "+dico_bd[2]+", 'retour' : "+dico_bd[3]+"}}\n\n"
            bd.write(ligne)
        dico_bd = []

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

def select_periode():
    vacances = {
    'vac_ete' : ['5/07/2015', '1/09/2015'],
    'toussaint' : ['17/10/2015', '2/11/2015'],
    'noel' : ['19/12/2015', '4/01/2016'],
    'hiver' : ['13/02/2016', '29/02/2016'],
    'printemps' : ['9/04/2016', '25/04/2016']
    }

    date = datetime.now()
    if len(str(date.month)) == 1:
        mois = '0' + str(date.month)
    else:
        mois = str(date.month)
    date = str(date.day)+'/'+str(mois)+'/'+str(date.year)

    for vacance in vacances:
        posterieur = date_posterieur(date,vacances[vacance][0])
        anterieur = date_anterieur(date,vacances[vacance][1])

        if posterieur == True and anterieur == True:
            if vacance == 'vac_ete':
                retour = 2
                break
            else:
                retour = 1
                break
        elif posterieur == False or anterieur == False:
            retour = 0
    return retour

###############################################################

def select_ville():
    '''recupère la liste des villes et la renvoi sous forme de tableau'''
    ville_aller = []
    periode = ['scol', 'vac_ete', 'autres_vac']

    for ligne in bd.lignes:
        for sens in bd.lignes[ligne]:
            if sens == 'aller':
                for row in bd.lignes[ligne][sens]:
                    for i in range(len(row)):
                        if row[i][0] not in ville_aller and row[i][0] not in periode:
                            ville_aller.append(row[i][0])

    ville_aller.sort()
    return ville_aller

def select_sens(ville_depart, ville_arriver, num_ligne, lignes):
    '''recup le sens voulu grace a la position des ville dans la liste'''
    if lignes[num_ligne].ville_aller.index(ville_depart) < lignes[num_ligne].ville_aller.index(ville_arriver):
        return 'aller'
    else:
        return 'retour'

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
    heure = strftime("%H:%M", localtime())
    heure = heure.split(':')
    heure = int(str(heure[0])+str(heure[1]))
    heure = 930 #pour les test
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
    '''cree un hash dans lequel seront toute les lignes'''
    lignes = {}
    for num_ligne in bd.lignes:
        lignes[str(num_ligne)] = Ligne(num_ligne)

    for ligne in lignes:
        if ville_depart in lignes[ligne].ville_aller and ville_arriver in lignes[ligne].ville_aller:
            num_ligne = ligne
            break

    periode = select_periode()
    sens = select_sens(ville_depart, ville_arriver, num_ligne, lignes)

    if sens == 'aller' :fiche_horaire = lignes[num_ligne].aller[periode]
    elif sens == 'retour' :fiche_horaire = lignes[num_ligne].retour[periode]

    index_jour = select_jour(fiche_horaire)

    depart, arriver = select_depart_arriver(fiche_horaire, index_jour, ville_depart, ville_arriver)

    if num_ligne == '12' and sens == 'aller':
        depart = depart[1:]
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
    #print('1-select 2-insert')
    #choix = input()
    choix = '1' #pour les test
    if choix == '1':
        main()
    elif choix == '2':
        insert()