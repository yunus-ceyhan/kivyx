from kivy.app import App
from kivy.properties import ColorProperty, OptionProperty, DictProperty, ObjectProperty, BooleanProperty,StringProperty
from kivyx.colors import x_colors
from kivy.event import EventDispatcher
from kivy.clock import Clock
from kivy.core.window import Window

class Theming(EventDispatcher):
    theme = StringProperty("Light")
    colorx = DictProperty()
    paletx = DictProperty()
    bgr_color = ColorProperty()
    card_color = ColorProperty()
    primary_color = ColorProperty()
    accent_color = ColorProperty()
    txt_color = ColorProperty()
    opposite_color = ColorProperty()
    white_color = ColorProperty()
    black_color = ColorProperty()

    red_color= ColorProperty()
    green_color = ColorProperty()
    blue_color = ColorProperty()
    yellow_color = ColorProperty()
    disabled_color = ColorProperty()
    trans_color = ColorProperty()
    shadow_color = ColorProperty([0.5,0.5,0.5,0.05])

    def __init__(self, **kwargs):
        super(Theming, self).__init__(**kwargs)
        self.theme = App.get_running_app().theme_style
        self.paletx = x_colors["Palet"]
        if self.theme == "Dark":
            self.colorx = x_colors["Dark"]           
        else:
            self.colorx = x_colors["Light"]
        self.bgr_color = self.colorx["bg"]
        self.card_color = self.colorx["card"]
        self.primary_color = self.colorx["primary"]
        self.accent_color = self.colorx["accent"]
        self.txt_color = self.colorx["txt"]
        self.opposite_color = self.colorx["opposite"]

        self.white_color = self.paletx["white"]
        self.black_color = self.paletx["black"]
        self.red_color = self.paletx["red"]
        self.green_color = self.paletx["green"]
        self.blue_color = self.paletx["blue"]
        self.yellow_color = self.paletx["yellow"]
        self.trans_color = self.paletx["trans"]
        self.disabled_color = self.paletx["disabled"]

        #Window.clearcolor = self.bgr_color



