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
right=Motor(Port.C)

# robot = DriveBase(left, right, 55, 120)
# robot = DriveBase(left, right, 55, 120)
robot=DriveBase(left,right,55,121)

# robot.straight(1000)    # ロボットを直進させる
# robot.turn(90)          # ロボットを時計回りに 90度旋回する
# ev3.screen.print("Moji")  # スクリーンに Moji を表示
robot.straight(600)
robot.turn(90)
robot.straight(800)
robot.turn(90)
robot.straight(400)
robot.turn(90)
robot.straight(400)
robot.turn(270)
robot.straight(380)
robot.turn(-90)
robot.straight(560)
ev3.screen.print("2")
wait(1000)
robot.turn(-90)
robot.straight(690)
robot.turn(90)
robot.straight(690)
robot.turn(90)
# robot.straight(690)
robot.straight(690)