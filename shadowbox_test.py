

from kivy.app import App 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import  NumericProperty, StringProperty
from kivyx.screen import XScreen

Builder.load_string("""
#:import hex kivy.utils.get_color_from_hex

<MainApp>:
    XBoxLayout:
        spacing: dp(10)
        padding: [dp(20),dp(50),dp(20),dp(20)]
        orientation: "vertical"
        bg_color: root.card_color
        BoxLayout:
            size_hint: None, None
            size: dp(300), dp(120)
            pos_hint: {"center_x": .5}
            offs_x: dp(int(float(offset_x.text))) if offset_x.text and offset_x.text != "-" else 0
            offs_y: dp(int(float(offset_y.text))) if offset_y.text and offset_y.text != "-" else 0
            sp_rd: dp(int(float(spread_radius.text))) if spread_radius.text and spread_radius.text != "-" else 0
            bl_rd: dp(int(float(blur_radius.text))) if blur_radius.text and blur_radius.text != "-" else 0
            alp:alpha.value
            clr: "#"+color.text
            
            box_rad: dp(bx_rad.value)
            shw_rad: dp(sh_rad.value)
            canvas.before:
                Color:
                    rgba: (0, 0, 0, self.alp if self.alp else 0)
                BoxShadow:
                    pos: self.pos
                    size: self.size
                    offset: self.offs_x, self.offs_y
                    spread_radius: self.sp_rd
                    border_radius: [self.shw_rad,self.shw_rad,self.shw_rad,self.shw_rad] if self.shw_rad else [0,0,0,0]
                    blur_radius: self.bl_rd
            canvas.after:
                Color:
                    rgba: hex(self.clr) if self.clr else hex("#ffffff")
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [self.box_rad,self.box_rad,self.box_rad,self.box_rad] if self.box_rad else [0,]
                        
        BoxLayout:
            Label:
                text: "box_color"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
            TextInput:
                id: color
                text: "ffffff"
                hint_text: "#"
                color: 0,0,0,1
                size_hint: None, None
                size: dp(100), dp(30)
                multiline: False
                    
        BoxLayout:
            Label:
                text: "box_radius"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
                
            Slider:
                id: bx_rad
                max: 100
                min: 0
                value: 0
                size_hint_y: None
                height: dp(30)
            Label:
                text: str(bx_rad.value)[:4]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False
                        
        BoxLayout:
            Label:
                text: "shadow_radius"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
                
            Slider:
                id: sh_rad
                max: 100
                min: 0
                value: 0
                size_hint_y: None
                height: dp(30)
            Label:
                text: str(sh_rad.value)[:4]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False

        BoxLayout:
            Label:
                text: "offset_x"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
            Slider:
                id: x
                max: 100
                min: - 100
                value: 0
                size_hint_y: None
                height: dp(30)
            TextInput:
                id: offset_x
                text: str(x.value)[:3]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False
                
        BoxLayout:
            Label:
                text: "offset_y"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
            Slider:
                id: y
                max: 100
                min: - 100
                value: 0
                size_hint_y: None
                height: dp(30)
            TextInput:
                id: offset_y
                text: str(y.value)[:3]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False
                
        BoxLayout:
            Label:
                text: "spread_radius"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
            Slider:
                id: spread
                max: 100
                min: - 100
                value: 0
                size_hint_y: None
                height: dp(30)
            TextInput:
                id: spread_radius
                text: str(spread.value)[:3]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False
                
        BoxLayout:
            Label:
                text: "blur_radius"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
            Slider:
                id: blur
                max: 100
                min: 0
                value: 0
                size_hint_y: None
                height: dp(30)
            TextInput:
                id: blur_radius
                text: str(blur.value)[:3]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False
                
        BoxLayout:
            Label:
                text: "alpha"
                color: 0,0,0,1
                size_hint: None,None
                size: dp(100), dp(30)
                
            Slider:
                id: alpha
                max: 1.0
                min: 0.0
                value: 0.5
                size_hint_y: None
                height: dp(30)
            Label:
                id: alpha_val
                text: str(alpha.value)[:3]
                color: 0,0,0,1
                size_hint: None, None
                size: dp(50), dp(30)
                multiline: False
        
            

""")
        
class MainApp(Theming,XScreen):
    text = StringProperty("test title")
    offset_x = NumericProperty(0)
    offset_y = NumericProperty(0)
    spread_radius = NumericProperty(0)
    blur_radius = NumericProperty(0)
    def __init__(self, **kw):
        super().__init__(**kw)

class TestApp(App):
    theme_style = StringProperty()
    main = MainApp()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        return self.main


TestApp().run()
