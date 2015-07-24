#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
Pour utiliser le gestionnaire décommentez les lignes de test
repéré avec #ligne de test
'''

import os
import Data, time, random
from time import localtime, strftime
from datetime import datetime

class Ligne(object):
    '''Objet contenant une ligne qui sera instancier plusieurs fois'''
    def __init__(self, ligne):
        self.num_ligne = ligne
        self.villes_aller = self.init_ville(self.num_ligne, 'aller')
        self.villes_retour = self.init_ville(self.num_ligne, 'retour')
        self.aller = Data.lignes[ligne]['aller']
        self.retour = Data.lignes[ligne]['retour']
        self.ligne = Data.lignes[ligne]

    def init_ville(self, num_ligne, Sens):
        '''Initialise la liste des villes'''
        villes = []
        periode = ['scol', 'vac_ete', 'autres_vac']

        for sens in Data.lignes[num_ligne]:
            if sens == Sens:
                for row in Data.lignes[num_ligne][sens]:
                    for i in range(len(row)):
                        if row[i][0] not in villes and row[i][0] not in periode:
                            villes.append(row[i][0])

        return villes

class Insert(object):
    '''Objet d'insertion dans la BD'''
    def __init__(self):
        self.dossier = os.listdir('sources')

    def lecture_fichier(self, path):
        '''Lit un csv ou un txt et le renvoi sous forme de tableau.'''
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

    def suppr_inutile(self, tableau):
        '''Supprime les colonnes inutile (contenant ND(non désservi))'''
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

    def inscription(self, lignes, dico_lignes):
        '''Inscrit les données dans la BD'''
        estInscrit = True
        while estInscrit:
            try:
                with open('Data.py', 'a') as bd:
                    bd.write(lignes)
                    bd.write(dico_lignes)
                    estInscrit = False
            except NameError:
                print('Echec de lecture du fichier : '+NameError)
                continue

    def insert(self):
        '''Insert les données du dossier "sources" dans la BD'''
        lignes = []
        dico_lignes = ["lignes = {\n"]
        for i in range(len(self.dossier)):
            paths = []
            path_dossier = 'sources/' + self.dossier[i]
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
                fichier = self.lecture_fichier(path)

                scol = [fichier[1]] + fichier[4:]
                scol = self.suppr_inutile(scol)

                fichier = self.lecture_fichier(path)

                vac_ete = [fichier[2]] + fichier[4:]
                vac_ete = self.suppr_inutile(vac_ete)

                fichier = self.lecture_fichier(path)

                autre_vac = [fichier[3]] + fichier[4:]
                autre_vac = self.suppr_inutile(autre_vac)

                if dico_bd == []:
                    dico_bd.append(fichier[0][0])
                    dico_bd.append(fichier[0][1])
                    dico_bd.append(fichier[0][2])
                else:
                    dico_bd.append(fichier[0][2])

                '''inscrit les tableaux dans une var'''
                lignes.append(fichier[0][2]+' = [\n'+str(scol)+',\n'+str(autre_vac)+',\n'+str(vac_ete)+']\n')

            if i == len(self.dossier)-1:
                dico_lignes.append("    '"+dico_bd[1]+"': {'aller': "+dico_bd[2]+", 'retour': "+dico_bd[3]+"}\n}")
            else:
                dico_lignes.append("    '"+dico_bd[1]+"': {'aller': "+dico_bd[2]+", 'retour': "+dico_bd[3]+"},\n")
        lignes = ''.join(lignes)
        dico_lignes = ''.join(dico_lignes)
        self.inscription(lignes, dico_lignes)

class Temps(object):
    '''Objet de gestion de la date et de l'heure '''
    def __init__(self):
        self.date = self.init_date()
        self.heure = self.init_heure()
        self.numJourAn = self.init_numjouran()
        self.numJourSem = self.init_numjoursem()
        self.jour_feries = ['15/8/2015','1/11/2015','11/11/2015','25/12/2015','1/1/2016','28/3/2016','1/5/2016','5/5/2016','16/5/2016','14/7/2016']
        self.jour = self.init_jour()
        self.vacances = {'vac_ete': ['5/07/2015', '1/09/2015'], 'toussaint': ['17/10/2015', '2/11/2015'], 'noel': ['19/12/2015', '4/01/2016'], 'hiver': ['13/02/2016', '29/02/2016'], 'printemps': ['9/04/2016', '25/04/2016']}
        self.periode = self.init_periode()

    def init_date(self):
        '''Mise en forme de la date'''
        objet_date = datetime.now()
        if len(str(objet_date.month)) == 1:
            mois = '0' + str(objet_date.month)
        else:
            mois = str(objet_date.month)
        date = str(objet_date.day)+'/'+mois+'/'+str(objet_date.year)
        return date

    def init_heure(self):
        '''Initialisation de l'heure'''
        heure = strftime("%H:%M", localtime())
        heure = heure.split(':')
        heure = int(str(heure[0])+str(heure[1]))
        return heure

    def init_numjouran(self):
        '''Donne le numéro du jour dans l'année'''
        date = self.date.split('/')
        jour, mois, annee = date
        jour, mois, annee = int(jour), int(mois), int(annee)
        if ((annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0):  # bissextile?
            return (0,31,60,91,121,152,182,213,244,274,305,335,366)[mois-1] + jour
        else:
            return (0,31,59,90,120,151,181,212,243,273,304,334,365)[mois-1] + jour

    def init_numjoursem(self):
        '''Donne le numéro du jour de la semaine'''
        date = self.date.split('/')
        annee = int(date[2])-1
        jour = (annee+(annee//4)-(annee//100)+(annee//400)+self.numJourAn) % 7
        if jour == 0: jour = 7
        return jour

    def init_jour(self):
        if self.date in self.jour_feries:
            return 'Ferie'
        return ['Lundi', 'Mardi', 'mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'][self.numJourSem-1]

    def date_anterieur(self, premiere_date, seconde_date):
        '''Dit si une premiere date est antèrieure ou égale à une seconde date'''
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

    def date_posterieur(self, premiere_date, seconde_date):
        '''Dit si une premiere date est postérieure ou égale à une seconde date'''
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

    def init_periode(self):
        '''Initialise la période de l'année'''
        for vacance in self.vacances:
            posterieur = self.date_posterieur(self.date, self.vacances[vacance][0])
            anterieur = self.date_anterieur(self.date, self.vacances[vacance][1])

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

class Select(object):
    ''''Objet selection des horaires'''
    def __init__(self, ville_depart, ville_arriver):
        self.lignes = self.init_lignes()
        self.ville_depart = ville_depart
        self.ville_arriver = ville_arriver
        self.date = Temps()
        self.num_ligne = self.init_num_ligne()
        self.sens = self.init_sens()
        self.fiche = self.init_fiche()
        self.index_jour =self.init_index_jour()
        self.index_heure = None
        self.depart, self.arriver = self.init_depart_arriver()
        self.select_horaire(self.depart)
        self.select_horaire(self.arriver)

    def init_lignes(self):
        '''Initialise le dictionnaire contenant les objets ligne'''
        lignes = {}
        for num_ligne in Data.lignes:
            lignes[str(num_ligne)] = Ligne(num_ligne)
        return lignes

    def init_num_ligne(self):
        '''Détermine le numéro de la ligne'''
        for ligne in self.lignes:
            if self.ville_depart in self.lignes[ligne].villes_aller and self.ville_arriver in self.lignes[ligne].villes_aller:
                return ligne

    def init_sens(self):
        '''Détermine le sens grace à la position des villes dans la liste'''
        if self.lignes[self.num_ligne].villes_aller.index(self.ville_depart) < self.lignes[self.num_ligne].villes_aller.index(self.ville_arriver):
            return 'aller'
        else:
            return 'retour'

    def init_fiche(self):
        '''Renvoi la fiche voule grace au sens'''
        if self.sens == 'aller': return self.lignes[self.num_ligne].aller[self.date.periode]
        elif self.sens == 'retour': return self.lignes[self.num_ligne].retour[self.date.periode]

    def init_index_jour(self):
        '''Détermine l'index des colonnes voulue (jour) pour selectionner les bons horaires'''
        index_jour = []
        aujourdhui = self.date.jour
        aujourdhui = aujourdhui[0]
        for jour in self.fiche[0]:
            if jour != self.fiche[0][0] and jour != self.fiche[0][1]:
                if aujourdhui in jour:
                    index_jour.append(self.fiche[0].index(jour))
        index_jour.reverse()
        index_jour.append(1)
        index_jour.append(0)
        index_jour.reverse()
        return index_jour

    def init_depart_arriver(self):
        '''Sélectionne les lignes contenant les villes de depart et d'arriver'''
        depart = []
        arriver = []
        for horaire in self.fiche:
            buffer_depart = []
            buffer_arriver = []
            if horaire[0] == self.ville_depart:
                for index in self.index_jour:
                    buffer_depart.append(horaire[index])
            elif horaire[0] == self.ville_arriver:
                for index in self.index_jour:
                    buffer_arriver.append(horaire[index])
            if buffer_arriver != []:
                arriver.append(buffer_arriver)
            if buffer_depart != []:
                depart.append(buffer_depart)

        if self.num_ligne == '12':
            depart = depart[1:]

        self.index_heure = self.init_index_heure(depart)
        depart = self.select_horaire(depart)
        arriver = self.select_horaire(arriver)

        return depart, arriver

    def init_index_heure(self, depart):
        '''Détermine l'index des colonnes voulue (heure) pour selectionner les bons horaires'''
        index_heure = []
        for DepArr in depart:
            if depart.index(DepArr) == 1: break
            for heure in DepArr:
                try:
                    decoupe = heure.split(':')
                    decoupe = int(str(decoupe[0])+str(decoupe[1]))
                    if decoupe > self.date.heure:
                        if str(DepArr.index(heure)) not in index_heure:
                            index_heure.append(DepArr.index(heure))
                except:
                    index_heure.append(DepArr.index(heure))
        return index_heure

    def select_horaire(self, ligne):
        '''Renvoi la ville, l'arret et les horaire en fonction des index des heures voulue'''
        tab_retour = []
        for arret in ligne:
            tab_selection = []
            for heure in arret:
                if arret.index(heure) in self.index_heure:
                    tab_selection.append(heure)
                else:
                    continue
            tab_retour.append(tab_selection)
        return tab_retour

################################################
'''Section fonctions app'''

def select_ville():
    '''Recupère la liste des villes et la renvoi sous forme de tableau'''
    villes_aller = []
    periode = ['scol', 'vac_ete', 'autres_vac']

    for ligne in Data.lignes:
        for sens in Data.lignes[ligne]:
            if sens == 'aller':
                for row in Data.lignes[ligne][sens]:
                    for i in range(len(row)):
                        if row[i][0] not in villes_aller and row[i][0] not in periode:
                            villes_aller.append(row[i][0])

    villes_aller.sort()
    return villes_aller

def select_seconde_ville(ville_selectionne):
    '''Recupère la liste des villes et la renvoi sous forme de tableau'''
    villes_retour = []
    periode = ['scol', 'vac_ete', 'autres_vac']

    for ligne in Data.lignes:
        villes = []
        for sens in Data.lignes[ligne]:
            if sens == 'aller':
                for row in Data.lignes[ligne][sens]:
                    for i in range(len(row)):
                        if row[i][0] not in villes and row[i][0] not in periode:
                            villes.append(row[i][0])
        if ville_selectionne in villes:
            villes_retour = villes

    villes_retour.remove(ville_selectionne)
    villes_retour.sort()
    return villes_retour

def select_horaire(depart, arriver):
    '''Le select général
    Les valeurs demandées sont sous cette forme:
    depart = 'LE CHEYLARD'
    arriver = 'CHARMES'
    '''
    if depart != None or arriver != None:
        selection = Select(depart, arriver)
        return selection.depart, selection.arriver
    else:
        return 'ERREUR'

################################################

if __name__ == '__main__':#lignes de test
    #print('1-select 2-insert')
    #choix = input()
    choix = '1'
    if choix == '1':
        test_select = Select('LE CHEYLARD', 'CHARMES')
        print(test_select.index_heure)
        for row in test_select.depart: print(row)
        for row in test_select.arriver: print(row)

        #main()
    elif choix == '2':
        insertion = Insert()
        insertion.insert()