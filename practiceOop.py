class Robot:
	#attributes
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self. weight = weight
	#behavior
	def introduce_self(self):
		print("hi my name is " + self.name, '\n'
		"my favorite color is", self.color,'\n'
		"i weigh approximately", self.weight )
		
#instantiated object attributes
r1 = Robot("chappie", "blue", 80)
#r1.name = "chappie"
#r1.color = "blue"
#r1.weight = 80

r2 = Robot("sunny", "orange", 90)
#r2.name = "sunny"
#r2.color = "orange"
#r2.weight = 90

#instantiated object behavior
r1.introduce_self()

r2.introduce_self()