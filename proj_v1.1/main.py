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
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
	ObjectProperty, ListProperty, StringProperty

Window.size = (1280, 700)

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
		Clock.schedule_interval(time.update, 1)
		root.add_widget(graph)
		root.add_widget(time)
		return root

if __name__ == '__main__':
	TransportApp().run()

