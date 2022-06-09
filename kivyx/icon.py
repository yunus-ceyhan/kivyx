from kivy.lang import Builder
from kivyx.label import XLabel
from kivy.properties import StringProperty, ColorProperty
import os

dirname = os.path.dirname(__file__)

filename = os.path.join(dirname, 'data/icon.ttf')

Builder.load_string("""
#:import x_icons kivyx.icon_def.x_icons
#:import os os
<XIcon>:
    text: x_icons[root.icon] if root.icon and root.icon in x_icons.keys() else ""
    font_name: root.fontname
    font_size: "24dp"
    size_hint: None, None
    size: self.font_size , self.font_size
    pos_hint: {"center_x": .5 , "center_y": .5}
    color: root.color

""")

class XIcon(XLabel):
    icon = StringProperty()
    color = ColorProperty([0,0,0,1])
    fontname = filename

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = self.txt_color
