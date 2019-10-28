import gclib
import time
import threading

class GclibWrapper:

    # #{ __init__()

    def __init__(self, n_stages, step2deg, dummy=False, debug=False):

        self.dummy = dummy
        self.debug = debug

        self.n_stages = n_stages

        print("Initializing galib")

        if not self.dummy:
            self.g = gclib.py()

        self.fast_delay = 0.1
        self.slow_delay = 1.0
        self.step2deg = step2deg

        self.mutex_get_position = threading.Lock()

        if dummy:
            self.positions = []

            for i in range(0, n_stages):
                self.positions.append(0)

    # #} end of __init__()

    # #{ unit2steps()

    def unit2steps(self, axis, amount):

        return int(round(float(amount) * float(self.step2deg[axis])))

    # #} end of

    # #{ steps2unit()

    def steps2unit(self, axis, amount):

        return float(amount) / float(self.step2deg[axis])

    # #} end of steps2unit()

    # #{ setPosition()

    def setPosition(self, axis, value):

        self.positions[axis] = value

    # #} end of setPosition()

    # #{ open()

    def open(self, address):

        # --address /dev/ttyUSB4 --handshake NONE --baud 19200

        if not self.dummy:
            print("Opening with address '{}'".format(address))
            res = []
            try:
                res = self.g.GOpen(address)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass
        else:
            print("Opening dummy")
            res = "dummy initialized"

        print("result: '{}'".format(res))

        time.sleep(self.slow_delay)

    # #} end of open()

    # #{ close()

    def close(self):

        # --address /dev/ttyUSB4 --handshake NONE --baud 19200

        if not self.dummy:
            print("Closing the device")
            res = []
            try:
                res = self.g.GClose()
            except ValueError as ve:
                print("Error: ".format(ve))
                pass
        else:
            print("closing dummy")
            res = "dummy closed"

        print("result: '{}'".format(res))

        time.sleep(self.slow_delay)

    # #} end of open()

    # #{ setSpeed()

    def setSpeed(self, speeds):

        print("Setting speeds to: {}".format(speeds))

        self.speed = speeds

        command="SP "

        if len(speeds) == 1:
            command = "SP {}".format(speeds[0])
        else:
            for idx,speed in enumerate(speeds):
                command += str(speed)
                if idx < len(speeds)-1:
                    command += ","

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        time.sleep(self.fast_delay)

    # #} end of setSpeed()

    # #{ setAcceleration()

    def setAcceleration(self, accelerations):

        print("Setting accelerations to: {}".format(accelerations))

        self.acceleration = accelerations

        command="AC "

        if len(accelerations) == 1:
            command = "AC {}".format(accelerations[0])
        else:
            for idx,acceleration in enumerate(accelerations):
                command += str(acceleration)
                if idx < len(accelerations)-1:
                    command += ","

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        time.sleep(self.fast_delay)

    # #} end of setAcceleration()

    # #{ setDeceleration()

    def setDeceleration(self, decelerations):

        print("Setting decelerations to: {}".format(decelerations))

        self.deceleration = decelerations

        command="DC "

        if len(decelerations) == 1:
            command = "DC {}".format(decelerations[0])
        else:
            for idx,deceleration in enumerate(decelerations):
                command += str(deceleration)
                if idx < len(decelerations)-1:
                    command += ","

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        time.sleep(self.fast_delay)

    # #} end of setDeceleration()

    # #{ setOrigin()

    def setOrigin(self):

        print("Setting origin")

        command="DP 0,0"

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))

            for idx,value in enumerate(self.positions):
                self.positions[idx] = 0
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                return False

        time.sleep(self.slow_delay)

        return True

    # #} end of setAcceleration()

    # #{ setForwardLimit()

    def setForwardLimit(self, forward_limits):

        self.forward_limits = forward_limits

        # check the limits
        for idx,limit in enumerate(forward_limits):
            if limit < 0:
                print("Forwrad limit out of limit!!!")
                return

        print("Setting forward_limits to: {}".format(forward_limits))

        command="FL "

        if len(forward_limits) == 1:
            command = "FL {}".format(forward_limits[0])
        else:
            for idx,limit in enumerate(forward_limits):
                command += str(limit)
                if idx < len(forward_limits)-1:
                    command += ","

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        time.sleep(self.fast_delay)

    # #} end of setForwardLimit()

    # #{ setBackwardLimit()

    def setBackwardLimit(self, backward_limits):

        self.backward_limits = backward_limits

        # check the limits
        for idx,limit in enumerate(backward_limits):
            if limit > 0:
                print("Backward limit out of limit!!!")
                return

        print("Setting backward_limits to: {}".format(backward_limits))

        command="BL "

        if len(backward_limits) == 1:
            command = "BL {}".format(backward_limits[0])
        else:
            for idx,limit in enumerate(backward_limits):
                command += str(limit)
                if idx < len(backward_limits)-1:
                    command += ","

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        time.sleep(self.fast_delay)

    # #} end of setBackwardLimit()

    # #{ checkLimits()

    def checkLimits(self, axis, value):

        if (value >= self.forward_limits[axis]) or (value <= self.backward_limits[axis]):

            return False

        else:

            return True

    # #} end of checkLimits()

    # #{ motorsOn()

    def motorsOn(self):

        command = "SH"

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        time.sleep(self.fast_delay)

    # #} end of motorsOn()

    # #{ getPositionSteps()

    def getPositionSteps(self, axis):

        self.mutex_get_position.acquire()

        command = "RP"+chr(axis+ord('A'))

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))

            self.mutex_get_position.release()
            return self.positions[axis]
        else:
            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                res = self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

            self.mutex_get_position.release()
            return int(res)

    # #} end of getPositionSteps()

    # #{ getPositionSteps()

    def getPositionUnit(self, axis):

        current_position = self.getPositionSteps(axis)
        return self.steps2unit(axis, current_position)

    # #}

    # #{ moveRelative()

    def moveRelative(self, axis, amount):

        command = "PR "

        amount_converted = self.unit2steps(axis, amount)

        current_position = self.getPositionSteps(axis)
        position_reference = current_position + amount_converted

        if not self.checkLimits(axis, position_reference):
            print("!!! value {} is out of limit for axis {}".format(amount, axis))
            return False

        if self.n_stages == 1:
            command = "PR {}".format(amount_converted)
        else:
            for i in range(0, self.n_stages):

                if axis == i:
                    command += str(amount_converted)
                else:
                    command += "0"

                if i < self.n_stages-1:
                    command += ","

        command += ";BG;"

        execution_time = abs(float(amount))/float(self.steps2unit(axis, self.speed[axis]))

        if self.dummy:
            if self.debug:
                print("Dummy command: {}".format(command))

            print("Moving dummy stage {} relatively by {}, will take: {} s".format(axis, amount, execution_time))
            time.sleep(execution_time)

            self.setPosition(axis, position_reference)

        else:
            print("Moving stage {} relatively by {}".format(axis, amount))

            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                res = self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        # wait while we move

        time.sleep(1.0)

        while abs(current_position - position_reference) >= self.steps2unit(axis, 0.01):

            print("Waiting for the motion to finish: current {} reference {}".format(current_position, position_reference))
            current_position = self.getPositionSteps(axis)
            time.sleep(1.0)

        time.sleep(1.0)

        return True

    # #} end of moveRelative()

    # #{ moveAbsoute()

    def moveAbsolute(self, axis, amount):

        command = "PA "

        amount_converted = self.unit2steps(axis, amount)

        current_position = self.getPositionSteps(axis)
        position_reference = amount_converted

        if not self.checkLimits(axis, position_reference):
            print("!!! value {} is out of limit for axis {}".format(amount, axis))
            return False

        if self.n_stages == 1:
            command = "PA {}".format(amount_converted)
        else:
            for i in range(0, self.n_stages):

                if axis == i:
                    command += str(amount_converted)
                else:
                    command += str(self.getPositionSteps(i))

                if i < self.n_stages-1:
                    command += ","

        command += ";BG;"

        execution_time = float(abs(amount-self.steps2unit(axis, current_position)))/float(self.steps2unit(axis, self.speed[axis]))

        if self.dummy:
            print("Moving dummy stage {} to {}, will take: {} s".format(axis, amount, execution_time))

            if self.debug:
                print("Dummy command: {}".format(command))

            time.sleep(execution_time)

            self.setPosition(axis, position_reference)

        else:
            print("Moving stage {} to {}".format(axis, amount))

            res = []
            try:
                if self.debug:
                    print("Executing command: {}".format(command))
                res = self.g.GCommand(command)
            except ValueError as ve:
                print("Error: ".format(ve))
                pass

        # wait while we move

        while abs(current_position - position_reference) >= self.steps2unit(axis, 0.01):

            print("Waiting for the motion to finish: current {} reference {}".format(current_position, position_reference))
            current_position = self.getPositionSteps(axis)
            time.sleep(1.0)

        time.sleep(1.0)

        return True

    # #} end of moveRelative()

    # #{ moveAllAbsolute()

    def moveAllAbsolute(self, amounts):

        for idx,amount in enumerate(amounts):
            result = self.moveAbsolute(idx, amount)

            if not result:
                return False

        return True

    # #} end of moveAllAbsolute()
