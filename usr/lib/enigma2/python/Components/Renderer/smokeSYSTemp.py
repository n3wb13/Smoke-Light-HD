from Components.VariableText import VariableText
from enigma import eLabel
from Renderer import Renderer
from os import path, popen

class smokeSYSTemp(Renderer, VariableText):
	def __init__(self):
		Renderer.__init__(self)
		VariableText.__init__(self)
		
	GUI_WIDGET = eLabel

	def changed(self, what):
		if not self.suspended:
			smokeSYSTemp = "-- "
			try:
				if path.exists('/proc/stb/sensors/temp0/value'):
					out_line = popen("cat /proc/stb/sensors/temp0/value").readline()
					smokeSYSTemp = out_line.replace('\n', '')
				elif path.exists('/proc/stb/fp/temp_sensor'):
					out_line = popen("cat /proc/stb/fp/temp_sensor").readline()
					smokeSYSTemp = out_line.replace('\n', '')
				if not smokeSYSTemp == "-- " and len(smokeSYSTemp) > 2:
					smokeSYSTemp = smokeSYSTemp[:2]
			except:
				pass
			self.text = smokeSYSTemp + str('\xc2\xb0') + "C"
			
	def onShow(self):
		self.suspended = False
		self.changed(None)

	def onHide(self):
		self.suspended = True

