from kivy.core.text import LabelBase
from kivyx.iso import iso_codes
from kivy.utils import platform
import os
import xml.etree.ElementTree as ET

FONT_PATH = os.path.join("/", "system", "fonts/")
FONT_XML_PATHS = [os.path.join("/", "system", "etc", "fonts.xml"), os.path.join("/", "system", "etc", "system_fonts.xml")]
FONT_DICT = {}

from kivyx import fonts_path

fonts = [
    {
        "name": "regular",
        "fn_regular": fonts_path + "Roboto-Regular.ttf",
        "fn_bold": fonts_path + "Roboto-Bold.ttf",
        "fn_italic": fonts_path + "Roboto-Italic.ttf",
        "fn_bolditalic": fonts_path + "Roboto-BoldItalic.ttf",
    },
    {
        "name": "thin",
        "fn_regular": fonts_path + "Roboto-Thin.ttf",
        "fn_italic": fonts_path + "Roboto-ThinItalic.ttf",
    },
    {
        "name": "light",
        "fn_regular": fonts_path + "Roboto-Light.ttf",
        "fn_italic": fonts_path + "Roboto-LightItalic.ttf",
    },
    {
        "name": "medium",
        "fn_regular": fonts_path + "Roboto-Medium.ttf",
        "fn_italic": fonts_path + "Roboto-MediumItalic.ttf",
    },
    {
        "name": "black",
        "fn_regular": fonts_path + "Roboto-Black.ttf",
        "fn_italic": fonts_path + "Roboto-BlackItalic.ttf",
    },

]

for font in fonts:
    LabelBase.register(**font)

def device_lang():
    if platform == "android":
        from jnius import autoclass
        Locale = autoclass('java.util.Locale')
        context = autoclass('org.kivy.android.PythonActivity').mActivity
        resources = context.getResources()
        config = resources.getConfiguration()
        locale = config.locale
        return locale.getLanguage()
    else:
        return "en"

def system_font(language=None):
    if not language:
        language = device_lang()
    else:
        language = language.split("-")[0]
    if language.lower() in iso_codes.keys():
        if iso_codes[language.lower()] in FONT_DICT.keys():
            return FONT_DICT[iso_codes[language.lower()]]
        else:
            return "Roboto"
    else:
        raise ValueError(
            "The language definition must be in iso639-1 or iso639-2 code formats such as 'en' or 'eng'")

def is_font_exist(font):
    if os.path.isfile(os.path.join(FONT_PATH, font)):
        return font
        
def register_font(lang, name, font):
    if not lang in FONT_DICT.keys():
        LabelBase.register(name= name,
                            fn_regular=FONT_PATH + font,
                            fn_bold= None,
                            fn_italic= None,
                            fn_bolditalic= None)
        FONT_DICT[lang] = name

if platform == "android":
    for font_xml_path in FONT_XML_PATHS:
        if os.path.exists(font_xml_path):
            tree = ET.parse(font_xml_path)
            root = tree.getroot()
            lang_families = [item for item in root.findall("family") if item and 'lang' in item.attrib]

            for family in lang_families:
                lang_code = family.attrib["lang"]
                if lang_code == "ja":
                    lang_code = "Jpan"
                elif lang_code == "ko":
                    lang_code = "Kore"
                else:
                    lang_code = lang_code.split("-")[1].split(",")[0].strip()
                font_elements = family.findall("font")
                if font_elements:
                    font_name = font_elements[0].text.strip()
                    if is_font_exist(font_name):
                        name = font_name.split(".")[0].split("-")[0]
                        register_font(lang_code,name,font_name)
