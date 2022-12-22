from kivy.uix.screenmanager import Screen
from kivy.properties import ColorProperty
from kivy.lang import Builder

Builder.load_string("""
<XScreen>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            size: self.size[0]*2, self.size[1]*2
            pos: self.pos

""")

class XScreen(Screen):
    bg_color = ColorProperty([0,0,0,0])