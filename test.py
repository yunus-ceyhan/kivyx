

from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, DictProperty, NumericProperty, BooleanProperty, OptionProperty,StringProperty, ObjectProperty
#from kivyx.button import XFlatRIconButton, XIconButton
from kivyx.floatlayout import XFloatLayout
from kivy.animation import Animation
from kivy.metrics import dp, sp
from kivy.uix.behaviors import ButtonBehavior
from kivyx.behavior import RectangularBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar

from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
#from kivyx.button import XFlatButton
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivy.properties import StringProperty,ColorProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivyx.card import XCard
from kivyx.label import XLabel
from kivyx.line import XLiney
from kivy.uix.widget import Widget
from kivyx.button import XButton, XIconButton
from kivyx.icon import XIcon

from kivy.uix.image import Image

from kivyx.boxlayout import XBoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty,OptionProperty
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivyx.alert import xalert

#TextInput.

Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Transition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import hex kivy.utils.get_color_from_hex

<MainApp>:
    XBoxLayout:
        spacing: dp(10)
        padding: [dp(20),dp(100),dp(20),dp(20)]
        orientation: "vertical"
        bg_color: root.bgr_color
        XCard:


""")



        
class MainApp(Theming,XScreen):
    text = StringProperty("test title")
    offset_x = NumericProperty(0)
    offset_y = NumericProperty(0)
    spread_radius = NumericProperty(0)
    blur_radius = NumericProperty(0)
    def __init__(self, **kw):
        super().__init__(**kw)
        
        xalert(text= "merhaba")


class TestApp(App):
    theme_style = StringProperty()
    main = MainApp()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        return self.main


TestApp().run()
