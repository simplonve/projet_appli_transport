#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

import gestion_bd

from time import localtime, strftime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
	ObjectProperty, ListProperty, StringProperty


class Ville(DropDown):
    pass

class SelectionArretDepart(Screen):
    top_layout = ObjectProperty(None)
    dd_bnt = ObjectProperty (None)

    def __init__(self, *args, **kargs):
        super(SelectionArretDepart, self).__init__(*args, **kargs)
        self.drop_down = Ville()

        dropdown = DropDown()
        villes = gestion_bd.select_ville()
        for ville in villes:
            btn = Button(text='%r' % ville, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        mainbutton = Button(text='Selectionner votre arrêt de départ:', size_hint=(1,1))

        mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        self.top_layout.add_widget(mainbutton)

class SelectionArretArrive(Screen):
    top_layout = ObjectProperty(None)
    dd_bnt = ObjectProperty (None)

    def __init__(self, *args, **kargs):
        super(SelectionArretArrive, self).__init__(*args, **kargs)
        self.drop_down = Ville()

        dropdown = DropDown()
        villes = gestion_bd.select_ville()
        for ville in villes:
            btn = Button(text='%r' % ville, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        mainbutton = Button(text="Selectionner votre arrêt d'arrivée :", size_hint=(1,1))
        
        mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        #self.value = mainbutton.text
        self.top_layout.add_widget(mainbutton)

class BoutonValider(Screen):
    def __init__(self, *args, **kargs):
        super(BoutonValider, self).__init__(*args, **kargs)
        btn1 = Button(text='Valider')
        btn1.bind(on_press=self.callback)
        self.top_layout.add_widget(btn1)

    def callback(instance, value):
        #print(arreta.value)
        print('My button <%s> state is <%s>' % (instance, value.text))


class Timer(Label):
    def update(self, *args):
        self.text = strftime("%H:%M:%S", localtime())

class Designe(Widget):
    pass

class TransportApp(App):
    def build(self):
        root = FloatLayout()
        graph = Designe()
        time = Timer()
        arretd = SelectionArretDepart()
        arreta = SelectionArretArrive()
        valider = BoutonValider()
        Clock.schedule_interval(time.update, 1)
        root.add_widget(graph)
        root.add_widget(time)
        root.add_widget(arretd)
        root.add_widget(arreta)
        root.add_widget(valider)
        return root

if __name__ == '__main__':
    TransportApp().run()
