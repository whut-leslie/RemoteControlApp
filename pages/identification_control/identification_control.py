from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class BackImageButton(ButtonBehavior, Image):
    pass
class QRCodeRecognitionControlImageButton(ButtonBehavior, Image):
    pass

class GestureRecognitionControlImageButton(ButtonBehavior, Image):
    pass

class IdentificationControlPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class IdentificationControlApp(App):
    def build(self):
        return IdentificationControlPage()


if __name__ == "__main__":
    IdentificationControlApp().run()
