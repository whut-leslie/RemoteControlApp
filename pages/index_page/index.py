# 导入 kivy 的 App 类，它是所有 kivy 应用的基类
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen


import GlobalShared


class RemoteConImageButton(ButtonBehavior, Image):
    pass


class WifiImageButton(ButtonBehavior, Image):
    pass


class MenuImageButton(ButtonBehavior, Image):
    pass


class IndexPage(Screen):
    # 初始化
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        # self.tick = Image(source='Img/tick.png',
        #                   allow_stretch=False,
        #                   keep_ratio=True,
        #                   pos_hint={"center_x": 0.73, "center_y": 0.8},
        #                   size_hint=(0.08, 0.08))
        #
        # self.wrong = Image(source='Img/wrong.png',
        #                    allow_stretch=False,
        #                    keep_ratio=True,
        #                    pos_hint={"center_x": 0.73, "center_y": 0.8},
        #                    size_hint=(0.08, 0.08))
        # self.check_wifi_status()


    def check_wifi_status(self):
        if GlobalShared.error is True:
            self.remove_widget(self.tick)
            self.remove_widget(self.wrong)
            self.add_widget(self.wrong)
            GlobalShared.error = False


    @staticmethod
    def wifi_slide_button():
        App.get_running_app().screen_manager.current = 'Wifi'

    @staticmethod
    def remote_control_slide_button():
        App.get_running_app().screen_manager.current = 'RemoteControl'

    @staticmethod
    def obstacle_avoid_slide_button():
        App.get_running_app().screen_manager.current = 'ObstacleAvoid'

    @staticmethod
    def line_patrol_slide_button():
        App.get_running_app().screen_manager.current = 'LinePatrol'

    @staticmethod
    def object_detection_slide_button():
        App.get_running_app().screen_manager.current = 'ObjectDetection'

    @staticmethod
    def target_tracking_slide_button():
        App.get_running_app().screen_manager.current = 'TargetTracking'

    @staticmethod
    def target_recognition_slide_button():
        App.get_running_app().screen_manager.current = 'TargetRecognition'

    @staticmethod
    def identification_control_slide_button():
        App.get_running_app().screen_manager.current = 'IdentificationControl'

    @staticmethod
    def auto_driving_slide_button():
        App.get_running_app().screen_manager.current = 'AutoDriving'


# 从 App 类中继承了 kivy 应用最基本的方法，如创建窗口、设置窗口的大小和位置等
class IndexApp(App):
    # 实现 TestApp 类的 build 方法（继承自 App 类）
    def build(self):
        # build 方法返回的控件，在 Kivy 中，称之为“根控件” (root widget)
        # Kivy 将自动缩放根控件，让它填满整个窗口。
        return IndexPage()


if __name__ == "__main__":
    IndexApp().run()
