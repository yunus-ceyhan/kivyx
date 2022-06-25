"""
<MainApp>:
    bg_color: root.bgr_color
    XChip:
        right_icon: "check"
        left_icon: "android"
        text: "hello"
        pos_hint: {"center_x":.5,"center_y":.5}
        type: "outlined"
        bg_color: root.red_color
        #text_color: root.opposite_color


"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, OptionProperty, StringProperty
from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivyx.theming import Theming

Builder.load_string("""

<XChip>:
    size_hint: None, None
    height: dp(32)
    padding: [dp(16),0,dp(16),0] if not root.right_icon and not root.left_icon else [dp(4),0,dp(16),0]\
        if not root.right_icon else [dp(16),0,dp(4),0]\
        if not root.left_icon else [dp(4),0,dp(4), 0]
    width: max(dp(24) + ic.width + icr.width + lb.texture_size[0], dp(32))
    #spacing: dp(8) if root.icon else 0
    bg_color: self.bg_color if root.type == "filled" else [0,0,0,0]
    radius: [dp(8),]
    canvas.after:
        Color:
            rgba: root.txt_color if root.type != "filled" else root.trans_color
        Line:
            width: dp(0.4)
            rounded_rectangle: (self.x, self.y, self.width, self.height,dp(8)) 
        
    XIcon:
        id: ic
        icon: root.left_icon
        font_size: "17dp"
        size_hint: None,None
        size: dp(32) if root.left_icon else 0, dp(32)
        color: root.icon_color
    XLabel:
        id: lb
        text: root.text
        aligned: False
        pos_hint: {"center_y":.5}
        color: root.text_color
        font_size: "13sp"
    XIcon:
        id: icr
        icon: root.right_icon
        font_size: "17dp"
        size_hint: None,None
        size: dp(32) if root.right_icon else 0, dp(32)
        color: root.icon_color
""")


class XChip(Theming, XBoxLayout):
    type = OptionProperty("outlined", options=["filled", "outlined"])
    left_icon = StringProperty()
    right_icon = StringProperty()
    text = StringProperty()
    text_color = ColorProperty()
    icon_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
