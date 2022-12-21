
"""
<MainApp>:
    XButton:
        text: "open bottom sheet"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: bottom_sheet.open_menu()

    XBottomSheet:
        id: bottom_sheet
        XBottomSheetContent:
            orientation: "vertical"
            XIconListItem:
                icon: "android"
                text: "android"
            XIconListItem:
                icon: "android"
                text: "android"
            XIconListItem:
                icon: "android"
                text: "android"
            XIconListItem:
                icon: "android"
                text: "android"

"""

from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import  ColorProperty, ListProperty, DictProperty, NumericProperty, BooleanProperty, StringProperty
from kivyx.floatlayout import XFloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock


Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect

<XBottomSheet>:
    id: bs
    size_hint: 1,1
    pos_hint: root.main_pos
    on_press: root.close()
    BoxLayout:
        orientation: "vertical"
        pos_hint: bs.pos_hint
        XToolbar:
            id: scr
            size_hint_y: None
            height: root.scroll_height
            radius: [dp(16), dp(16),0,0]
            bg_color: root.back_color
            top: True
            elevation: 0.3
            padding: [0,dp(16),0,dp(16)]
            ScrollView:
                id: sc
                bar_width: 0
                effect_cls: ScrollEffect
                BoxLayout:
                    id: bx
                    orientation: "vertical"
                    size_hint_y: None
                    height: max(self.minimum_height,scr.height - dp(32))

<XBottomSheetContent>:
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {'center_x': .5, 'center_y': .5}
                

""")

class XBottomSheetContent(BoxLayout):
    pass

class XBottomSheet(Theming,ButtonBehavior,XFloatLayout):
    scroll_height = NumericProperty(0)
    main_pos = DictProperty({"center_x": .5, "center_y": -2})
    expandable = BooleanProperty(False)
    status = StringProperty('closed')
    back_color = ColorProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_anim_stop')
        self.register_event_type('on_anim_start')
        super(XBottomSheet, self).__init__(**kwargs)
        self.back_color = self.card_color
        Window.bind(on_keyboard=self.keyboard)

    def keyboard(self, window, key, *largs):
        if key == 27:
            if self.status == 'opened':
                self.close()

    def add_widget(self,widget,*args):
        if isinstance(widget, XBottomSheetContent):
            self.ids.bx.add_widget(widget)
        else:
            super(XBottomSheet, self).add_widget(widget)

    def open(self,*args):
        if self.status == 'closed' and self.ids.bx.height > 0:
            self.dispatch("on_anim_start")
            self.main_pos = {"center_x": .5, "center_y": .5}
            box_height =  self.ids.bx.height + dp(32) if self.expandable else min(dp(134),self.ids.bx.height + dp(32)) 
            anim = Animation(scroll_height = box_height,bg_color = [0,0,0,.5], duration = 0.1)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            self.status = 'opened'
        else:
            Clock.schedule_once(self.open,0.1)

    def close(self,*args):
        try:
            self.main_pos = {"center_x": .5, "center_y": -2}
            anim = Animation(scroll_height = 0,bg_color = [0,0,0,0] , duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = lambda *args: self.dispatch("on_anim_stop"))
            anim.bind(on_complete = self.set_status)      
        except:
            pass
        
    def set_status(self,*args):
        self.status = "closed"
        
    def on_anim_stop(self,*args):
        pass

    def on_anim_start(self,*args):
        pass
