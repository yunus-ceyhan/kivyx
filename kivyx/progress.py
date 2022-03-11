"""
<MainApp>:
    XProgress:
        pos_hint: {"center_x":.5,"center_y":.5}
        value: 50

"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, BooleanProperty, OptionProperty
from kivy.uix.progressbar import ProgressBar


Builder.load_string("""
<XProgress>:
    canvas:
        Clear
        Color:
            rgba:  root.back_color
        Rectangle:
            size:    (self.width , dp(4)) if self.orientation == 'horizontal' else (dp(4),self.height)
            pos:   (self.x, self.center_y - dp(4)) if self.orientation == 'horizontal' \
                else (self.center_x - dp(4),self.y)
        Color:
            rgba:  root.track_color
        Rectangle:
            size:     (self.width*self.value_normalized, sp(4)) if self.orientation == 'horizontal' else (sp(4), \
                self.height*self.value_normalized)
            pos:    (self.width*(1-self.value_normalized)+self.x if self.reversed else self.x, self.center_y - dp(4)) \
                if self.orientation == 'horizontal' else \
                (self.center_x - dp(4),self.height*(1-self.value_normalized)+self.y if self.reversed else self.y)

""")

class XProgress(Theming,ProgressBar):
    reversed = BooleanProperty(False)
    orientation = OptionProperty('horizontal', options=['horizontal', 'vertical'])
    back_color = ColorProperty()
    track_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_color = self.disabled_color
        self.track_color = self.primary_color
