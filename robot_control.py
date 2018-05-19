import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.cleanup()


class Robot(object):
    """docstring for Robot"""
    def __init__(self):
        super(Robot, self).__init__()
        
        

        self.pins = {
        "left_motor_speed_pin":15, #green
        "left_motor_forward_pin":29, #yellow
        "left_motor_backward_pin":22, #blue

        "right_motor_speed_pin":11, #red
        "right_motor_forward_pin":7, #orange
        "right_motor_backward_pin":16, #brown
        }

        self.speed_pins = [self.pins["left_motor_speed_pin"], self.pins["right_motor_speed_pin"] ]
        self.forward_pins = [self.pins["left_motor_forward_pin"], self.pins["rights_motor_forward_pin"] ]
        self.backward_pins = [self.pins["left_motor_backward_pin"], self.pins["right_motor_backward_pin"] ]


        for pin in self.speed_pins:
            print("setting up pin:"+str(pin))
            GPIO.setup(pin, GPIO.OUT)

        for pin in self.forward_pins:
            print("setting up pin:"+str(pin))
            GPIO.setup(pin, GPIO.OUT)

        for pin in self.backward_pins:
            print("setting up pin:"+str(pin))
            GPIO.setup(pin, GPIO.OUT)


        self.speed_pwms = {}
        self.speed_pwms["left"] = GPIO.PWM(self.pins["left_motor_speed_pin"], 1000)
        self.speed_pwms["right"] = GPIO.PWM(self.pins["right_motor_speed_pin"], 1000)
        



    def MoveForward(self):
        for pin in self.forward_pins:

            GPIO.output(pin, GPIO.HIGH)

        for pin in self.backward_pins:
            GPIO.output(pin, GPIO.LOW)
        

    def MoveBackward(self):
        for pin in self.backward_pins:
            GPIO.output(pin, GPIO.HIGH)

        for pin in self.forward_pins:
            GPIO.output(pin, GPIO.LOW)


    def Stop(self):
        for pin in self.forward_pins:
            GPIO.output(pin, GPIO.LOW)

        for pin in self.backward_pins:
            GPIO.output(pin, GPIO.LOW)


    def SpinClockwise(self):
        GPIO.output(self.pins["left_motor_forward_pin"], GPIO.HIGH)
        GPIO.output(self.pins["right_motor_backward_pin"], GPIO.HIGH)

        GPIO.output(self.pins["left_motor_backward_pin"], GPIO.LOW)
        GPIO.output(self.pins["right_motor_forward_pin"], GPIO.LOW)


    def SpinAntiClockwise(self):
        GPIO.output(self.pins["left_motor_forward_pin"], GPIO.LOW)
        GPIO.output(self.pins["right_motor_backward_pin"], GPIO.LOW)

        GPIO.output(self.pins["left_motor_backward_pin"], GPIO.HIGH)
        GPIO.output(self.pins["right_motor_forward_pin"], GPIO.HIGH)


    def SetSpeed(self,speed):
        if(speed < 1 and speed > 0):
            speed = speed*100

        for pwm in self.speed_pwms:
            self.speed_pwms[pwm].start(speed)

    def SetSpeedLeft(self,speed):
        if(speed < 1 and speed > 0):
            speed = speed*100

        self.speed_pwms["left"].start(speed)


    def SetSpeedRight(self,speed):
        if(speed < 1 and speed > 0):
            speed = speed*100

        self.speed_pwms["right"].start(speed)
    

    def TurnLeft(self,speed):
        if(speed < 1 and speed > 0):
            speed = speed*100

        self.speed_pwms["left"].start(speed/2)
        self.speed_pwms["right"].start(speed)


    def TurnRight(self,speed):
        if(speed < 1 and speed > 0):
            speed = speed*100

        self.speed_pwms["left"].start(speed)
        self.speed_pwms["right"].start(speed/2)


if __name__ == '__main__':
    robot = Robot()

    robot.SetSpeed(90)

    robot.MoveForward()
    time.sleep(1)

    robot.SpinClockwise()
    time.sleep(1)

    robot.MoveBackward()
    time.sleep(1)

    robot.SpinAntiClockwise()
    time.sleep(1)

    robot.MoveForward()
    time.sleep(1)

    robot.TurnLeft(90)
    time.sleep(1)

    robot.Stop()