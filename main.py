#!/usr/bin/env python3
## For .kv file syntax =
## pythonid:kvid
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    pass
class FourthWindow(Screen):
    pass
class WindowManagerWindow(Screen):
    pass

kv = Builder.load_file("my.kv")

class MyGrid(Widget):
    item = ObjectProperty(None)
    price = ObjectProperty(None)

    def button(self):
        print("Name: ", self.item.text, "Price: ", self.price.text)
        self.item.text = ""
        self.price.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__== "__main__":
    MyApp().run()
