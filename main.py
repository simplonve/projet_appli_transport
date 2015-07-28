#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.0')
import gestion_bd
from kivy.app import App
from datetime import datetime
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton

Window.size=(720, 1280)
Window.clearcolor = (0.3, 0.3, 0.3, 1)

class MainApp(App):
    def build(self):
        ''''Initialisation de l'app (text et bouton)'''
        self.fenetre = FloatLayout()
        self.date = self.init_date()
        self.label_ville_depart = 'Ville de départ !' #pour les test : 'Ville de départ !' en temp normal
        self.ville_depart = None #pour les test : None en temp normal
        self.arret_depart = None #pour les test : None en temp normal
        self.status_ville_depart = None #permet de gerer si c'est pour le bouton de depart ou d'arriver
        self.label_ville_arriver = 'Ville d\'arriver !' #pour les test : 'Ville d\'arriver !' en temp normal
        self.ville_arriver = None #pour les test : None en temp normal
        self.arret_arriver = None #pour les test : None en temp normal
        self.init_list_adapter_alphabet()
        self.init_list_adapter_ville([])
        self.init_list_adapter_arret([])
        self.titre = Label(text='[color=2ecc71]Le Sept[/color]',
                    markup= True,
                    font_size= 50,
                    pos_hint={'x': 0, 'center_y': 0.8})

        self.bouton_date = Button(text='[color=2ecc71]'+self.date+'[/color]',
                    font_size_hint= 0.5,
                    markup= True,
                    size_hint=(0.3,0.05),
                    pos_hint={'x': 0.35, 'center_y': 0.6})

        self.init_bouton_label_ville_depart()
        self.init_bouton_label_ville_arriver()

        self.bouton_recherche = Button(text='[color=2ecc71]Recherche[/color]',
                    font_size_hint= 0.5,
                    markup= True,
                    size_hint=(0.3,0.05),
                    pos_hint={'x': 0.35, 'center_y': 0.2})

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
            data=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
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
        self.bouton_label_ville_depart = Button(text='[color=2ecc71]'+self.label_ville_depart+'[/color]',
                font_size_hint= 0.5,
                markup= True,
                size_hint=(0.3,0.05),
                pos_hint={'x': 0.35, 'center_y': 0.5})

    def init_bouton_label_ville_arriver(self):
        '''Initialise le bouton ville d'arriver'''
        self.bouton_label_ville_arriver = Button(text='[color=2ecc71]'+self.label_ville_arriver+'[/color]',
                    font_size_hint= 0.5,
                    markup= True,
                    size_hint=(0.3,0.05),
                    pos_hint={'x': 0.35, 'center_y': 0.4})

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
            self.afficher_resultat()

    def afficher_resultat(self):
        '''Vide la fenêtre et affiche les resultats'''
        self.fenetre.clear_widgets()
        self.affichage_ville_depart = Label(text=self.ville_depart,
            markup= True,
            font_size= 15,
            pos_hint={'x': -0.2, 'center_y': 0.90})

        self.affichage_ville_arriver = Label(text=self.ville_arriver,
            markup= True,
            font_size= 15,
            pos_hint={'x': 0.2, 'center_y': 0.90})

        self.affichage_arret_depart = Label(text=self.arret_depart,
            markup= True,
            font_size= 15,
            pos_hint={'x': -0.2, 'center_y': 0.88})

        self.affichage_arret_arriver = Label(text=self.arret_arriver,
            markup= True,
            font_size= 15,
            pos_hint={'x': 0.2, 'center_y': 0.88})

        self.affichage_date = Label(text=str(self.date),
            markup= True,
            font_size= 15,
            pos_hint={'x': -0.43, 'center_y': 0.98})

        '''Pour chaque horaire, l'affiche'''
        for ville in self.retour:
            i = 1
            for bus in self.retour[ville]:
                if ville == self.ville_depart:
                    self.affichage_horaire_depart = Label(text='Départ à '+self.retour[ville]['bus'+str(i)][1],
                        markup= True,
                        font_size= 15,
                        pos_hint={'x': -0.2, 'center_y': 0.85-(i/16)})
                    self.fenetre.add_widget(self.affichage_horaire_depart)
                    i += 1
                else:
                    self.affichage_horaire_arriver = Label(text='Arrivée à '+self.retour[ville]['bus'+str(i)][1],
                        markup= True,
                        font_size= 15,
                        pos_hint={'x': 0.2, 'center_y': 0.85-(i/16)})
                    self.fenetre.add_widget(self.affichage_horaire_arriver)
                    i += 1

        self.fenetre.add_widget(self.affichage_ville_depart)
        self.fenetre.add_widget(self.affichage_ville_arriver)
        self.fenetre.add_widget(self.affichage_arret_depart)
        self.fenetre.add_widget(self.affichage_arret_arriver)
        self.fenetre.add_widget(self.affichage_date)

if __name__ == '__main__':
    MainApp().run()