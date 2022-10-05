from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color
from kivy.graphics.instructions import InstructionGroup
from kivy.uix.button import Button


class WifiImageButton(ButtonBehavior, Image):
    pass


class BackImageButton(ButtonBehavior, Image):
    pass


class ConnectImageButton(ButtonBehavior, Image):
    pass


class WifiPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class WifiApp(App):
    def build(self):
        return WifiPage()


if __name__ == "__main__":
    WifiApp().run()
