"""
<MainApp>:
    XSegmentTab:
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
from kivy.properties import StringProperty, NumericProperty, ColorProperty, ListProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivyx.segmentcontrol import XSegmentTextItem, XSegmentIconItem



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
        bg_color: root.tab_color
        elevation: root.elevation
        XSegmentControl:
            id: bx
            pos_hint: {"center_x": .5,"center_y": .5}
            style: root.tab_style
            item_width: root.item_width
            radius:[root.tab_radius,]
            bg_color: root.tab_color
            bar_color: root.bar_color
            item_color: root.item_color
            
    ScreenManager:
        id: sm
        transition: Transition()

""")


class XSegmentItem(Theming,XScreen):
    text = StringProperty()
    text_color = ColorProperty()
    font_size = NumericProperty("16sp")
    bubble_text = StringProperty()
    bubble_color = ColorProperty([0,0,0,0])
    bubble_line_color = ColorProperty([0,0,0,0])
    bubble_text_color = ColorProperty([0,0,0,0])
    bubble_radius = ListProperty((dp(4),dp(4),dp(4),dp(4)))
    def __init__(self, **kwargs):
        super(XSegmentItem,self).__init__(**kwargs)
        self.bg_color = self.bgr_color

        
        



class XSegmentTab(Theming,XBoxLayout):
    item_width = NumericProperty()
    tab_style = StringProperty('m2')
    tab_radius = NumericProperty(0)
    tab_color = ColorProperty()
    bar_color = ColorProperty()
    item_mode = StringProperty("text")
    elevation = NumericProperty(0.05)
    item_color = ColorProperty()
    current_tab = StringProperty()
    text_color = ColorProperty()
    font_size = NumericProperty("16sp")
    bubble_color = ColorProperty([0,0,0,0])
    bubble_line_color = ColorProperty([0,0,0,0])
    bubble_text_color = ColorProperty([0,0,0,0])
    bubble_radius = ListProperty((dp(4),dp(4),dp(4),dp(4)))

    def __init__(self, **kwargs):
        super(XSegmentTab,self).__init__(**kwargs)
        self.tab_color =  self.card_color
        self.bar_color = self.bgr_color
        self.item_color = self.card_color
        self.text_color = self.txt_color
        self.bubble_color = self.bgr_color
        self.bubble_line_color = self.card_color
        self.bubble_text_color = self.txt_color
        self.bubble_radius = (dp(8),dp(8),dp(8),dp(8))
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def add_widget(self,widget,*args):
        if isinstance(widget, XSegmentItem):
            button = XSegmentTextItem() if self.item_mode == "text" else XSegmentIconItem()
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
            if isinstance(i,XSegmentTextItem) or isinstance(i,XSegmentIconItem):
                screens.append(i)            
        for i in range(len(self.ids.sm.screens)):
            if self.item_mode == "text":
                screens[l-i].text = self.ids.sm.screens[i].text
                screens[l-i].bubble_text = self.ids.sm.screens[i].bubble_text
                screens[l-i].bubble_color = self.bubble_color
                screens[l-i].bubble_radius = self.bubble_radius
                screens[l-i].text_color = self.txt_color
                screens[l-i].font_size = self.font_size
                screens[l-i].bubble_color = self.bubble_color
                screens[l-i].bubble_text_color = self.bubble_text_color
                screens[l-i].bubble_line_color = self.bubble_line_color
                
            else:
                screens[l-i].icon = self.ids.sm.screens[i].icon
                

    def change_screen(self,widget,button,*args):
        self.ids.sm.current = widget.name
