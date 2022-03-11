from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ColorProperty
from kivyx.theming import Theming

Builder.load_string("""
<XLabel>:
    halign: "center"
    valign: 'middle'
    text_size: (self.width,None) if root.aligned else (None,None)
    color: root.text_color
""")

class XLabel(Theming,Label):
    aligned = BooleanProperty(True)
    text_color = ColorProperty([0,0,0,1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color