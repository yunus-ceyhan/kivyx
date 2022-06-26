

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

<MainApp>:
    bg_color: root.card_color
    padding: [dp(50),]
    BoxLayout:
        size_hint: None,None
        size: dp(400), self.minimum_height
        pos_hint: {"center_x": .5 , "center_y": .5}
        orientation: "vertical"
        spacing: dp(32)
        XInput:
            height: dp(48)
            back_color: root.card_color
            helper: "merhaaba"
        XInput:
            height: dp(148)




""")



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
