"""
<MainApp>:
    ESidePanel:
        id: tab_panel
        ESideItem:
            name: "tab1"
            icon: "apple"
        ESideItem:
            name: "tab2"
            icon: "magnify"
        ESideItem:
            name: "tab3"
            icon: "play"
        ESideItem:
            name: "tab4"
            icon: "file"
            XButton:
                text: "hllo"
"""

from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivyx.button import XIconButton
from kivy.properties import StringProperty,ColorProperty
from kivy.clock import Clock
from kivy.core.window import Window


Builder.load_string("""
#:import Transition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window

<ESideButton>:
    opacity: .5
    size_hint: None, None
    size: dp(48),dp(48)
    canvas.before:
        Color:
            rgba: root.item_color
        Rectangle:
            pos: self.pos
            size: dp(3), self.height

<ESidePanel>:
    XBoxLayout:
        orientation: "vertical"
        size_hint_x: None
        width: dp(48)
        bg_color: root.card_color
        BoxLayout:
            id: bt
            bg_color: root.card_color
            orientation: "vertical"
            sie_hint_y: None
            height: max(self.minimum_height,dp(48))

        Widget:
            size_hint_y: None
            height: Window.height - bt.height

    ScreenManager:
        id: sm
        transition: Transition()

""")

class ESideButton(XIconButton):
    item_color = ColorProperty([0,0,0,0])

class ESideItem(XScreen):
    icon = StringProperty()

class ESidePanel(Theming,XBoxLayout):
    active_item_color = ColorProperty([0,0,0,0])
    def __init__(self, **kwargs):
        super(ESidePanel,self).__init__(**kwargs)
        

    def __init__(self, **kwargs):
        super(ESidePanel, self).__init__(**kwargs)
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def add_widget(self,widget,*args):
        if isinstance(widget, ESideItem):
            button = ESideButton()
            button.bind(on_press = lambda x:self.change_screen(widget,button))
            button.bind(on_press = lambda x:self.dispatch('on_tab_press', button))
            button.bind(on_release = lambda x:self.dispatch('on_tab_release', button))
            self.ids.bt.add_widget(button)
            self.ids.sm.add_widget(widget)
        else:
            super(ESidePanel, self).add_widget(widget)

    def update(self,*args):
        if self.active_item_color == [0,0,0,0]:
            self.active_item_color = self.primary_color
        l = len(self.ids.sm.screens) - 1
        for i in range(len(self.ids.sm.screens)):
            self.ids.bt.children[l-i].icon = self.ids.sm.screens[i].icon
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

