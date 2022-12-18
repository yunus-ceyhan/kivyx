

from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, DictProperty, NumericProperty, BooleanProperty, OptionProperty,StringProperty, ObjectProperty
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
        bg_color: root.bgr_color
        XItem:
            id: cl
            radius: [dp(12),]
            text: root.text
            second_text: "test secondry text"
            #left_icon: "envelope-simple-d"
            #right_icon: "envelope-simple-d"
            image: "./kivyx/data/icon.png"
            right_text: "100%"
            button_text: "extend"
            button_right_icon: "envelope-simple"
            button_style: "text"
            badge_icon: "envelope-simple"
            on_press: self.badge_icon = ""
        XButton:
            text: "change"
            on_release:
                root.text = "change text"
        
            

""")
        
class MainApp(Theming,XScreen):
    text = StringProperty("test title")
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
