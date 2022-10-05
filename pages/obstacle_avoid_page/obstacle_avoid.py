from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


class LeftLampImageButton(ButtonBehavior, Image):
    pass


class RightLampImageButton(ButtonBehavior, Image):
    pass


class BackImageButton(ButtonBehavior, Image):
    pass

class UltrasonicInfraredImageButton(ButtonBehavior, Image):
    pass


class UltrasonicImageButton(ButtonBehavior, Image):
    pass


class ObstacleAvoidPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class ObstacleAvoidApp(App):
    def build(self):
        return ObstacleAvoidPage()


if __name__ == "__main__":
    ObstacleAvoidApp().run()
