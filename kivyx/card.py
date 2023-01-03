from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty, BooleanProperty
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.metrics import dp
from kivy.clock import Clock

Builder.load_string("""
<XCard>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, root.elevation
        BoxShadow:
            pos: self.pos
            size: self.size
            offset: root.shadow_x, root.shadow_y
            spread_radius: root.shadow_distance
            border_radius: root.shadow_radius
            blur_radius: root.shadow_blur
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        Color:
            rgba: root.line_color if root.outline else root.trans_color
        Line:
            width: root.outline_width
            rounded_rectangle: (self.x- dp(0.5), self.y- dp(0.5), self.width+dp(1), self.height + dp(1),root.radius[0])

""")

class XCard(Theming,BoxLayout):
    bg_color = ColorProperty()
    radius = ListProperty([0,0,0,0])
    shadow_radius = ListProperty([0,0,0,0])
    elevation = NumericProperty(0.16)
    shadow_distance = NumericProperty( - dp(5))
    shadow_blur = NumericProperty(dp(10))
    shadow_x = NumericProperty(0)
    shadow_y = NumericProperty( - dp(2))
    outline = BooleanProperty(False)
    outline_width = NumericProperty(0.6)

    def __init__(self, **kwargs):
        super(XCard, self).__init__(**kwargs)
        self.bg_color = self.card_color
        Clock.schedule_once(self.set_radius)
    
    def set_radius(self,*args):
        self.shadow_radius = self.radius if len(self.radius) == 4 else \
            [self.radius[0],self.radius[0],self.radius[0],self.radius[0]]
            
