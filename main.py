from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")


class StartScreen(Screen):
    pass


class LoginManager(ScreenManager):
    pass


class CreateScreen(Screen):
    pass
