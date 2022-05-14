"""
<MainApp>:
    XSegmentPanel:
        #active_item_color: "#ff3434"
        id: tab_panel
        XSegmentItem:
            name: "tab1"
            text: "Themes"
            item_type: "left"
        XSegmentItem:
            name: "tab2"
            text: "Walpapers"
            item_type: "center"

        XSegmentItem:
            name: "tab3"
            text: "Icon pascks"
            item_type: "right"
            text: "revennue"


"""

from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivyx.segmentcontrol import XSegmentTextItem



Builder.load_string("""
#:import Transition kivy.uix.screenmanager.NoTransition
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Window kivy.core.window.Window

<XSegmentTab>:
    orientation: "vertical"
    XToolbar:
        size_hint_y: None
        height: dp(56)
        padding: [(Window.width - bx.width)/2,0,0,0]
        XSegmentControl:
            id: bx
            pos_hint: {"center_x": .5,"center_y": .5}
            style: root.tab_style
            item_width: root.item_width
            radius:[root.tab_radius,]
            
    ScreenManager:
        id: sm
        transition: Transition()

""")


class XSegmentItem(Theming,XScreen):
    text = StringProperty()
    def __init__(self, **kwargs):
        super(XSegmentItem,self).__init__(**kwargs)
        self.bg_color = self.bgr_color
        



class XSegmentTab(Theming,XBoxLayout):
    item_width = NumericProperty()
    tab_style = StringProperty('m2')
    tab_radius = NumericProperty(0)    

    def __init__(self, **kwargs):
        super(XSegmentTab,self).__init__(**kwargs)
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def add_widget(self,widget,*args):
        if isinstance(widget, XSegmentItem):
            button = XSegmentTextItem()
            button.bind(on_press = lambda x:self.change_screen(widget,button))
            button.bind(on_press = lambda x:self.dispatch('on_tab_press', button))
            button.bind(on_release = lambda x:self.dispatch('on_tab_release', button))
            self.ids.bx.add_widget(button)
            self.ids.sm.add_widget(widget)
        else:
            super(XSegmentTab, self).add_widget(widget)

    def update(self,*args):
        l = len(self.ids.sm.screens) - 1
        screens = []
        for i in self.ids.bx.ids.s.children:
            if isinstance(i,XSegmentTextItem):
                screens.append(i)            
        for i in range(len(self.ids.sm.screens)):
            screens[l-i].text = self.ids.sm.screens[i].text

    def change_screen(self,widget,button,*args):
        self.ids.sm.current = widget.name