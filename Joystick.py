import pygame
import sys
import time
import motor_lib as ml
HatArr = []
StickArr = [1,2,3,4]
ButtArr = [0,1,2,3,4,5,6,7,8,9,10,11,12]
"""
0 = left / right
1 = front / back
2 = throttel
3 = twist

"""

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    print("Joystick has been initialized.")
else:
    print("No Joystick found.")
    exit(1)


joystick = pygame.joystick.Joystick(0)
joystick.init()
print(joystick.get_id())
print("Number of axis detected : %d" % (joystick.get_numaxes()))
print("Number of buttons detected : %d" % (joystick.get_numbuttons()))

while True:
    try:
        pygame.event.get()
        StickArr[0] = joystick.get_axis(0)
        StickArr[1] = joystick.get_axis(1)
        StickArr[2] = joystick.get_axis(2)
        StickArr[3] = joystick.get_axis(3)
        ButtArr[0] = joystick.get_button(0)

        move = ml.joy_sort(StickArr[0])
        ml.move(1,move)
        print("left / right : %.2f | front / back : %.2f | throttle : %.2f | Twist : %.2f | Move : %.2f" % (StickArr[0], StickArr[1], StickArr[2], StickArr[3], move))
        time.sleep(.5)
    except KeyboardInterrupt:
        sys.exit()






