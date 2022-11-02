"""
<MainApp>:
    XButton:
        text: "open bottom sheet"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: dialog.open()

    XDialog:
        id: dialog
        title: "Close App"
        expandable: False
        XDialogContent:
            XLabel:
                text: "hello there what are you guys doing today"*10
                size_hint_y: None
                aligned: True
                #halign: "left"
                height: self.texture_size[1]

        XDialogButton:
            text: "CANCEL"
            on_release: dialog.close()
        XDialogButton:
            text: "OK"

"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import ListProperty, DictProperty, NumericProperty, BooleanProperty,StringProperty
from kivyx.button import XButton
from kivyx.floatlayout import XFloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Builder.load_string("""
#:import Window kivy.core.window.Window

<XDialog>:
    id: bs
    size_hint: 1,1
    pos_hint: root.main_pos
    #on_press: root.close()
    XCard:
        orientation: "vertical"
        id: scr
        size_hint: None,None
        height: root.scroll_height
        width: dp(320) if Window.width < Window.height else dp(400)
        radius: [dp(24),]
        padding: [dp(24),dp(16),dp(24),dp(16)]
        pos_hint: {"center_x": .5, "center_y": .5}
        spacing: dp(12)
        opacity: root.opacity
        XLabel:
            id: title
            text: root.title
            bold: False
            font_size: "20sp"
            aligned: True
            halign: "left"
            size_hint_y: None
            height: dp(48)
        ScrollView:
            id: sc
            bar_width: dp(2)
            #effect_cls: ScrollEffect
            size_hint_y: None
            height: bx.height if root.expandable else min(dp(150), bx.height)
            BoxLayout:
                id: bx
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
        Widget:
        BoxLayout:
            id: bt
            size_hint_y: None
            height: self.minimum_height
            Widget:

<XDialogContent>:
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height

<XDialogButton>:
    style: "text"
                

""")

class XDialogButton(XButton):
    pass

class XDialogContent(BoxLayout):
    pass

class XDialog(Theming,ButtonBehavior,XFloatLayout):
    title = StringProperty()
    scroll_height = NumericProperty(0)
    main_pos = DictProperty({"center_x": .5, "center_y": -2})
    expandable = BooleanProperty(False)
    radius = ListProperty([dp(10),dp(10),0,0])
    opacity = NumericProperty(0)
    status = StringProperty('closed')

    def __init__(self, **kwargs):
        self.register_event_type('on_anim_stop')
        self.register_event_type('on_anim_start')
        super(XDialog, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.keyboard)

    def keyboard(self, window, key, *largs):
        if key == 27:
            if self.status == 'opened':
                self.close()

    def add_widget(self,widget,*args):
        if isinstance(widget, XDialogContent):
            self.ids.bx.add_widget(widget)

        elif isinstance(widget, XDialogButton):
            self.ids.bt.add_widget(widget)
        else:
            super(XDialog, self).add_widget(widget)

    def open(self,*args):
        if self.scroll_height < 1:
            self.dispatch("on_anim_start")
            self.main_pos = {"center_x": .5, "center_y": .5}
            box_height =  self.ids.bx.height + dp(110) + self.ids.bt.height\
                if self.expandable else min(dp(300),self.ids.bx.height + dp(110) + self.ids.bt.height) 
            anim = Animation(scroll_height = box_height,bg_color = [0,0,0,.5],opacity = 1, duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            self.status = "opened"
            
    def close(self,*args):
        try:
            anim = Animation(scroll_height = 0,bg_color = [0,0,0,0] ,opacity = 0,duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            anim.bind(on_complete = self.set_status)
            self.main_pos = {"center_x": .5, "center_y": -2}
        except:
            pass
        
    def set_status(self,*args):
        self.status = "closed"

    def on_anim_stop(self,*args):
        pass

    def on_anim_start(self,*args):
        pass
