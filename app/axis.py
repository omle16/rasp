import Adafruit_PCA9685
from time import sleep

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
