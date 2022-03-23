from curses import window
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
from openpyxl import Workbook, worksheet, workbook
from openpyxl.reader.excel import load_workbook
import os

game = Game()

class MatchScreen (Screen):
    teamNum = ObjectProperty(None)
    matchNum = ObjectProperty(None)

    autonHighLbl = ObjectProperty(None)
    autonLowLbl = ObjectProperty(None)
    teleopHighLbl = ObjectProperty(None)
    teleopLowLbl = ObjectProperty(None)

    redTeamBtn = ObjectProperty(None)
    blueTeamBtn = ObjectProperty(None)

    def resetData(self):
        game.team = ""
        self.redTeamBtn.disabled = False
        self.blueTeamBtn.disabled = False
        game.autonHigh = 0
        game.autonLow = 0
        game.teleopHigh = 0
        game.teleopLow = 0
        self.autonHighLbl.text = str(game.autonHigh)
        self.autonLowLbl.text = str(game.autonLow)
        self.teleopHighLbl.text = str(game.teleopHigh)
        self.teleopLowLbl.text = str(game.teleopLow)

    def teamSelect(self, team):
        if team == "red":
            game.team = "red"
            self.redTeamBtn.disabled = True
            self.blueTeamBtn.disabled = False
        elif team == "blue":
            game.team = "blue"
            self.redTeamBtn.disabled = False
            self.blueTeamBtn.disabled = True

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
    def matchEnd(self):
        androidPath = "/storage/emulated/0/Download/2022Scouting/"
        windowsPath = "./sheets/"
        path = windowsPath
        if not os.path.isdir(path):
            os.makedirs(path)
        path += "data.xlsx"
        matchScreen = self.manager.get_screen("match")
        print("Team #:", matchScreen.teamNum.text, "Match:", matchScreen.matchNum.text, "Ah:", game.autonHigh, "Al:", game.autonLow, "Th:", game.teleopHigh, "Tl:", game.teleopLow, "Team:", game.team)
        try:
            wb = load_workbook(windowsPath)
            ws = wb.active
        except:
            wb = Workbook()
            ws = wb.active
            ws.append(["Team #", "Match #", "Team", "Auton High", "Auton Low", "Teleop High", "Teleop Low"])
        ws.append([matchScreen.teamNum.text, matchScreen.matchNum.text, game.team, game.autonHigh, game.autonLow, game.teleopHigh, game.teleopLow])
        wb.save(path)
        matchScreen.resetData()


class ScreenManager (ScreenManager):
    pass

kv = Builder.load_file("MatchScreen.kv")

class MainWindow (App):
    def build(self):
        return kv

if __name__ == "__main__":
    MainWindow().run()