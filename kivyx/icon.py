from kivy.lang import Builder
from kivyx.label import XLabel
from kivy.properties import StringProperty, ColorProperty
from kivy.clock import Clock
import os

dirname = os.path.dirname(__file__)

solid = os.path.join(dirname, 'data/solid.otf')
brand = os.path.join(dirname, 'data/brands.otf')
regular = os.path.join(dirname, 'data/regular.otf')
duotone = os.path.join(dirname, 'data/duotone.otf')
light = os.path.join(dirname, 'data/light.otf')

Builder.load_string("""
#:import x_icons kivyx.icon_def.x_icons
#:import os os
<XIcon>:
    text: x_icons[root.icon] if root.icon and root.icon in x_icons.keys() else ""
    font_name: root.fonts[root.icon.split("-")[-1]] if root.icon and root.icon in x_icons.keys() else "roboto"
    font_size: "18dp"
    size_hint: None, None
    size: self.font_size , self.font_size
    pos_hint: {"center_x": .5 , "center_y": .5}
    color: root.color

""")

class XIcon(XLabel):
    icon = StringProperty()
    color = ColorProperty([0,0,0,1])
    fonts = {"s": solid,
            "b": brand,
            "r": regular,
            "d": duotone,
            "l": light}
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = self.txt_color
