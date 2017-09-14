#!/usr/bin/env python
import RPi.GPIO as IO
import time                     #calling time to provide delays in program
import os 			#execute standard Unix or Linux shell commands using Python
IO.setwarnings(False)           #do not show any warnings
IO.setmode (IO.BCM)
IO.setup(21,IO.OUT)           # initialize GPIO as an output.

p = IO.PWM(21,100)          #GPIO as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle
while 1:                               #execute loop forever
	charge = float (os.popen("cat /proc/loadavg|awk '{print $1}'").read())
	if charge == 0:
        	charge = 0.01
	temps = 1/(100*charge)

	for x in range (50):                          #execute loop for 50 times, x being incremented from 0 to 49.
		p.ChangeDutyCycle(x+1)               #change duty cycle for varying the brightness of LED.
		time.sleep(temps)                           #sleep
      
	for x in range (50):                         #execute loop for 50 times, x being incremented from 0 to 49.
		p.ChangeDutyCycle(51-x)        #change duty cycle for changing the brightness of LED.
		time.sleep(temps)                          #sleep
