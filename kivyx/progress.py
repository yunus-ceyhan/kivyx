"""
<MainApp>:
    BoxLayout:
        orientation: "vertical"
        spacing: dp(24)
        
        XProgress:
            pos_hint: {"center_x":.5,"center_y":.5}
            value: 50
        
        XCProgress:
            pos_hint: {"center_x":.5,"center_y": .5}
            value: 67
            animation: True
            style: "m2"
            max_width: dp(150)
            cap: "round"
            text_opacity: 1
            text_bold: True
            text: "ACCURACY"
            cap: "round"
            #text_font_size: "18sp"
            #percent_font_size: "40sp"
            #percent_symbol: False
            back_color: root.xcolors["black"]
            line_back_color: root.trans_color
            text_color: root.xcolors["white"]
            #cap: "square"
            line_color: root.xcolors["sun"]
"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, BooleanProperty, OptionProperty, NumericProperty, ListProperty, StringProperty
from kivy.uix.progressbar import ProgressBar
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.clock import Clock


Builder.load_string("""
<XProgress>:
    canvas:
        Clear
        Color:
            rgba:  root.back_color
        RoundedRectangle:
            size:    (self.width , root.thickness) if self.orientation == 'horizontal' else (root.thickness,self.height)
            pos:   (self.x, self.center_y - root.thickness) if self.orientation == 'horizontal' \
                else (self.center_x - root.thickness,self.y+root.thickness)
            radius: root.radius
        Color:
            rgba:  root.track_color
        RoundedRectangle:
            size:     (self.width*self.value_normalized, root.thickness) if self.orientation == 'horizontal' else (root.thickness, \
                self.height*self.value_normalized)
            pos:    (self.width*(1-self.value_normalized)+self.x if self.reversed else self.x, self.center_y - root.thickness) \
                if self.orientation == 'horizontal' else \
                (self.center_x - root.thickness,self.height*(1-self.value_normalized)+self.y if self.reversed else self.y + root.thickness)
            radius: root.radius


<XCProgress>:
    size_hint: None,None
    canvas.before:
        Color:
            rgba: root.back_color if root.style == "m2" else root.trans_color
        Ellipse:
            pos: self.pos
            size: self.size
            angle_start: -180
            angle_end: 180
        
        Color:
            rgba: root.line_back_color
        Line:
            cap: root.cap
            width: (self.width/24) if root.style == "m2"\
                else (self.width/56) if root.style == "m3"\
                    else (root.max_width / 16)
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2, 360, 0) if root.style == "m2"\
                    else (self.center_x, self.center_y, min(self.width, self.height)
                / 2, 140, -140) if root.style == "m3"\
                    else (self.center_x, self.center_y- self.height/2, min(self.width, self.height*2)
                / 2, 90, - 90)
    canvas.after:
        Color:
            rgba: root.line_color if root.value > 0 else (0,0,0,0)
        Line:
            width: (root.max_width / 16) if root.style == "m4" else (self.width/24)
            cap: root.cap
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2, ( 0 + (round(root.value)*3.6)) , 0) if root.style == "m2"\
                    else (self.center_x, self.center_y, min(self.width, self.height)
                / 2, (-140 + (round(root.value)*2.8)) , - 140) if root.style == "m3"\
                    else (self.center_x, self.center_y- self.height/2, min(self.width, self.height*2)
                / 2, - 90 + (round(root.value)*1.8) , - 90)
        
    XLabel:
        id: lb
        text: (str(round(root.value))+"%" if root.percent_symbol else str(round(root.value))) if not root.percent_text else root.percent_text
        size_hint: None, None
        size: root.size
        text_size: None, None
        font_size: ((root.max_width / 6) if root.style == "m3" else (root.max_width / 5)) if not root.percent_font_size else root.percent_font_size
        bold: root.text_bold
        pos: (root.pos[0] + (root.max_width/2)- self.width/2, ((root.pos[1] + root.height/2)\
            if not root.text else (root.pos[1] + root.height/1.7)) - self.height /2) if root.style == "m2"\
            else (root.pos[0] + (root.max_width/2)- self.width/2, (root.pos[1] - root.height/2)+self.font_size/2) if root.style == "m3"\
                else (root.pos[0] + (root.max_width/2)- self.width/2, ((root.pos[1] - root.height/2)+self.font_size/2))\
                    if root.text else (root.pos[0] + (root.max_width/2)- self.width/2, (root.pos[1] - root.height/2))
        opacity: root.text_opacity
        color: root.text_color
        
    XLabel:
        text: root.text
        size_hint: None, None
        size: root.size
        font_name: "light"
        text_size: None, None
        font_size: root.max_width / 8 if not root.text_font_size else root.text_font_size
        pos: (root.pos[0] + (root.max_width/2) - self.width/2, (root.pos[1] + root.height/2) - self.height /1.55) if root.style == "m2"\
            else (root.pos[0] + (root.max_width/2)- self.width/2, (root.pos[1] + root.height/2) - self.height /2) if root.style == "m3"\
                else (root.pos[0] + (root.max_width/2)- self.width/2, (root.pos[1] - root.height/1.5)+self.font_size/2)
        opacity: root.text_opacity/1.2
        color: root.text_color

""")

class XProgress(Theming,ProgressBar):
    thickness = NumericProperty(dp(4))
    reversed = BooleanProperty(False)
    orientation = OptionProperty('horizontal', options=['horizontal', 'vertical'])
    back_color = ColorProperty()
    track_color = ColorProperty()
    radius = ListProperty([0,])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_color = self.disabled_color
        self.track_color = self.primary_color
        
class XCProgress(Theming,Widget):
    text = StringProperty()
    cap = StringProperty("round")
    percent_text = StringProperty()
    line_color = ColorProperty([0,0,0,0])
    line_back_color = ColorProperty([0,0,0,0])
    back_color = ColorProperty([0,0,0,0])
    text_color = ColorProperty([0,0,0,0])
    text_opacity = NumericProperty(.7)
    text_bold = BooleanProperty(True)
    percent_symbol = BooleanProperty(True)
    value = NumericProperty(0)
    animation = BooleanProperty(True)
    style = OptionProperty("m2", options = ["m2","m4","m3","m2"])
    max_width = NumericProperty(1)
    percent_font_size = NumericProperty()
    text_font_size = NumericProperty()
    animation_speed = NumericProperty(0.5)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_color = self.primary_color
        self.line_back_color = self.bgr_color
        self.text_color = self.txt_color
        self.back_color = self.trans_color
        Clock.schedule_once(self.check)
        
    def check(self,*args):
        self.size = (self.max_width, self.max_width/2) if self.style == "m4" else (self.max_width,self.max_width)
        if self.animation:
            Clock.schedule_once(self.update)
            
            
    def update(self,*args):       
        self.temporary = self.value
        anim = Animation(value = 0, duration = self.animation_speed)
        anim.bind(on_complete = self.update2)
        anim.start(self)
        
    def update2(self,*args):
        anim = Animation(value = self.temporary, duration = self.animation_speed)
        anim.start(self)
