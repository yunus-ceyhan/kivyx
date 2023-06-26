from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

Builder.load_string("""
<XShadow>:
    size_hint_y: None
    height: dp(15)
""")

class XShadow(BoxLayout):
    elevation = NumericProperty(0.15)
    

