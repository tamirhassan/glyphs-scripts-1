# MenuTitle: Auto-name Instances
# -*- coding: utf-8 -*-

__doc__ = """
Names active instances based on set weight and width classes and user-defined exceptions.
"""

import vanilla


class AutoNamer:
	def __init__(self):

		self.font = Font

		self.widthExceptions = {}
		self.selectedWidthClass = None
		self.widths = []

		self.weightExceptions = {}
		self.selectedWeightClass = None
		self.weights = []

		self.exceptionName = None

		self.widthButtonList = []
		self.weightButtonList = []

		self.ypos = 0

		if Glyphs.defaults["com.eweracs.AutoNameInstances.exceptionprefs"]:
			for key in Glyphs.defaults["com.eweracs.AutoNameInstances.exceptionprefs"]:
				self.widthExceptions[key] = Glyphs.defaults["com.eweracs.AutoNameInstances.exceptionprefs"][key]

		self.update_widths()

		self.w = vanilla.FloatingWindow((0, 0), "Auto-name Instances")

		setattr(self.w, "widthExceptionsTitle", vanilla.TextBox((10, 10, -10, 14), "Add width name exceptions",
		                                                        sizeStyle="small"))

		setattr(self.w, "addWidthException", vanilla.PopUpButton((10, self.ypos, 140, 20), self.widths,
		        callback=self.pick_exception_from_list))
		setattr(self.w, "addWidthArrow", vanilla.TextBox((160, self.ypos, -10, 14), u"\u2192", sizeStyle="regular"))
		setattr(self.w, "addWidthName", vanilla.EditText((190, self.ypos - 1, 130, 22), callback=self.exception_name))
		setattr(self.w, "addWidthButton", vanilla.Button((330, self.ypos, 50, 20), "Add", callback=self.add))

		setattr(self.w, "divider", vanilla.HorizontalLine((10, self.ypos, -10, 1)))

		setattr(self.w, "weightExceptionsTitle", vanilla.TextBox((10, self.ypos, -10, 14), "Add weight name exceptions",
		                                                        sizeStyle="small"))

		setattr(self.w, "addWeightException", vanilla.PopUpButton((10, self.ypos, 140, 20), self.widths,
		                                                         callback=self.pick_exception_from_list))
		setattr(self.w, "addWeightArrow", vanilla.TextBox((160, self.ypos, -10, 14), u"\u2192", sizeStyle="regular"))
		setattr(self.w, "addWName", vanilla.EditText((190, self.ypos - 1, 130, 22), callback=self.exception_name))
		setattr(self.w, "addWidthButton", vanilla.Button((330, self.ypos, 50, 20), "Add", callback=self.add))

		setattr(self.w, "weightExceptionsTitle", vanilla.TextBox((10, self.ypos, -10, 14), "Add weight name exceptions",
		                                                         sizeStyle="small"))

		setattr(self.w, "autoname", vanilla.Button((10, self.ypos, -10, 20), "Auto-name instances",
		                                           callback=self.auto_name_instances))

		self.redraw()

		self.w.setDefaultButton(self.w.autoname)

		self.w.open()
		self.w.makeKey()

	def pick_exception_from_list(self, sender):
		self.selectedWidthClass = self.widths[sender.get()]

	def exception_name(self, sender):
		self.exceptionName = sender.get()

	def add(self, sender):
		if self.exceptionName is not None:
			self.widthExceptions[self.selectedWidthClass] = self.exceptionName
		self.update_widths()
		self.redraw()
		Glyphs.defaults["com.eweracs.AutoNameInstances.exceptionprefs"] = self.widthExceptions

	def clear(self, sender):
		for i, item in enumerate(self.widthButtonList):
			if item is sender:
				del self.widthExceptions[list(self.widthExceptions.items())[i][0]]
		self.update_widths()
		self.redraw()
		Glyphs.defaults["com.eweracs.AutoNameInstances.exceptionprefs"] = self.widthExceptions

	def redraw(self):
		try:
			for i in range(len(self.widthButtonList)):
				delattr(self.w, str(i) + "width")
				delattr(self.w, str(i) + "arrow")
				delattr(self.w, str(i) + "exception")
				delattr(self.w, str(i) + "button")

		except Exception as e:
			print(e)

		self.ypos = 34

		self.widthButtonList = []

		for i in range(len(self.widthExceptions)):
			width = vanilla.TextBox((10, self.ypos, -10, 17), list(self.widthExceptions)[i])
			widtharrow = vanilla.TextBox((160, self.ypos, -10, 14), u"\u2192", sizeStyle="regular")
			widthexception = vanilla.TextBox((190, self.ypos, 130, 22), list(self.widthExceptions.items())[i][1])
			widthbutton = vanilla.Button((330, self.ypos, 50, 20), "Clear", callback=self.clear)

			setattr(self.w, str(i) + "width", width)
			setattr(self.w, str(i) + "arrow", widtharrow)
			setattr(self.w, str(i) + "exception", widthexception)
			setattr(self.w, str(i) + "button", widthbutton)

			self.widthButtonList.append(widthbutton)

			self.ypos = widthbutton.getPosSize()[1] + 32

		self.w.addException.show(len(self.widths) > 0)
		self.w.addArrow.show(len(self.widths) > 0)
		self.w.addName.show(len(self.widths) > 0)
		self.w.addButton.show(len(self.widths) > 0)

		self.w.addException.setItems(self.widths)
		self.w.addName.set("")

		self.w.addException.setPosSize((10, self.ypos, 140, 20))
		self.w.addArrow.setPosSize((160, self.ypos, -10, 14))
		self.w.addName.setPosSize((190, self.ypos - 1, 130, 22))
		self.w.addButton.setPosSize((330, self.ypos, 50, 20))

		if len(self.widths) > 0:
			self.ypos += 32

		self.w.divider.setPosSize((10, self.ypos, -10, 1))

		self.ypos += 14

		self.w.weightExceptionsTitle.setPosSize((10, self.ypos, -10, 14))

		self.ypos += 24

		for i in range(len(self.weightExceptions)):
			weight = vanilla.TextBox((10, self.ypos, -10, 17), list(self.weightExceptions)[i])
			weightarrow = vanilla.TextBox((160, self.ypos, -10, 14), u"\u2192", sizeStyle="regular")
			weightexception = vanilla.TextBox((190, self.ypos, 130, 22), list(self.weightExceptions.items())[i][1])
			weightbutton = vanilla.Button((330, self.ypos, 50, 20), "Clear", callback=self.clear)

			setattr(self.w, str(i) + "weight", weight)
			setattr(self.w, str(i) + "arrow", weightarrow)
			setattr(self.w, str(i) + "exception", weightexception)
			setattr(self.w, str(i) + "button", weightbutton)

			self.weightButtonList.append(weightbutton)

			self.ypos = weightbutton.getPosSize()[1] + 32

		self.w.addWeightException.show(len(self.weights) > 0)
		self.w.addWeightArrow.show(len(self.weights) > 0)
		self.w.addWeightName.show(len(self.weights) > 0)
		self.w.addWeightButton.show(len(self.weights) > 0)

		self.w.addWeightException.setItems(self.weights)
		self.w.addWeightName.set("")

		self.w.addWeightException.setPosSize((10, self.ypos, 140, 20))
		self.w.addWeightArrow.setPosSize((160, self.ypos, -10, 14))
		self.w.addWeightName.setPosSize((190, self.ypos - 1, 130, 22))
		self.w.addWeightButton.setPosSize((330, self.ypos, 50, 20))

		if len(self.weights) > 0:
			self.ypos += 32

		self.w.autoname.setPosSize((10, self.ypos, -10, 20))

		self.w.resize(390, self.ypos + 32)

	def update_widths(self):
		self.widths = [width for width in [
			"Ultra Condensed",
			"Extra Condensed",
			"Condensed",
			"SemiCondensed",
			"Medium (normal)",
			"Semi Expanded",
			"Expanded",
			"Extra Expanded",
			"Ultra Expanded"
		] if width not in self.widthExceptions]

		if len(self.widths) > 0:
			self.selectedWidthClass = self.widths[0]

	def update_weights(self):
		self.weights = [weight for weight in [
			"Thin",
			"UltraLight",
			"ExtraLight",
			"Light",
			"Normal",
			"Regular",
			"Medium",
			"DemiBold",
			"SemiBold",
			"Bold",
			"UltraBold",
			"ExtraBold",
			"Black",
			"Heavy"
		] if weight not in self.weightExceptions]

	def auto_name_instances(self, sender):
		if self.font is None:
			Message("Open a font file!", title="Error")

		self.w.close()

		for i in self.font.instances:
			if i.active:
				if str(Glyphs.versionNumber)[0] == "3":  # Glyphs 3
					weight_name = i.weightClassName
					width_name = i.widthClassName
					if "Medium" in i.widthClassName and "Medium" not in self.widthExceptions:
						width_name = ""
					if i.widthClassName in self.widthExceptions:
						width_name = self.widthExceptions[i.widthClassName]
					if i.weightClassName == "Regular" or i.weightClassName == "Normal":
						weight_name = ""
					if len(weight_name) > 1 and len(width_name) > 1:
						i.name = " ".join([weight_name, width_name])
					elif len(weight_name) > 1:
						i.name = weight_name
					elif len(width_name) > 1:
						i.name = width_name
					if i.name == "":
						i.name = "Regular"
					if i.isItalic:
						i.name += " Italic"
				else:  # Glyphs 2
					weight_name = i.weight
					width_name = i.width
					if "Medium" in i.width and "Medium" not in self.widthExceptions:
						width_name = ""
					if i.width in self.widthExceptions:
						width_name = self.widthExceptions[i.width]
					if i.weight == "Regular" or i.weight == "Normal":
						weight_name = ""
					if len(weight_name) > 1 and len(width_name) > 1:
						i.name = " ".join([weight_name, width_name])
					elif len(weight_name) > 1:
						i.name = weight_name
					elif len(width_name) > 1:
						i.name = width_name
					if i.name == "":
						i.name = "Regular"
					if i.isItalic:
						i.name += " Italic"


AutoNamer()
