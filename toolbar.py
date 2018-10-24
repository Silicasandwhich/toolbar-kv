from kivy.uix.gridlayout import GridLayout
from kivy.app import App
import kivy
kivy.require("1.9.0")


class ToolbarGridLayout(GridLayout):
    pass


class ToolbarApp(App):
    def build(self):
        return ToolbarGridLayout


tApp = ToolbarApp()
tApp.run()