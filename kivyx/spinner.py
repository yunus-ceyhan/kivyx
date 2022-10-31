from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ColorProperty, BooleanProperty
from kivy.animation import Animation
from kivyx.theming import Theming

Builder.load_string('''
<XSpinner>:
	opacity: 1 if root.active else 0
	pos_hint: {"center_x": .5, "center_y": .5}
	disabled: False if root.active else True
	canvas.before:
		PushMatrix
		Rotate:
			angle: self._rotation_angle
			origin: self.center
	canvas:
		Color:
			rgba: self.color
			a: self._alpha
		Line:
			circle: self.center_x, self.center_y, self.width / 2, \
			self._angle_start, self._angle_end
			cap: 'square'
			width: dp(2)
	canvas.after:
		PopMatrix

''')


class XSpinner(Theming,Widget):

	determinate = BooleanProperty(False)
	determinate_time = NumericProperty(2)
	active = BooleanProperty(True)
	color = ColorProperty()

	_alpha = NumericProperty(0)
	_rotation_angle = NumericProperty(360)
	_angle_start = NumericProperty(0)
	_angle_end = NumericProperty(8)

	def __init__(self, **kwargs):
		super(XSpinner, self).__init__(**kwargs)
		self.color = self.primary_color
		self._alpha_anim_in = Animation(_alpha=1, duration=.8, t='out_quad')
		self._alpha_anim_out = Animation(_alpha=0, duration=.3, t='out_quad')
		self._alpha_anim_out.bind(on_complete=self._reset)

		if self.determinate:
			self._start_determinate()
		else:
			self._start_loop()

	def _start_determinate(self, *args):
		self._alpha_anim_in.start(self)

		_rot_anim = Animation(_rotation_angle=0,
		                      duration=self.determinate_time * .7,
		                      t='out_quad')
		_rot_anim.start(self)

		_angle_start_anim = Animation(_angle_end=360,
		                              duration=self.determinate_time,
		                              t='in_out_quad')
		_angle_start_anim.bind(on_complete=lambda *x: \
			self._alpha_anim_out.start(self))

		_angle_start_anim.start(self)

	def _start_loop(self, *args):
		if self._alpha == 0:
			_rot_anim = Animation(_rotation_angle=0,
			                      duration=2,
			                      t='linear')
			_rot_anim.start(self)

		self._alpha = 1
		self._alpha_anim_in.start(self)
		_angle_start_anim = Animation(_angle_end=self._angle_end + 270,
		                              duration=.6,
		                              t='in_out_cubic')
		_angle_start_anim.bind(on_complete=self._anim_back)
		_angle_start_anim.start(self)

	def _anim_back(self, *args):
		_angle_back_anim = Animation(_angle_start=self._angle_end - 8,
		                             duration=.6,
		                             t='in_out_cubic')
		_angle_back_anim.bind(on_complete=self._start_loop)

		_angle_back_anim.start(self)

	def on__rotation_angle(self, *args):
		if self._rotation_angle == 0:
			self._rotation_angle = 360
			if not self.determinate:
				_rot_anim = Animation(_rotation_angle=0,
				                      duration=2)
				_rot_anim.start(self)

	def _reset(self, *args):
		Animation.cancel_all(self, '_angle_start', '_rotation_angle',
		                     '_angle_end', '_alpha')
		self._angle_start = 0
		self._angle_end = 8
		self._rotation_angle = 360
		self._alpha = 0
		self.active = False

	def on_active(self, *args):
		if not self.active:
			self._reset()
		else:
			if self.determinate:
				self._start_determinate()
			else:
				self._start_loop()
