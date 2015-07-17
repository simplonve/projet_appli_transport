#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from time import localtime, strftime
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
	ObjectProperty, ListProperty, StringProperty

Window.size = (1280, 700)

class Widgets(Widget):
	pass


class TransportApp(App):
	def build(self):
		titre = Label(	text=strftime("%H:%M", localtime),
					markup= True,
					font_size= 50,
					pos_hint={'x': 0, 'center_y': 0.9})
		return Widgets()





if __name__ == '__main__':
	TransportApp().run()

