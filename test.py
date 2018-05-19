import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.cleanup()

GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

left_speed = GPIO.PWM(15, 1000)
left_speed.start(90)

GPIO.output(29, GPIO.HIGH)

time.sleep(1)

GPIO.output(29, GPIO.LOW)


right_speed = GPIO.PWM(11, 1000)
right_speed.start(90)

GPIO.output(7, GPIO.HIGH)

time.sleep(1)

GPIO.output(7, GPIO.LOW)