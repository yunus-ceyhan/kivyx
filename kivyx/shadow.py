"""
<MainApp>:
    bg_color: '#F3F6EB'
    Shadow:
        pos_hint: {'center_y':.5}
        height: dp(3)
        elevation: 0.6
        reverse: True
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.widget import Widget

Builder.load_string("""
<XShadow>:
    size_hint_y: None
    height: dp(1.5)
    canvas.before:
        PushMatrix
        Rotate:
            angle: 180 if root.reverse else 0
            origin: self.center
        Color:
            rgba: 0,0,0,root.percent(root.elevation,100)       
        Rectangle:
            size: self.size[0], dp(root.percent(self.height,30))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,70))
        Color:
            rgba: 0,0,0,root.percent(root.elevation,70)       
        Rectangle:
            size: self.size[0],  dp(root.percent(self.height,20))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,50))
        Color:
            rgba: 0,0,0,root.percent(root.elevation,50)       
        Rectangle:
            size: self.size[0],  dp(root.percent(self.height,15))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,35))
        Color:
            rgba: 0 ,0,0, root.percent(root.elevation,35)       
        Rectangle:
            size: self.size[0],  dp(root.percent(self.height,12.5))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,22.5))
        Color:
            rgba: 0,0,0, root.percent(root.elevation,22.5)       
        Rectangle:
            size: self.size[0],  dp(root.percent(self.height,10))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,12.5))
        Color:
            rgba: 0,0,0, root.percent(root.elevation,12.5)       
        Rectangle:
            size: self.size[0],  dp(root.percent(self.height,7.5))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,5))
        Color:
            rgba: 0,0,0, root.percent(root.elevation,5)       
        Rectangle:
            size: self.size[0],  dp(root.percent(self.height,5))
            pos: self.pos[0], self.pos[1] + dp(root.percent(self.height,0))            
    canvas.after:
        PopMatrix
""")


class XShadow(Widget):
    elevation = NumericProperty(0.1)
    reverse = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def percent(self, max, percent):
        return (max/100)*percent        
