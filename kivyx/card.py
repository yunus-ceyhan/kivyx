from kivyx.boxlayout import XBoxLayout
from kivy.properties import ListProperty, NumericProperty, ColorProperty,OptionProperty
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.metrics import dp

Builder.load_string("""
<XCard>:
    canvas.before:
        Color:
            rgba: 0,0,0, root.percent(root.elevation,90)       
        RoundedRectangle:
            size: self.size[0] + dp(0.5) , self.size[1] + dp(1)
            pos: self.pos[0] - dp(0.25), self.pos[1] - dp(0.5)
            radius: root.radius
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,90)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,2)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,2)) , self.size[1] + dp(root.percent(root.distance,1))
            pos: self.pos[0] - dp(root.percent(root.distance,1)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,1)), self.pos[1] - dp(root.percent(root.distance,2))
            radius: [root.radius[0]+(root.percent(root.distance,1)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,80)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,3)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,3)) , self.size[1] + dp(root.percent(root.distance,1.5))
            pos: self.pos[0] - dp(root.percent(root.distance,1.5)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,1.5)), self.pos[1] - dp(root.percent(root.distance,3))
            radius: [root.radius[0]+(root.percent(root.distance,1.5)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,70)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,5)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,5)), self.size[1] + dp(root.percent(root.distance,2.5))
            pos: self.pos[0] - dp(root.percent(root.distance, 2.5)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,2.5)), self.pos[1] - dp(root.percent(root.distance,5))
            radius: [root.radius[0]+(root.percent(root.distance,2.5)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,60)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,8)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,8)), self.size[1] + dp(root.percent(root.distance,4))
            pos: self.pos[0] - dp(root.percent(root.distance, 4)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,4)), self.pos[1] - dp(root.percent(root.distance,8))
            radius: [root.radius[0]+(root.percent(root.distance,4)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,50)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,12)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,12)), self.size[1] + dp(root.percent(root.distance,6))
            pos: self.pos[0] - dp(root.percent(root.distance, 6)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,6)), self.pos[1] - dp(root.percent(root.distance,13))
            radius: [root.radius[0]+(root.percent(root.distance,6)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,40)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,17)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,17)) , self.size[1] + dp(root.percent(root.distance,8.5))
            pos: self.pos[0] - dp(root.percent(root.distance, 8.5)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,8.5)), self.pos[1] - dp(root.percent(root.distance,17))
            radius: [root.radius[0]+(root.percent(root.distance,8.5)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,30)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,23)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,23)), self.size[1] + dp(root.percent(root.distance,11.5))
            pos: self.pos[0] - dp(root.percent(root.distance, 11.5)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,11.5)), self.pos[1] - dp(root.percent(root.distance,23))
            radius: [root.radius[0]+(root.percent(root.distance,11.5)/10),]

        Color:
            rgba: 0,0,0, root.percent(root.elevation,20)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,29)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,29)), self.size[1] + dp(root.percent(root.distance,15.5))
            pos: self.pos[0] - dp(root.percent(root.distance, 15.5)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,15.5)), self.pos[1] - dp(root.percent(root.distance,31))
            radius: [root.radius[0]+(root.percent(root.distance,15.5)/10),]
        Color:
            rgba: 0,0,0, root.percent(root.elevation,10)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,38)/2) if root.type == "button" else self.size[0] + dp(root.percent(root.distance,38)), self.size[1] + dp(root.percent(root.distance,19))
            pos: self.pos[0] - dp(root.percent(root.distance, 19)/2) if root.type == "button" else self.pos[0] - dp(root.percent(root.distance,19)), self.pos[1] - dp(root.percent(root.distance,38))
            radius: [root.radius[0]+(root.percent(root.distance,19)/10),]
            
        Color:
            rgba: 0,0,0, root.percent(root.elevation,5)       
        RoundedRectangle:
            size: self.size[0] + dp(root.percent(root.distance,50)/2) , self.size[1] + dp(root.percent(root.distance,25))
            pos: self.pos[0] - dp(root.percent(root.distance, 25)/2), self.pos[1] - dp(root.percent(root.distance,50))
            radius: [root.radius[0]+(root.percent(root.distance,25)/10),]

        Color:
            rgba: root.bg_color
        RoundedRectangle:
            size: self.size[0],self.size[1]
            pos: (self.pos[0] , self.pos[1])
            radius: root.radius

""")

class XCard(Theming,XBoxLayout):
    bg_color = ColorProperty()
    radius = ListProperty([0,])
    type = OptionProperty('card', options = ['card','button'])
    elevation = NumericProperty(0.02)
    distance = NumericProperty(dp(6))
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bg_color = self.card_color


    def percent(self, max, percent):
        return (max/100)*percent