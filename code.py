import RPi.GPIO as GPIO
import time

TRIG = 16
ECHO = 18
BUZZ = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(BUZZ,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

pwm = GPIO.PWM(12,100)
pwm.start(0)

try:
	while True:
		GPIO.output(TRIG,False)
		time.sleep(1)
		GPIO.output(TRIG, True)
		time.sleep(0.0001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)==0:
			pulse_start = time.time()

		while GPIO.input(ECHO)==1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)   #calculate to centimeters
		percent = (distance / 25) * 100 #calculate it assuming 25cm is largest distance
		if percent > 100:
			percent = 100		#max intensity is 100%
		percent = (-1)*(percent - 100)	#invert intennsity (further away = less noise)
		pwm.ChangeDutyCycle(percent)
		print("Distance: " + str(distance) + " Intensity: " + str(percent))

except KeyboardInterrupt:
		print("Stopping")

pwm.stop()
GPIO.cleanup()
