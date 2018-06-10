import RPi.GPIO as GPIO
import time

from robot_control import Robot


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

robot = Robot()

while True:
    print(robot.GetUltraSonicDistance())      