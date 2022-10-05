from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class LoginImageButton(ButtonBehavior, Image):
    pass


class LoginPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class LoginApp(App):
    def build(self):
        return LoginPage()


if __name__ == "__main__":
    LoginApp().run()
