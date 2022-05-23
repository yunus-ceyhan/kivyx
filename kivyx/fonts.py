from kivy.core.text import LabelBase

from kivyx import fonts_path

fonts = [
    {
        "name": "Roboto",
        "fn_regular": fonts_path + "Roboto-Regular.ttf",
        "fn_bold": fonts_path + "Roboto-Bold.ttf",
        "fn_italic": fonts_path + "Roboto-Italic.ttf",
        "fn_bolditalic": fonts_path + "Roboto-BoldItalic.ttf",
    },
    {
        "name": "RobotoThin",
        "fn_regular": fonts_path + "Roboto-Thin.ttf",
        "fn_italic": fonts_path + "Roboto-ThinItalic.ttf",
    },
    {
        "name": "RobotoLight",
        "fn_regular": fonts_path + "Roboto-Light.ttf",
        "fn_italic": fonts_path + "Roboto-LightItalic.ttf",
    },
    {
        "name": "RobotoMedium",
        "fn_regular": fonts_path + "Roboto-Medium.ttf",
        "fn_italic": fonts_path + "Roboto-MediumItalic.ttf",
    },
    {
        "name": "RobotoBlack",
        "fn_regular": fonts_path + "Roboto-Black.ttf",
        "fn_italic": fonts_path + "Roboto-BlackItalic.ttf",
    },

]

for font in fonts:
    LabelBase.register(**font)
