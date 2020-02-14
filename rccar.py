import RPi.GPIO as GPIO
import time

steer1 = 13
steer2 = 19
drive1 = 26
drive2 = 15

# 21 and 19 are one pair
# 26 and 13 are the other
GPIO.setmode(GPIO.BCM)
GPIO.setup(steer1, GPIO.OUT)
GPIO.setup(steer2, GPIO.OUT)
GPIO.setup(drive1, GPIO.OUT)
GPIO.setup(drive2, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 1000)

def move_forward(duration, power):
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.HIGH)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.LOW)
 pwm.start(power)

 time.sleep(duration)
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.LOW)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.LOW)

def move_backward(duration, power):
 GPIO.output(drive1, GPIO.HIGH)
 GPIO.output(drive2, GPIO.LOW)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.LOW)
 pwm.start(power)

 time.sleep(duration)
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.LOW)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.LOW)


def turn_left(duration, power):
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.HIGH)
 GPIO.output(steer1, GPIO.HIGH)
 GPIO.output(steer2, GPIO.LOW)
 pwm.start(power)

 time.sleep(duration)
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.LOW)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.LOW)


def turn_right(duration, power):
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.HIGH)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.HIGH)
 pwm.start(power)

 time.sleep(duration)
 GPIO.output(drive1, GPIO.LOW)
 GPIO.output(drive2, GPIO.LOW)
 GPIO.output(steer1, GPIO.LOW)
 GPIO.output(steer2, GPIO.LOW)


def cleanup():
 GPIO.cleanup()
