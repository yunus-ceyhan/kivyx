from kivyx.boxlayout import XBoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty,OptionProperty
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.clock import Clock

Builder.load_string("""
<XCard>:
    canvas.before:
        Color:
            rgba: 0,0,0, root.elevation/2
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
            
        Color:
            rgba: 0,0,0, root.elevation/1.8
            
        RoundedRectangle:
            size: self.size[0] + dp(7.2) , self.size[1] + dp(6.2)
            pos: self.pos[0] - dp(3.6), self.pos[1] - dp(3.6)
            radius: root.radius
        Color:
            rgba: 0,0,0, root.elevation/1.6   
        RoundedRectangle:
            size: self.size[0] + dp(6.4) , self.size[1] + dp(5.4)
            pos: self.pos[0] - dp(3.2), self.pos[1] - dp(3.2)
            radius: root.radius
        Color:
            rgba: 0,0,0, root.elevation/1.4    
        RoundedRectangle:
            size: self.size[0] + dp(5.6) , self.size[1] + dp(4.6)
            pos: self.pos[0] - dp(2.8), self.pos[1] - dp(2.8)
            radius: root.radius                        
        Color:
            rgba: 0,0,0, root.elevation/1.2                           
        RoundedRectangle:
            size: self.size[0] + dp(4.8) , self.size[1] + dp(3.8)
            pos: self.pos[0] - dp(2.4), self.pos[1] - dp(2.4)
            radius: root.radius
        Color:
            rgba: 0,0,0, root.elevation            
        RoundedRectangle:
            size: self.size[0] + dp(4) , self.size[1] + dp(3)
            pos: self.pos[0] - dp(2), self.pos[1] - dp(2)
            radius: root.radius                                                                       
        Color:
            rgba: 0,0,0, root.elevation*1.2                                                                                                                                 
        RoundedRectangle:
            size: self.size[0] + dp(3.2) , self.size[1] + dp(2.2)
            pos: self.pos[0] - dp(1.6), self.pos[1] - dp(1.6)
            radius: root.radius
            
        Color:
            rgba: 0,0,0, root.elevation*2
        RoundedRectangle:
            size: self.size[0] + dp(2.4) , self.size[1] + dp(1.4)
            pos: self.pos[0] - dp(1.2), self.pos[1] - dp(1.2)
            radius: root.radius
        Color:
            rgba: 0,0,0, root.elevation *4
        RoundedRectangle:
            size: self.size[0] + dp(1.6) , self.size[1] + dp(0.6)
            pos: self.pos[0] - dp(0.8), self.pos[1] - dp(0.8)
            radius: root.radius                                                                                                                                                                                                                                                                                    
        Color:
            rgba: 0,0,0, root.elevation*10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        RoundedRectangle:
            size: self.size[0] + dp(0.8) , self.size[1] + dp(0.3)
            pos: self.pos[0] - dp(0.4), self.pos[1] - dp(0.4)
            radius: root.radius
         
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            size: self.size[0],self.size[1]
            pos: (self.pos[0] , self.pos[1] + dp(1) ) if root.type == 'button' else self.pos
            radius: root.radius


""")

class XCard(Theming,XBoxLayout):
    bg_color = ColorProperty()
    radius = ListProperty([0,])
    type = OptionProperty('card', options = ['card','button'])
    elevation = NumericProperty(0.003)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bg_color = self.card_color
