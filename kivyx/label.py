from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ColorProperty, StringProperty
from kivyx.theming import Theming
from kivyx.fonts import system_font
from kivy.clock import Clock

Builder.load_string("""
<XLabel>:
    halign: "center"
    valign: 'middle'
    text_size: (self.width,self.height) if root.aligned else (None,None)
    color: root.text_color

""")

class XLabel(Theming,Label):
    aligned = BooleanProperty(True)
    text_color = ColorProperty([0,0,0,1])
    language = StringProperty()
    system_font = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        Clock.schedule_once(self.update)
        
    def update(self,*args):
        if self.system_font:
            self.font_name = system_font(self.language) if self.language else system_font()
