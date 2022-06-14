"""
<MainApp>:
    bg_color: root.bgr_color
    XSegmentControl:
        pos_hint: {"center_x": .5, "center_y":.5}
        item_width:  dp(120)
        radius: [dp(16),]
        style: "m3"
        XSegmentTextItem:
            text: "Global"
        XSegmentTextItem:
            text: "China"
        XSegmentIconItem:
            icon: "apple"
"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, NumericProperty, StringProperty,OptionProperty
from kivyx.floatlayout import XFloatLayout
from kivyx.boxlayout import XBoxLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivyx.button import XFlatButton
from kivy.clock import Clock
from kivyx.line import XLiney
from kivy.uix.widget import Widget
from kivyx.behavior import RectangularBehavior


Builder.load_string("""
<XSegmentControl>:
    id: xsc
    size_hint: None, None
    height: dp(56)
    width: s.width + dp(34)
    bg_color: root.card_color
    canvas.before:
        Color:
            rgba: root.bar_color
        RoundedRectangle:
            size: self.size[0] - dp(30), (self.size[1] - dp(16)) if root.style == 'm3' else (self.size[1] - dp(18))
            pos: self.pos[0] + dp(15), (self.pos[1] + dp(8))  if root.style == 'm3' else (self.pos[1] + dp(9))
            radius: root.radius
    canvas.after:
        Color:
            rgba: root.line_color# if root.style == 'm3' else root.trans_color
        Line:
            width: dp(0.2)
            rounded_rectangle: (self.x + dp(15), (self.y + dp(8)) if root.style == 'm3' else (self.y + dp(9)) , self.width - dp(30), (self.height - dp(16)) if root.style == 'm3' else (self.height - dp(18)),root.radius[0]) 
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
        pos: [self.pos[0], xsc.pos[1] + (xsc.height -self.height)/2 ]
        bg_color: root.item_color

    XBoxLayout:
        id: s
        radius: root.radius
        size_hint: None,None
        height: dp(40)
        width: max(self.minimum_width, root.item_width)
        pos_hint: {"center_x": .5, "center_y":.5}


<XSegmentTextItem>:
    pos_hint: {"center_y":.5}
    size_hint_y: None
    height: dp(36)
    text: root.text
    
<XSegmentIconItem>:
    pos_hint: {"center_y":.5}
    size_hint: None, None
    height: dp(36)
    width: root.button_width
    padding: [(root.button_width/2) - (ic.width/2),0,0,0]
    XIcon:
        id: ic
        icon: root.icon
        pos_hint: {"center_x": .5, "center_y":.5}
        halign: 'center'
        text_color: root.text_color
    
    

""")


class XSegmentTextItem(XFlatButton):
    text = StringProperty()

class XSegmentIconItem(RectangularBehavior,XBoxLayout):
    icon = StringProperty()
    text_color = ColorProperty()
    button_width = NumericProperty()
    def __init__(self, **kwargs):
        super(XSegmentIconItem, self).__init__(**kwargs)
        self.text_color = self.txt_color


class XSegmentControl(XFloatLayout, Theming):
    item_width = NumericProperty()
    radius = ListProperty([0, ])
    line_color = ColorProperty()
    bar_color = ColorProperty()
    style = OptionProperty('m2', options = ['m2','m3'])
    item_color = ColorProperty()
    current_pos = NumericProperty(0)

    def __init__(self, **kwargs):
        super(XSegmentControl, self).__init__(**kwargs)
        self.bar_color = self.bgr_color
        self.item_color = self.card_color
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
                    i.ripple_radius = self.radius
                self.ids.b.width = self.item_width
                for x in self.ids.fake.children:
                    if not isinstance(x, XLiney):
                        x.size_hint_x = None
                        x.width = self.item_width
                    else:
                        x.height = dp(24)  if self.style == 'm3' else dp(37)
            Clock.schedule_once(self.select_first)

    def select_first(self, *args):
        self.line_color = [.5,.5,.5,.5] if self.style == 'm2' else [.5,.5,.5,.1]
        self.ids.b.radius = [self.radius[0],0,0,self.radius[0]] if self.style == 'm2' else [self.radius[0],]
        self.ids.b.width = self.ids.s.children[-1].width
        self.ids.b.pos = [self.ids.s.children[-1].pos[0],
                          self.ids.s.children[-1].pos[1]]
        self.ind = len(self.ids.fake.children) - 1
        if self.style == 'm3':
            self.fade_out()
        self.current_pos = self.ids.s.children[-1].pos[0]

    def add_widget(self, button, *args):
        if isinstance(button, XSegmentTextItem) or isinstance(button,  XSegmentIconItem):
            button.bind(on_press=lambda x: self.change_segment(button))
            button.bind(on_press=lambda x: self.dispatch(
                'on_tab_press', button))
            button.bind(on_release=lambda x: self.dispatch(
                'on_tab_release', button))
            self.ids.s.add_widget(button)
            self.ids.fake.add_widget(Widget())
            self.ids.fake.add_widget(XLiney(size_hint_y=None, height=dp(24), pos_hint={"center_y": .5}, width=dp(1), opacity=.3))
            self.ids.s.add_widget(XLiney(size_hint_y=None, height=dp(24), pos_hint={"center_y": .5}, width=dp(1), opacity=0))
        else:
            super(XSegmentControl, self).add_widget(button)

    def change_segment(self, button):
        self.current_pos = button.pos[0]
        if button == self.ids.s.children[-1]:
            self.ids.b.radius = [self.radius[0],0,0,self.radius[0]] if self.style == 'm2' else [self.radius[0],]
        elif button == self.ids.s.children[0]:
            self.ids.b.radius = [0,self.radius[0],self.radius[0],0] if self.style == 'm2' else [self.radius[0],]
        else:
            self.ids.b.radius = [0,] if self.style == 'm2' else [self.radius[0],]
            
        for i in self.ids.fake.children:
            i.opacity = .3
            i.height = dp(24)  if self.style == 'm3' else dp(37)
        self.ids.b.width = button.width
        if self.style == 'm3':
            anim = Animation(pos=button.pos, duration= 0.1)
            anim.start(self.ids.b)
            anim.bind(on_complete=self.fade_out)
        else:
            self.ids.b.pos = button.pos
        self.ind = self.ids.s.children.index(button)

    def fade_out(self, *args):
        if self.style == 'm3':
            try:
                self.ids.fake.children[self.ind+1].opacity = 0
            except:
                pass
            try:
                self.ids.fake.children[self.ind-1].opacity = 0
            except:
                pass
