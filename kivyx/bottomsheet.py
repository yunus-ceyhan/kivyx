
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
        XCard:
            id: scr
            size_hint_y: None
            height: root.scroll_height
            radius: root.radius
            bg_color: root.back_color
            ScrollView:
                id: sc
                bar_width: 0
                effect_cls: ScrollEffect
                BoxLayout:
                    id: bx
                    orientation: "vertical"
                    size_hint_y: None
                    height: max(self.minimum_height,scr.height)

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
    radius = ListProperty([dp(10),dp(10),0,0])
    status = StringProperty('closed')
    back_color = ColorProperty()

    def __init__(self, **kwargs):
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
        if self.scroll_height < 1:
            self.main_pos = {"center_x": .5, "center_y": .5}
            box_height =  self.ids.bx.height + dp(10) if self.expandable else min(dp(112),self.ids.bx.height) 
            anim = Animation(scroll_height = box_height,bg_color = [0,0,0,.3], duration = 0.1)
            anim.start(self)
            self.status = 'opened'
            
    def close(self,*args):
        try:
            self.main_pos = {"center_x": .5, "center_y": -2}
            anim = Animation(scroll_height = 0,bg_color = [0,0,0,0] , duration = 0.2)
            anim.start(self)
            #anim.bind(on_complete = self.set_pos)
            self.status = 'closed'
        except:
            pass
            
