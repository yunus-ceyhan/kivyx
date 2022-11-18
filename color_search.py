from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty
from kivyx.behavior import RectangularBehavior
from kivyx.card import XCard
from kivyx.screen import XScreen
from kivyx.colors import x_colors



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
            cols: round(w.width/dp(100))
            viewclass: "Search"
            bar_color: root.primary_color
            padding: [dp(16),]
            spacing: dp(10)
            exact_height: dp(90)
            on_scroll_move:
                t.title = ''
            


            
<Search>:
    on_release:
        app.main.ids.t.title = root.name
        Clipboard.copy(root.text)
    spacing: dp(5)
    padding: [dp(12),0,0,0]
    orientation: "vertical"
    XLabel:
        text: root.name
        aligned: True
        halign: "center"
        shorten: False
        text_color: .5,.5,.5,0
    XLabel:
        text: root.text
        aligned: True
        halign: "center"
        shorten: False
        text_color: .5,.5,.5,0
        
""")

class Search(RectangularBehavior,XCard):
    text = StringProperty()
    name = StringProperty()
    
    
class MainApp(Theming,XScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.get_search("")
        
    def get_search(self,keyword,*args):
        self.ids.search.data = []
        for i in x_colors["Colors"].keys():
            if i.startswith(keyword.strip()) or keyword.strip() in i:
                for x in x_colors["Colors"][i]:
                    widget = {"bg_color": x, "text": x, "name": f"{i} {x_colors['Colors'][i].index(x)+1}" }
                    if not widget in self.ids.search.data:
                        self.ids.search.data.append(widget)
        
        

class TestApp(App):
    theme_style = StringProperty()
    def build(self):
        self.theme_style = "Dark"
        self.colorx = Theming()
        self.main = MainApp()
        return self.main


TestApp().run()