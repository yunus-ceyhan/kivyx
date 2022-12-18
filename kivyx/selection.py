
"""
<MainApp>:
    XSwitch:
        pos_hint: {"center_x": .5, "center_y": .5}
        active: True
        style: "m3"
        
"""

from kivyx.behavior import CircularBehavior
from kivy.clock import Clock
from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivy.properties import ColorProperty, BooleanProperty, OptionProperty
from kivy.metrics import dp
from kivy.animation import Animation


Builder.load_string("""
<XSwitch>:
    size_hint: None,None
    size: (dp(36),dp(16) if root.style == "m2" else dp(22))
    radius: [dp(8),] if root.style == "m2" else [dp(10),]
    bg_color: root.back_color
    on_press: root.change_status()
    padding: [0,0,0,0] if root.style == "m2" else [dp(1),0,0,0]
    opacity: (.5 if self.parent.disabled else 1) if self.parent else 1
    XWidget:
        id: ic
        size_hint: None,None
        size: dp(20),dp(20)
        bg_color: root.toggle_color
        radius: [dp(180),]
        pos_hint: {"center_y": .5}

""")

class XSwitch(CircularBehavior,XBoxLayout):
    toggle_color = ColorProperty()
    back_color = ColorProperty()
    active_color = ColorProperty()
    active = BooleanProperty(False)
    style = OptionProperty("m2", options = ["m2","m3"])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.toggle_color = self.card_color
        self.back_color = self.disabled_color
        self.active_color = self.accent_color
        Clock.schedule_once(self.set_status)
        
    def set_status(self,*args):
        if self.active:
            self.padding = [dp(16),0,0,0] if self.style == "m2" else [dp(15),0,0,0]
            self.back_color = self.active_color
        else:
            self.padding =[0,0,0,0] if self.style == "m2" else [dp(1),0,0,0]
            self.back_color = self.disabled_color

    def change_status(self,ststus = False,*args):
        if not self.active:
            anim = Animation(padding = [dp(16),0,0,0] if self.style == "m2" else [dp(15),0,0,0], duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = self.change_color)
        else:
            anim = Animation(padding = [0,0,0,0] if self.style == "m2" else [dp(1),0,0,0], duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = self.change_color)

    def change_color(self,*args):
        if self.active:
            self.back_color = self.disabled_color
            self.active = False
        else:
            self.back_color = self.active_color
            self.active = True
