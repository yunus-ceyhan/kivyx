"""
<MainApp>:
    bg_color: root.bgr_color
    XScreen:
        name: "main_screen"
        bg_color: root.bgr_color
        XSegmentControl:
            pos_hint: {"center_x": .5, "center_y":.5}
            item_width:  dp(320)
            radius: [dp(8),]
            style: "m3"
            XSegmentTextItem:
                text: "Global"
                bubble_text: "12"
            XSegmentTextItem:
                text: "China"
            XSegmentIconItem:
                icon: "alarm-f"
"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, NumericProperty, StringProperty,OptionProperty, ObjectProperty
from kivyx.floatlayout import XFloatLayout
from kivyx.boxlayout import XBoxLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivyx.behavior import RectangularBehavior
from kivy.clock import Clock
from kivyx.line import XLiney
from kivy.uix.widget import Widget
from kivyx.behavior import RectangularBehavior
from kivy.core.window import Window


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
        pos: root.current_button.pos if root.current_button != None else [self.pos[0], xsc.pos[1] + (xsc.height -self.height)/2 ]
        bg_color: root.item_color
        elevation: 0.2
        shadow_distance: - dp(1)
        shadow_y: 0
        shadow_blur: dp(4)

    XBoxLayout:
        id: s
        radius: root.radius
        size_hint: None,None
        height: dp(40)
        width: max(self.minimum_width, root.item_width)
        pos_hint: {"center_x": .5, "center_y":.5}


<XSegmentTextItem>:
    size_hint_y: None
    height: dp(36)
    pos_hint: {"center_y":.5}
    spacing: dp(16) if root.bubble_text else 0
    padding: [(self.width/2)-(l1.width +l2.width + self.spacing)/2]
    XLabel:
        id: l1
        size_hint: None, None
        height: dp(36)
        width: self.texture_size[0]
        text_size: None,None
        text: root.text
        pos_hint: {"center_x": .5, "center_y":.5}
        color: root.text_color
        font_size: root.font_size
    XLabel:
        id: l2
        size_hint: None, None
        height: dp(36)
        text: root.bubble_text
        size_hint: None, None
        height: dp(36)
        width: self.texture_size[0]
        text_size: None,None
        pos_hint: {"center_x": .5, "center_y":.5}
        font_size: "10sp"
        bold: True
        color: root.bubble_text_color
        canvas.before:
            Color:
                rgba: root.bubble_color if root.bubble_text else (0,0,0,0)
            RoundedRectangle:
                size: self.size[0] + dp(12), self.size[1] - dp(16)
                pos: self.pos[0]-dp(6), self.pos[1] + dp(8)
                radius: root.bubble_radius
            Color:
                rgba: root.bubble_line_color if root.bubble_text else (0,0,0,0)
            Line:
                width: dp(1.5)
                rounded_rectangle: (self.x - dp(7), self.y + dp(7), self.width + dp(14), self.height - dp(14), root.bubble_radius[0])
        
<XSegmentIconItem>:
    pos_hint: {"center_y":.5}
    size_hint_y: None
    height: dp(36)
    #width: root.button_width
    padding: [(self.width/2) - (ic.width/2),0,0,0]
    XIcon:
        id: ic
        icon: root.icon
        pos_hint: {"center_x": .5, "center_y":.5}
        halign: 'center'
        text_color: root.text_color
    
    

""")


class XSegmentTextItem(RectangularBehavior,XBoxLayout):
    text = StringProperty()
    text_color = ColorProperty()
    font_size = NumericProperty("16sp")
    bubble_text = StringProperty()
    bubble_color = ColorProperty([0,0,0,0])
    bubble_line_color = ColorProperty([0,0,0,0])
    bubble_text_color = ColorProperty([0,0,0,0])
    bubble_radius = ListProperty((dp(10),))
    def __init__(self, **kwargs):
        super(XSegmentTextItem, self).__init__(**kwargs)
        self.text_color = self.txt_color
        self.bubble_color = self.accent_color
        self.bubble_text_color = self.txt_color
        self.bubble_line_color = self.card_color
        
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
    current_button = ObjectProperty()

    def __init__(self, **kwargs):
        super(XSegmentControl, self).__init__(**kwargs)
        self.bar_color = self.bgr_color
        self.item_color = self.card_color
        self.ind = 0
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Window.bind(on_flip = self.on_window_resize)
        Clock.schedule_once(self.adjust)

    def on_window_resize(self, *a,**kv):
        try:
            self.ids.b.pos = self.current_button.pos
        except Exception as e:
            pass

    def on_tab_press(self, *args):
        for i in self.ids.fake.children:
            i.opacity = 0

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
                    if self.ids.s.children.index(i) == 4:
                        i.opacity = 1
                    else:
                        if not isinstance(i, XLiney):
                            i.opacity = .9
                            button_width = i.width
                self.ids.b.width = self.item_width
                for x in self.ids.fake.children:
                    if not isinstance(x, XLiney):
                        x.size_hint_x = None
                        x.width = self.item_width/3
                    else:
                        x.height = dp(20)  if self.style == 'm3' else dp(37)
                        x.width = dp(2) if self.style == "m3" else dp(1)
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
        self.current_button = self.ids.s.children[-1]

    def add_widget(self, button, *args):
        if isinstance(button, XSegmentTextItem) or isinstance(button,  XSegmentIconItem):
            button.bind(on_press=lambda x: self.change_segment(button))
            button.bind(on_press=lambda x: self.dispatch(
                'on_tab_press', button))
            button.bind(on_release=lambda x: self.dispatch(
                'on_tab_release', button))
            self.ids.s.add_widget(button)
            self.ids.fake.add_widget(Widget())
            self.ids.fake.add_widget(XLiney(size_hint_y=None, height=dp(20), pos_hint={"center_y": .5}, width=dp(1.5), opacity=.5))
            self.ids.s.add_widget(XLiney(size_hint_y=None, height=dp(20), pos_hint={"center_y": .5}, width=dp(1.5), opacity=0))
        else:
            super(XSegmentControl, self).add_widget(button)

    def change_segment(self, button):
        self.current_button = button
        if button == self.ids.s.children[-1]:
            self.ids.b.radius = [self.radius[0],0,0,self.radius[0]] if self.style == 'm2' else [self.radius[0],]
        elif button == self.ids.s.children[0]:
            self.ids.b.radius = [0,self.radius[0],self.radius[0],0] if self.style == 'm2' else [self.radius[0],]
        else:
            self.ids.b.radius = [0,] if self.style == 'm2' else [self.radius[0],]
            
        for x in self.ids.s.children:
            if self.ids.s.children.index(x) == self.ids.s.children.index(button):
                x.opacity = 1
            else:
                if not isinstance(x, XLiney):
                    x.opacity = .9
            
        for i in self.ids.fake.children:
            if isinstance(i, XLiney):
                i.opacity = 0.5
                i.height = dp(20)  if self.style == 'm3' else dp(37)
                i.width = dp(1.5) if self.style == "m3" else dp(1)
                
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
