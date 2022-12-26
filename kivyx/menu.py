"""
<MainApp>:
    XIconButton:
        text: ""
        icon: "apple"
        pos_hint: {"center_x": .5 , "center_y": .5}
        on_release:
            menu1.open(self)
    XDotMenu:
        id: menu1
        #box_width: dp(160)
        XDotItem:
            text: "App"
            icon: "apple"
        XDotItem:
            text: "Google Store"
            icon: "gmail"

    XMenu:
        id: menu2
        expandable: False
        direction: "lb"
        XFlatButton:
            text: "12"
            button_width: dp(150)
        XFlatButton:
            text: "13"
            button_width: dp(150)
        XFlatButton:
            text: "14"
            button_width: dp(150)
            text: "12"
            button_width: dp(150)
        XFlatButton:
            text: "13"
            button_width: dp(150)
        XFlatButton:
            text: "14"
            button_width: dp(150)



"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ColorProperty, ListProperty, DictProperty, NumericProperty, BooleanProperty, OptionProperty,StringProperty
from kivyx.button import XButton
from kivyx.floatlayout import XFloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivyx.behavior import RectangularBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_string("""
#:import Window kivy.core.window.Window
#:import effect kivy.effects.scroll.ScrollEffect

<XMenu>:
    size_hint: None, None
    size: Window.width,Window.height
    pos_hint: root.main_pos
    on_press: root.close()
    XCard:
        id: scr
        size_hint: None,None
        height: root.scroll_height
        width: root.scroll_width
        radius: [dp(5),]
        pos: root.caller_pos
        opacity: 1 if root.scroll_width > 0 else 0
        shadow_distance: - dp(3)
        ScrollView:
            bar_width: 0
            effect_cls: effect
            radius: [dp(5),]

            BoxLayout:
                id: bx
                orientation: "vertical"
                size_hint: None, None
                height: self.minimum_height
                width: self.minimum_width
                padding: [dp(5),]


<XDotMenu>:
    size_hint: None, None
    size: Window.width,Window.height
    pos_hint: root.main_pos
    on_press: root.close()
    XCard:
        id: scr
        size_hint: None,None
        height: root.scroll_height
        width: root.scroll_width 
        radius: [dp(8),]
        pos: root.caller_pos
        opacity: 1 if root.scroll_width > 0 else 0
        padding: [dp(4),dp(8),dp(4),dp(8)]
        bg_color: root.color
        shadow_distance: - dp(3)
        ScrollView:
            bar_width: 0
            effect_cls: effect
            BoxLayout:
                id: bx
                orientation: "vertical"
                size_hint: None, None
                height: self.minimum_height
                width: self.minimum_width
                

<XDotItem>:
    id: bx
    size_hint: None, None
    height: dp(48)
    width: max(li.width + lb.texture_size[0] + dp(70) , dp(64) )
    padding: [dp(24),0,0,0]
    spacing: dp(12)

    XIcon:
        id: li
        icon: root.icon
        aligned: True
        halign: "left"
        color: root.icon_color
        size_hint_x: None
        width: self.width if root.icon else 0
    XLabel:
        id: lb
        text: root.text
        aligned: False
        halign: "left"
        valign: "middle"
        font_size: "17sp"
        text_color: root.text_color

""")

class XDotItem(RectangularBehavior,BoxLayout):
    icon = StringProperty()
    text = StringProperty()
    icon_color = ColorProperty()
    text_color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color


class XDotMenu(Theming,ButtonBehavior,XFloatLayout):
    color = ColorProperty()
    caller_pos = ListProperty([1,1])
    scroll_height = NumericProperty(0)
    scroll_width = NumericProperty(0)
    main_pos = DictProperty({"center_x": 2, "center_y": 2})
    expandable = BooleanProperty(False)
    box_width = NumericProperty(dp(200))
    status = StringProperty('closed')

    def __init__(self, **kwargs):
        self.register_event_type('on_anim_stop')
        self.register_event_type('on_anim_start')
        super(XDotMenu, self).__init__(**kwargs)
        self.color = self.card_color
        Window.bind(on_keyboard=self.keyboard)

    def keyboard(self, window, key, *largs):
        if key == 27:
            if self.status == 'opened':
                self.close()
            return True
        else:
            return False

    def add_widget(self,widget,*args):
        if isinstance(widget, XDotItem):
            self.ids.bx.add_widget(widget)
        else:
            super(XDotMenu, self).add_widget(widget)

    def open(self,*args):
        self.widget_pos = [Window.width,Window.height]
        if self.scroll_height < 1:
            self.dispatch("on_anim_start")
            self.main_pos = {"center_x": .5, "center_y": .5}
            self.caller_pos = (self.widget_pos[0] - self.scroll_width, self.widget_pos[1] - self.scroll_height)
            box_height =  self.ids.bx.height if self.expandable else min(dp(218),self.ids.bx.height + dp(12)) 
            box_width = self.ids.bx.width if self.expandable else max(dp(20),self.ids.bx.width + dp(8))
            final_pos = (self.widget_pos[0] - (box_width + dp(8)), self.widget_pos[1] - (box_height + dp(8)))
            anim2 = Animation(caller_pos = final_pos,duration = 0.2)
            anim2.start(self)
            anim = Animation(scroll_height = box_height,scroll_width = box_width,duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            self.status = "opened"

    def close(self,*args):
        try:
            anim2 = Animation(caller_pos = (self.widget_pos[0] , self.widget_pos[1]) ,duration = 0.2)
            anim2.start(self)
            anim = Animation(scroll_height = 0,scroll_width = 0, duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            self.main_pos = {"center_x": 2, "center_y": 2}
            self.status = "closed"
        except:
            pass
        
    def on_anim_stop(self,*args):
        pass

    def on_anim_start(self,*args):
        pass

class XMenu(Theming,ButtonBehavior,XFloatLayout):
    color = ColorProperty()
    caller_pos = ListProperty([1,1])
    scroll_height = NumericProperty(0)
    scroll_width = NumericProperty(0)
    main_pos = DictProperty({"center_x": 2, "center_y": 2})
    expandable = BooleanProperty(False)
    direction = OptionProperty("lb", options = ["lb","rb","lt","rt"])
    status = StringProperty('closed')

    def __init__(self, **kwargs):
        self.register_event_type('on_anim_stop')
        self.register_event_type('on_anim_start')
        super(XMenu, self).__init__(**kwargs)
        self.color = self.card_color
        Window.bind(on_keyboard=self.keyboard)

    def keyboard(self, window, key, *largs):
        if key == 27:
            self.close()

    def add_widget(self,widget,*args):
        if isinstance(widget, XButton):
            self.ids.bx.add_widget(widget(style= "text"))
        else:
            super(XMenu, self).add_widget(widget)

    def open(self,widget,*args):
        self.widget_pos = widget.pos
        if self.scroll_height < 1:
            self.dispatch("on_anim_start")
            self.main_pos = {"center_x": .5, "center_y": .5}
            self.caller_pos = (self.widget_pos[0] - self.scroll_width, self.widget_pos[1] - self.scroll_height)
            box_height =  self.ids.bx.height if self.expandable else min(dp(175),self.ids.bx.height) 
            box_width = self.ids.bx.width if self.expandable else max(dp(20),self.ids.bx.width)
            if self.direction == "lb":
                self.final_pos = (self.widget_pos[0] - (box_width-widget.width), self.widget_pos[1] - (box_height + self.ids.bx.padding[1]))
            elif self.direction == "rb":
                self.final_pos = (self.widget_pos[0], self.widget_pos[1] - (box_height + self.ids.bx.padding[1]))
            elif self.direction == "lt":
                self.final_pos = (self.widget_pos[0] - (box_width-widget.width), self.widget_pos[1] + (widget.height +self.ids.bx.padding[1]))
            elif self.direction == "rt":
                self.final_pos = (self.widget_pos[0] , self.widget_pos[1] + (widget.height +self.ids.bx.padding[1]))
            #self.caller_pos = self.final_pos

            anim2 = Animation(caller_pos = self.final_pos,duration = 0.2)
            anim2.start(self)
            anim = Animation(scroll_height = box_height,scroll_width = box_width,duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            self.status = 'opened'

            

    def close(self,*args):
        try:
            anim2 = Animation(caller_pos = self.widget_pos ,duration = 0.2)
            anim2.start(self)
            anim = Animation(scroll_height = 0,scroll_width = 0, duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            self.main_pos = {"center_x": 2, "center_y": 2}
            self.status = 'closed'
        except:
            pass
        
    def on_anim_stop(self,*args):
        pass

    def on_anim_start(self,*args):
        pass
