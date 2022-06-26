from kivy.app import App
from kivy.properties import ColorProperty, OptionProperty, DictProperty, ObjectProperty, BooleanProperty,StringProperty
from kivyx.colors import x_colors
from kivy.event import EventDispatcher
from kivy.clock import Clock
from kivy.core.window import Window

class Theming(EventDispatcher):
    theme = StringProperty("Light")
    colorx = DictProperty()
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
    xcolors = {
        "red" :   "#E36036",
        "red2":   "#e74c3c",
        "red3":   "#e74c3c",
        "grey":   "#7f8c8d",
        "green":  "#30C29E",
        "green2": "#1abc9c",
        "green3": "#16a085",
        "green4": "#2ecc71",
        "green5": "#27ae60",
        "blue" :  "#4686EE",
        "blue2": "#3498db",
        "blue3": "#2980b9",
        "yellow": "#FFD369",
        "sun":    "#f1c40f",
        "black" : "#222831",
        "white": "#EEEEEE",
        "orange": "#f39c12",
        "carrot": "#e67e22",
        "pumpkin": "#d35400",
        "silver": "#bdc3c7",
        "purple": "#9b59b6",
        "purple2": "#8e44ad",
        "asphalt": "#34495e",
        "midnight": "#2c3e50",
        "clouds": "#ecf0f1",
        "trans": "#ffffff00"
    }

    def __init__(self, **kwargs):
        super(Theming, self).__init__(**kwargs)
        self.theme = App.get_running_app().theme_style
        if self.theme == "Dark":
            self.colorx = x_colors["Dark"]           
        else:
            self.colorx = x_colors["Light"]
        self.bgr_color = self.colorx["bg"]
        self.card_color = self.colorx["card"]
        self.primary_color = self.colorx["primary"]
        self.accent_color = self.colorx["accent"]
        self.txt_color = self.colorx["txt"]
        self.txt_medium = self.colorx["txt_medium"]
        self.txt_light = self.colorx["txt_light"]
        self.opposite_color = self.colorx["opposite"]
        self.disabled_color = self.colorx["disabled"]




