from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout



class RemoteControlPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'



class BackImageButton(ButtonBehavior, Image):
    pass


class LeftImageButton(ButtonBehavior, Image):
    pass


class RightImageButton(ButtonBehavior, Image):
    pass

class TurnLeftImageButton(ButtonBehavior, Image):
    pass


class TurnRightImageButton(ButtonBehavior, Image):
    pass

class TurnUpImageButton(ButtonBehavior, Image):
    pass


class TurnDownImageButton(ButtonBehavior, Image):
    pass

class StopImageButton(ButtonBehavior, Image):
    pass


class BuzzerImageButton(ButtonBehavior, Image):
    pass
class RemoteControlApp(App):
    def build(self):
        return RemoteControlPage()


if __name__ == "__main__":
    RemoteControlApp().run()
