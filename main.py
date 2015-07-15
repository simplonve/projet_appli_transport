#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
	ObjectProperty, ListProperty, StringProperty

Window.size=(720, 1280)

class FondEcran(FloatLayout):
	def __init__(self, **kwargs):
		super(FondEcran, self).__init__(**kwargs)


class accueil(Widget):
	def position(self):
		return

class ClassiqueApp(App):

	def build(self):
		parent = FloatLayout()
		titre = Label(	text='[color=ff3333]Bienvenue[/color]',
						markup= True,
						font_size= 50,
						Color= (1, 0, 0),
						pos_hint={'x': 0, 'center_y': 0.9})
		btn1 = Button(	text='[color=2ecc71]Valider Recherche[/color]',
						font_size_hint= 0.2,
						markup= True,
						size_hint=(.2,.1),
						pos_hint={'x': 0.2, 'center_y': .1})
		btn2 = Button(	text='[color=2ecc71]Nouvelle Recherche[/color]',
						font_size_hint= .1,
						markup= True,
						size_hint=(.2,.1),
						pos_hint={'x': 0.6, 'center_y': .1})
		parent.add_widget(titre)
		parent.add_widget(btn1)
		parent.add_widget(btn2)
		return parent

if __name__ == '__main__':
	ClassiqueApp().run()