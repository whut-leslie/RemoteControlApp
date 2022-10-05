from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class BackImageButton(ButtonBehavior, Image):
    pass


class FaceDetectionImageButton(ButtonBehavior, Image):
    pass

class ColorDetectionImageButton(ButtonBehavior, Image):
    pass
class MoveDetectionImageButton(ButtonBehavior, Image):
    pass

class ObjectDetectionPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'

class ObjectDetectionApp(App):
    def build(self):
        return ObjectDetectionPage()


if __name__ == "__main__":
    ObjectDetectionApp().run()
