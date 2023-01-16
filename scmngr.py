from kivy.config import Config
Config.set('kivy', 'exit_on_escape', 'False')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivyx.theming import Theming
from kivy.properties import ListProperty, StringProperty

Builder.load_string("""
<Main>:
    XScreen:
        name: "sc1"
        bg_color: root.bgr_color
        XButton:
            text: "go screen 2"
            on_release: root.change_screen("sc2")
        
    XScreen:
        name: "sc2"
        bg_color: root.bgr_color
        XButton:
            text: "go screen 3"
            on_release: root.change_screen("sc3")
        
    XScreen:
        name: "sc3"
        bg_color: root.bgr_color
        XButton:
            text: "go back"
            on_release: root.change_screen("back")
""")

class Main(Theming, ScreenManager):
    pages = ListProperty()
    previous = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pages.append("sc1")
        
    def change_screen(self,target,*a):
        print(self.pages)
        self.previous = self.pages[-1]
        if target == "back":
            if len(self.pages) > 1:
                self.pages.pop()
                self.current = self.pages[-1]
            else:
                self.current = self.pages[-1]
        else:
            if target in self.pages:
                self.pages.remove(target)
                self.pages.append(target)
                self.current = self.pages[-1]
            else:
                self.pages.append(target)
                self.current = self.pages[-1]
        print(self.pages)
        print(self.previous)
                

class TestApp(App):
    main = Main()
    def build(self):
        return self.main
    
TestApp().run()