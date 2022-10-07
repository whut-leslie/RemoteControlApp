from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class BackImageButton(ButtonBehavior, Image):
    pass


class FaceTrackingImageButton(ButtonBehavior, Image):
    pass


class ColorTrackingImageButton(ButtonBehavior, Image):
    pass


class ColorFollowImageButton(ButtonBehavior, Image):
    pass


class RedColorImageButton(ButtonBehavior, Image):
    pass


class GreenColorImageButton(ButtonBehavior, Image):
    pass


class BlueColorImageButton(ButtonBehavior, Image):
    pass


class YellowColorImageButton(ButtonBehavior, Image):
    pass


class TargetTrackingPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class TargetTrackingApp(App):
    def build(self):
        return TargetTrackingPage()


if __name__ == "__main__":
    TargetTrackingApp().run()
