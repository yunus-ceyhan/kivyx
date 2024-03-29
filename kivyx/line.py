from kivyx.boxlayout import XBoxLayout
from kivy.lang import Builder
from kivyx.theming import Theming
Builder.load_string("""
<XLinex>:
    orientation: "vertical"
    size_hint_y: None
    height: dp(0.6)
    bg_color: root.line_color
    
<XLiney>:
    orientation: "horizontal"
    size_hint_x: None
    width: dp(1)
    bg_color: root.line_color

""")

class XLinex(Theming,XBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class XLiney(Theming,XBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
