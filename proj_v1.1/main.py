#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.0')
import gestion_bd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class Designe(Widget):
    pass

class MainView(BoxLayout):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
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

        list_view = ListView(adapter=self.list_adapter)
        self.add_widget(list_view)


    def selection_change(self, adapter, *args):
        print ('---- selection change')
        for element in adapter.selection:
            x = element.index #index du truc selectionner
            if self.ville_depart != None:
                self.ville_arriver = adapter.data[x]
                for row in gestion_bd.select_horaire(self.ville_depart, self.ville_arriver): print(row)
            if self.ville_depart == None:
                self.ville_depart = adapter.data[x]
                self.list_adapter.data = gestion_bd.select_seconde_ville(str(adapter.data[x]))

class TransportApp(App):
    def build(self):
        root = FloatLayout()
        graph = Designe()
        root.add_widget(graph)
        return root

if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MainView(width=800))
    #TransportApp().run()
