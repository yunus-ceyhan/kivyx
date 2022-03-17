"""
<MainApp>:
    XProgress:
        pos_hint: {"center_x":.5,"center_y":.5}
        value: 50

"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, BooleanProperty, OptionProperty, NumericProperty, ListProperty
from kivy.uix.progressbar import ProgressBar
from kivy.metrics import dp


Builder.load_string("""
<XProgress>:
    canvas:
        Clear
        Color:
            rgba:  root.back_color
        RoundedRectangle:
            size:    (self.width , root.thickness) if self.orientation == 'horizontal' else (root.thickness,self.height)
            pos:   (self.x, self.center_y - root.thickness) if self.orientation == 'horizontal' \
                else (self.center_x - root.thickness,self.y+root.thickness)
            radius: root.radius
        Color:
            rgba:  root.track_color
        RoundedRectangle:
            size:     (self.width*self.value_normalized, root.thickness) if self.orientation == 'horizontal' else (root.thickness, \
                self.height*self.value_normalized)
            pos:    (self.width*(1-self.value_normalized)+self.x if self.reversed else self.x, self.center_y - root.thickness) \
                if self.orientation == 'horizontal' else \
                (self.center_x - root.thickness,self.height*(1-self.value_normalized)+self.y if self.reversed else self.y + root.thickness)
            radius: root.radius

""")

class XProgress(Theming,ProgressBar):
    thickness = NumericProperty(dp(4))
    reversed = BooleanProperty(False)
    orientation = OptionProperty('horizontal', options=['horizontal', 'vertical'])
    back_color = ColorProperty()
    track_color = ColorProperty()
    radius = ListProperty([0,])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_color = self.disabled_color
        self.track_color = self.primary_color
