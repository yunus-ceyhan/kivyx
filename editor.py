
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty, BooleanProperty
import os
import ast
import re
from kivy.metrics import sp, dp
from kivy.uix.scrollview import ScrollView
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App
app = App.get_running_app()
#XApp.theme_cls.
from kivy.uix.boxlayout import BoxLayout
from io import StringIO
import sys
import ast
import traceback, threading
import jedi
from jedi import settings
settings.dynamic_array_additions= False
from pylint import epylint as lint
app_folder = os.path.dirname(os.path.abspath(__file__))
from kivy.utils import get_color_from_hex as hex
from kivy.uix.widget import Widget
from kivyx.icon import XIcon
from kivy.animation import Animation



#from kvdroid import keyboard_height

app_folder = os.path.dirname(os.path.abspath(__file__))


Builder.load_string("""
#:import PythonLexer kivy.extras.highlight.PythonLexer   
#:import Python3TracebackLexer pygments.lexers.python.Python3TracebackLexer
#:import Python3Lexer pygments.lexers.python.Python3Lexer
#:import hex kivy.utils.get_color_from_hex
#:import Clipboard kivy.core.clipboard.Clipboard
#:import Window kivy.core.window.Window
#:import os os
<CodeEditor>:
    orientation: "vertical"
    canvas:
        Color:
            rgba: hex("1E1E1E")
        Rectangle:
            size: self.size[0]-dp(3),self.size[1]
            pos: self.pos[0]+dp(1.5),self.pos[1]


                CodeInput:
                    id: code
                    text: root.text
                    lexer: Python3Lexer()
                    style_name: 'default'
                    auto_indent: False
                    write_tab: True 
                    bold: False           
                    #font_name: root.code_font
                    hint_text: '#py3'
                    tab_width: 4
                    size_hint: None, None
                    height: max(self.minimum_height, scroller.height)
                    width: max(root.mini_width,scroller.width)
                    font_size: root.font_size
                    text_validate_unfocus: True
                    cursor_color: app.theme_cls.secondary_text_color
                    background_color: 0,0,0,0#app.color_cls("divider_color")
                    foreground_color: app.theme_cls.secondary_text_color
                    selection_color: app.theme_cls.divider_color
                    hint_text_color: app.theme_cls.divider_color
                    on_text: root.dispatch('on_text', *args)
                    on_cursor: root.dispatch('on_cursor', *args)
                    padding: [dp(5),dp(3),dp(5),dp(3)]
                    on_touch_down: sglist.clear_widgets()
                    #on_size: root.set_lines()
                    canvas.after:
                        Color:
                            rgba: .5, .5, .5, .2
                        Line:
                            width: dp(.5)
                            rectangle: (self.pos[0]+dp(4), self.cursor_pos[1] - self.line_height, self.width-dp(8), self.line_height)



                Label:
                    id: fatal
                    text: "~~"
                    color: [1,0,0,1]
                    font_size: root.font_size
                    text_size: self.size
                    bold: True
                    size_hint: None,None
                    height: code.line_height
                    width: dp(30)
                    halign: 'center'
                    valign: 'bottom'
                    opacity: 0

                Widget:
                    id: selection
                    size_hint: None,None
                    size: 0,0
                    canvas.after:
                        Color:
                            rgba: .5,.5,.5,.5
                        Rectangle:
                            size: self.size#[0], self.line_height
                            pos: self.pos#[0], self.cursor_pos[1] - self.line_height

                FloatLayout:
                    id: floatline
                    size_hint: None,None
                    size: float.size
                    pos: float.pos


<MYLabel>:
    text: 'test'
    color: .5,.5,.5,1
    font_size: root.num_font_size 
    text_size: self.size[0]-dp(5),self.size[1]
    size_hint: None,None
    width: min(self.text_size[0]+dp(5),dp(30))
    height: root.lheight
    halign: 'right'
    valign: 'middle'
    #opacity: .6
            
<Suggest>:
    orientation: "vertical"
    size_hint_y: None
    height: dp(30)
    BoxLayout:
        Widget:
            size_hint_x: None
            width: dp(10)
        XLabel:
            text: root.text
            theme_text_color: 'Secondary'
            font_style: "Caption"
            shorten: True
            shorten_from: 'right'
            markup: True
            halign: "left"
            pos_hint: {"center_y":.5}
            md_bg_color: root.bg_color


<Line>:
    size_hint: None,None
    size: dp(.9),root.sizey
    pos: root.posx,root.posy
    canvas.after:
        Color:
            rgba: .5,.5,.5,.3
        Rectangle:
            size: self.size#[0], self.line_height
            pos: self.pos#[0], self.cursor_pos[1] - self.line_height

""")

class MButton(ButtonBehavior,XIcon):
    pass

class Line(Widget):
    posx= NumericProperty(0)
    posy= NumericProperty(0)
    sizey= NumericProperty(0)

class Suggest(ButtonBehavior, BoxLayout):
    text = StringProperty()
    bg_color = ListProperty([0, 0, 0, 0])
    complete = StringProperty()

    def __init__(self, **kwargs):
        super(Suggest, self).__init__(**kwargs)


class MYLabel(Label):
    color = ListProperty()
    num_font_size = NumericProperty()
    lheight = NumericProperty()

    def __init__(self, **kwargs):
        super(MYLabel, self).__init__(**kwargs)


class CodeEditor(BoxLayout):
    font_size = NumericProperty()
    text = StringProperty("")
    code_lines = NumericProperty()
    mini_width = NumericProperty()
    line = NumericProperty(1)
    current_row = NumericProperty()
    current_col = NumericProperty()
    current_len = NumericProperty(1)
    warning = StringProperty()
    islint = BooleanProperty(False)
    isjedi = BooleanProperty(False)
    search_index = ListProperty()
    num_index = NumericProperty(0)
    xcode = NumericProperty(0)
    ycode = NumericProperty(0)
    sc_start = NumericProperty(1)



    def __init__(self, **kwargs):
        super(CodeEditor, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.hook_keyboard)
        self.register_event_type('on_text')
        self.register_event_type('on_cursor')
        self.code_lines = len(self.ids.code._lines)
        self.font_size = sp(13)
        self.islint = False
        self.mini_width = dp(3000)
        self.symbol = [":",".","(",")","[","]",";","*","/","\\","\"","'","=","+","_","-","#","^"," "]

    def scroll_start(self,*args):
        self.sc_start = args[0]

    def scroll_move(self,*args):
        if args[0] > self.sc_start:
            if args[0] > .99:
                animation = Animation(height = dp(150),duration=0.2)
                animation.start(self.ids.bottom_bar) 
        else:
            animation = Animation(height = dp(300),duration=0.2)
            animation.start(self.ids.bottom_bar) 


    def search_plus(self,*args):
        if self.num_index < len(self.search_index)-1:
            self.num_index += 1
        if self.search_index:
            try:
                self.ids.search_label.text = self.search_index[self.num_index]["s_l"]
                self.ids.scroller.scroll_y = self.search_index[self.num_index]["s_y"]
                self.ids.scroller.scroll_x = self.search_index[self.num_index]["s_x"]
                self.ids.selection.pos = self.search_index[self.num_index]["s_p"]
                self.ids.selection.size = self.search_index[self.num_index]["s_s"]
            except Exception as e:
                print(e,self.num_index)
        
        
    def search_minus(self,*args):
        if self.num_index > 0:
            self.num_index -= 1
        if self.search_index:
            try:
                self.ids.search_label.text = self.search_index[self.num_index]["s_l"]
                self.ids.scroller.scroll_y = self.search_index[self.num_index]["s_y"]
                self.ids.scroller.scroll_x = self.search_index[self.num_index]["s_x"]
                self.ids.selection.pos = self.search_index[self.num_index]["s_p"]
                self.ids.selection.size = self.search_index[self.num_index]["s_s"]
            except Exception as e:
                print(e,self.num_index)

    def on_text_search(self,*args):
        self.search_index = []
        index = [] 
        self.num_index = 0
        for n, t in enumerate(self.ids.code.text.splitlines()):
            if args[0] in t:
                index.append([n+1,t.index(args[0])])
        if index:
            for r in range(len(index)):
                col = index[r][0]
                row = index[r][1]
                y = max(0,1.0 -((1.0/len(self.ids.code._lines))*col))
                try:
                    s = self.ids.code._lines[col].split(self.ids.search_input.text)
                except:
                    s =[]
                if s:
                    l = len(s[0])
                else:
                    l = 0
                try:
                    x = min(0,1.0 - (1.0/ ((len(self.ids.code._lines[col])+1)*l)))
                except:
                    x = 0.0
                try:
                    s_p = ((self.ids.code._lines_labels[col].width / len(self.ids.code._lines[col]))* row, self.ids.num.children[len(self.ids.num.children)-col].pos[1])
                except:
                    s_p = (0,0)
                try:
                    s_s = ((self.ids.code._lines_labels[col].width / len(self.ids.code._lines[col]))*len(self.ids.search_input.text),self.ids.code.line_height)
                except:
                    s_s = (0,0)
                s_l = str(r+1)+"/"+str(len(index))
                self.search_index.append({"s_x":x,"s_y":y,"s_p":s_p,"s_s":s_s,"s_l":s_l })
            try:
                self.ids.search_label.text = self.search_index[0]["s_l"]
                self.ids.scroller.scroll_y = self.search_index[0]["s_y"]
                self.ids.scroller.scroll_x = self.search_index[0]["s_x"]
                self.ids.selection.pos = self.search_index[0]["s_p"]
                self.ids.selection.size = self.search_index[0]["s_s"]
            except Exception as e:
                print(e)
        else:
            self.ids.search_label.text = "0/0" 
           

    def on_cursor(self, instance, newPos):       
        self.xcode = 0
        self.ycode = 0
        Clock.schedule_once(self.set_cursor_history, 1)
        if not (isinstance(self.ids.scroller, ScrollView) and self.ids.code.multiline):
            return super(self.ids.code, self).on_cursor(instance, newPos)
        if newPos[0] == 0:
            self.ids.scroller.scroll_x = 0
            self.xcode = 0
        else:
            over_width = self.ids.code.width - self.ids.scroller.width
            if over_width <= 0.0:
                over_width = 0.1
            view_start = over_width * self.ids.scroller.scroll_x
            view_end = view_start + self.ids.scroller.width
            offset = self.ids.code.cursor_offset()
            desired_view_start = offset - 5
            desired_view_end = offset + \
                self.ids.code.padding[0] + self.ids.code.padding[2] + \
                self.ids.code.cursor_width + 5
            if desired_view_start < view_start:
                self.ids.scroller.scroll_x = max(
                    0, desired_view_start / over_width)

            elif desired_view_end > view_end:
                self.ids.scroller.scroll_x = min(
                    1, (desired_view_end - self.ids.scroller.width) / over_width)

            if desired_view_start < view_start:
                self.xcode = 0
            elif desired_view_end > view_end - (self.ids.autoscrl.width+dp(2)):
                self.xcode = 1

        if newPos[1] == 1.01:
            self.ids.scroller.scroll_y = 1
            
        else:
            over_height = self.ids.code.height - self.ids.scroller.height
            if over_height <= 0.0:
                over_height = 0.1
            view_start1 = over_height * self.ids.scroller.scroll_y
            view_end1 = view_start1 + self.ids.scroller.height
            offset1 = self.ids.code.cursor_pos[1]
            desired_view_start1 = offset1 - self.ids.code.line_height
            desired_view_end1 = offset1 + \
                self.ids.code.padding[1] + self.ids.code.padding[3] + \
                self.ids.code.line_height 
            if desired_view_start1 < view_start1:
                self.ids.scroller.scroll_y = max(0, desired_view_start1 / over_height)
            elif desired_view_end1 > view_end1:
                try:
                    self.ids.scroller.scroll_y = min(
                        1, (desired_view_end1 - self.ids.scroller.height) / over_height)
                except:
                    pass
            if desired_view_start1 < view_start1:
                self.ycode = 0
            elif desired_view_end1 > view_end1 - (dp(130)-(self.ids.code.line_height)):
                self.ycode = 1
            else:
                self.ycode = 0    
        self.color_numpad()    

    def on_text(self, instance, newText):
        self.abs = []

        def addnum(num):
            nums = [0]
            temp = {}
            
            for n,i in enumerate(self.ids.code._lines):
                if i.startswith(" "*(num+1)):
                    if nums[0] == 0:
                        nums = []
                        nums.append(n)
                    else:
                        if n-1 in nums:
                            nums.append(n)
                        else:
                            #nums.append(n)
                            temp[num] = nums
                            nums = [0]
                            if len(temp) > 0:
                                self.abs.append(temp)
                                temp = {}
                else:
                    match = re.findall('^.', i)
                    if match:
                        temp[num] = nums
                        nums = [0]
                        if len(temp) > 0:
                            self.abs.append(temp)
                            temp = {}
                    else:
                        nums.append(n)

            if len(nums) > 0:
                #nums.append(n)
                temp[num] = nums
                if len(temp) > 0:
                    self.abs.append(temp)
                    temp = {}
        space = 0
        for i in self.ids.code._lines:
            if i.startswith(" "):
                if len(re.findall("^\s+",i)[0]) > space:
                    space = len(re.findall("^\s+",i)[0])
        colum = list(range(4,space,4))
        for num in colum:
            addnum(num)
        

    def set_lines(self,*args):
        self.ids.floatline.clear_widgets()
        if len(self.abs) > 0:
            for i in self.abs:
                for d in i.keys():
                    if len(i[d]) > 0:
                        h = len(i[d])
                        size_y = (h)*self.ids.code.line_height
                        try:
                            pos_y = self.ids.num.children[(len(self.ids.num.children) - i[d][0])].pos[1] - ((h)*self.ids.code.line_height)
                        except:
                            pos_y = 0
                        try:
                            pos_x = ((self.ids.code._lines_labels[i[d][0]].width/len(self.ids.code._lines[i[d][0]]))*d)+(self.ids.code._lines_labels[i[d][0]].width/len(self.ids.code._lines[i[d][0]])) 
                        except:
                            pos_x = 0
                        if pos_x != 0 and pos_y != 0:
                            line = Line(posx = pos_x,
                                            posy = pos_y,
                                            sizey = size_y)
                            self.ids.floatline.add_widget(line,index = 0)
        self.abs = []



    def set_cursor_history(self, *args):
        self.current_row = self.ids.code.cursor_row
        self.current_col = self.ids.code.cursor_col
        self.current_len = len(self.ids.code._lines)

    def hook_keyboard(self, window, key, *largs):
        Clock.schedule_once(self.set_lines,0.1)
        with open(app_folder+'/temp.py', 'w') as f:
            f.write(self.ids.code.text)
            f.close()
        try:
            self.warning = ""
            self.ids.fatal.opacity = 0
            self.ids.num.children[len(self.ids.num.children)-self.line].color = .5,.5,.5,1
        except:
            pass
        if key == 13:
            if "\t" in self.ids.code.text:
                self.ids.code.text = self.ids.code.text.replace("\t","    ")
            try:
                space = re.findall("^\s+", self.ids.code._lines[self.current_row])[0]
            except:
                space = ""
            if len(self.ids.sglist.children) > 0:
                try:
                    self.ids.code.do_backspace()
                    self.ids.code.do_backspace()
                    self.ids.code.insert_text(
                        self.ids.sglist.children[0].complete)
                    self.ids.sglist.clear_widgets()
                except:
                    pass
            else:
                if self.ids.code._lines[self.current_row].strip().endswith(':'):
                    self.ids.code.insert_text(space+"    ")
                else:
                    self.ids.code.insert_text(space)
            if self.ids.code._lines_labels[self.ids.code.cursor_row-1].width > 1:
                self.tlint = threading.Thread(target = self.get_error)
                self.tlint.daemon = True
                if self.islint == False:
                    self.islint = True
                    self.tlint.start()

        elif key in range(33, 250):
            match = re.findall('^[a-zA-Z]+', chr(key))
            if match:
                self.ids.sglist.clear_widgets()
                self.tjedi = threading.Thread(target = self.get_comp,args= (self.ids.code.text,self.ids.code.cursor_col,self.ids.code.cursor_row+1,),)
                self.tjedi.deamon = True
                if self.isjedi == False:
                    self.isjedi = True
                    self.tjedi.start()
            else:
                self.ids.sglist.clear_widgets()

        else:
            self.ids.sglist.clear_widgets()

        if len(self.ids.num.children) != len(self.ids.code._lines):
            self.text_changed()

    def get_error(self,*args):
            pylint_opts = app_folder+'/temp.py --msg-template=|{line}&{msg}$ --jobs=0 --output-format=parseable'
            (pylint_stdout, pylint_stderr) = lint.py_run(pylint_opts ,return_std=True)
            result = pylint_stdout.getvalue().split("|")
            text = ""
            if len(result) == 2:
                self.line = int(result[-1].split("$")[0].split("&")[0])
                self.color_number()
                text = " "+result[-1].split("$")[0].replace("&"," - ")+"\n\n"
                self.ids.output2.text = text
                self.ids.pr_tab.text = f"PROBLEMS {len(text.splitlines())-1}" if len(text.splitlines())-1 > 0 else "PROBLEMS"

            elif len(result) > 2:
                for i in result[1:-1]:
                    text += i.replace("&"," - ").replace("$","")
                self.ids.output2.text = " "+text
                self.ids.pr_tab.text = f"PROBLEMS {len(text.splitlines())-1}" if len(text.splitlines())-1 > 0 else "PROBLEMS"
            else:
                self.ids.output2.text = ""
            self.islint = False

 #               self.warning = result[-1].split("$")[0].split("&")[1]
 #               self.line = int(result[-1].split("$")[0].split("&")[0])
 #               self.color_number()

    def get_comp(self, source,line,colum):
        self.ids.sglist.clear_widgets()
        try:
            script = jedi.Script(source, path=app_folder+'/temp.py')
            completions = script.complete(colum,line)[:10]
            if completions:
                for a in completions:
                    self.ids.sglist.add_widget(
                        Suggest(text=a.name,complete = a.complete, on_release = self.insert_suggest))
            self.isjedi = False
        except Exception as e:
            print(e)
     
    def color_numpad(self,*args):
        self.ids.lr.text = f"Ln {self.ids.code.cursor_row+1}"
        self.ids.lc.text = f"Col {self.ids.code.cursor_col+1}"
        try:
            for i in self.ids.num.children:
                i.color = .5,.5,.5,1
            self.ids.num.children[len(self.ids.num.children)-self.ids.code.cursor_row-1].color = .9,.9,.9,.8
        except:
            pass
    def color_number(self, *args):
        self.ids.fatal.pos = self.ids.code._lines_labels[self.line-1].width+dp(
            5), self.ids.num.children[len(self.ids.num.children)-self.line].pos[1]
        self.ids.fatal.opacity = 1
        self.ids.num.children[len(self.ids.num.children)-self.line].color = 1,0,0,1

    def insert_suggest(self, *args):
        self.ids.code.do_backspace()
        self.ids.code.insert_text(args[0].complete)
        self.ids.sglist.clear_widgets()
        self.ids.code.focus = True

    def text_changed(self, *args):
        Clock.schedule_once(self.change, 0.01)

    def change(self, *args):
        os.chdir(app_folder)
        if len(self.ids.code._lines) != self.code_lines :
            self.col = len(self.ids.code._lines)
            self.ids.num.clear_widgets()
            for i in range(self.col):
                label = MYLabel(text=str(
                    i+1), num_font_size=self.font_size, lheight=self.ids.code.line_height)
                self.ids.num.add_widget(label)
            self.code_lines = len(self.ids.code._lines)

    def insert(self, *args):
        self.ids.code.re_indent
        # self.ids.code.insert_text("\t")

class PythonIDE(App):


    def build(self):
        self.theme_style = "Dark"
        return CodeEditor()

    def color_cls(self,color):
        colors ={"bg_normal":"22243B",
                        "bg_dark": "21233B",
                        "divider_color": "2F2F56",
                        "bg_light":"7970C3",
                        "icons_color":"56598B",
                        "selection_color": "2B2C49",
                        "warning_color":"FFDC81"}
        return hex(colors[color])


if __name__ == "__main__":
    PythonIDE().run()