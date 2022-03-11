from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.metrics import dp

Builder.load_string("""
<XRcBoxList>:
    bar_color: 0,0,0,0
    bar_width: dp(0)
    RecycleBoxLayout:
        spacing:  root.spacing
        default_size_hint: 1, None
        default_size: 1, root.exact_height
        size_hint_y: None
        height: max(self.minimum_height, root.max_height)
        orientation: 'vertical'
        padding: root.padding
        
<XRcGridList>:
    bar_color: 0,0,0,0
    bar_width: dp(0)
    RecycleGridLayout:
        cols: root.cols
        spacing:  root.spacing
        default_size_hint: 1, None
        default_size: 1, root.exact_height
        size_hint_y: None
        height: max(self.minimum_height, root.max_height)
        orientation: root.orientation
        padding: root.padding

""")

class XRcBoxList(RecycleView):
    max_height = NumericProperty()
    exact_height = NumericProperty("56dp")
    spacing = NumericProperty("10dp")
    padding = ListProperty([dp(15),])
    def __init__(self, **kwargs):
        super(XRcBoxList, self).__init__(**kwargs)
        self.data = []
        
class XRcGridList(RecycleView):
    orientation = StringProperty("lr-tb")
    max_height = NumericProperty()
    exact_height = NumericProperty("56dp")
    cols = NumericProperty(1)
    spacing = NumericProperty("10dp")
    padding = ListProperty([dp(15),])
    def __init__(self, **kwargs):
        super(XRcGridList, self).__init__(**kwargs)
        self.data = []