#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot= DriveBase(left, right, 50,127)

ev3.speaker.beep()
ev3.screen.print("1")   # 1 を表示
wait(2000)              # 1秒止まる
robot.straight(650)
robot.turn(90)
robot.straight(550)
robot.turn(90)
robot.straight(400)
robot.turn(90)
robot.straight(380)
robot.turn(-90)
robot.straight(350)
robot.turn(-90)
robot.straight(500)
robot.straight(30)
robot.straight(30)
ev3.screen.print(2)
wait(2000)
robot.turn(-10)
robot.turn(-10)
robot.turn(-10)
robot.turn(-20)
robot.turn(-20)
robot.turn(-10)
robot.turn(-10)
robot.straight(360)

