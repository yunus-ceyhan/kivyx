
"""
<MainApp>:
    XBoxLayout:
        spacing: dp(120)
        padding: [dp(120),]
        orientation: "vertical"
        bg_color: root.bgr_color
        XItem:
            radius: [dp(12),]
            text: "test title"
            second_text: "test second text"
            #left_icon: "envelope-simple-d"
            #right_icon: "envelope-simple-d"
            image: "./kivyx/data/icon.png"
            right_text: "100%"
            button_text: "extend"
            button_right_icon: "envelope-simple"
            button_style: "text"
            badge_icon: "envelope-simple"
            on_press: self.badge_icon = ""
"""

from kivy.lang import Builder
from kivy.properties import ColorProperty, NumericProperty, StringProperty, BooleanProperty
from kivy.metrics import dp
from kivyx.behavior import RectangularBehavior
from kivy.uix.boxlayout import BoxLayout
from kivyx.card import XCard
from kivyx.label import XLabel
from kivyx.button import XButton, XIconButton
from kivyx.icon import XIcon
from kivyx.selection import XSwitch
from kivy.uix.image import Image
from kivy.clock import Clock


Builder.load_string("""
<XItem>:
    size_hint_y: None
    height: dp(56)
    spacing: dp(12)
    padding: [0,0,dp(16) if root.add_selection else dp(8),0]

""")

class Rectangular(RectangularBehavior,BoxLayout):
    pass

class XItem(XCard):
    
    left_icon = StringProperty()
    left_icon_color = ColorProperty()
    
    right_icon = StringProperty()
    right_icon_color = ColorProperty()
    
    image = StringProperty()
    
    button_text = StringProperty()
    button_left_icon = StringProperty()
    button_right_icon = StringProperty()
    button_icon_color = ColorProperty()
    button_color = ColorProperty()
    button_style = StringProperty("filled")
    
    text = StringProperty()
    text_color = ColorProperty()
    font_name = StringProperty("Roboto")
    font_size = NumericProperty("15sp")
    bold = BooleanProperty(False)
    
    second_text = StringProperty()
    second_text_color = ColorProperty()
    second_font_name = StringProperty("Roboto")
    second_font_size = NumericProperty("14sp")
    
    right_text = StringProperty()
    right_text_color = ColorProperty()
    right_font_name = StringProperty("Roboto")
    right_font_size = NumericProperty("12sp")
    
    badge_icon = StringProperty()
    badge_icon_color = ColorProperty()
    
    add_selection = BooleanProperty(False)
    selection_active = BooleanProperty(False)
    selection_style = StringProperty("m3")
    selection_toggle_color = ColorProperty()
    selection_active_color = ColorProperty()
    selection_opacity = NumericProperty(1)
    
    
    def __init__(self, **kwargs):
        super(XItem, self).__init__(**kwargs)
        self.text_color = self.txt_color
        self.second_text_color = self.txt_medium
        self.right_text_color = self.txt_light
        self.right_icon_color = self.txt_color
        self.left_icon_color = self.txt_color
        self.button_color = self.accent_color
        self.button_icon_color = self.txt_color
        self.badge_icon_color = self.txt_color
        self.selection_toggle_color = self.card_color
        self.selection_active_color = self.accent_color
        self.register_event_type('on_press')
        self.register_event_type('on_release')
        self.register_event_type('on_button_press')
        self.register_event_type('on_button_release')
        self.register_event_type('on_right_icon_press')
        self.register_event_type('on_right_icon_release')
        self.register_event_type('on_selection')
        Clock.schedule_once(self.set_widget)
        
    def on_press(self, *args):
        pass

    def on_release(self, *args):
        pass

    def on_button_press(self, *args):
        pass

    def on_button_release(self, *args):
        pass
        
    def on_right_icon_press(self, *args):
        pass

    def on_right_icon_release(self, *args):
        pass
    
    def on_selection(self, *args):
        pass
    
    def set_widget(self,*args):
        self.clear_widgets()
        
        main = Rectangular(
            padding = [dp(8) if self.image else dp(16) ,dp(8),dp(12),dp(8)],
            spacing = dp(16),
        )
        main.bind(on_press = lambda x:self.dispatch('on_press', main))
        main.bind(on_release = lambda x:self.dispatch('on_right_icon_release', main))
        body = BoxLayout(
            orientation = "vertical"
        )

        title = BoxLayout(
            spacing = dp(8)
        )

        self.badge = XIcon(
            icon = self.badge_icon,
            color = self.badge_icon_color,
            font_size = "13sp",
            pos_hint = {"center_y": .5},
        )

        self.main_label = XLabel(
            text = self.text,
            text_color = self.txt_color,
            font_name = self.font_name,
            font_size = self.font_size,
            bold = self.bold,
            aligned = True,
            halign = "left",
            valign = "middle",
            shorten = True,
            shorten_from = "right",
            pos_hint = {"center_y": .5}
        )
        self.second_label = XLabel(
            text = self.second_text,
            text_color = self.second_text_color,
            font_name = self.second_font_name,
            font_size = self.second_font_size,
            aligned = True,
            halign = "left",
            valign = "middle",
            shorten = True,
            shorten_from = "right",
            pos_hint = {"center_y": .5}
        )
        
        self.right_label = XLabel(
            text = self.right_text,
            text_color = self.right_text_color,
            font_name = self.right_font_name,
            font_size = self.right_font_size,
            aligned = True,
            halign = "right",
            valign = "middle",
            shorten = True,
            shorten_from = "right",
            pos_hint = {"center_y": .5}
        )
        
        self.left_ic = XIcon(
            icon = self.left_icon,
            color = self.left_icon_color,
            pos_hint = {"center_y": .5},
        )
        
        self.right_ic = XIconButton(
            icon = self.right_icon,
            icon_color = self.right_icon_color,
            pos_hint = {"center_y": .5}
        )
        self.right_ic.bind(on_press = lambda x:self.dispatch('on_right_icon_press', self.right_ic))
        self.right_ic.bind(on_release = lambda x:self.dispatch('on_right_icon_release', self.right_ic))
        
        self.img = Image(
            source = self.image,
            size_hint = (None,None),
            size = (self.height - dp(16),self.height - dp(16)),
            keep_ratio = False,
            allow_stretch = True
        )
        
        self.button = XButton(
            text = self.button_text,
            left_icon = self.button_left_icon,
            right_icon = self.button_right_icon,
            bg_color = self.button_color,
            icon_color = self.button_icon_color,
            style = self.button_style,
            pos_hint = {"center_y": .5},
        )
        self.button.bind(on_press = lambda x:self.dispatch('on_button_press', self.button))
        self.button.bind(on_release = lambda x:self.dispatch('on_button_release', self.button))
        
        self.switch = XSwitch(
            active = self.selection_active,
            style = self.selection_style,
            toggle_color = self.selection_toggle_color,
            active_color = self.selection_active_color,
            opacity = self.selection_opacity,
            pos_hint = {"center_y": .5}
        )
        
        self.switch.bind(on_release = lambda x:self.dispatch('on_selection', self.switch))
        
        body.add_widget(title)
        main.add_widget(body)
        self.add_widget(main)
        
        if self.badge_icon:
            title.add_widget(self.badge)
        if self.text:
            title.add_widget(self.main_label)
        if self.second_text:
            body.add_widget(self.second_label)
        if self.left_icon:
            main.add_widget(self.left_ic, 1)
        if self.right_icon:
            self.add_widget(self.right_ic)
        if self.image:
            main.add_widget(self.img, 1)
        if self.right_text:
            main.add_widget(self.right_label)
        if self.button_text:
            self.add_widget(self.button)
        if self.add_selection:
            self.add_widget(self.switch)
            
    def on_text(self, instance,value):
        try:
            self.main_label.text = value
        except:
            pass
        
    def on_bold(self, instance,value):
        try:
            self.main_label.bold = value
        except:
            pass
        
    def on_text_color(self, instance,value):
        try:
            self.main_label.text_color = value
        except:
            pass
        
    def on_second_text(self, instance,value):
        try:
            self.second_label.text = value
        except:
            pass
        
    def on_second_text_color(self, instance,value):
        try:
            self.second_label.text_color = value
        except:
            pass
        
    def on_right_text(self, instance,value):
        try:
            self.right_label.text = value
        except:
            pass
        
    def on_right_text_color(self, instance,value):
        try:
            self.right_label.text_color = value
        except:
            pass
        
    def on_image(self, instance,value):
        try:
            self.img.source = value
        except:
            pass
        
    def on_left_icon(self, instance,value):
        try:
            self.left_ic.icon = value
        except:
            pass
        
    def on_left_icon_color(self, instance,value):
        try:
            self.left_ic.icon_color = value
        except:
            pass
        
    def on_right_icon(self, instance,value):
        try:
            self.right_ic.icon = value
        except:
            pass
        
    def on_right_icon_color(self, instance,value):
        try:
            self.right_ic.icon_color = value
        except:
            pass
        
    def on_button_text(self, instance,value):
        try:
            self.button.text = value
        except:
            pass
        
    def on_button_left_icon(self, instance,value):
        try:
            self.button.left_icon = value
        except:
            pass
        
    def on_button_right_icon(self, instance,value):
        try:
            self.button.right_icon = value
        except:
            pass
        
    def on_button_icon_color(self, instance,value):
        try:
            self.button.icon_color = value
        except:
            pass
            
    def on_badge_icon(self, instance,value):
        try:
            self.badge.icon = value
        except:
            pass
        
    def on_badge_icon_color(self, instance,value):
        try:
            self.badge.icon_color = value
        except:
            pass
        
    def on_selection_opacity(self, instance,value):
        try:
            self.switch.opacity = value
        except:
            pass
