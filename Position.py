from math import sin, cos, radians, acos

class CalculationPosition:
	def __init__(self, Length, Width, Angle, StepX = 0, StepY = 0):
		self.Length = Length
		self.Width = Width
		self.Angle = Angle
		self.StepX = StepX
		self.StepY = StepY

	def define_сoordinates_contour(self):
		self.Diagonal = (((self.Width/2)**2 + (self.Length/2)**2)**0.5)*2
		if -self.Angle != 0:
			AngleDiagonal = (radians(-self.Angle) -
						acos((self.Length/2)/(self.Diagonal/2)))
			self.x1 = sin(AngleDiagonal)*(self.Diagonal/2) + self.StepX
			self.y1 = cos(AngleDiagonal)*(self.Diagonal/2) + self.StepY
			self.x2 = cos(AngleDiagonal)*(self.Diagonal/2) + self.StepX
			self.y2 = sin(AngleDiagonal)*(self.Diagonal/2) + self.StepY
			self.x3 = -sin(AngleDiagonal)*(self.Diagonal/2) + self.StepX
			self.y3 = -cos(AngleDiagonal)*(self.Diagonal/2) + self.StepY
			self.x4 = -cos(AngleDiagonal)*(self.Diagonal/2) + self.StepX
			self.y4 = -sin(AngleDiagonal)*(self.Diagonal/2) + self.StepY
		else:
			self.x1 = -self.Length/2 + self.StepX
			self.y1 = self.Width/2 + self.StepY
			self.x2 = self.Length/2 + self.StepX
			self.y2 = self.Width/2 + self.StepY
			self.x3 = self.Length/2 + self.StepX
			self.y3 = -self.Width/2 + self.StepY
			self.x4 = -self.Length/2 + self.StepX
			self.y4 = -self.Width/2 + self.StepY
		self.point1 = (self.x1, self.y1)
		self.point2 = (self.x2, self.y2)
		self.point3 = (self.x3, self.y3)
		self.point4 = (self.x4, self.y4)
		self.Coordinates = [self.point1, self.point2, self.point3, self.point4]
		return self.Coordinates

	def get_text_metrics(self, Size):
		if self.Length >= Size:
			self.SizeText = Size
		else:
			self.SizeText = self.Length
		# tk_root = Tkinter.Tk()
		# font = tkFont.Font(family = 'GOST type A (plotter)', size = self.SizeText, slant = "italic")
		self.WithText = 50 #(font.measure(self.TextKompas))

		return (self.SizeText, self.WithText)

	def define_сoordinates_text(self):
		if self.Angle < 0:
			self.xText = -sin(radians(-self.Angle)) * self.SizeText/2 - sin(radians(-self.Angle)) * self.WithText/2 + self.StepX
			self.yText = -cos(radians(-self.Angle)) * self.SizeText/2 + cos(radians(-self.Angle)) * self.WithText/2 + self.StepY
		elif self.Angle > 0:
			self.xText = cos(radians(-self.Angle)) * self.SizeText/2 + sin(radians(-self.Angle)) * self.WithText/2 + self.StepX
			self.yText = -cos(radians(-self.Angle)) * self.SizeText/2 - cos(radians(-self.Angle)) * self.WithText/2 + self.StepY
		else:
			self.xText = +self.SizeText/2 + self.StepX
			self.yText = -self.WithText/2 + self.StepY
		self.CoordinatesText = (self.xText, self.yText)
		return self.CoordinatesText

	def direction_text(self, Top = 0, Down = 0, Left = 0, Right = 0):
		if self.Angle > 0:
			if Top != 0:
				self.xdText += sin(radians(-self.Angle)) * Top
				self.ydText += cos(radians(-self.Angle)) * Top
			if Down != 0:
				self.xdText += -sin(radians(-self.Angle)) * Down
				self.ydText += -cos(radians(-self.Angle)) * Down
			if Left != 0:
				self.xdText += sin(radians(-self.Angle)) * Left
				self.ydText += -cos(radians(-self.Angle)) * Left
			if Right != 0:
				self.xdText += -sin(radians(-self.Angle)) * Right
				self.ydText += cos(radians(-self.Angle)) * Right
		elif self.Angle < 0:
			if Top != 0:
				self.xdText += sin(radians(-self.Angle)) * Top
				self.ydText += cos(radians(-self.Angle)) * Top
			if Down != 0:
				self.xdText += -sin(radians(-self.Angle)) * Down
				self.ydText += -cos(radians(-self.Angle)) * Down
			if Left != 0:
				self.xdText += -sin(radians(-self.Angle)) * Left
				self.ydText += cos(radians(-self.Angle)) * Left
			if Right != 0:
				self.xdText += sin(radians(-self.Angle)) * Right
				self.ydText += -cos(radians(-self.Angle)) * Right	
		else:
			if Top != 0:
				self.xdText += Top
			if Down != 0:
				self.xdText += -Down
			if Left != 0:
				self.ydText += -Left
			if Right != 0:
				self.ydText += Right
		return (self.xdText, self.ydText)