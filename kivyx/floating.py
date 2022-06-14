
"""
<MainApp>:
    bg_color: "#F3F6EA"
    XFabBase:
        icon: "apple"
    XFab:
        text: "hello world"
        icon: "apple"
        on_release: self.extend_button()
        
     XActionFab:
        icon: "apple"
        XFabItem:
            icon: "android"
        XFabItem:
            icon: "pencil"
        XFabItem:
            icon: "mail"

"""

from kivyx.behavior import RectangularBehavior
from kivy.clock import Clock
from kivyx.card import XCard
from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivy.properties import StringProperty, ColorProperty, NumericProperty, ListProperty
from kivyx.theming import Theming
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.animation import Animation

Builder.load_string("""
#:import Window kivy.core.window.Window
        
<XFabTextBase>:
    id: fab
    size_hint: None,None
    size: (max((self.padding[0]+self.padding[2])+ic.width+lb.texture_size[0]+self.spacing,dp(56))\
        if root.text else dp(56) ,dp(56))
    padding: [dp(16),dp(16),dp(20),dp(16)] if root.text else [dp(16),]
    spacing: dp(16)
    radius: [dp(16),]
    XIcon:
        id: ic
        icon: root.icon
        text_color: root.icon_color
    XLabel:
        id: lb
        aligned: False 
        text: root.text
        color: root.icon_color

<XFab>:
    size_hint: None, None
    width: Window.width
    height: dp(88)
    padding: dp(16)
    Widget:
    XFabTextBase:
        id: fb
        icon: root.icon
        text: root.text
        icon_color: root.icon_color
        on_press: root.dispatch('on_press',*args)
        on_release: root.dispatch('on_release',*args)
        bg_color: root.button_bg_color
        elevation: root.elevation
        distance: root.distance

<XFabBase>:
    size_hint: None,None
    size:  dp(56) ,dp(56)
    padding: [dp(16),]
    spacing: dp(16)
    radius: [dp(16),]
    XIcon:
        icon: root.icon
        text_color: root.icon_color

<XFabItem>:
    id: item
    size_hint: None, None
    width: Window.width
    height: dp(40)
    padding: [0,0,dp(25),0]
    pos_hint: {"center_y": .5}
    Widget:
    XFabBase:
        size_hint: None,None
        size: dp(40),item.height
        padding: [dp(8),]
        radius: [dp(12),]
        icon: root.icon
        icon_color: root.icon_color
        on_press: root.dispatch('on_press',*args)
        on_release: root.dispatch('on_release',*args)


<XActionFab>:
    orientation: "vertical"
    spacing: dp(8)
    ScrollView:
        id: scr
        size_hint_y: None
        height: 0
        on_scroll_stop: root.set_action() if self.height > 0 else None
        BoxLayout:
            id: bx
            orientation: "vertical"
            spacing: dp(16)
            size_hint_y: None
            height: scr.height

    BoxLayout:
        id: bt
        size_hint: None, None
        width: Window.width
        height: dp(88)
        padding: dp(16)
        Widget:
        XFabBase:
            id: fb
            icon: root.icon
            icon_color: root.icon_color
            on_press: root.dispatch('on_press',*args)
            on_release: root.dispatch('on_release',*args)

""")

class XFabTextBase(RectangularBehavior,XCard):
    icon =  StringProperty()
    text =  StringProperty()
    icon_color = ColorProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_radius = [dp(15),]
        self.icon_color = self.txt_color
        


class XFab(Theming, XBoxLayout):
    icon =  StringProperty()
    text =  StringProperty()
    icon_color = ColorProperty()
    button_bg_color = ColorProperty()
    elevation = NumericProperty(0.05)
    distance = NumericProperty(dp(14))
    status = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = self.txt_color
        self.button_bg_color = self.card_color
        self.register_event_type('on_press')
        self.register_event_type('on_release')
        Clock.schedule_once(self.adjust)
        
        
        
    def adjust(self,*args):
        self.status = "extended" if self.text else "shrinked"
        self.current_width = self.ids.fb.width
        self.current_text = self.text


    def extend_button(self,status,*args):
        if status == "shrink" and self.text:
            self.current_width = self.ids.fb.width
            self.current_text = self.text
            self.remove_text()
            self.status = "shrinked"
        elif status == "extend":
            Clock.schedule_once(self.add_text,0.2)
            anim = Animation(width = self.current_width, duration = 0.1)
            anim.start(self.ids.fb)
            self.status = "extended"

    def remove_text(self,*args):
        self.text = ""

    def add_text(self,*args):
        self.text = self.current_text

    def on_press(self, *args):
        pass

    def on_release(self, *args):
        pass

class XFabBase(RectangularBehavior,XCard):
    icon =  StringProperty()
    icon_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_radius = [dp(12),]
        self.icon_color = self.txt_color    

class XFabItem(Theming,XBoxLayout):
    icon =  StringProperty()
    icon_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = self.txt_color
        self.register_event_type('on_press')
        self.register_event_type('on_release')

    def on_press(self, *args):
        pass

    def on_release(self, *args):
        pass

class XActionFab(Theming,XBoxLayout):
    icon =  StringProperty()
    icon_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = self.txt_color
        self.register_event_type('on_press')
        self.register_event_type('on_release')

    def add_widget(self,widget,*args):
        if isinstance(widget, XFabItem):
            self.ids.bx.add_widget(widget)
        else:
            super(XActionFab, self).add_widget(widget)

    def set_action(self,*args):
        if self.ids.scr.height == 0:
            anim = Animation(height = Window.height - self.ids.bt.height,duration = 0.4)
            anim.start(self.ids.scr)
        else:
            anim = Animation(height = 0,duration = 0.1)
            anim.start(self.ids.scr)

    def on_press(self, *args):
        pass

    def on_release(self, *args):
        self.set_action()

