

from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)


Builder.load_string("""


<MainApp>:
    id: scr_mngr
    Screen:
        name: "main_screen"
        XSidenav:
            id: sn
            anim_type: ["fade_in","slide_above_anim","slide_above_simple","reveal_below_anim","reveal_below_simple"][1]
            separator_image_width: dp(1)
            on_anim_stop: root.anim_stop()
            XBoxLayout:
                orientatiom: "vertical"
                bg_color: app.colorx.card_color

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
                    bg_color: self.bgr_color
                    XBotnavItem:
                        name: "news"
                        text: "Newest"
                        icon: "newspaper"
                        BoxLayout:
                            orientation: "vertical"
                            XBoxLayout:
                                bg_color: root.card_color
                                

                        XFab:
                            icon: "apple"
                            text: "apple"
                            on_press: self.extend_button("extend") if self.status == "shrinked" else self.extend_button("shrink")
                            on_release: bottom_sheet.open()


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
            expandable: False
            on_anim_start: print(self.status)
            on_anim_stop: print(self.status)
            XDialogContent:
                XLabel:
                    text: "hello there what are you guys doing today"*10
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
    
    def anim_stop(self,):
        print("hellllloooooo")

class TestApp(App):
    theme_style = StringProperty()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        Window.clearcolor = (1, 1, 1, 1)
        return MainApp()


TestApp().run()
