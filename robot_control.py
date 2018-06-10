import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)




class Robot(object):
    """docstring for Robot"""
    def __init__(self):
        super(Robot, self).__init__()
        
        

        self.pins = {
        "left_motor_speed_pin":15, #green
        "left_motor_forward_pin":29, #yellow
        "left_motor_backward_pin":22, #blue

        "right_motor_speed_pin":11, #purple
        "right_motor_forward_pin":7, #orange
        "right_motor_backward_pin":16, #brown

        "ultrasonic_trig":37,                                   
        "ultrasonic_echo":35                                  
        }

        self.speed_pins = [self.pins["left_motor_speed_pin"], self.pins["right_motor_speed_pin"] ]
        self.forward_pins = [self.pins["left_motor_forward_pin"], self.pins["right_motor_forward_pin"] ]
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

        GPIO.setup(self.pins["ultrasonic_trig"],GPIO.OUT)                  #Set pin as GPIO out
        GPIO.setup(self.pins["ultrasonic_echo"],GPIO.IN)                   #Set pin as GPIO in

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


    def GetUltraSonicDistance(self,calibration=0.5):
        GPIO.output(self.pins["ultrasonic_trig"], False)                 #Set TRIG as LOW
        print "Waitng For Sensor To Settle"
        time.sleep(0.5)                            #Delay of 2 seconds

        GPIO.output(self.pins["ultrasonic_trig"], True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                      #Delay of 0.00001 seconds
        GPIO.output(self.pins["ultrasonic_trig"], False)                 #Set TRIG as LOW

        while GPIO.input(self.pins["ultrasonic_echo"])==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse

        while GPIO.input(self.pins["ultrasonic_echo"])==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 

        pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)            #Round to two decimal points

        return distance
        
        if distance > 2 and distance < 400:      #Check whether the distance is within range
            print "Distance:",distance - calibration,"cm"  #Print distance with 0.5 cm calibration
        else:
            print "Out Of Range"                   #display out of range


    def CleanUp(self):
        GPIO.cleanup()


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

    robot.CleanUp()