from kivy.uix.gridlayout import GridLayout
from kivy.properties import ColorProperty
from kivy.lang import Builder

Builder.load_string("""
<XGridLayout>:
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            size: self.size
            pos: self.pos

""")

class XGridLayout(GridLayout):
    bg_color = ColorProperty([0,0,0,0])