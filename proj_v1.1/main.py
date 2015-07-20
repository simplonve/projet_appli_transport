#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from time import localtime, strftime
from kivy.app import App
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

# Window.size = (1280, 700)

class Ville(DropDown):
    pass

class ChoixLigne(DropDown):
    pass
 
 
class Depart(FloatLayout):
    def __init__(self, **kwargs):

        super(Depart, self).__init__(**kwargs)
        self.dropdown = Ville()
        self.mainbutton = Button(	text='Selectionner votre ville de départ :',
        							size_hint=(.7,.1),
									pos_hint={'x': .15, 'center_y': .6})

        self.add_widget(self.mainbutton)

        self.mainbutton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select=self.callback)
 
    def callback(self, instance, x):
        '''x est self.mainbutton.text actualisé'''

class Arrivee(FloatLayout):
    def __init__(self, **kwargs):

        super(Arrivee, self).__init__(**kwargs)
        self.dropdown = Ville()
        self.mainbutton = Button(	text="Selectionner votre ville d'arrivée :",
        							size_hint=(.7,.1),
									pos_hint={'x': .15, 'center_y': .4})

        self.add_widget(self.mainbutton)

        self.mainbutton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select=self.callback)
 
    def callback(self, instance, x):
        '''x est self.mainbutton.text actualisé'''

class Ligne(FloatLayout):
    def __init__(self, **kwargs):

        super(Ligne, self).__init__(**kwargs)
        self.dropdown = ChoixLigne()
        self.mainbutton = Button(	text="Selectionner votre ligne :",
        							size_hint=(.7,.1),
									pos_hint={'x': .15, 'center_y': .8})

        self.add_widget(self.mainbutton)

        self.mainbutton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select=self.callback)
 
    def callback(self, instance, x):
        '''x est self.mainbutton.text actualisé'''

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
		depart = Depart()
		arrive = Arrivee()
		ligne = Ligne()
		Clock.schedule_interval(time.update, 1)
		root.add_widget(graph)
		root.add_widget(time)
		root.add_widget(depart)
		root.add_widget(arrive)
		root.add_widget(ligne)
		return root

if __name__ == '__main__':
	TransportApp().run()

