from kivy.lang import Builder
from kivyx.card import XCard
from kivy.properties import ColorProperty, BooleanProperty, NumericProperty, StringProperty, OptionProperty, ListProperty
from kivyx.theming import Theming
from kivyx.label import XLabel
from kivyx.behavior import RectangularBehavior
from kivy.metrics import dp


Builder.load_string("""
<XToolbar>:
    size_hint_y: None
    height: sp(64)
    elevation: 0.16
    shadow_y: dp(1) if root.top else 0
    shadow_distance: -dp(2)
    shadow_blur: dp(9)
    
<XAppSearchbar>:
    padding: [dp(24),0,dp(24),0]
    XBoxLayout:
        id: sbx
        bg_color: root.bar_color
        radius: [dp(7),] if root.style == 'm2' else [dp(24),]
        size_hint_y: None
        height: dp(48)
        pos_hint: {"center_y": .5}
        padding: [0,] if root.style == 'm2' else [dp(4),0,dp(4),0]
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
        font_size: "18sp"
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
        width: dp(48) if root.halign == "center" and root.middle_icon else 0
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

class XToolbar(XCard):
    top = BooleanProperty(False)
    line_width = NumericProperty("0.5dp")
    def __init__(self, **kwargs):
        super(XToolbar, self).__init__(**kwargs)


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
