"""
<MainApp>:
    ETabPanel:
        id: tab_panel
        ETabItem:
            name: "tab1"
            text: "Themes"
        ETabItem:
            name: "tab2"
            text: "Walpapers"
        ETabItem:
            name: "tab3"
            text: "Icon pascks"
        ETabItem:
            name: "tab4"
            text: "revennue"
            XButton:
                text: "hllo"
"""

from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty, BooleanProperty, NumericProperty
from kivyx.boxlayout import XBoxLayout
from kivyx.button import XFlatButton
from kivyx.theming import Theming
from kivyx.screen import XScreen
from kivy.clock import Clock
from kivy.core.window import Window


Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import Transition kivy.uix.screenmanager.NoTransition

<ETabButton>:
    size_hint_y: None
    height: dp(34)
    opacity: .5
    text_color: self.opposite_color
    radius: [0,]
    style: "text"
    canvas.before:
        Color:
            rgba: root.item_color
        Rectangle:
            pos: (self.pos[0] + self.padding[0],self.pos[1]) if root.bottom_line else self.pos
            size: (self.size[0]- (self.padding[0]*2),dp(1)) if root.bottom_line else self.size

<ETabPanel>:
    id: etab
    orientation: "vertical"
    XBoxLayout:
        size_hint_y: None
        height: root.tab_bar_height
        bg_color: root.bar_bg_color
        ScrollView:
            id: sc
            bar_width: 0
            effect_cls: ScrollEffect
            BoxLayout:
                id: bt
                size_hint_x: None
                width: max(self.minimum_width,sc.width)
                spacing: dp(1)
    ScreenManager:
        id: sm
        transition: Transition()



""")

class ETabButton(XButton):
    item_color = ColorProperty([0,0,0,0])
    bottom_line  = BooleanProperty(False)

class ETabItem(XScreen):
    text = StringProperty()

class ETabPanel(Theming,XBoxLayout):
    active_item_color = ColorProperty([0,0,0,0])
    remove_long_pressed_tab = BooleanProperty(False)
    tab_bar_height = NumericProperty("34dp")
    tab_item_font_size = NumericProperty("13sp")
    bottom_line = BooleanProperty(False)
    bar_bg_color = ColorProperty([0,0,0,0])
    def __init__(self, **kwargs):
        super(ETabPanel,self).__init__(**kwargs)
        

    def __init__(self, **kwargs):
        super(ETabPanel, self).__init__(**kwargs)
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')
        Clock.schedule_once(self.update,1)

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass

    def add_widget(self,widget,*args):
        if isinstance(widget, ETabItem):
            button = ETabButton()
            button.bind(on_press = lambda x:self.change_screen(widget,button))
            button.bind(on_press = lambda x:self.count_press(widget,button))
            button.bind(on_press = lambda x:self.dispatch('on_tab_press', button))
            button.bind(on_release = lambda x:self.dispatch('on_tab_release', button))
            button.bind(on_release = lambda x:self.remove_screen())
            self.ids.bt.add_widget(button)
            self.ids.sm.add_widget(widget)
        else:
            super(ETabPanel, self).add_widget(widget)
    
    def update_item_text(self,widget,text,*args):
        l = len(self.ids.sm.screens) - 1
        self.ids.bt.children[l - self.ids.sm.screens.index(widget)].text = text

    def update(self,*args):
        if self.active_item_color == [0,0,0,0]:
            self.active_item_color = self.bgr_color
        l = len(self.ids.sm.screens) - 1
        for i in range(len(self.ids.sm.screens)):
            self.ids.bt.children[l-i].text = self.ids.sm.screens[i].text
            self.ids.bt.children[l-i].font_size = self.tab_item_font_size
            self.ids.bt.children[l-i].height = self.tab_bar_height
            self.ids.bt.children[l-i].bottom_line = self.bottom_line
            if i == 0:
                self.ids.bt.children[l-i].item_color = self.active_item_color
                self.ids.bt.children[l-i].opacity = 1
                self.ids.bt.children[l-i].text_color = self.txt_color

    def change_screen(self,widget,button,*args):
        self.ids.sm.current = widget.name
        for i in self.ids.bt.children:
            i.item_color = self.trans_color
            i.opacity = .5
            i.text_color = self.txt_color
        button.item_color = self.active_item_color
        button.opacity = 1
        button.text_color = self.txt_color
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

    def count_press(self,widget,button,*args):
        if self.remove_long_pressed_tab:
            self.rwidget = widget
            self.rbutton = button
            self.count = 0
            Clock.schedule_interval(self.increase_count,0.5)

    def increase_count(self,*args):
        if self.remove_long_pressed_tab:
            self.count += 1
            if self.count > 1:
                self.ids.sm.remove_widget(self.rwidget)
                self.ids.bt.remove_widget(self.rbutton)
                Clock.unschedule(self.increase_count)

    def remove_screen(self,*args):
        if self.remove_long_pressed_tab:    
            Clock.unschedule(self.increase_count)
            self.count = 0

