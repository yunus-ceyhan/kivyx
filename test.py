

from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivyx.theming import Theming
from kivy.properties import StringProperty


Builder.load_string("""


<MainApp>:
    id: scr_mngr
    Screen:
        name: "main_screen"
        XSidenav:
            id: sn
            anim_type: ["fade_in","slide_above_anim","slide_above_simple","reveal_below_anim","reveal_below_simple"][1]
            separator_image_width: dp(1)
            XBoxLayout:
                orientatiom: "vertical"
                bg_color: app.colorx.card_color

            BoxLayout:
                orientation: "vertical"
                XBotnav:
                    id: botnav
                    bg_color: self.bgr_color
                    XBotnavItem:
                        name: "news"
                        text: "Newest"
                        icon: "newspaper"
                        BoxLayout:
                            orientation: "vertical"
                            XAppSearchbar:
                                text: "Search for Themes"
                                left_icon: "menu"
                                right_icon: "dots-vertical"
                                on_left_icon_release: sn.toggle_state()
                                on_right_icon_release: menu.open()
                                elevation:0
                            XTabPanel:
                                id: tab_panel
                                XTabItem:
                                    name: "tab1"
                                    text: "Themes"
                                XTabItem:
                                    name: "tab2"
                                    text: "Walpapers"
                                XTabItem:
                                    name: "tab3"
                                    text: "Icons"
                                XTabItem:
                                    name: "tab4"
                                    text: "Fonts"
                        XFab:
                            icon: "apple"
                            on_press: self.extend_button()
                            on_release: bottom_sheet.open()


                    XBotnavItem:
                        name: "podcast"
                        text: "Podcast"
                        icon: "podcast"
                        BoxLayout:
                            orientation: "vertical"
                            XAppToolbar:
                                title: "Demo App"
                                left_icon: "menu"
                                right_icon: "dots-vertical"
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


class MainApp(ScreenManager):
    pass

class TestApp(App):
    theme_style = StringProperty()
    def build(self):
        self.theme_style = "Light"
        self.colorx = Theming()
        return MainApp()


TestApp().run()
