"""
<MainApp>:
    XBoxLayout:
        spacing: dp(20)
        padding: [dp(20),]
        orientation: "vertical"
        XButton:
            bg_color: self.primary_color
            text: self.style.title()
            style: "elevated" 
            #button_width: dp(380)
            #right_icon: "plus"
            left_icon: "plus"
            rounded: True
            text_color: root.colors("green",1)
            icon_color: self.text_color


"""


from kivy.lang import Builder
from kivyx.behavior import RectangularBehavior,CircularBehavior
from kivyx.boxlayout import XBoxLayout
from kivy.properties import StringProperty, ListProperty, BooleanProperty, ColorProperty, NumericProperty, OptionProperty
from kivyx.theming import Theming
from kivy.metrics import dp, sp
from kivy.clock import Clock

Builder.load_string("""
<XButton>:
    size_hint: None,None
    height: dp(40) if root.rounded else dp(48)
    width: root.button_width if root.button_width > 10\
        else max((self.padding[0]+self.padding[2])+lb.texture_size[0]+icr.width+icl.width,dp(64))
        
    padding: [((self.width - (lb.texture_size[0]+icr.width+icl.width))/2) + dp(8),0,0,0]\
        if not root.left_icon and root.right_icon and root.button_width > 10\
            else [((self.width - (lb.texture_size[0]+icr.width+icl.width))/2) - dp(8),0,0,0]\
                if not root.right_icon and root.right_icon and root.button_width > 10\
                    else [(self.width - (lb.texture_size[0]+icr.width+icl.width))/2,0,0,0]\
                        if root.button_width > 0 else [dp(24),0,dp(24),0]\
                            if not root.left_icon and not root.right_icon else [dp(8),0,dp(24),0]\
                                if root.left_icon and not root.right_icon else [dp(16),0,dp(8),0]\
                                    if root.right_icon and not root.left_icon else [dp(8),0,dp(8),0]\
                                        if root.right_icon and root.left_icon else [0,]

    radius: [dp(16),] if root.rounded else [dp(8),]
    
    canvas.before:
        Clear:
        Color:
            rgba: root.line_color if root.style == "outlined" else root.trans_color
        Line:
            width: dp(0.6)
            rounded_rectangle: (self.x- dp(0.5), self.y- dp(0.5), self.width+dp(1), self.height + dp(1),self.radius[0])

    XIcon:
        id: icl
        icon: root.left_icon
        color: root.icon_color
        font_size: "18sp"
        size_hint: None,None
        height: root.height
        width: dp(32) if root.left_icon else 0
        disabled: False if self.icon else True
        opacity: 1 if self.text else 0
    Label:
        id: lb
        size_hint_x: None
        width: self.texture_size[0]
        #aligned: True if root.button_width > self.texture_size[0] else False
        text: root.text
        bold: root.bold
        color: root.text_color 
        text_size: None, None
    XIcon:
        id: icr
        font_size: "18sp"
        icon: root.right_icon
        color: root.icon_color
        size_hint: None,None
        height: root.height
        width: dp(32) if root.right_icon else 0
        disabled: False if self.icon else True
        opacity: 1 if self.text else 0
        
<XIconButton>:
    size_hint: None, None
    size: dp(48),dp(48)
    padding: [(self.size[1]-root.font_size)/2,]
    XIcon:
        icon: root.icon
        aligned: True
        halign: "center"
        valign: "middle"
        font_size: root.font_size
        color: root.icon_color

        
<XSard>:
    canvas.before:

        Color:
            rgba: 0,0,0, root.percent(root.elevation,25)       
        RoundedRectangle:
            size: self.size[0] + dp(2) , self.size[1] + dp(1)
            pos: self.pos[0] - dp(1), self.pos[1] +dp(1)
            radius: root.radius                      
        Color:
            rgba: 0,0,0, root.percent(root.elevation,75)       
        RoundedRectangle:
            size: self.size[0] + dp(1.0) , self.size[1] + dp(0.5)
            pos: self.pos[0] - dp(0.5), self.pos[1] +dp(0.5)
            radius: root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,125)       
        RoundedRectangle:
            size: self.size[0] + dp(0.5) , self.size[1] + dp(0.25)
            pos: self.pos[0] - dp(0.25), self.pos[1] +dp(0.25)
            radius: root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,175)       
        RoundedRectangle:
            size: self.size[0] - dp(2), self.size[1] + dp(root.percent(root.distance,10))
            pos: self.pos[0] + dp(1), self.pos[1]-dp(root.percent(root.distance,20))
            radius: [root.radius[0]+(root.percent(root.distance,2)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,150)       
        RoundedRectangle:
            size: self.size[0] - dp(1.5), self.size[1] + dp(root.percent(root.distance,18))
            pos: self.pos[0] + dp(0.75), self.pos[1] - dp(root.percent(root.distance,36))
            radius: [root.radius[0]+(root.percent(root.distance,6)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,125)       
        RoundedRectangle:
            size: self.size[0] - dp(1), self.size[1] + dp(root.percent(root.distance,26))
            pos: self.pos[0] + dp(0.5), self.pos[1] - dp(root.percent(root.distance,52))
            radius: [root.radius[0]+(root.percent(root.distance,9)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation, 100)       
        RoundedRectangle:
            size: self.size[0] , self.size[1] + dp(root.percent(root.distance,34))
            pos: self.pos[0] , self.pos[1] - dp(root.percent(root.distance,68))
            radius: [root.radius[0]+(root.percent(root.distance,9)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,75)       
        RoundedRectangle:
            size: self.size[0] + dp(1), self.size[1] + dp(root.percent(root.distance,42))
            pos: self.pos[0] - dp(0.5), self.pos[1] - dp(root.percent(root.distance,84))
            radius: [root.radius[0]+(root.percent(root.distance,12)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,52)       
        RoundedRectangle:
            size: self.size[0] + dp(1.5), self.size[1] + dp(root.percent(root.distance,50))
            pos: self.pos[0] - dp(0.5), self.pos[1] - dp(root.percent(root.distance,100))
            radius: [root.radius[0]+(root.percent(root.distance,14)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,35)       
        RoundedRectangle:
            size: self.size[0] + dp(2), self.size[1] + dp(root.percent(root.distance,58))
            pos: self.pos[0] - dp(1), self.pos[1] - dp(root.percent(root.distance,116))
            radius: [root.radius[0]+(root.percent(root.distance,16)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,20)       
        RoundedRectangle:
            size: self.size[0] +dp(3) , self.size[1] + dp(root.percent(root.distance,66))
            pos: self.pos[0] - dp(1.5), self.pos[1] - dp(root.percent(root.distance,132))
            radius: [root.radius[0]+(root.percent(root.distance,17)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,10)       
        RoundedRectangle:
            size: self.size[0] +dp(4), self.size[1] + dp(root.percent(root.distance,74))
            pos: self.pos[0] - dp(2), self.pos[1] - dp(root.percent(root.distance,148))
            radius: [root.radius[0]+(root.percent(root.distance,18)/10),] if root.soft else root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,5)       
        RoundedRectangle:
            size: self.size[0] + dp(5) , self.size[1]  + dp(root.percent(root.distance,82))
            pos: self.pos[0] -dp(2.5) , self.pos[1] - dp(root.percent(root.distance,164))
            radius: [root.radius[0]+(root.percent(root.distance,18.5)/10),] if root.soft else root.radius
                        
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            size: self.size[0],self.size[1]
            pos: (self.pos[0] , self.pos[1])
            radius: root.radius

""")


class XSard(Theming, XBoxLayout):
    bg_color = ColorProperty()
    radius = ListProperty([0, ])
    elevation = NumericProperty(0.035)
    distance = NumericProperty(dp(1.2))
    soft = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bg_color = self.card_color

    def percent(self, max, percent):
        return (max/100)*percent


class XButton(RectangularBehavior, XSard):
    text = StringProperty()
    right_icon = StringProperty()
    left_icon = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    line_color = ColorProperty()
    icon_color = ColorProperty()
    button_width = NumericProperty(0)
    style = OptionProperty("elevated", options=["filled", "outlined","text","elevated"])
    rounded = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(XButton, self).__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
        self.line_color = self.txt_color
        Clock.schedule_once(self.set_radius)

    def set_radius(self, *args):
        self.ripple_radius = self.radius
        self.elevation = 0 if self.style != "elevated" else 0.035
        if self.style == "text" or self.style == "outlined":
            self.bg_color = self.trans_color
            
class XIconButton(CircularBehavior, XBoxLayout):
    icon = StringProperty()
    font_size = NumericProperty(sp(22))
    icon_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = self.txt_color
