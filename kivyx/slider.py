"""
<MainApp>:
    XSlider:
        pos_hint: {"center_x":.5,"center_y":.5}

"""
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty
from kivy.uix.slider import Slider


Builder.load_string("""
<XSlider>:
    size_hint_y: None
    height: dp(20)
    cursor_size: [dp(20),dp(20)]
    background_disabled_horizontal: "./kivyx/data/loading.png"
    background_disabled_vertical: "./kivyx/data/loading.png"
    background_horizontal: "./kivyx/data/loading.png"
    background_vertical: "./kivyx/data/loading.png"
    cursor_disabled_image: "./kivyx/data/loading.png"
    cursor_image: "./kivyx/data/loading.png"

    canvas.after:
        Color:
            rgba: root.back_color
        RoundedRectangle:
            size: self.size[0] - dp(30), dp(4)
            pos: self.pos[0] + dp(15) ,self.pos[1] + (self.height/2) - dp(4)
            radius: [dp(3),]

        Color:
            rgba: root.track_color
        RoundedRectangle:
            size: self.value_pos[0] - dp(80), dp(6)
            pos: self.pos[0] + dp(15)  ,self.pos[1] + (self.height/2) - dp(6)
            radius: [dp(3.5),]

        Color:
            rgba: root.cursor_color
        RoundedRectangle:
            size: dp(20),dp(20)
            pos: self.value_pos[0] - self.cursor_width/2,self.pos[1] + (self.height/2) - dp(12.5)
            radius: [dp(90),]

""")

class XSlider(Theming,Slider):
    back_color = ColorProperty()
    track_color = ColorProperty()
    cursor_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_color = self.disabled_color
        self.track_color = self.primary_color
        self.cursor_color = self.primary_color
