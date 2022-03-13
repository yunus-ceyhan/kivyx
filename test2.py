

from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, DictProperty, NumericProperty, BooleanProperty, OptionProperty,StringProperty
from kivyx.button import XFlatRIconButton, XIconButton
from kivyx.floatlayout import XFloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivyx.behavior import RectangularBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar

from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivyx.button import XFlatButton
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivy.properties import StringProperty,ColorProperty
from kivy.clock import Clock
from kivy.core.window import Window



Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Transition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window

<MainApp>:
    bg_color: root.bgr_color
    XChip:
        right_icon: "check"
        left_icon: "android"
        text: "hello"
        pos_hint: {"center_x":.5,"center_y":.5}
        type: "outlined"
        bg_color: root.red_color
        #text_color: root.opposite_color



<XChip>:
    size_hint: None, None
    height: dp(32)
    padding: [dp(16),0,dp(16),0] if not root.right_icon and not root.left_icon else [dp(8),0,dp(16),0]\
        if not root.right_icon else [dp(16),0,dp(8),0]\
        if not root.left_icon else [dp(8),0,dp(8), 0]
    width: max(dp(24) + ic.width + icr.width + lb.texture_size[0], dp(32))
    #spacing: dp(8) if root.icon else 0
    bg_color: self.bg_color if root.type == "filled" else [0,0,0,0]
    radius: [dp(8),]
    canvas.after:
        Color:
            rgba: root.txt_color if root.type != "filled" else root.trans_color
        Line:
            width: dp(1)
            rounded_rectangle: (self.x, self.y, self.width, self.height,dp(8)) 
        
    XIcon:
        id: ic
        icon: root.left_icon
        font_size: "18dp"
        size_hint: None,None
        size: dp(32) if root.left_icon else 0, dp(32)
        color: root.text_color
    XLabel:
        id: lb
        text: root.text
        aligned: False
        pos_hint: {"center_y":.5}
        color: root.text_color
    XIcon:
        id: icr
        icon: root.right_icon
        font_size: "18dp"
        size_hint: None,None
        size: dp(32) if root.right_icon else 0, dp(32)
        color: root.text_color
""")



class XChip(Theming,XBoxLayout):
    type = OptionProperty("outlined",options= ["filled","outlined"])
    left_icon = StringProperty()
    right_icon = StringProperty()
    text = StringProperty()
    text_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color

class MainApp(Theming,XScreen):
    def __init__(self, **kw):
        super().__init__(**kw)


class TestApp(App):
    theme_style = StringProperty()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        return MainApp()


TestApp().run()
