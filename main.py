#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.0')
import gestion_bd
from kivy.app import App
from datetime import datetime
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.core.text import LabelBase
from kivy.core.text import LabelBase

Window.clearcolor = (1, 1, 1, 1)
KIVY_FONTS = [{
        "name": "Soft Elegance",
        "fn_regular": "fonts/Soft Elegance.ttf",
    }]

for font in KIVY_FONTS:
    LabelBase.register(**font)

class MainApp(App):
    def build(self):
        ''''Initialisation de l'app (text et bouton)'''
        self.fenetre = FloatLayout()
        self.date = self.init_date()
        self.label_ville_depart = 'Ville de départ !' #pour les test : 'Ville de départ !' en temp normal
        self.ville_depart = None #pour les test : None en temp normal
        self.arret_depart = None #pour les test : None en temp normal
        self.status_ville_depart = None #permet de gerer si c'est pour le bouton de depart ou d'arriver
        self.label_ville_arriver = 'Ville d\'arrivée !' #pour les test : 'Ville d\'arriver !' en temp normal
        self.ville_arriver = None #pour les test : None en temp normal
        self.arret_arriver = None #pour les test : None en temp normal
        self.init_list_adapter_alphabet()
        self.init_list_adapter_ville([])
        self.init_list_adapter_arret([])
        self.titre = Image(source='Images/le_sept.png',
                    size_hint=(.6, .8),
                    pos_hint={'x': 0.2, 'center_y': 0.80})

        self.bouton_date = Button(text='[color=682279]'+self.date+'[/color]',
                    font_size= 35,
                    font_name= 'fonts/Soft Elegance.ttf',
                    background_color=(1, 1, 1, 0),
                    markup= True,
                    size_hint=(.3, .1),
                    pos_hint={'x': 0.35, 'center_y': 0.55})

        self.init_bouton_label_ville_depart()
        self.init_bouton_label_ville_arriver()

        self.bouton_recherche = Button(text='[color=682279]Recherche[/color]',
                    font_size=35,
                    font_name= 'fonts/Soft Elegance.ttf',
                    background_color=(1, 1, 1, 0),
                    markup=True,
                    size_hint=(.3, .1),
                    pos_hint={'x': 0.35, 'center_y': 0.1})

        self.bouton_label_ville_depart.bind(on_press=self.afficher_alphabet)
        self.bouton_label_ville_arriver.bind(on_press=self.afficher_alphabet)
        self.bouton_recherche.bind(on_press=self.recherche)

        self.fenetre.add_widget(self.titre)
        self.fenetre.add_widget(self.bouton_date)
        self.fenetre.add_widget(self.bouton_label_ville_depart)
        self.fenetre.add_widget(self.bouton_label_ville_arriver)
        self.fenetre.add_widget(self.bouton_recherche)
        return self.fenetre

    def init_date(self):
        '''Initialise la date'''
        objet_date = datetime.now()
        if len(str(objet_date.month)) == 1:
            mois = '0' + str(objet_date.month)
        else:
            mois = str(objet_date.month)
        date = str(objet_date.day)+'/'+mois+'/'+str(objet_date.year)
        return date

    def init_list_adapter_alphabet(self):
        ''''Initialise les données de la liste de l'alphabet'''
        self.list_adapter_alphabet = ListAdapter(
            data=gestion_bd.select_alphabet(),
            cls=ListItemButton,
            sorted_keys=[],
            selection_mode='multiple',
            )

    def init_list_adapter_ville(self, donnee):
        '''Initialise les données de la liste des villes'''
        self.list_adapter_ville = ListAdapter(
            data=donnee,
            cls=ListItemButton,
            sorted_keys=[],
            selection_mode='multiple',
            )

    def init_list_adapter_arret(self, donnee):
        '''Initialise les données de la liste des arrets'''
        self.list_adapter_arret = ListAdapter(
            data=donnee,
            cls=ListItemButton,
            sorted_keys=[],
            selection_mode='multiple',
            )

    def init_bouton_label_ville_depart(self):
        '''Initialise le bouton ville de depart'''
        self.bouton_label_ville_depart = Button(text='[color=682279]'+self.label_ville_depart+'[/color]',
                font_size= 35,
                font_name= "fonts/Soft Elegance.ttf",
                background_color=(1, 1, 1, 0),
                markup= True,
                size_hint=(0.4,0.1),
                pos_hint={'x': 0.3, 'center_y': 0.4})

    def init_bouton_label_ville_arriver(self):
        '''Initialise le bouton ville d'arriver'''
        self.bouton_label_ville_arriver = Button(text='[color=682279]'+self.label_ville_arriver+'[/color]',
                font_size=35,
                markup= True,
                font_name= "fonts/Soft Elegance.ttf",
                background_color=(1, 1, 1, 0),
                size_hint=(0.4,0.1),
                pos_hint={'x': 0.3, 'center_y': 0.25})

    def afficher_alphabet(self, value):
        '''Affiche la liste de l'alphabet'''
        if self.status_ville_depart == None:
            self.list_adapter_alphabet.bind(on_selection_change=self.afficher_list_ville)
            self.list_view_alphabet = ListView(adapter=self.list_adapter_alphabet)
            self.fenetre.add_widget(self.list_view_alphabet)
        else:
            self.init_list_adapter_alphabet()
            self.list_adapter_alphabet.bind(on_selection_change=self.afficher_list_ville)
            self.list_view_alphabet = ListView(adapter=self.list_adapter_alphabet)
            self.fenetre.add_widget(self.list_view_alphabet)

    def afficher_list_ville(self, adapter):
        '''
        Initialise la liste des villes, supprime la liste de l'alphabet
        et affiche la liste des villes
        '''
        if self.status_ville_depart == None:
            for element in adapter.selection:
                index_element = element.index
                self.init_list_adapter_ville(gestion_bd.select_villes(str(adapter.data[index_element])))
                self.fenetre.remove_widget(self.list_view_alphabet)
                self.list_adapter_ville.bind(on_selection_change=self.select_ville)
                self.list_view_ville = ListView(adapter=self.list_adapter_ville)
                self.fenetre.add_widget(self.list_view_ville)
        else:
            for element in adapter.selection:
                index_element = element.index
                self.init_list_adapter_ville(gestion_bd.select_seconde_villes(self.label_ville_depart, adapter.data[index_element]))
                self.fenetre.remove_widget(self.list_view_alphabet)
                self.list_adapter_ville.bind(on_selection_change=self.select_ville)
                self.list_view_ville = ListView(adapter=self.list_adapter_ville)
                self.fenetre.add_widget(self.list_view_ville)

    def select_ville(self, adapter):
        '''
        Self.label_ville_depart devient le nom de la ville de départ
        Initialise la liste des arrets
        '''
        if self.status_ville_depart == None:
            for element in adapter.selection:
                index_element = element.index
                self.label_ville_depart = adapter.data[index_element]
                self.ville_depart = adapter.data[index_element]
                self.status_ville_depart = 'ville'
                self.init_list_adapter_arret(gestion_bd.select_arrets(self.label_ville_depart))
                self.select_arret()
        else:
            for element in adapter.selection:
                index_element = element.index
                self.label_ville_arriver = adapter.data[index_element]
                self.ville_arriver = adapter.data[index_element]
                self.init_list_adapter_arret(gestion_bd.select_arrets(self.label_ville_arriver))
                self.select_arret()

    def select_arret(self):
        '''Supprime la listes des villes, affiche la liste des arrets'''
        if self.status_ville_depart == 'ville':
            self.fenetre.remove_widget(self.list_view_ville)
            self.list_adapter_arret.bind(on_selection_change=self.modif_bouton)
            self.list_view_arret = ListView(adapter=self.list_adapter_arret)
            self.fenetre.add_widget(self.list_view_arret)
        else:
            self.fenetre.remove_widget(self.list_view_ville)
            self.list_adapter_arret.bind(on_selection_change=self.modif_bouton)
            self.list_view_arret = ListView(adapter=self.list_adapter_arret)
            self.fenetre.add_widget(self.list_view_arret)

    def modif_bouton(self, adapter):
        '''Modifie les bouton depart ou arriver'''
        if self.status_ville_depart == 'ville':
            for element in adapter.selection:
                index_element = element.index
                self.label_ville_depart = "'"+self.label_ville_depart+", "+adapter.data[index_element]+"'"
                self.status_ville_depart = 'ville+arret'
                self.arret_depart = adapter.data[index_element]
                self.fenetre.remove_widget(self.list_view_arret)
                self.fenetre.remove_widget(self.bouton_label_ville_depart)
                self.init_bouton_label_ville_depart()
                self.fenetre.add_widget(self.bouton_label_ville_depart)
        else:
            for element in adapter.selection:
                index_element = element.index
                self.label_ville_arriver = "'"+self.label_ville_arriver+", "+adapter.data[index_element]+"'"
                self.arret_arriver = adapter.data[index_element]
                self.fenetre.remove_widget(self.list_view_arret)
                self.fenetre.remove_widget(self.bouton_label_ville_arriver)
                self.init_bouton_label_ville_arriver()
                self.fenetre.add_widget(self.bouton_label_ville_arriver)

    def recherche(self, value):
        '''Le select général'''
        if self.label_ville_depart != 'Ville de départ !' and self.label_ville_arriver != 'Ville d\'arriver !':
            self.retour = gestion_bd.select_horaire(self.ville_depart, self.arret_depart, self.ville_arriver, self.arret_arriver)
            if self.retour == 'ERREUR':
                self.fenetre.clear_widgets()
                self.affichage_erreur = Label(text='[color=682279]Quelque chose s\'est mal passer[/color]',
                        markup= True,
                        font_size= 35,
                        pos_hint={'x': 0, 'center_y': 0.60})

                self.bouton_retour = Button(text='[color=682279]Retour[/color]',
                        font_size= 35,
                        font_name= "fonts/Soft Elegance.ttf",
                        markup= True,
                        size_hint=(0.4,0.1),
                        pos_hint={'x': 0.3, 'center_y': 0.4})

                self.bouton_retour.bind(on_press=MainApp().run())
                self.fenetre.add_widget(self.affichage_erreur)
                self.fenetre.add_widget(self.bouton_retour)
            else:
                self.afficher_resultat()

    def afficher_resultat(self):
        '''Vide la fenêtre et affiche les resultats'''
        self.fenetre.clear_widgets()
        self.affichage_ville_depart = Label(text='[color=682279]'+self.ville_depart+'[/color]',
            markup= True,
            font_size= 25,
            pos_hint={'x': -0.2, 'center_y': 0.90})

        self.affichage_ville_arriver = Label(text='[color=682279]'+self.ville_arriver+'[/color]',
            markup= True,
            font_size= 25,
            pos_hint={'x': 0.2, 'center_y': 0.90})

        self.affichage_arret_depart = Label(text='[color=682279]'+self.arret_depart+'[/color]',
            markup= True,
            font_size= 25,
            pos_hint={'x': -0.2, 'center_y': 0.83})

        self.affichage_arret_arriver = Label(text='[color=682279]'+self.arret_arriver+'[/color]',
            markup= True,
            font_size= 25,
            pos_hint={'x': 0.2, 'center_y': 0.83})

        self.affichage_date = Label(text='[color=682279]'+str(self.date)+'[/color]',
            markup= True,
            font_size= 25,
            pos_hint={'x': -0.38, 'center_y': 0.98})

        '''Pour chaque horaire, l'affiche'''
        for ville in self.retour:
            i = 1
            for bus in self.retour[ville]:
                if ville == self.ville_depart:
                    self.affichage_horaire_depart = Label(text='[color=682279]'+'Départ à '+self.retour[ville]['bus'+str(i)][1]+'[/color]',
                        markup= True,
                        font_size= 30,
                        pos_hint={'x': -0.2, 'center_y': 0.70-i/16})
                    self.fenetre.add_widget(self.affichage_horaire_depart)
                    i += 1
                else:
                    self.affichage_horaire_arriver = Label(text='[color=682279]'+'Arrivée à '+self.retour[ville]['bus'+str(i)][1]+'[/color]',
                        markup= True,
                        font_size= 30,
                        pos_hint={'x': 0.2, 'center_y': 0.70-i/16})
                    self.fenetre.add_widget(self.affichage_horaire_arriver)
                    i += 1

        self.fenetre.add_widget(self.affichage_ville_depart)
        self.fenetre.add_widget(self.affichage_ville_arriver)
        self.fenetre.add_widget(self.affichage_arret_depart)
        self.fenetre.add_widget(self.affichage_arret_arriver)
        self.fenetre.add_widget(self.affichage_date)

if __name__ == '__main__':
    MainApp().run()