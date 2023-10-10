from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")


accounts = {"Aaron": "Boofin"}


class LoginPageApp(App):

    def build(self):
        return LoginManager()


class StartScreen(Screen):
    def next_page(self, screen_to):
        self.manager.current = screen_to


class LoginManager(ScreenManager):
    pass


class CreateScreen(Screen):
    def create_account(self, username, password, password_confirm):
        special = "~!@#$%^&*()_+-=."
        has_special = False
        numbers = "1234567890"
        has_numbers = False
        has_capital = False
        has_lowercase = False
        for i in password.text:
            if i in special:
                has_special = True
            if i in numbers:
                has_numbers = True
            if i.capitalize() == i:
                has_capital = True
            if i.lower() == i:
                has_lowercase = True

        if (username.text not in accounts) and (password.text == password_confirm.text) and has_special and has_numbers and has_capital and has_lowercase and (len(password.text) > 7):
            accounts[username.text] = password.text
            self.manager.current = "login"
        else:
            self.ids.isval.color = (1,0,0,1)

    def log(self):
        self.manager.current = "login"


class LoginScreen(Screen):
    def login(self, username, password):
        if username.text in accounts and accounts[username.text] == password.text:
            self.manager.current = "logged"
    def create(self):
        self.manager.current = "create"


class LoggedIn(Screen):
    def logout(self):
        self.manager.current = "start"


LoginPageApp().run()
