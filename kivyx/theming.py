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
    txt_light = ColorProperty()
    txt_medium = ColorProperty()
    txt_bold = ColorProperty()
    opposite_color = ColorProperty()
    shadow_color = ColorProperty([0.5,0.5,0.5,0.05])
    trans_color = ColorProperty([0.0,0.0,0.0,0.0])
    disabled_color = ColorProperty()
    xcolors = x_colors["Colors"]

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
        self.txt_light = self.colorx["txt_bold"]
        self.txt_medium = self.colorx["txt_medium"]
        self.txt_light = self.colorx["txt_light"]
        self.opposite_color = self.colorx["opposite"]
        self.disabled_color = self.colorx["disabled"]
        
    def colors(self,name, hue = 6):
        if name and str(name) in self.xcolors.keys() and hue in range(1,11):
            return self.xcolors[str(name)][int(hue)-1]
        else:
            return self.trans_color

