import socket
import struct

from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup

import GlobalShared


class WifiImageButton(ButtonBehavior, Image):
    pass


class BackImageButton(ButtonBehavior, Image):
    pass


class ConnectImageButton(ButtonBehavior, Image):
    pass


class WifiPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.ip_input.text = GlobalShared.host
        self.host_input = self.ids.ip_input
        self.ids.port_input.text = str(GlobalShared.port)
        self.port_input = self.ids.port_input

    @staticmethod
    def index_slide_button():
        App.get_running_app().screen_manager.current = 'Index'

    def change_host_and_ip(self, host, port):
        # Change host and ip
        GlobalShared.host = host
        GlobalShared.port = int(port)

    def try_connect(self):
        self.change_host_and_ip(self.host_input.text, self.port_input.text)

        self.wifi_active()

    def wifi_active(self):
        # Try connect

        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        address = (GlobalShared.host, GlobalShared.port)
        try:
            s.connect(address)
            answer = s.recv(2)
            if answer == b'GC':
                GlobalShared.wifi = True
        except socket.error:
            GlobalShared.wifi = False


    def open_popup(self):
        self.popup.open()
class WifiApp(App):
    def build(self):
        return WifiPage()


if __name__ == "__main__":
    WifiApp().run()
