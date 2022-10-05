from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from pages.login_page.login import LoginPage
from pages.index_page.index import IndexPage
from pages.wifi_page.wifi import WifiPage
from pages.remote_control_page.remote_control import RemoteControlPage
from pages.obstacle_avoid_page.obstacle_avoid import ObstacleAvoidPage
from pages.line_patrol_page.line_patrol import LinePatrolPage
from pages.object_detection_page.object_detection import ObjectDetectionPage
from pages.target_tracking_page.target_tracking import TargetTrackingPage
from pages.target_recognition_page.target_recognition import TargetRecognitionPage
from pages.identification_control.identification_control import IdentificationControlPage
from pages.auto_driving.auto_driving import AutoDrivingPage



class MyApp(App):

    def build(self):
        # 加载kv文件
        self.load_kv("pages/login_page/login.kv")
        self.load_kv("pages/index_page/index.kv")
        self.load_kv("pages/wifi_page/wifi.kv")
        self.load_kv("pages/remote_control_page/remotecontrol.kv")
        self.load_kv("pages/obstacle_avoid_page/obstacleavoid.kv")
        self.load_kv("pages/line_patrol_page/linepatrol.kv")
        self.load_kv("pages/object_detection_page/objectdetection.kv")
        self.load_kv("pages/target_tracking_page/targettracking.kv")
        self.load_kv("pages/target_recognition_page/targetrecognition.kv")
        self.load_kv("pages/identification_control/identificationcontrol.kv")
        self.load_kv("pages/auto_driving/autodriving.kv")

        self.screen_manager = ScreenManager()
        pages = {'Login': LoginPage(), 'Index': IndexPage(), 'Wifi': WifiPage(), 'RemoteControl': RemoteControlPage()
                 , 'ObstacleAvoid': ObstacleAvoidPage(), 'LinePatrol': LinePatrolPage(),
                 'ObjectDetection': ObjectDetectionPage(),
                 'TargetTracking': TargetTrackingPage(),'TargetRecognition': TargetRecognitionPage(),
                 'IdentificationControl': IdentificationControlPage(),'AutoDriving': AutoDrivingPage()}
        for item, page in pages.items():
            self.default_page = page
            screen = Screen(name=item)
            # 添加页面
            screen.add_widget(self.default_page)
            # 向屏幕管理器添加页面
            self.screen_manager.add_widget(screen)
        return self.screen_manager


if __name__ == '__main__':
    recite_app = MyApp()
    # 设置标题
    recite_app.title = 'ControlApp'
    recite_app.run()
