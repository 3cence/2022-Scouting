from game import Game
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

game = Game()

class MatchScreen (Screen):
    autonHighLbl = ObjectProperty(None)
    autonLowLbl = ObjectProperty(None)
    teleopHighLbl = ObjectProperty(None)
    teleopLowLbl = ObjectProperty(None)

    def addGoal(self, goal):
        if goal == "ah":
            game.autonHigh += 1
            self.autonHighLbl.text = str(game.autonHigh)
        elif goal == "al":
            game.autonLow += 1
            self.autonLowLbl.text = str(game.autonLow)
        elif goal == "th":
            game.teleopHigh += 1
            self.teleopHighLbl.text = str(game.teleopHigh)
        elif goal == "tl":
            game.teleopLow += 1
            self.teleopLowLbl.text = str(game.teleopLow)

    def removeGoal(self, goal):
        if goal == "ah":
            game.autonHigh -= 1
            if game.autonHigh < 0:
                game.autonHigh = 0
            self.autonHighLbl.text = str(game.autonHigh)
        elif goal == "al":
            game.autonLow -= 1
            if game.autonLow < 0:
                game.autonLow = 0
            self.autonLowLbl.text = str(game.autonLow)
        elif goal == "th":
            game.teleopHigh -= 1
            if game.teleopHigh < 0:
                game.teleopHigh = 0
            self.teleopHighLbl.text = str(game.teleopHigh)
        elif goal == "tl":
            game.teleopLow -= 1
            if game.teleopLow < 0:
                game.teleopLow = 0
            self.teleopLowLbl.text = str(game.teleopLow)
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