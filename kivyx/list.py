from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty, NumericProperty
from kivyx.behavior import RectangularBehavior
from kivy.uix.boxlayout import BoxLayout
from kivyx.theming import Theming
from kivyx.boxlayout import XBoxLayout
from kivyx.card import XCard

Builder.load_string("""
<XListItem>:
    size_hint_y: None
    height: dp(48)
    padding: [dp(24),0,0,0]
    spacing: dp(12)
    XLabel:
        id: lb
        text: root.text
        aligned: True
        halign: "left"
        valign: "middle"
        font_size: root.font_size
        front_name: root.font_name
        text_color: root.text_color
<XIconListItem>:
    size_hint_y: None
    height: dp(56)
    padding: [dp(4),dp(4),dp(16),dp(4)]
    spacing: dp(4)
    bg_color: root.card_color
    XIcon:
        id: li
        icon: root.icon
        aligned: True
        halign: "center"
        valign: "middle"
        color: root.icon_color
        size_hint: None, None
        size: dp(48), dp(48)
    XLabel:
        id: lb
        text: root.text
        aligned: True
        halign: "left"
        valign: "middle"
        font_size: root.font_size
        front_name: root.font_name
        text_color: root.text_color
        size_hint_y: None
        height: dp(48)
        
<XImageListItem>:
    size_hint_y: None
    height: dp(48)
    padding: [dp(6),dp(6),dp(6),dp(6)]
    spacing: dp(12)
    bg_color: root.card_color
    Image:
        id: li
        source: root.source
        size_hint: None,None
        size: dp(36),dp(36)
        keep_ratio: False
        allow_stretch: True
    XLabel:
        id: lb
        text: root.text
        aligned: True
        halign: "left"
        valign: "middle"
        font_size: root.font_size
        front_name: root.font_name
        text_color: root.text_color,
        
<XImageTwoLineListItem>:
    size_hint_y: None
    height: dp(56)
    padding: [dp(10),]
    spacing: dp(10)
    bg_color: root.card_color
    Image:
        source: root.source
        size_hint: None,None
        size: dp(36),dp(36)
        keep_ratio: False
        allow_stretch: True
    BoxLayout:
        spacing: dp(8)
        orientation: "vertical"
        XLabel:
            text: root.title
            aligned: True
            halign: "left"
            valign: "middle"
            font_size: root.font_size
            font_name: root.font_name
            text_color: root.text_color
            shorten: True
            shorten_from: "right"          
        XLabel:
            text: root.text
            aligned: True
            halign: "left"
            valign: "middle"
            font_size: root.font_size - sp(3)
            #front_name: root.font_name
            text_color: root.text_color
            shorten: True
            
<XTwoIconListItem>:
    size_hint_y: None
    height: dp(56)
    #padding: [0,0,dp(4),0]
    XIconListItem:
        icon: root.left_icon
        text: root.text
        on_press: root.dispatch('on_press', *args)
        on_release: root.dispatch('on_release', *args)
        font_size: root.font_size
        front_name: root.font_name
        bg_color: [0,0,0,0]
        elevation: 0
    XIconButton:
        icon: root.right_icon
        aligned: True
        halign: "right"
        color: root.icon_color
        on_press: root.dispatch('on_right_icon_press', *args)
        on_release: root.dispatch('on_right_icon_release', *args)
        size_hint: None, None
        size: dp(56),dp(56)
        
        
<XCustomListItem>:
    id: xc
    size_hint_y: None
    height: dp(56)
    XImageTwoLineListItem:
        id: xim
        height: xc.height
        source: root.image_source
        title: root.title
        text: root.text
        font_size: root.font_size
        front_name: root.font_name
        text_color: root.text_color        
        on_press: root.dispatch('on_press', *args)
        on_release: root.dispatch('on_release', *args)        
    XIconButton:
        icon: root.right_icon
        aligned: True
        halign: "right"
        color: root.icon_color
        on_press: root.dispatch('on_right_icon_press', *args)
        on_release: root.dispatch('on_right_icon_release', *args)
""")

class XListItem(RectangularBehavior,BoxLayout):
    text = StringProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color

class XTwoIconListItem(XCard):
    left_icon = StringProperty()
    right_icon = StringProperty("bookmark-outline")
    text = StringProperty()
    icon_color = ColorProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')
        self.register_event_type('on_press')
        self.register_event_type('on_release')

    def on_press(self,*args):
        pass

    def on_release(self,*args):
        pass

    def on_right_icon_press(self,*args):
        pass

    def on_right_icon_release(self,*args):
        pass
        
class XCustomListItem(XCard):
    image_source = StringProperty()
    right_icon = StringProperty("bookmark-outline")
    title = StringProperty()
    text = StringProperty()
    icon_color = ColorProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super(XCustomListItem, self).__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')
        self.register_event_type('on_press')
        self.register_event_type('on_release')

    def on_press(self,*args):
        pass

    def on_release(self,*args):
        pass

    def on_right_icon_press(self,*args):
        pass

    def on_right_icon_release(self,*args):
        pass
    
class XIconListItem(RectangularBehavior,XCard):
    icon = StringProperty()
    text = StringProperty()
    icon_color = ColorProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
        
class XImageListItem(RectangularBehavior,BoxLayout):
    source = StringProperty()
    text = StringProperty()
    icon_color = ColorProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
        
class XImageTwoLineListItem(RectangularBehavior,XCard):
    source = StringProperty()
    title = StringProperty()
    text = StringProperty()
    icon_color = ColorProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("16sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color
