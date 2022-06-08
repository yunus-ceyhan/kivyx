from kivy.lang import Builder
from kivyx.label import XLabel
from kivy.properties import StringProperty, ColorProperty
import os
dirname = os.path.dirname(__file__)
material = os.path.join(dirname, 'data/icon.ttf')
solid = os.path.join(dirname, 'data/Free-Solid-900.otf')
brand = os.path.join(dirname, 'data/Brands-Regular-400.otf')
regular = os.path.join(dirname, 'data/Free-Regular-400.otf')

Builder.load_string("""
#:import x_icons kivyx.icon_def.x_icons
#:import os os
<XIcon>:
    text: x_icons[root.icon] if root.icon and root.icon in x_icons.keys() else ""
    font_name: root.s_font if self.text.startswith("s-") else root.b_font if self.text.startswith("s-") else root.r_font if self.text.startswith("r-") else m_font
    font_size: "24dp"
    size_hint: None, None
    size: self.font_size , self.font_size
    pos_hint: {"center_x": .5 , "center_y": .5}
    color: root.color

""")

class XIcon(XLabel):
    icon = StringProperty()
    color = ColorProperty([0,0,0,1])
    m_fonnt = material
    s_font = solid
    b_font = brand
    r_font = regular
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = self.txt_color
