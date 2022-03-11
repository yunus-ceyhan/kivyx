from kivy.uix.widget import Widget
from kivy.properties import ColorProperty,ListProperty
from kivy.lang import Builder

Builder.load_string("""
<XWidget>:
    canvas.before:
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius

""")

class XWidget(Widget):
    bg_color = ColorProperty([0,0,0,0])
    radius = ListProperty([0,])
