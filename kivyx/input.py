
from kivy.lang import Builder
from kivy.properties import ColorProperty, NumericProperty, BooleanProperty,StringProperty
from kivyx.theming import Theming
from kivy.clock import Clock
from kivyx.floatlayout import XFloatLayout
from kivy.core.window import Window


Builder.load_string("""
<XInput>:
    id: main
    size_hint_y: None
    height: dp(48)
    pos_hint: {"center_x": .5 , "center_y": .5}
    bg_color: root.back_color
    canvas.before:
        Color:
            rgba: root.line_color
        Line:
            width: dp(0.6)
            rounded_rectangle: (self.x, self.y, self.width, self.height,dp(4))
    BoxLayout:
        pos_hint: {"center_x": .5 , "center_y": .5}
        TextInput:
            id: input
            text: root.text
            pos_hint: {"center_x": .5 , "center_y": .5}
            padding: [dp(16) ,(root.height /2) - (self.font_size/1.5),dp(12)\
                if not root.icon else 0,0]\
                    if not self.multiline else [dp(16) ,dp(12),dp(12)\
                        if not root.icon else 0,dp(12)]
            multiline: False if root.height <= dp(56) else True
            background_color: 0,0,0,0
            foreground_color: root.text_color
            on_text_validate: root.dispatch('on_text_validate', *args)
            on_text: root.dispatch('on_text', *args)
            cursor_color: root.line_color
        XIconButton:
            icon: root.icon
            height: main.height
            width: main.height if root.icon else 0
            disabled: False if root.icon else True
            opacity: 1 if root.icon else 0
            on_press: root.dispatch('on_icon_press', *args)
            on_release: root.dispatch('on_icon_release', *args)
        
    XLabel:
        text: root.title
        color: 0,0,0,1
        size_hint: None, None
        size: self.texture_size[0], dp(20)
        text_size: None, None
        aligned: True
        halign: "left"
        font_size: "12sp"
        color: root.title_color if not input.focus else root.line_color
        pos: [input.pos[0] + dp(16),((input.pos[1] + root.height) - (self.font_size/1.5))\
            if input.focus else ((input.pos[1] + root.height/2) - (self.height/2))\
                    if not input.text else ((input.pos[1] + root.height) - (self.font_size/1.5))]\
                        if not input.multiline else\
                            [input.pos[0] + dp(16),((input.pos[1] + root.size[1]) - (self.font_size/1.5))\
                                if input.focus else ((input.pos[1] + root.height) - dp(28))\
                                    if not input.text else (input.pos[1] + input.size[1] - (self.font_size/1.5))]
        canvas.before:
            Color:
                rgba: root.back_color
            Rectangle:
                size: self.size[0] + dp(8), self.size[1]/2
                pos: self.pos[0]-dp(4), self.pos[1]# - self.size[1]/2


""")


class XInput(Theming,XFloatLayout):
    back_color = ColorProperty()
    line_color = ColorProperty()
    title_color = ColorProperty()
    text_color = ColorProperty()
    icon_color = ColorProperty()
    
    icon = StringProperty("")
    text = StringProperty()
    title = StringProperty("Label aligement")
    focus = BooleanProperty()
    state = NumericProperty(1)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_color = self.bgr_color
        self.icon_color = self.txt_color
        self.line_color = self.txt_light
        self.title_color = self.txt_medium
        self.text_color = self.txt_color
        Window.bind(on_flip=self.color_line)
        self.register_event_type('on_text_validate')
        self.register_event_type('on_text')
        self.register_event_type('on_icon_press')
        self.register_event_type('on_icon_release')

    def color_line(self,*args):
        if self.ids.input.focus == False and self.state == 0:
            self.line_color = self.txt_light
            self.state = 1

        elif self.ids.input.focus == True and self.state == 1:
            self.line_color = self.xcolors["blue"]
            self.state = 0


    def on_text_validate(self, *args):
        pass

    def on_text(self, *args):
        pass

    def on_icon_press(self, *args):
        pass

    def on_icon_release(self, *args):
        pass

