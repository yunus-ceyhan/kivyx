"""
<MainApp>:
    id: scr_mngr
    XBotnav:
        id: botnav
        bg_color: self.bgr_color
        on_tab_release: root.tab_changed()
        active_item_color: root.accent_color
        XBotnavItem:
            name: "sets"
            text: "Settings"
            icon: "cog-outline"
            active_icon: "cog"

"""
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivyx.boxlayout import XBoxLayout
from kivy.lang import Builder
from kivyx.screen import XScreen
from kivy.properties import StringProperty, ColorProperty, NumericProperty
from kivyx.theming import Theming
from kivy.animation import Animation
from kivy.metrics import dp

Builder.load_string("""
#:import Transition kivy.uix.screenmanager.NoTransition

<XBotnav>:
    orientation: "vertical"
    ScreenManager:
        id: sm
        transition: Transition()
    XToolbar:
        id: bt
        size_hint_y: None
        height: dp(80)
        top: True
        padding: [dp(8),0,dp(8),0]
        spacing: dp(8)
        bg_color: root.bar_color
        elevation: 0
        distance: '2dp'
        line_color: (0,0,0,0.1)

<BotnavIcon>:
    size_hint_y: None
    height: dp(80)
    spacing: dp(6)
    orientation: "vertical"
    padding: [0,dp(10),0,dp(16)]
    XBoxLayout:
        radius: [dp(16),]
        bg_color: root.item_color
        size_hint: None, None
        size: dp(64),dp(32)
        padding: [(self.width/2) - (ic.width/2),dp(10),0,dp(10)]
        pos_hint: {"center_x": .5 , "center_y": .5}
        XIcon:
            id: ic
            icon: root.icon
            pos_hint: {"center_x": .5 , "center_y": .5}
            font_size: "24sp"
            color: root.icon_color
    XLabel:
        text: root.text
        pos_hint: {"center_x": .5 , "center_y": .5}
        text_color: root.text_color
        font_size: root.font_size


""")

class BotnavIcon(Theming,ButtonBehavior, BoxLayout):
    icon = StringProperty()
    text = StringProperty()
    item_color = ColorProperty([0,0,0,0])
    text_color = ColorProperty([0,0,0,1])
    icon_color = ColorProperty()
    font_size = NumericProperty("13sp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color = self.txt_color
        self.icon_color = self.txt_color

class XBotnavItem(XScreen):
    icon = StringProperty()
    text = StringProperty()
    active_icon = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active_icon = self.icon
    

class XBotnav(Theming,XBoxLayout):
    active_item_color = ColorProperty([0,0,0,0])
    text_color = ColorProperty([0,0,0,0])
    active_text_color = ColorProperty([0,0,0,0])
    bar_color = ColorProperty([0,0,0,0])
    current_tab = StringProperty()
    def __init__(self, **kwargs):
        super(XBotnav, self).__init__(**kwargs)
        self.bar_color = self.card_color
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass


    def add_widget(self,widget,*args):
        if isinstance(widget, XBotnavItem):
            button = BotnavIcon()
            button.bind(on_release = lambda x:self.change_screen(widget,button))
            button.bind(on_press = lambda x:self.dispatch('on_tab_press'))
            button.bind(on_release = lambda x:self.dispatch('on_tab_release'))
            self.ids.bt.add_widget(button)
            self.ids.sm.add_widget(widget)
            self.lenght = len(self.ids.sm.screens)
        else:
            super(XBotnav, self).add_widget(widget)

    def update(self,*args):
        if self.active_item_color == [0,0,0,0]:
            self.active_item_color = self.bgr_color
        if self.active_text_color == [0,0,0,0]:
            self.active_text_color = self.txt_color
        if self.text_color == [0,0,0,0]:
            self.text_color = self.txt_color
        l = len(self.ids.sm.screens) - 1
        for i in range(len(self.ids.sm.screens)):
            self.ids.bt.children[l-i].text = self.ids.sm.screens[i].text
            self.ids.bt.children[l-i].icon = self.ids.sm.screens[i].icon
            self.ids.bt.children[l-i].icon_color =  self.text_color
            if i == 0:
                self.ids.bt.children[l-i].item_color = self.active_item_color
                self.ids.bt.children[l-i].icon_color =  self.active_text_color
                self.ids.bt.children[l-i].icon = self.ids.sm.screens[i].active_icon
                #self.ids.bt.children[l-i].font_size = "14sp"


    def change_screen(self,widget,button,*args):
        self.ids.sm.current = widget.name
        l = len(self.ids.sm.screens) - 1
        for i in range(len(self.ids.sm.screens)):
            self.ids.bt.children[l-i].text = self.ids.sm.screens[i].text
            self.ids.bt.children[l-i].icon = self.ids.sm.screens[i].icon
            self.ids.bt.children[l-i].icon_color =  self.text_color
            self.ids.bt.children[l-i].item_color =  self.trans_color
            
        def cont(*args):
            button.icon = widget.active_icon
            return Animation(height = dp(80), duration = 0.1).start(button)
            
        button.item_color = self.active_item_color
        button.icon_color = self.active_text_color
            
        anim = Animation(height = dp(75), duration = 0.1)
        anim.start(button)
        anim.bind(on_complete = cont)
        Clock.schedule_once(self.determine_current)
        
        
    def determine_current(self,*args):
        self.current_tab = self.ids.sm.current
        
