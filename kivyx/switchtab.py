"""
<MainApp>:
    XSwitchPanel:
        #active_item_color: "#ff3434"
        id: tab_panel
        XSwitchItem:
            name: "tab1"
            text: "Themes"
            item_type: "left"
        XSwitchItem:
            name: "tab2"
            text: "Walpapers"
            item_type: "center"

        XSwitchItem:
            name: "tab3"
            text: "Icon pascks"
            item_type: "right"
            text: "revennue"


"""

from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivy.properties import StringProperty,ColorProperty, OptionProperty
from kivy.clock import Clock
from kivyx.behavior import RectangularBehavior



Builder.load_string("""
#:import Transition kivy.uix.screenmanager.NoTransition
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Window kivy.core.window.Window


<XSwitchButton>:
    id: btn
    XLabel:
        id: lbl
        size_hint: None, None
        height: dp(42)
        width: dp(115)
        text: root.text
        aligned: True
        halign: "center"
        color: root.text_color
        canvas.before:
            Color:
                rgba: root.item_color
            RoundedRectangle:
                pos: self.pos[0] + dp(0.5), self.pos[1] + dp(0.5)
                size: self.size[0] - dp(1), self.size[1] - dp(1)
                radius: [0,0,0,0] if root.item_type == "center" else [dp(7),0,0,dp(7)] if root.item_type == "left" else [0,dp(7),dp(7),0]


<XSwitchPanel>:
    orientation: "vertical"
    XToolbar:
        id: bt
        size_hint_y: None
        height: dp(66)
        padding: [(Window.width - dp(345))/2,0,0,0]
        BoxLayout:
            id: bt
            size_hint: None, None
            size: dp(345), dp(42)
            pos_hint: {"center_x": .5,"center_y": .575}
            canvas.before:
                Color:
                    rgba: root.disabled_color
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(7),]
    ScreenManager:
        id: sm
        transition: Transition()

""")

class XSwitchButton(RectangularBehavior,XBoxLayout):
    item_color = ColorProperty([0,0,0,0])
    text_color = ColorProperty([0,0,0,0])
    item_type = OptionProperty("center", options = ["left","center","right"])
    text = StringProperty()

class XSwitchItem(Theming,XScreen):
    text = StringProperty()
    item_type = OptionProperty("center", options = ["left","center","right"])
    def __init__(self, **kwargs):
        super(XSwitchItem,self).__init__(**kwargs)
        self.bg_color = self.bgr_color



class XSwitchPanel(Theming,XBoxLayout):
    active_item_color = ColorProperty([0,0,0,0])
    active_text_color = ColorProperty([0,0,0,0])
    def __init__(self, **kwargs):
        super(XSwitchPanel,self).__init__(**kwargs)
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def add_widget(self,widget,*args):
        if isinstance(widget, XSwitchItem):
            button = XSwitchButton()
            button.bind(on_press = lambda x:self.change_screen(widget,button))
            button.bind(on_press = lambda x:self.dispatch('on_tab_press', button))
            button.bind(on_release = lambda x:self.dispatch('on_tab_release', button))
            self.ids.bt.add_widget(button)
            self.ids.sm.add_widget(widget)
        else:
            super(XSwitchPanel, self).add_widget(widget)

    def update(self,*args):
        if self.active_item_color == [0,0,0,0]:
            self.active_item_color = self.bgr_color
        if self.active_text_color == [0,0,0,0]:
            self.active_text_color = self.txt_color
        l = len(self.ids.sm.screens) - 1
        for i in range(len(self.ids.sm.screens)):
            self.ids.bt.children[l-i].text = self.ids.sm.screens[i].text
            self.ids.bt.children[l-i].item_type = self.ids.sm.screens[i].item_type
            self.ids.bt.children[l-i].text_color = self.disabled_color
            self.ids.bt.children[l-i].item_color = self.card_color
            if i == 0:
                self.ids.bt.children[l-i].item_color = self.active_item_color
                #self.ids.bt.children[l-i].opacity = 1
                self.ids.bt.children[l-i].text_color = self.active_text_color

    def change_screen(self,widget,button,*args):
        self.ids.sm.current = widget.name
        for i in self.ids.bt.children:
            i.item_color = self.trans_color
            #i.opacity = .5
            i.text_color = self.disabled_color
            i.item_color = self.card_color
        button.item_color = self.active_item_color
        button.opacity = 1
        button.text_color = self.active_text_color
