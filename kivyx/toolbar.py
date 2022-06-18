from xmlrpc.client import Boolean
from kivy.app import App
from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivy.properties import ColorProperty, BooleanProperty, NumericProperty, StringProperty
from kivyx.theming import Theming
Builder.load_string("""
<XToolbar>:
    bg_color: root.bg_color
    size_hint_y: None
    height: sp(64)
    pos_hint: {"top": 1}
    canvas.after:
        Color:
            rgba: [0,0,0,root.elevation]
        Rectangle:
            size: self.size[0], dp(1)
            pos: (self.pos[0], self.height-dp(1) if root.top else self.pos[1])

<XAppSearchbar>:
    padding: [dp(20),0,dp(20),0]
    top: False
    XBoxLayout:
        id: sbx
        bg_color: root.bar_color
        radius: [dp(7),]
        size_hint_y: None
        height: dp(48)
        pos_hint: {"center_y": .5}
        XIconButton:
            icon: root.left_icon
            on_press: root.dispatch('on_left_icon_press', *args)
            on_release: root.dispatch('on_left_icon_release', *args)

        XFlatButton:
            text: root.text
            on_press: root.dispatch('on_bar_press', *args)
            on_release: root.dispatch('on_bar_release', *args)
            size_hint: None, None
            height: dp(48)
            button_width: sbx.width - dp(144)
            halign: "left"
            font_size: "17sp"
            font_name: root.font_name
            opacity: .5
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

    TextInput:
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

    XLabel:
        text: root.title
        bold: False
        font_size: "20sp"
        opacity: .9
        aligned: False if root.right_icon and root.left_icon else True 
        halign: "left"
        shorten: True
        shorten_from: "right"
        font_name: root.font_name

    XIconButton:
        icon: root.right_icon
        on_press: root.dispatch('on_right_icon_press', *args)
        on_release: root.dispatch('on_right_icon_release', *args)
""")

class XToolbar(Theming,XBoxLayout):
    bg_color = ColorProperty()
    top = BooleanProperty(False)
    elevation = NumericProperty(0.09)
    def __init__(self, **kwargs):
        super(XToolbar, self).__init__(**kwargs)
        self.bg_color = self.card_color

class XAppToolbar(XToolbar):
    title = StringProperty()
    focus = BooleanProperty(False)
    right_icon = StringProperty()
    left_icon = StringProperty()
    font_name = StringProperty("Roboto")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_left_icon_press')
        self.register_event_type('on_left_icon_release')
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')       


    def on_left_icon_press(self, *args):
        pass

    def on_left_icon_release(self, *args):
        pass

    def on_right_icon_press(self, *args):
        pass

    def on_right_icon_release(self, *args):
        pass

class XAppSearchbar(XToolbar):
    text = StringProperty()
    right_icon = StringProperty()
    middle_icon = StringProperty()
    left_icon = StringProperty()
    font_name = StringProperty("Roboto")
    bar_color = ColorProperty()
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
