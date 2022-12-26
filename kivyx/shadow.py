from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

Builder.load_string("""
<XShadow>:
    size_hint_y: None
    height: dp(15)
    canvas.before:
        Color:
            rgba: (0, 0, 0, root.elevation)
        BoxShadow:
            pos: self.pos
            size: self.size
            offset: 0, - dp(1)
            spread_radius: - dp(4)
            border_radius: [0,0,0,0]
            blur_radius: dp(10)
""")

class XShadow(BoxLayout):
    elevation = NumericProperty(0.3)
    

