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
from kivyx.card import XCard
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

    radius: [dp(20),] if root.rounded else [dp(8),]


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
        font_name: root.font_name
        font_size: root.font_size
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


""")




class XButton(RectangularBehavior, XCard):
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
    outline_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty(sp(14))

    def __init__(self, **kwargs):
        super(XButton, self).__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
        self.shadow_y  = - dp(2)
        self.shadow_distance = - dp(1)
        self.shadow_blur = dp(5)
        self.outline_color = self.line_color
        Clock.schedule_once(self.set_radius)

    def set_radius(self, *args):
        self.ripple_radius = self.radius
        self.shadow_radius = self.radius if len(self.radius) == 4 else \
            [self.radius[0],self.radius[0],self.radius[0],self.radius[0]]
        self.elevation = 0 if self.style != "elevated" else 0.2
        if self.style == "text" or self.style == "outlined":
            self.bg_color = self.trans_color
        self.outline = True if self.style == "outlined" else False

            
class XIconButton(CircularBehavior, XBoxLayout):
    icon = StringProperty()
    font_size = NumericProperty(sp(22))
    icon_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = self.txt_color
