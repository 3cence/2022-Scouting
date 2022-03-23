import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class MatchScreen (Screen):
    pass

class PostmatchScreen (Screen):
    pass

class ScreenManager (ScreenManager):
    pass

kv = Builder.load_file("MatchScreen.kv")

class MainWindow (App):
    def build(self):
        return kv

if __name__ == "__main__":
    MainWindow().run()