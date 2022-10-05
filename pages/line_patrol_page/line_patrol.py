from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


class BackImageButton(ButtonBehavior, Image):
    pass


class LinePatrolImageButton(ButtonBehavior, Image):
    pass


class PrisonImageButton(ButtonBehavior, Image):
    pass


class LinePatrolPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'


class LinePatrolApp(App):
    def build(self):
        return LinePatrolPage()


if __name__ == "__main__":
    LinePatrolApp().run()
