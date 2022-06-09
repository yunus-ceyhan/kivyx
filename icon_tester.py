from kivy.app import App
from kivy.uix.label import Label

class Test(App):
    def build(self):
        return Label(text = "",
                    font_name = "",
                    font_size = "")
                    
Test().run()