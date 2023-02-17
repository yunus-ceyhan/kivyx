from kivyx.bottomsheet import XBottomSheet, XBottomSheetContent
from kivyx.label import XLabel
from kivy.properties import ColorProperty, NumericProperty, BooleanProperty,StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.metrics import dp

class xalert(XBottomSheet):
    text = StringProperty()
    font_size = NumericProperty(16)
    font_name = StringProperty("Roboto")
    bold = BooleanProperty(False)
    time = NumericProperty(0.1)
    color = ColorProperty()
    callback = ObjectProperty()
    def __init__(self, **kwargs):
        super(xalert,self).__init__(**kwargs)
        self.expandable = True
        self.back_opacity = [0,0,0,0]
        self.top_radius = 0
        self.vertical_padding = 0
        self.back_color = self.txt_color
        self.text_color = self.colors("white",4)
        Clock.schedule_once(self.open_xalert, self.time)
            
    def open_xalert(self,*args):
        label = XLabel(text = self.text,
                        size_hint_y=None,
                        height= dp(20),
                        aligned=True,
                        halign="left",
                        font_name=self.font_name,
                        font_size=self.font_size,
                        pos_hint= {"center_y": .1},
                        bold= self.bold)
        content = XBottomSheetContent(padding =[dp(16),dp(16),0,0])
        content.add_widget(label)
        label.text_color= self.text_color
        self.add_widget(content)
        from kivy.app import App
        from kivy.uix.screenmanager import ScreenManager,Screen
        if self.callback:
            self.callback.add_widget(self)
        else:
            print(self.text)
            
        self.open()
        if not self.permanent:
            Clock.schedule_once(self.destroy_xalert,3)
        else:
            self.permanent = False
            
    def destroy_xalert(self,*args):
        try:
            self.parent.remove_widget(self)
        except: pass
