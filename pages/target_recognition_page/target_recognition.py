from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class BackImageButton(ButtonBehavior, Image):
    pass


class QRCodeRecognitionImageButton(ButtonBehavior, Image):
    pass


class ObjectRecognitionImageButton(ButtonBehavior, Image):
    pass
class GestureRecognitionImageButton(ButtonBehavior, Image):
    pass
class TargetRecognitionPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class TargetRecognitionApp(App):
    def build(self):
        return TargetRecognitionPage()



if __name__ == "__main__":
    TargetRecognitionApp().run()
