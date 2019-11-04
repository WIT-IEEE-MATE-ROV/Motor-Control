import Adafruit_PCA9685 as Ada
pwm = Ada.PCA9685()
frequency = 400
pwm.frequency = frequency

def joy_sort(arr):
    if (arr > 0):
        moveval = (1350 - (300 * StickArr[1]))
    if (arr [0] < 0):
        moveval = (1350 - (300 * StickArr[1]))
    if (arr == 0 or StickArr[1] == -0):
        moveval = 1350
    return moveval

def move(channel, on_time):
    pwm.set_pwm(channel, 0, on_time)

def initialize():
#   will fix later just a temp function for danversport event
    pwm.set_pwm(1, 0, 1650)
    pwm.set_pwm(1, 0, 900)
    pwm.set_pwm(1, 0, 1350)

