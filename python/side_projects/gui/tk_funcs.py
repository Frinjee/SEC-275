from tkinter import *

class HideScrollbar(Scrollbar):

	def set_highs_lows(self, high, low):

		if float(low) <= 0.0 and float(high) >= 1.0:

			self.tk.call('grid', 'remove', self)
		else:
			self.grid()
		Scrollbar.set(self, high, low)