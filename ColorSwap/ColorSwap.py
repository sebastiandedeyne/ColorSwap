import sublime, sublime_plugin
import string

class ColorswapCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				colorInput = self.view.substr(region)
				output = ""

				if (colorInput[0:3] == "rgb"):
					colorInput = colorInput[4:len(colorInput)-1]
					array = string.split(colorInput,',')
					output = "#"
					for x in array:
						x = hex(int(x))[2:]
						if (len(x) == 1):
							x = "0" + x
						output += x
				elif (colorInput[0] == "#"):
					colorInput = colorInput[1:]
					if (len(colorInput) == 6):
						array = [colorInput[i:i+2] for i in range(0, len(colorInput), 2)]
					else:
						array = list(colorInput)
					output = "rgb("
					for x in array:
						if (len(x) == 1):
							x += x
						x = str(int("0x" + x, 0)) + ","
						output += x
					output = output[0:-1]
					output += ")"

				self.view.replace(edit, region, output)