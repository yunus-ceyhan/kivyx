from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty, BooleanProperty
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle, Line

class XCard(Theming,BoxLayout):
    radius = ListProperty((0, 0, 0, 0))
    shadow_color = ListProperty((0, 0, 0, 0.0))
    shadow_blur = NumericProperty(10)
    shadow_x = NumericProperty(0)
    shadow_y = NumericProperty(-2)
    bg_color = ListProperty((0, 0, 0, 0))
    elevation = NumericProperty(0.16)
    shadow_distance = NumericProperty(-5)
    outline = BooleanProperty(False)
    outline_width = NumericProperty(0.6)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0,0,0,self.elevation/14)
        self.bg_color = self.bgr_color
        self.bind(pos=self.update_shadow, size=self.update_shadow, radius=self.update_shadow, shadow_color=self.update_shadow, shadow_blur=self.update_shadow, shadow_x=self.update_shadow, shadow_y=self.update_shadow, bg_color=self.update_shadow)
        self.update_shadow()

    def update_shadow(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.shadow_color)
            x = self.shadow_distance 
            y = self.shadow_distance 
            
            for i in range(1, int(self.shadow_blur)+1):
                alpha = self.shadow_color[3] * (self.shadow_blur-i)/self.shadow_blur
                RoundedRectangle(pos=(self.x-(x/2)-(i/2)+self.shadow_x, self.y-(y/2)-(i/2)+self.shadow_y), size=(self.width+x+i, self.height+y+i), radius=tuple(r+i for r in self.radius), segments=30, group='shadow')
                Color(rgba=(self.shadow_color[0], self.shadow_color[1], self.shadow_color[2], alpha))
            Color(rgba=(self.bg_color))
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius, segments=30)
            Color(rgba=(self.line_color if self.outline else self.trans_color))
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, self.radius[0]),width=self.outline_width)
            
