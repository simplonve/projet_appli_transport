#! /usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime

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
        print(vacance)
        print(posterieur)
        print(anterieur)

        if posterieur == True and anterieur == True:
            if vacance == 'vac_ete':
                return 'vac_ete'
            else:
                return 'autres_vac'
        elif posterieur == False or anterieur == False:
            retour = 'scol'
    return retour

date = datetime.now()
if len(str(date.month)) == 1:
    mois = '0' + str(date.month)
else:
    mois = str(date.month)
date = str(date.day)+'/'+str(mois)+'/'+str(date.year)

periode = select_periode(date)
print('----------')
print(periode)



