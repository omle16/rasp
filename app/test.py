from time import sleep
import Adafruit_PCA9685

class axis:
	def __init(self):
		# Initialise the PCA9685 using the default address (0x40).
		self.pwm = pwm = Adafruit_PCA9685.PCA9685()
		
		# Configure min and max servo pulse lengths
		self.position_min = 150  # Min pulse length out of 4096
		self.position_max = 600  # Max pulse length out of 4096
	
		# Set frequency to 60hz, good for servos.
		self.pwm.set_pwm_freq(60)
		
	def move_axis_pwm(self, axis_number, value):
		self.pwm.set_pwm(axis_number, 0, value)
		self.value[axis_number] = value 
		
	def move_axis_percent(self, axis_number, position):
		self.move_axis_percent(axis_number, position)
		self.position[axis_number] = position
		
# ~ class parrot:
	# ~ """this is the instance attribute """
	# ~ species = "bird"
	
	# ~ def __init__(self, name, age):
		# ~ self.name = name
		# ~ self.age = age
		
# ~ blue = parrot("blue", 10)
# ~ woo = parrot("woo", 15)

# ~ print("Blue is a {}".format(blue.__class__.species))
# ~ sleep(1)
# ~ print("{} is {} years old".format(blue.name, blue.age))
# ~ print("{} is {} years old".format(woo.name, woo.age))





















# ~ import contant

# ~ a = [1, 2, 3]

# ~ for i in range(0, 2):
	# ~ print a[i]
	# ~ sleep(1)


# ~ print ('This is only a test')

# ~ a, b, c = 10, 20, "apple"
# ~ print (a)
# ~ print (b)
# ~ print (c)

# ~ for i in range(1,20):
	# ~ print i
	# ~ sleep (0.5)
	# ~ if i == 5:
		# ~ break


# ~ class something(object):
	# ~ print ("Class message")
	# ~ def func1(self):
		# ~ a = 10
		# ~ b = 10
		# ~ print a*b
	
	# ~ def func2(self):
		# ~ a = 10
		# ~ b = 20
		# ~ print a*b

# ~ while True:
	# ~ something().func1()
	# ~ sleep(1)
	# ~ something().func2()
	# ~ sleep(1)

# ~ something().func1(10, 10)
# ~ sleep(0.5)
# ~ something().func2(10, 5)
