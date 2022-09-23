"""
<MainApp>:
    XTabPanel:
        active_item_color: "#ff3434"
        id: tab_panel
        XTabItem:
            name: "tab1"
            text: "Themes"
        XTabItem:
            name: "tab2"
            text: "Walpapers"
        XTabItem:
            name: "tab3"
            text: "Icon pascks"
        XTabItem:
            name: "tab4"
            text: "revennue"


"""

from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivy.properties import StringProperty,ColorProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivyx.behavior import RectangularBehavior


Builder.load_string("""
#:import Transition kivy.uix.screenmanager.NoTransition
#:import ScrollEffect kivy.effects.scroll.ScrollEffect

<XTabButton>:
    id: btn
    padding: [self.width / 6,0,0,0]
    opacity: .5
    XLabel:
        id: lbl
        size_hint: None, None
        height: dp(48)
        width: self.width
        text: root.text
        aligned: True
        halign: "center"
        canvas.before:
            Color:
                rgba: root.item_color
            RoundedRectangle:
                pos: self.pos[0] + dp(15), self.pos[1]+dp(1)
                size: self.width-dp(30),dp(2)
                radius: [dp(5),dp(5),0,0]

<XTabPanel>:
    orientation: "vertical"
    XToolbar:
        size_hint_y: None
        height: dp(48)
        ScrollView:
            id: sc
            bar_width: 0
            effect_cls: ScrollEffect
            BoxLayout:
                id: bt
                size_hint_x: None
                width: max(self.minimum_width,sc.width)
                Widget:
                    size_hint_x: None
                    width: dp(24) if bt.width > sc.width else 0
    ScreenManager:
        id: sm
        transition: Transition()

""")

class XTabButton(RectangularBehavior,XBoxLayout):
    item_color = ColorProperty([0,0,0,0])
    text = StringProperty()

class XTabItem(XScreen):
    text = StringProperty()

class XTabPanel(Theming,XBoxLayout):
    active_item_color = ColorProperty([0,0,0,0])
    def __init__(self, **kwargs):
        super(XTabPanel,self).__init__(**kwargs)
        super(XTabPanel, self).__init__(**kwargs)
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def add_widget(self,widget,*args):
        if isinstance(widget, XTabItem):
            button = XTabButton()
            button.bind(on_press = lambda x:self.change_screen(widget,button))
            button.bind(on_press = lambda x:self.dispatch('on_tab_press', button))
            button.bind(on_release = lambda x:self.dispatch('on_tab_release', button))
            self.ids.bt.add_widget(button)
            self.ids.sm.add_widget(widget)
        else:
            super(XTabPanel, self).add_widget(widget)

    def update(self,*args):
        if self.active_item_color == [0,0,0,0]:
            self.active_item_color = self.primary_color
        l = len(self.ids.sm.screens) - 1
        for i in range(len(self.ids.sm.screens)):
            self.ids.bt.children[l-i].text = self.ids.sm.screens[i].text
            if i == 0:
                self.ids.bt.children[l-i].item_color = self.active_item_color
                self.ids.bt.children[l-i].opacity = 1
                self.ids.bt.children[l-i].text_color = self.active_item_color

    def change_screen(self,widget,button,*args):
        self.ids.sm.current = widget.name
        for i in self.ids.bt.children:
            i.item_color = self.trans_color
            i.opacity = .5
            i.text_color = self.txt_color
        button.item_color = self.active_item_color
        button.opacity = 1
        button.text_color = self.active_item_color
        #if button.pos[0] > (Window.width - button.width):
        over_width = self.ids.bt.width - self.ids.sc.width
        if over_width <= 0.0:
            over_width = 0.1
        view_start = over_width * self.ids.sc.scroll_x
        view_end = view_start + self.ids.sc.width
        offset = button.pos[0]
        desired_view_start = offset - ((Window.width/2) - (button.width/2))
        desired_view_end = offset + ((Window.width/2) + (button.width/2))
        if desired_view_start < view_start:
            self.ids.sc.scroll_x = max(
                0, desired_view_start / over_width)

        elif desired_view_end > view_end:
            self.ids.sc.scroll_x = min(
                1, (desired_view_end - self.ids.sc.width) / over_width)
        #else:
        #    self.ids.sc.scroll_x = 0