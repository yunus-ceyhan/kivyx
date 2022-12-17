from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty
from kivyx.behavior import RectangularBehavior
from kivyx.card import XCard
from kivyx.screen import XScreen
from kivyx.icon_def import x_icons
from kivy.clock import Clock
import threading, re



Builder.load_string("""
#:import Clipboard kivy.core.clipboard.Clipboard
#:import w kivy.core.window.Window

<MainApp>:
    bg_color: root.bgr_color
    XBoxLayout:
        orientation: "vertical"
        XSearchbar:
            id: search_bar
            on_right_icon_release: self.ids.input.text = ""
            on_text: root.get_search(self.ids.input.text)
            left_icon: "magnifying-glass-b"
            right_icon: "backspace-b"
            #elevation: 0.

        XAppToolbar:
            id: t
            left_icon: ''
            right_icon: self.title
            size_hint_y: None
                        
        XRcGridList:
            id: search
            cols: round(w.width/dp(68))
            viewclass: "Search"
            bar_color: root.primary_color
            padding: [dp(16),]
            spacing: dp(10)
            exact_height: dp(48)
            on_scroll_move:
                t.title = ''
            


            
<Search>:
    on_release:
        app.main.ids.t.title = root.text
        Clipboard.copy(root.icon)
    spacing: dp(5)
    padding: [dp(12),0,0,0]
    XIcon:
        icon: root.icon
    XLabel:
        text: root.text if root.mode == 'text' else ''
        aligned: True
        halign: "left"
        shorten: True
        
""")

class Search(RectangularBehavior,XCard):
    icon = StringProperty()
    text = StringProperty()
    mode = StringProperty('text')
    
    
class MainApp(Theming,XScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.get_search("")
        
    def get_search(self,keyword,*args):
        self.ids.search.data = []
        for i in x_icons.keys():
            if i.startswith(keyword.strip()) or keyword.strip() in i:
                widget = {"icon": i.strip(),"text": i.strip(), 'mode':'icon'}
                if not widget in self.ids.search.data:
                    self.ids.search.data.append(widget)
        
        

class TestApp(App):
    def build(self):
        self.theme_style = "Dark"
        self.colorx = Theming()
        self.main = MainApp()
        return self.main


TestApp().run()