

from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty
from kivy.core.window import Window


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
                        
                    
            BoxLayout:
                orientation: "vertical"
                #spacing: dp(10)
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
                    bar_color: root.colors("bluegrey",2)
                    
                XSegmentTab:
                    #active_item_color: "#ff3434"
                    id: tab_panel
                    size_hint_y: None
                    height: dp(64)
                    item_width: dp(400)
                    tab_style: "m3"
                    tab_radius: dp(16)
                    XSegmentItem:
                        name: "tab1"
                        text: "Themes"
                        item_type: "left"
                    XSegmentItem:
                        name: "tab2"
                        text: "Walpapers"
                        item_type: "center"

                    XSegmentItem:
                        name: "tab3"
                        text: "Icon pascks"
                        item_type: "right"
                        text: "revennue"
                XBotnav:
                    id: botnav
                    on_tab_release: print(self.current_tab)
                    active_item_color: root.colors("bluegrey",4)
                    XBotnavItem:
                        name: "news"
                        text: "Newest"
                        icon: "cards-b"
                        active_icon: "cards-f"
                        BoxLayout:
                            orientation: "vertical"
                            XBoxLayout:
                                

                        XFab:
                            icon: "apple"
                            text: "apple"
                            on_press: self.extend_button("extend") if self.status == "shrinked" else self.extend_button("shrink")
                            on_release:
                                bottom_sheet.open()


                    XBotnavItem:
                        name: "podcast"
                        text: "Podcast"
                        icon: "podcast"
                        BoxLayout:
                            orientation: "vertical"
                            XAppToolbar:
                                title: "Demo App"
                                left_icon: "activity"
                                middle_icon: "airplane"
                                right_icon: "alarm"
                                halign: "left"
                                on_left_icon_release: sn.toggle_state()
                            Widget:
                    XBotnavItem:
                        name: "practise"
                        text: "Practise"
                        icon: "cards-outline"
                        BoxLayout:
                            orientation: "vertical"
                            XSearchbar:
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
            XBottomSheetContent:
                orientation: "vertical"
                XIconListItem:
                    icon: "android"
                    text: "android"
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
                    text: "hello there what are you guys doing today "*22
                    size_hint_y: None
                    aligned: True
                    #halign: "left"
                    height: self.texture_size[1]

            XDialogButton:
                text: "CANCEL"
                on_release: dialog.close()
            XDialogButton:
                text: "OK"


""")


class MainApp(ScreenManager,Theming):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    def anim_stop(self,):
        print("hellllloooooo")

class TestApp(App):
    def build(self):
        self.theme_style = "Light"
        return MainApp()


TestApp().run()
