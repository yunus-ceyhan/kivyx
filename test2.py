

from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, DictProperty, NumericProperty, BooleanProperty, OptionProperty,StringProperty
#from kivyx.button import XFlatRIconButton, XIconButton
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

from kivyx.boxlayout import XBoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty,OptionProperty
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
#TextInput.

Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Transition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import hex kivy.utils.get_color_from_hex

<MainApp>:
    XBoxLayout:
        spacing: dp(120)
        padding: [dp(120),]
        orientation: "vertical"
        bg_color: root.accent_color
        XButton:
            bg_color: self.primary_color
            text: self.style.title()
            style: "elevated" 
            #button_width: dp(380)
            #right_icon: "plus"
            left_icon: "plus"
            rounded: True
            text_color: root.colors("green",1)
            icon_color: self.text_color
            


""")

        


class MainApp(Theming,XScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        print(self.colors("blue"))


class TestApp(App):
    theme_style = StringProperty()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        return MainApp()


TestApp().run()
