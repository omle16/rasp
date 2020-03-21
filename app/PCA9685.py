#Python script to use the PCA9685

import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address=0x40)

#Frequence valid for all motors, value from 40 to 1000
pwm.set_pwm_freq(50)

#Example of comand to position a motor, the difference will be calculated
pwm.set_pwm(0, 0, 150)  	#<-- this is the same
pwm.set_pwm(0, 600, 750) 	#<-- as this one






