from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivy.properties import ColorProperty, BooleanProperty, NumericProperty, StringProperty, OptionProperty
from kivyx.theming import Theming
from kivyx.label import XLabel
from kivyx.behavior import RectangularBehavior


Builder.load_string("""
<XToolbar>:
    bg_color: root.bg_color
    size_hint_y: None
    height: sp(64)
    canvas.before:
        Color:
            rgba: 0,0,0, root.percent(root.elevation,5)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,100))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,100))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius   
        Color:
            rgba: 0,0,0, root.percent(root.elevation,12)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,70))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,70))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
        Color:
            rgba: 0,0,0, root.percent(root.elevation,15)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,50))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,50))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,19)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,35))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,35))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
        Color:
            rgba: 0,0,0, root.percent(root.elevation,24)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,20))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,20))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
        Color:
            rgba: 0,0,0, root.percent(root.elevation,30)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,10))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,10))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
        Color:
            rgba: 0,0,0, root.percent(root.elevation,37)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,5))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,5))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
        Color:
            rgba: 0,0,0,root.percent(root.elevation,45)
        RoundedRectangle:
            size: self.size[0], dp(root.percent(root.distance,3))
            pos: self.pos[0],self.pos[1] - dp(root.percent(root.distance,3))\
                                            if not root.top else self.pos[1] + self.height
            radius: root.radius
            
    canvas.after:
        Color:
            rgba: root.trans_color if root.elevation > 0 else root.line_color
        RoundedRectangle:
            size: self.size[0], root.line_width
            pos: self.pos[0],self.pos[1] if not root.top else self.pos[1] + (self.height - root.line_width)
            radius: root.radius

<XAppSearchbar>:
    padding: [dp(24),0,dp(24),0]
    XBoxLayout:
        id: sbx
        bg_color: root.bar_color
        radius: [dp(7),] if root.style == 'm2' else [dp(24),]
        size_hint_y: None
        height: dp(48)
        pos_hint: {"center_y": .5}
        padding: [0,] if root.style == 'm2' else [dp(4),0,0,0]
        XIconButton:
            icon: root.left_icon
            on_press: root.dispatch('on_left_icon_press', *args)
            on_release: root.dispatch('on_left_icon_release', *args)

        CLabel:
            text: root.text
            on_press: root.dispatch('on_bar_press', *args)
            on_release: root.dispatch('on_bar_release', *args)
            size_hint_y: None
            height: dp(48)
            aligned: True
            halign: "left"
            font_size: "17sp"
            font_name: root.font_name
            opacity: .9
        XIconButton:
            icon: root.middle_icon
            on_press: root.dispatch('on_middle_icon_press', *args)
            on_release: root.dispatch('on_middle_icon_release', *args)
            disabled: False if self.icon else True
            opacity: 1 if self.icon else 0
        XIconButton:
            icon: root.right_icon
            on_press: root.dispatch('on_right_icon_press', *args)
            on_release: root.dispatch('on_right_icon_release', *args)


<XSearchbar>:
    padding: [dp(2),dp(8),dp(2),dp(8)]
    text: input.text
    XIconButton:
        icon: root.left_icon
        on_press: root.dispatch('on_left_icon_press', *args)
        on_release: root.dispatch('on_left_icon_release', *args)

    XTextInput:
        id: input
        font_size: "20sp"
        font_name: root.font_name
        size_hint_y: None
        height: dp(48)
        focus: root.focus
        use_bubble: False
        use_handles: False
        background_color: 0,0,0,0
        foreground_color: root.txt_color
        cursor_color: root.txt_color
        cursor_width: "2sp"
        padding: (dp(14),dp(12),0,dp(12))
        hint_text: root.hint_text
        hint_text_font_size: "20sp"
        multiline: False
        pos_hint:{"center_y": .5}
        on_text_validate: root.dispatch('on_text_validate', *args)
        on_text: root.dispatch('on_text', *args)

    XIconButton:
        icon: root.right_icon
        on_press: root.dispatch('on_right_icon_press', *args)
        on_release: root.dispatch('on_right_icon_release', *args)

<XAppToolbar>:
    padding: [dp(2),dp(8),dp(2),dp(8)]
    XIconButton:
        icon: root.left_icon
        width: dp(48) if root.left_icon else dp(16)
        on_press: root.dispatch('on_left_icon_press', *args)
        on_release: root.dispatch('on_left_icon_release', *args)
    Widget:
        size_hint: None,None
        height: dp(48)
        width: dp(48) if root.halign == "center" and not root.middle_icon else 0
        disabled: True

    XLabel:
        text: root.title
        bold: False
        font_size: "20sp"
        opacity: .9
        aligned: True 
        halign: root.halign
        shorten_from: "right"
        font_name: root.font_name
        text_color: root.title_color
        
    XIconButton:
        icon: root.middle_icon
        on_press: root.dispatch('on_middle_icon_press', *args)
        on_release: root.dispatch('on_middle_icon_release', *args)
        disabled: False if self.icon else True
        opacity: 1 if self.icon else 0
        width: dp(48) if self.icon else 0

    XIconButton:
        icon: root.right_icon
        on_press: root.dispatch('on_right_icon_press', *args)
        on_release: root.dispatch('on_right_icon_release', *args)
        
<CLabel>:
""")

class CLabel(XLabel,RectangularBehavior):
    pass

class XToolbar(Theming,XBoxLayout):
    bg_color = ColorProperty()
    top = BooleanProperty(False)
    elevation = NumericProperty(0.08)
    distance = NumericProperty("3dp")
    line_color = ColorProperty()
    line_width = NumericProperty("0.5dp")
    def __init__(self, **kwargs):
        super(XToolbar, self).__init__(**kwargs)
        self.bg_color = self.card_color
        self.line_color = self.txt_color
        
    def percent(self, max, percent):
        return (max/100)*percent

class XAppToolbar(XToolbar):
    title = StringProperty()
    focus = BooleanProperty(False)
    right_icon = StringProperty()
    middle_icon = StringProperty()
    left_icon = StringProperty()
    font_name = StringProperty("Roboto")
    title_color = ColorProperty()
    halign = OptionProperty("center", options = ["left","right","center"])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title_color = self.txt_color
        self.register_event_type('on_left_icon_press')
        self.register_event_type('on_left_icon_release')
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')
        self.register_event_type('on_middle_icon_press')
        self.register_event_type('on_middle_icon_release')     


    def on_left_icon_press(self, *args):
        pass

    def on_left_icon_release(self, *args):
        pass

    def on_right_icon_press(self, *args):
        pass

    def on_right_icon_release(self, *args):
        pass
    
    def on_middle_icon_press(self, *args):
        pass

    def on_middle_icon_release(self, *args):
        pass

class XAppSearchbar(XToolbar):
    text = StringProperty()
    right_icon = StringProperty()
    middle_icon = StringProperty()
    left_icon = StringProperty()
    font_name = StringProperty("Roboto")
    bar_color = ColorProperty()
    style = OptionProperty("m2", options = ["m2","m3"])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bar_color = self.bgr_color
        self.register_event_type('on_bar_press')
        self.register_event_type('on_bar_release')
        self.register_event_type('on_left_icon_press')
        self.register_event_type('on_left_icon_release')
        self.register_event_type('on_middle_icon_press')
        self.register_event_type('on_middle_icon_release')
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')       

    def on_bar_press(self, *args):
        pass

    def on_bar_release(self, *args):
        pass

    def on_left_icon_press(self, *args):
        pass

    def on_left_icon_release(self, *args):
        pass

    def on_middle_icon_press(self, *args):
        pass

    def on_middle_icon_release(self, *args):
        pass

    def on_right_icon_press(self, *args):
        pass

    def on_right_icon_release(self, *args):
        pass

class XSearchbar(XToolbar):
    font_name = StringProperty("Roboto")
    hint_text = StringProperty("Search")
    focus = BooleanProperty(False)
    right_icon = StringProperty("")
    left_icon = StringProperty("chevron-left")
    state = NumericProperty(1)
    def __init__(self, **kwargs):
        super(XSearchbar, self).__init__(**kwargs)
        self.register_event_type('on_text_validate')
        self.register_event_type('on_text')
        self.register_event_type('on_left_icon_press')
        self.register_event_type('on_left_icon_release')
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')

    def on_text_validate(self, *args):
        pass

    def on_text(self, *args):
        pass

    def on_left_icon_press(self, *args):
        pass

    def on_left_icon_release(self, *args):
        pass

    def on_right_icon_press(self, *args):
        pass

    def on_right_icon_release(self, *args):
        self.ids.input.text = ""
        self.focus = True
