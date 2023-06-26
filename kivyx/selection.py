
"""
<MainApp>:
    XSwitch:
        pos_hint: {"center_x": .5, "center_y": .5}
        active: True
        style: "m3"
        
    XSelection:
        selections: [0]
        multiselection: False
        blured: False
        frame: True
        style: "filled"
        XSelectionItem:
            bg_color: root.accent_color
            XLabel:
                text: "Aa"
        XSelectionItem:
            id: slc2
            XLabel:
                text: "Aa"
        XSelectionItem:
            XLabel:
                text: "Aa"
        
"""

from kivyx.behavior import CircularBehavior
from kivy.clock import Clock
from kivy.lang import Builder
from kivyx.boxlayout import XBoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty,OptionProperty, BooleanProperty, ObjectProperty
from kivy.metrics import dp
from kivy.animation import Animation
from kivyx.theming import Theming
from kivyx.behavior import RectangularBehavior
from kivy.uix.boxlayout import BoxLayout
from kivyx.card import XCard
from kivy.uix.widget import Widget



Builder.load_string("""
<XSwitch>:
    size_hint: None,None
    size: (dp(36),dp(16) if root.style == "m2" else dp(22))
    radius: [dp(8),] if root.style == "m2" else [dp(10),]
    bg_color: root.back_color
    on_press: root.change_status()
    padding: [0,0,0,0] if root.style == "m2" else [dp(1),0,0,0]
    opacity: (.5 if self.parent.disabled else 1) if self.parent else 1
    XWidget:
        id: ic
        size_hint: None,None
        size: dp(20),dp(20)
        bg_color: root.toggle_color
        radius: [dp(180),]
        pos_hint: {"center_y": .5}
        
<XSelection>:
    id: current_selection
    size_hint_y: None
    height: dp(56)
    spacing: dp(10)
    Widget:

    
<XSelectionItem>:
    radius: [dp(8)]
    size_hint: None, None
    size: dp(48), dp(48)
    elevation: 0

""")

class XSelectionItem(RectangularBehavior,XCard):
    selected = BooleanProperty(False)

class XSelection(Theming,BoxLayout):
    frame = BooleanProperty(True)
    frame_color = ColorProperty()
    frame_width = NumericProperty(dp(2))
    frame_radius = ListProperty([0,0,0,0])
    style = OptionProperty("text", options=["filled","text"])
    blured = BooleanProperty(False)
    _selections = ListProperty()
    _main_widgets = ListProperty()
    selections = ListProperty()
    current_selection = ObjectProperty()
    multiselection = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super(XSelection,self).__init__(**kwargs)
        self.frame_color = self.accent_color
        self.register_event_type('on_item_press')
        self.register_event_type('on_item_release')
        Clock.schedule_once(self.update)

    def on_item_press(self, *args):
        pass

    def on_item_release(self, *args):
        pass


    def add_widget(self,widget,*args):
        if isinstance(widget, XSelectionItem):
            widget.bind(on_release = lambda x:self.update_selection(widget))
            widget.bind(on_press = lambda x:self.dispatch('on_item_press'))
            widget.bind(on_release = lambda x:self.dispatch('on_item_release'))
            super(XSelection, self).add_widget(widget)
            self.current_selection = widget
        else:
            super(XSelection, self).add_widget(widget)

    def update(self,*args):
        self.add_widget(Widget())
        for x in list(reversed(self.children)):
            if isinstance(x, XSelectionItem):
                self._main_widgets.append(x)
        if self.selections:
            for num in self.selections:
                if num in range(len(self._main_widgets)):
                    self._selections.append(self._main_widgets[num])
        for i in self._main_widgets:
            i.opacity = .5 if self.blured else 1
            i.outline = False
            i.outline_width = self.frame_width
            i.line_color = self.frame_color
            i.bg_color = i.bg_color if self.style == "filled" else self.trans_color
            i.selected = False
            if self.multiselection:
                if i in self._selections:
                    i.opacity = 1 
                    i.outline = True if self.frame else False
                    i.selected = True
                    self.current_selection = i
            else:
                if self._selections:
                    if i in self._selections:
                        i.opacity = 1
                        i.outline = True if self.frame else False
                        i.selected = True
                        self.current_selection = i


    def update_selection(self,widget,*args):
        if self.multiselection:
            widget.opacity = 1 if widget.opacity < 1 and self.blured else .5 if widget.opacity == 1 and self.blured else 1
            widget.outline = True if self.frame and widget.outline == False else False if widget.outline == True  and self.frame else False
            widget.selected = True if widget.selected == False else False
            self._selections.append(widget) if not widget in self._selections else self._selections.remove(widget)
            self.current_selection = widget
            self.selections = [self._main_widgets.index(x) for x in self._selections]
        else:
            for i in self._main_widgets:
                i.opacity = .5 if self.blured else 1
                i.outline = False
                i.selected = False
                self._selections.remove(i) if i in self._selections else None
                if i == widget:
                    i.opacity = 1
                    i.outline = True if self.frame else False
                    i.selected = True
                    self.current_selection = i
                    self._selections.append(i) if not i in self._selections else None
                    self.selections = [self._main_widgets.index(i)]
                    
    def clear_selections(self,*args):
        self.selections = []
        self._selections = []
        for i in self._main_widgets:
            i.opacity = .5 if self.blured else 1
            i.outline = False
            i.selected = False
        

class XSwitch(CircularBehavior,XBoxLayout):
    toggle_color = ColorProperty()
    back_color = ColorProperty()
    active_color = ColorProperty()
    active = BooleanProperty(False)
    style = OptionProperty("m2", options = ["m2","m3"])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.toggle_color = self.card_color
        self.back_color = self.disabled_color
        self.active_color = self.accent_color
        Clock.schedule_once(self.set_status)
        
    def set_status(self,*args):
        if self.active:
            self.padding = [dp(16),0,0,0] if self.style == "m2" else [dp(15),0,0,0]
            self.back_color = self.active_color
        else:
            self.padding =[0,0,0,0] if self.style == "m2" else [dp(1),0,0,0]
            self.back_color = self.disabled_color

    def change_status(self,ststus = False,*args):
        if not self.active:
            anim = Animation(padding = [dp(16),0,0,0] if self.style == "m2" else [dp(15),0,0,0], duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = self.change_color)
        else:
            anim = Animation(padding = [0,0,0,0] if self.style == "m2" else [dp(1),0,0,0], duration = 0.2)
            anim.start(self)
            anim.bind(on_complete = self.change_color)

    def change_color(self,*args):
        if self.active:
            self.back_color = self.disabled_color
            self.active = False
        else:
            self.back_color = self.active_color
            self.active = True
