

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

Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Transition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window




<MainApp>:
    bg_color: root.bgr_color
    XSegmentTab:
        tab_style: "m3"
        id: tab_panel
        XSegmentItem:
            name: "tab1"
            text: "Themes"
            item_type: "left"
        XSegmentItem:
            name: "tab2"
            text: "Walpapers"
            item_type: "center"

        XSegmentItem:
            name: "tab3"
            text: "Icon pascks"
            item_type: "right"
            text: "revennue"
            BoxLayout:
                padding: dp(50)
                orientation: "vertical"
                spacing: dp(50)


                XSlider:
                    id: sl1
                    max: 1.0
                    value: 0.1

                XSlider:
                    id: sl2
                    max: 100
                    min: 0
                    value: 0

                XCard:
                    radius: [dp(6),]
                    #shadow: sl1.value
                    type: "button"
                    #distance: sl2.value
                    size_hint: None, None
                    size: dp(156), dp(56)
                    elevation: 0.02


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
