from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)


Builder.load_string("""


<MainApp>:
    id: scr_mngr
    
    XScreen:
        name: "main_screen"
        bg_color: root.bgr_color
        XSegmentControl:
            pos_hint: {"center_x": .5, "center_y":.5}
            item_width:  dp(320)
            radius: [dp(8),]
            style: "m3"
            XSegmentTextItem:
                text: "Global"
                bubble_text: "12"
            XSegmentTextItem:
                text: "China"
            XSegmentIconItem:
                icon: "alarm-f"

""")


class MainApp(ScreenManager,Theming):
    pass

class TestApp(App):
    theme_style = StringProperty()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        Window.clearcolor = (1, 1, 1, 1)
        return MainApp()


TestApp().run()