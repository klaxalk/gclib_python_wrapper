#!/usr/bin/python

import gclib_wrapper

# initialize with 2 stages, each 12500 steps per unit, Dummy=True
wrapper = gclib_wrapper.GclibWrapper(2, [12500, 12500], True)

# open the device
wrapper.open("--address /dev/ttyUSB4 --handshake NONE --baud 19200")

# reset the coordinates to 0,0
wrapper.setOrigin()

# set the dynamics
wrapper.setSpeed([2500, 2500])
wrapper.setAcceleration([2500, 2500])
wrapper.setDeceleration([2500, 2500])

# set the boundaries
wrapper.setForwardLimit([100000, 100000])
wrapper.setBackwardLimit([-100000, -100000])

# enabled motors
wrapper.motorsOn()

print("Initial position: {} {}".format(wrapper.getPosition(0), wrapper.getPosition(1)))
print("")

# move relative in first axis by 1.0 unit
wrapper.moveRelative(0, 1.0)

print("Mid position: {} {}".format(wrapper.getPosition(0), wrapper.getPosition(1)))
print("")

# move absolute in second axis to coordinate 1.0
wrapper.moveAbsolute(1, 2.0)

print("Mid position: {} {}".format(wrapper.getPosition(0), wrapper.getPosition(1)))
print("")

# move absolute in all axes
wrapper.moveAllAbsolute([0.0, 0.0])

print("Final position: {} {}".format(wrapper.getPosition(0), wrapper.getPosition(1)))

wrapper.close()
