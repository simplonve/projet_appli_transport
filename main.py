#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.0')

import gestion_bd
from kivy.app import App
from kivy.properties import Property
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

Window.size=(720, 1280)
Window.clearcolor = (0.3, 0.3, 0.3, 1)

class MainApp(App):
    def build(self):
        self.parent = FloatLayout()
        self.titre = Label(text='[color=2ecc71]Le Sept[/color]',
                    markup= True,
                    font_size= 50,
                    pos_hint={'x': 0, 'center_y': 0.8})
        self.bouton = Button(text='[color=2ecc71]Rechercher un horaire[/color]',
                        font_size_hint= 0.1,
                        markup= True,
                        size_hint=(0.3,0.1),
                        pos_hint={'x': 0.35, 'center_y': 0.3})

        self.bouton.bind(on_press=self.ville_depart)

        self.parent.add_widget(self.titre)
        self.parent.add_widget(self.bouton)
        return self.parent

    def ville_depart(self, value):
        self.parent.remove_widget(self.titre)
        self.parent.remove_widget(self.bouton)
        liste_ville = ListeVille(self.parent)
        self.parent.add_widget(liste_ville.list_view)

class ListeVille(MainApp):
    def __init__(self, parent,**kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.parent = parent
        self.orientation = 'vertical'
        self.ville_depart = None
        self.ville_arriver = None

        self.list_adapter = ListAdapter(
            data=gestion_bd.select_ville(),
            cls=ListItemButton,
            sorted_keys=[],
            selection_mode='multiple',
            )
        self.list_adapter.bind(on_selection_change=self.selection_change)

        self.list_view = ListView(adapter=self.list_adapter)

    def selection_change(self, adapter, *args):
        for element in adapter.selection:
            x = element.index #index du truc selectionner
            print(adapter.data[x])
            if self.ville_depart != None:
                self.ville_arriver = adapter.data[x]
            if self.ville_depart == None:
                self.ville_depart = adapter.data[x]
                self.list_adapter.data = gestion_bd.select_seconde_ville(str(adapter.data[x]))
            if self.ville_arriver != None:
                self.retour = gestion_bd.select_horaire(self.ville_depart, self.ville_arriver)
                self.parent.remove_widget(self.list_view)
                affichage = Affichage(self.parent, self.ville_depart, self.ville_arriver, self.retour)
                self.parent.add_widget(affichage.affichage_ville_depart)
                self.parent.add_widget(affichage.affichage_ville_arriver)

class Affichage(MainApp):
    def __init__(self, parent, ville_depart, ville_arriver, retour, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.parent = parent
        self.retour = retour
        self.affichage_ville_depart = Label(text=ville_depart,
                    markup= True,
                    font_size= 50,
                    pos_hint={'x': 0, 'center_y': 0.98})
        self.affichage_ville_arriver = Label(text=ville_arriver,
                    markup= True,
                    font_size= 50,
                    pos_hint={'x': 0, 'center_y': 0.5})

        for ville in self.retour:
            for bus in self.retour[ville]:
                print(self.retour[ville][bus])


if __name__ == '__main__':
    MainApp().run()