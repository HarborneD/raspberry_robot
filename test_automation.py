import RPi.GPIO as GPIO
import time

from robot_control import Robot


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

robot = Robot()

robot.SetSpeed(70)

turn_distance = 20

while True:
    distance = robot.GetUltraSonicDistance()
    print(distance)

    if(distance < turn_distance):
        robot.SpinClockwise()
        time.sleep(1)
    else:
        robot.MoveForward()   