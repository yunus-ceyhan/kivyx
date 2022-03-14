"""
<MainApp>:
    XBoxLayout:
        spacing: dp(20)
        padding: [dp(20),]
        orientation: "vertical"
        XButton:
            text: "pfhhfghfghfghfghfgh"
            style: "m3"
            #button_width: dp(500)
            on_release:
                menu.open_menu(self)
        XFlatButton:
            text: "hello"
        XFlatIconButton:
            text: "hello"
            icon: "delete"
        XLIconButton:
            text: "Python Language"
            icon: "delete"
            style: "m2"
            #button_width: dp(500)
        XRIconButton:
            text: "hello"
            icon: "delete"

"""



from xmlrpc.client import Boolean
from kivy.lang import Builder
from kivyx.card import XCard
from kivy.uix.widget import Widget
from kivyx.behavior import RectangularBehavior, CircularBehavior
from kivyx.boxlayout import XBoxLayout
from kivy.properties import StringProperty, BooleanProperty, ColorProperty, NumericProperty, OptionProperty
from kivyx.theming import Theming
from kivy.metrics import dp
from kivy.clock import Clock

Builder.load_string("""
<XButton>:
    size_hint: None,None
    height: dp(42)
    width: root.button_width if root.button_width > 0 else max((self.padding[0]*2)+lb.texture_size[0],dp(64))
    padding: [dp(16),0,dp(16),0] if root.style == "m2" else [dp(24),0,dp(24),0]
    radius: [dp(5),] if root.style == "m2" else [dp(20),]
    XLabel:
        id: lb
        aligned: True if root.button_width > self.texture_size[0] else False
        text: root.text
        bold: root.bold
        color: root.text_color 

<XFlatButton>:
    size_hint: None,None
    height: dp(42)
    padding: [dp(16),0,dp(16),0]
    width: root.button_width if root.button_width else max((self.padding[0]*2)+lb.texture_size[0],dp(34))
    XLabel:
        id: lb
        aligned: True if root.button_width > self.texture_size[0] else False
        halign: root.halign
        text: root.text
        bold: root.bold
        color: root.text_color
        font_size: root.font_size

<XFlatIconButton>:
    size_hint: None, None
    height: dp(42)
    width: root.button_width if root.button_width > 0 else max(lb.texture_size[0]+ ic.width + dp(32),dp(64))
    padding: [dp(10),0,dp(16),0]
    radius: [dp(5),]
    spacing: dp(8)
    XIcon:
        id: ic
        icon: root.icon
        color: root.text_color
        halign: "left"
        font_size: "18sp"
    XLabel:
        id: lb
        aligned: True if root.button_width > self.texture_size[0] else False
        text: root.text
        bold: root.bold
        color: root.text_color
        halign: "left"

<XFlatRIconButton>:
    size_hint: None, None
    height: dp(42) 
    width: root.button_width if root.button_width > 0 else max(lb.texture_size[0]+ ic.width + dp(32),dp(64))
    padding: [dp(16),0,dp(16),0]
    radius: [dp(5),]
    spacing: dp(8)
    XLabel:
        id: lb
        aligned: True if root.button_width > self.texture_size[0] else False
        text: root.text
        bold: root.bold
        color: root.text_color
        halign: "right"
    XIcon:
        id: ic
        aligned: True if root.button_width > self.texture_size[0] else False
        font_size: "18sp"
        icon: root.icon
        color: root.text_color
        halign: "right"

<XIconButton>:
    size_hint: None, None
    size: dp(48),dp(48)
    padding: [dp(12),]
    XIcon:
        icon: root.icon
        aligned: True
        halign: "center"
        valign: "middle"

<XLIconButton>:
    size_hint: None, None
    height: dp(42) 
    width: root.button_width if root.button_width > 0 else max(lb.texture_size[0]+ ic.width + dp(32),dp(64)) \
        if self.style == "m2" else max(lb.texture_size[0]+ ic.width + dp(50),dp(64))
    padding: [dp(10),0,dp(16),0] if root.style == "m2" else [dp(20),0,dp(24),0] 
    radius: [dp(5),] if root.style == "m2" else [dp(20),]
    spacing: dp(8)
    XIcon:
        id: ic
        icon: root.icon
        color: root.text_color
        font_size: "18sp"
        aligned: True if root.button_width > self.texture_size[0] else False
        halign: "center"
    XLabel:
        id: lb
        aligned: True if root.button_width > self.texture_size[0] else False
        text: root.text
        bold: root.bold
        color: root.text_color
        halign: "left"

<XRIconButton>:
    size_hint: None, None
    height: dp(42) 
    width: root.button_width if root.button_width > 0 else max(lb.texture_size[0]+ ic.width + dp(38),dp(64)) \
        if self.style == "m2" else max(lb.texture_size[0]+ ic.width + dp(52),dp(64))
    padding: [dp(16),0,dp(16),0] if root.style == "m2" else [dp(24),0,dp(22),0] 
    radius: [dp(5),] if root.style == "m2" else [dp(20),]
    spacing: dp(8)
    XLabel:
        id: lb
        aligned: True if root.button_width > self.texture_size[0] else False
        text: root.text
        bold: root.bold
        color: root.text_color
        halign: "right"
    XIcon:
        id: ic
        aligned: True if root.button_width > self.texture_size[0] else False
        font_size: "18sp"
        icon: root.icon
        color: root.text_color
        halign: "right"
""")

class XButton(RectangularBehavior, XCard):
    text = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    button_width = NumericProperty(0)
    style = OptionProperty("m2", options = ["m2","m3"])
    def __init__(self, **kwargs):
        super(XButton, self).__init__(**kwargs)
        self.text_color = self.txt_color
        Clock.schedule_once(self.set_radius)

    def set_radius(self,*args):
        self.ripple_radius = self.radius






class XFlatButton(RectangularBehavior, XBoxLayout):
    text = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    button_width = NumericProperty(0)
    halign = StringProperty("left")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_radius = [dp(5),]
        self.text_color = self.txt_color


class XFlatIconButton(RectangularBehavior, XBoxLayout):
    text = StringProperty()
    icon = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    button_width = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_radius = [dp(5),]
        self.text_color = self.txt_color

class XFlatRIconButton(RectangularBehavior, XBoxLayout):
    text = StringProperty()
    icon = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    button_width = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color


class XIconButton(CircularBehavior, XBoxLayout):
    icon = StringProperty()

class XLIconButton(RectangularBehavior, XCard):
    text = StringProperty()
    icon = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    button_width = NumericProperty(0)
    style = OptionProperty("m2", options = ["m2","m3"])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        Clock.schedule_once(self.set_radius)

    def set_radius(self,*args):
        self.ripple_radius = self.radius
        print(self.width)


class XRIconButton(RectangularBehavior, XCard):
    text = StringProperty()
    icon = StringProperty()
    bold = BooleanProperty(False)
    text_color = ColorProperty()
    button_width = NumericProperty(0)
    style = OptionProperty("m2", options = ["m2","m3"])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        Clock.schedule_once(self.set_radius)

    def set_radius(self,*args):
        self.ripple_radius = self.radius
