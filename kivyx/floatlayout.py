from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ColorProperty
from kivy.lang import Builder

Builder.load_string("""
<XFloatLayout>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            size: self.size
            pos: self.pos

""")

class XFloatLayout(FloatLayout):
    bg_color = ColorProperty([0,0,0,0])