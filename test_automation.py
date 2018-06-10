import RPi.GPIO as GPIO
import time

from robot_control import Robot


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

robot = Robot()

turn_distance = 10

while True:
    distance = robot.GetUltraSonicDistance()

    if(distance < turn_distance):
        robot.SpinClockwise()
        time.sleep(1)
    else:
        robot.MoveForward()   