from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage
from kivy.properties import ListProperty
from kivy.loader import Loader
Loader.loading_image = './kivyx/data/loading.png'
Loader.error_image = './kivyx/data/loading.png'
Loader.max_upload_per_frame = 10
Loader.num_workers = 10

Builder.load_string("""
<XImage>:
    keep_ratio: False
    allow_stretch: True
    canvas.before:
        StencilPush
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius
        StencilUse
    canvas.after:
        StencilUnUse
        StencilPop

<XGifImage>:
    anim_delay: 0.03
    mipmap: True
    keep_ratio: False
    allow_stretch: True
    canvas.before:
        StencilPush
        RoundedRectangle:
            pos: self.pos[0]-dp(2) ,self.pos[1] + dp(1)
            size: self.size[0],self.size[1]
            radius: root.radius
        StencilUse
    canvas.after:
        StencilUnUse
        StencilPop

<XUrlImage>:
    keep_ratio: False
    allow_stretch: True
    canvas.before:
        StencilPush
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius
        StencilUse
    canvas.after:
        StencilUnUse
        StencilPop

""")

class XImage(Image):
    radius = ListProperty([0,])

class XGifImage(Image):
    radius = ListProperty([0,])

class XUrlImage(AsyncImage):
    radius = ListProperty([0,])