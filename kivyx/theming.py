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
    colors = DictProperty()
    bgr_color = ColorProperty()
    card_color = ColorProperty()
    primary_color = ColorProperty()
    accent_color = ColorProperty()
    txt_color = ColorProperty()
    opposite_color = ColorProperty()
    white_color = ColorProperty()
    black_color = ColorProperty()
    shadow_color = ColorProperty([0.5,0.5,0.5,0.05])
    trans_color = ColorProperty([0.0,0.0,0.0,0.0])
    disabled_color = ColorProperty()

    def __init__(self, **kwargs):
        super(Theming, self).__init__(**kwargs)
        self.colors =  x_colors["Palet"]
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
        self.disabled_color = self.colorx["disabled"]




