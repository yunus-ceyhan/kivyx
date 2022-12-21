
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock



Builder.load_string("""


<MainApp>:
    id: scr_mngr
    XScreen:
        name: "main_screen"
        XSidenav:
            id: sn
            anim_type: ["fade_in","slide_above_anim","slide_above_simple","reveal_below_anim","reveal_below_simple"][1]
            separator_image_width: dp(1)
            on_anim_stop: root.anim_stop()
            XBoxLayout:
                orientation: "vertical"
                padding: [dp(12),]
                bg_color: root.bgr_color
                XLabel:
                    text: "Activities"
                    bold: True
                    aligned: True
                    halign: "left"
                    color: root.txt_medium
                    size_hint_y: None
                    height: dp(48)
                    padding_x: dp(16)
                    
                    
                XCard:
                    radius: [dp(12),]
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: [dp(16),dp(4),]
                    #elevation: 0.5
                    #shadow_y: - dp(1)
                    #line_color: root.line_color
                    BoxLayout:
                        size_hint_y: None
                        height: dp(48)
                        disabled: True if system_pr.active else False
                        XLabel:
                            text: "Show non-exported activities"
                            font_size: "14sp"
                            aligned: True
                            halign: "left"
                            pos_hint: { "center_y": .5}
                        XSwitch:
                            pos_hint: { "center_y": .5}
                            active: True
                            style: "m3"
                            
                    BoxLayout:
                        size_hint_y: None
                        height: dp(48)
                        XLabel:
                            text: "Show user packages"
                            font_size: "14sp"
                            aligned: True
                            halign: "left"
                            pos_hint: { "center_y": .5}
                        XSwitch:
                            pos_hint: { "center_y": .5}
                            active: False
                            style: "m3"

                XLabel:
                    text: "Theme"
                    bold: True
                    aligned: True
                    halign: "left"
                    color: root.txt_medium
                    size_hint_y: None
                    height: dp(48)
                    padding_x: dp(16)
                    
                XCard:
                    radius: [dp(12),]
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: [dp(16),dp(4),]
                    BoxLayout:
                        size_hint_y: None
                        height: dp(48)
                        XLabel:
                            text: "Sytem provided"
                            font_size: "14sp"
                            aligned: True
                            halign: "left"
                            pos_hint: { "center_y": .5}
                        XSwitch:
                            id: system_pr
                            pos_hint: { "center_y": .5}
                            active: True
                            style: "m3"
                    BoxLayout:
                        size_hint_y: None
                        height: dp(48)
                        disabled: True if system_pr.active else False
                        XLabel:
                            text: "Dark theme"
                            font_size: "14sp"
                            aligned: True
                            halign: "left"
                            pos_hint: { "center_y": .5}
                        XSwitch:
                            pos_hint: { "center_y": .5}
                            active: False
                            style: "m3"
                            disabled: True if system_pr.active else False
                            
                XLabel:
                    text: "Contacts"
                    bold: True
                    aligned: True
                    halign: "left"
                    color: root.txt_medium
                    size_hint_y: None
                    height: dp(48)
                    padding_x: dp(16)
                    
                XCard:
                    radius: [dp(12),]
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    #padding: [dp(16),dp(4),]
                    XTwoIconListItem:
                        elevation: 0
                        text: "yunus.ceyhn@gmail.com"
                        left_icon: "envelope-simple-d"
                        right_icon: "arrow-square-up-right"
                        font_size: "14sp"
                        bg_color: root.trans_color
                    XTwoIconListItem:
                        elevation: 0
                        text: "yunus-ceyhan"
                        left_icon: "github-logo"
                        right_icon: "arrow-square-up-right"
                        font_size: "14sp"
                        bg_color: root.trans_color
                    XTwoIconListItem:
                        elevation: 0
                        text: "yunus_ceyhan"
                        left_icon: "twitter-logo-d"
                        right_icon: "arrow-square-up-right"
                        font_size: "14sp"
                        bg_color: root.trans_color
                        
                XLabel:
                    text: "About"
                    bold: True
                    aligned: True
                    halign: "left"
                    color: root.txt_medium
                    size_hint_y: None
                    height: dp(48)
                    padding_x: dp(16)
                    
                XCard:
                    radius: [dp(12),]
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: [dp(16),dp(4),]
                    BoxLayout:
                        size_hint_y: None
                        height: dp(48)
                        disabled: True
                        XLabel:
                            text: "Version"
                            font_size: "14sp"
                            aligned: True
                            halign: "left"
                            pos_hint: { "center_y": .5}
                        XLabel:
                            text: "5.83"
                            font_size: "14sp"
                            aligned: True
                            halign: "right"
                            pos_hint: { "center_y": .5}
                            
                Widget:
                        
                    
            XBoxLayout:
                orientation: "vertical"
                #spacing: dp(10)
                bg_color: root.bgr_color
                XAppSearchbar:
                    text: "Search for Themes"
                    left_icon: "list-b"
                    right_icon: "dots-three-vertical-b"
                    on_left_icon_release: sn.toggle_state()
                    on_right_icon_release:
                        menu.open()
                    elevation: 0
                    #distance: dp(3)
                    #top: True
                    line_color: 0,0,0,.2
                    bar_color: root.primary_color
                    style: 'm3'
                    

                XBotnav:
                    id: botnav
                    on_tab_release: print(self.current_tab)
                    active_item_color: root.accent_color
                    bar_color: root.primary_color
                    XBotnavItem:
                        name: "news"
                        text: "Newest"
                        icon: "cards-b"
                        active_icon: "cards-f"

                        XBoxLayout:
                            orientation: "vertical"
                            padding: [dp(50),dp(56),0,0]
                            spacing: dp(30)
                            
                            XToolbar:
                                top: False
                            XButton:
                                text: "hello"
                                bg_color: root.accent_color
                                #style: "outlined"
                                rounded: True
                             
                            XCard:
                                radius: [dp(16),]
                                orientation: "vertical"
                                size_hint: None, None
                                size: dp(100), dp(56)
                                padding: [dp(16),dp(4),]
                                elevation: .2
                                shadow_y:  -  dp(5)
                                shadow_blur: dp(17)
                                shadow_distance: - dp(4)
                                bg_color: root.accent_color
                            Widget:

                        



                    XBotnavItem:
                        id: podcast
                        name: "podcast"
                        text: "Podcast"
                        icon: "podcast"

                        BoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: podcast.height - tbb.height

                            XRcGridList:
                                id: rc
                                cols: 1
                                viewclass: "XItem"
                                #bar_color: root.primary_color
                                #bar_width: dp(5)
                                #padding: [dp(10),]
                                spacing: dp(10)
                                exact_height: dp(56)
                                
                        XAppToolbar:
                            id: tbb
                            title: "Demo App"
                            left_icon: "activity"
                            middle_icon: "airplane"
                            right_icon: "alarm"
                            halign: "left"
                            pos: self.pos[0], podcast.height - self.height
                            on_left_icon_release: sn.toggle_state()
                            
                        XFab:
                            id: fab
                            icon: "folder"
                            text: "apple"
                            button_bg_color: root.accent_color
                            
                            on_press: self.extend_button("extend") if self.status == "shrinked" else self.extend_button("shrink")
                            on_release:
                                bottom_sheet.open()

                    XBotnavItem:
                        name: "practise"
                        text: "Practise"
                        icon: "cards-outline"
                        BoxLayout:
                            orientation: "vertical"
                            XSearchbar:
                            XSegmentControl:
                                pos_hint: {"center_x": .5, "center_y":.5}
                                item_width:  dp(320)
                                radius: [dp(8),]
                                style: "m3"
                                XSegmentTextItem:
                                    text: "Global"
                                    bubble_text: "12"
                                XSegmentTextItem:
                                    text: "China"
                                XSegmentIconItem:
                                    icon: "alarm-f"
                            Widget:

                    XBotnavItem:
                        name: "saved"
                        text: "Saved"
                        icon: "bookmark"
                        XButton:
                            text: "hello"
                            style: "outlined"
            

        XDotMenu:
            id: menu
            on_anim_start: print(self.status)
            on_anim_stop: print(self.status)
            XDotItem:
                text: "Rate us"
                icon: "google-play"
            XDotItem:
                text: "Share App"
                icon: "share-variant"
            XDotItem:
                text: "Feedback"
                icon: "email"
            XDotItem:
                text: "Exit"
                icon: "exit-to-app"
                on_release: dialog.open()

        XBottomSheet:
            id: bottom_sheet
            on_anim_start: print(self.status)
            on_anim_stop: print(self.status)
            #expandable: True
            XBottomSheetContent:
                orientation: "vertical"
                XItem:
                    text: "android"
                    elevation: 0
                XIconListItem:
                    icon: "android"
                    text: "android"
                XIconListItem:
                    icon: "android"
                    text: "android"
                XIconListItem:
                    icon: "android"
                    text: "android"
        XDialog:
            id: dialog
            title: "Close App"
            expandable: True
            on_anim_start: print(self.status)
            on_anim_stop: print(self.status)
            XDialogContent:
                XLabel:
                    text: "hello there what are you guys doing today "*5
                    size_hint_y: None
                    aligned: True
                    #halign: "left"
                    height: self.texture_size[1]

            XDialogButton:
                text: "CANCEL"
                on_release: dialog.close()
                style: 'elevated'
                bg_color: root.accent_color
            XDialogButton:
                text: "OK"


""")


class MainApp(ScreenManager,Theming):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        l = []
        for i in range(100):
            l.append({'text': str(i), 'radius': [dp(8),], 'left_icon': 'folder', 'right_text': 'open'})
        self.ids.rc.data = l

        

    
    def anim_stop(self,):
        print("hellllloooooo")

class TestApp(App):
    def build(self):
        self.theme_style = "Light"
        return MainApp()


TestApp().run()
