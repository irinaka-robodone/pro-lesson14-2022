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

left=Motor(Port.B)
right=Motor(Port.C)
robot=DriveBase(left,right,55,120)
ev3.screen.print("1")
wait(1000)
robot.straight(650)
robot.turn(90)
robot.straight(600)
robot.turn(90)
robot.straight(380)
robot.turn(90)
robot.straight(420)
robot.turn(-90)
robot.straight(660)
robot.turn(-90)
ev3screen.print("2")
wait(1000)
robotstraight(800)
robot.turn(90)
robot.straight(770)
robot.turn(90)
robotstraight(860)
