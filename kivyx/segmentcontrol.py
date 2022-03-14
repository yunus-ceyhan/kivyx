"""
<MainApp>:
    bg_color: root.bgr_color
    XSegmentControl:
        pos_hint: {"center_x": .5, "center_y":.5}
        item_width:  dp(150)
        radius: [dp(16),]
        XSegmentItem:
            text: "Global"
        XSegmentItem:
            text: "China"
        XSegmentItem:
            text: "Downloads"
"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, NumericProperty
from kivyx.floatlayout import XFloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivyx.button import XFlatButton
from kivyx.theming import Theming
from kivy.clock import Clock
from kivyx.line import XLiney
from kivy.uix.widget import Widget


Builder.load_string("""
<XSegmentControl>:
    id: xsc
    size_hint: None, None
    height: dp(56)
    width: s.width + dp(32)
    bg_color: root.card_color
    canvas.before:
        Color:
            rgba: root.bgr_color
        RoundedRectangle:
            size: self.size[0] - dp(32), self.size[1] - dp(16)
            pos: self.pos[0] + dp(16), self.pos[1] + dp(8)
            radius: root.radius
    canvas.after:
        Color:
            rgba: root.line_color# if root.radius[0] > 0 else root.trans_color
        Line:
            width: dp(0.15)
            rectangle: (self.x + dp(16), self.y + dp(8) , self.width - dp(32), self.height - dp(16)) 
    XBoxLayout:
        id: fake
        radius: root.radius
        size_hint: None,None
        height: dp(40)
        width: self.minimum_width 
        pos_hint: {"center_x": .5, "center_y":.5}
        

    XCard:
        id: b
        radius: root.radius
        size_hint: None,None
        height: dp(36)
        width: s.children[0].width if len(s.children) > 0 else 0
        pos: s.children[0].pos if len(s.children) > 0 else [0,0]

    XBoxLayout:
        id: s
        radius: root.radius
        size_hint: None,None
        height: dp(40)
        width: max(self.minimum_width, root.item_width)
        pos_hint: {"center_x": .5, "center_y":.5}


<XSegmentItem>:
    pos_hint: {"center_y":.5}
    size_hint_y: None
    height: dp(36)


""")


class XSegmentItem(XFlatButton):
    pass


class XSegmentControl(XFloatLayout, Theming):
    item_width = NumericProperty()
    radius = ListProperty([0, ])
    line_color = ColorProperty()

    def __init__(self, **kwargs):
        super(XSegmentControl, self).__init__(**kwargs)
        self.ind = 0
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.adjust)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def adjust(self, *args):
        if self.ids.s.children:
            self.ids.fake.remove_widget(self.ids.fake.children[0])
            self.ids.s.remove_widget(self.ids.s.children[0])
            if self.item_width:
                for i in self.ids.s.children:
                    i.button_width = self.item_width
                    i.halign = "center"
                self.ids.b.width = self.item_width
                for x in self.ids.fake.children:
                    if not isinstance(x, XLiney):
                        x.size_hint_x = None
                        x.width = self.item_width
                    else:
                        x.height = dp(40) - (self.radius[0]*2)
            Clock.schedule_once(self.select_first)

    def select_first(self, *args):
        self.line_color = self.disabled_color if self.radius[0] == 0 else self.trans_color
        self.ids.b.width = self.ids.s.children[-1].width
        self.ids.b.pos = [self.ids.s.children[-1].pos[0],
                          self.ids.s.children[-1].pos[1]]
        self.ind = len(self.ids.fake.children) - 1
        self.fade_out()

    def add_widget(self, button, *args):
        if isinstance(button, XSegmentItem):
            button.bind(on_press=lambda x: self.change_segment(button))
            button.bind(on_press=lambda x: self.dispatch(
                'on_tab_press', button))
            button.bind(on_release=lambda x: self.dispatch(
                'on_tab_release', button))
            self.ids.s.add_widget(button)
            self.ids.fake.add_widget(Widget())
            self.ids.fake.add_widget(XLiney(size_hint_y=None, height=dp(
                40) - (self.radius[0]*2), pos_hint={"center_y": .5}, width=dp(1), opacity=.3))
            self.ids.s.add_widget(XLiney(size_hint_y=None, height=dp(
                40) - (self.radius[0]*2), pos_hint={"center_y": .5}, width=dp(1), opacity=0))
        else:
            super(XSegmentControl, self).add_widget(button)

    def change_segment(self, button):
        for i in self.ids.fake.children:
            i.opacity = .3
            i.height = dp(40) - (self.radius[0]*2)
        self.ids.b.width = button.width
        anim = Animation(pos=button.pos, duration=0.2)
        anim.start(self.ids.b)
        anim.bind(on_complete=self.fade_out)
        self.ind = self.ids.s.children.index(button)

    def fade_out(self, *args):
        try:
            self.ids.fake.children[self.ind+1].opacity = 0
        except:
            pass
        try:
            self.ids.fake.children[self.ind-1].opacity = 0
        except:
            pass
