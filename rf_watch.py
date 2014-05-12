#/////////////////////////////////////////////
#
#   Wireless AC Control Software 1.4 (alpha)
#   by Connor Nishijima and Andrew Neal
#
#/////////////////////////////////////////////

import RPi.GPIO as GPIO
import time

txPin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(txPin,GPIO.OUT)

directory = "/home/pi/wac2/"

freqJam = True

def commandCheck():
	f = open(directory + "command","r")
	command = f.read().strip("\n")
	f.close
	if not command == "":
		f = open(directory + "command","w")
		f.write("")
		f.close()
		return command
	else:
		return "NULL"

# IMPORT CHANNEL "ON" CODES ----------------------------------------

# SET A
f = open(directory + "rf_codes/chA/ch1on.data","r")
chA1on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chA/ch2on.data","r")
chA2on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chA/ch3on.data","r")
chA3on_data = f.read().replace(" ",'').strip("\n")
f.close()

# SET B
f = open(directory + "rf_codes/chB/ch1on.data","r")
chB1on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chB/ch2on.data","r")
chB2on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chB/ch3on.data","r")
chB3on_data = f.read().replace(" ",'').strip("\n")
f.close()

# SET C
f = open(directory + "rf_codes/chC/ch1on.data","r")
chC1on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chC/ch2on.data","r")
chC2on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chC/ch3on.data","r")
chC3on_data = f.read().replace(" ",'').strip("\n")
f.close()

# SET D
f = open(directory + "rf_codes/chD/ch1on.data","r")
chD1on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chD/ch2on.data","r")
chD2on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chD/ch3on.data","r")
chD3on_data = f.read().replace(" ",'').strip("\n")
f.close()
print chD3on_data

# SET E
f = open(directory + "rf_codes/chE/ch1on.data","r")
chE1on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chE/ch2on.data","r")
chE2on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chE/ch3on.data","r")
chE3on_data = f.read().replace(" ",'').strip("\n")
f.close()

# SET F
f = open(directory + "rf_codes/chF/ch1on.data","r")
chF1on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chF/ch2on.data","r")
chF2on_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chF/ch3on.data","r")
chF3on_data = f.read().replace(" ",'').strip("\n")
f.close()

# IMPORT CHANNEL "OFF" CODES ----------------------------------------

# SET A
f = open(directory + "rf_codes/chA/ch1off.data","r")
chA1off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chA/ch2off.data","r")
chA2off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chA/ch3off.data","r")
chA3off_data = f.read().replace(" ",'').strip("\n")
f.close()

# SET B
f = open(directory + "rf_codes/chB/ch1off.data","r")
chB1off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chB/ch2off.data","r")
chB2off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chB/ch3off.data","r")
chB3off_data = f.read().replace(" ",'').strip("\n")
f.close()

# SET C
f = open(directory + "rf_codes/chC/ch1off.data","r")
chC1off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chC/ch2off.data","r")
chC2off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chC/ch3off.data","r")
chC3off_data = f.read().replace(" ",'').strip("\n")
f.close()


# SET D
f = open(directory + "rf_codes/chD/ch1off.data","r")
chD1off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chD/ch2off.data","r")
chD2off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chD/ch3off.data","r")
chD3off_data = f.read().replace(" ",'').strip("\n")
f.close()


# SET E
f = open(directory + "rf_codes/chE/ch1off.data","r")
chE1off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chE/ch2off.data","r")
chE2off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chE/ch3off.data","r")
chE3off_data = f.read().replace(" ",'').strip("\n")
f.close()


# SET F
f = open(directory + "rf_codes/chF/ch1off.data","r")
chF1off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chF/ch2off.data","r")
chF2off_data = f.read().replace(" ",'').strip("\n")
f.close()

f = open(directory + "rf_codes/chF/ch3off.data","r")
chF3off_data = f.read().replace(" ",'').strip("\n")
f.close()

# SPECIAL CHANNEL X DATA

f = open(directory + "rf_codes/misc/chX.data","r")
chX_data = f.read().replace(" ",'').strip("\n")
f.close()

print "Channel A:"
print "CH1 ON:  " + str(chA1on_data)
print "CH2 ON:  " + str(chA2on_data)
print "CH3 ON:  " + str(chA3on_data)
print "CH1 OFF: " + str(chA1off_data)
print "CH2 OFF: " + str(chA2off_data)
print "CH3 OFF: " + str(chA3off_data)
print " "
print "Channel B:"
print "CH1 ON:  " + str(chB1on_data)
print "CH2 ON:  " + str(chB2on_data)
print "CH3 ON:  " + str(chB3on_data)
print "CH1 OFF: " + str(chB1off_data)
print "CH2 OFF: " + str(chB2off_data)
print "CH3 OFF: " + str(chB3off_data)
print " "
print "Channel C:"
print "CH1 ON:  " + str(chC1on_data)
print "CH2 ON:  " + str(chC2on_data)
print "CH3 ON:  " + str(chC3on_data)
print "CH1 OFF: " + str(chC1off_data)
print "CH2 OFF: " + str(chC2off_data)
print "CH3 OFF: " + str(chC3off_data)
print " "
print "Channel D:"
print "CH1 ON:  " + str(chD1on_data)
print "CH2 ON:  " + str(chD2on_data)
print "CH3 ON:  " + str(chD3on_data)
print "CH1 OFF: " + str(chD1off_data)
print "CH2 OFF: " + str(chD2off_data)
print "CH3 OFF: " + str(chD3off_data)
print " "
print "Channel E:"
print "CH1 ON:  " + str(chE1on_data)
print "CH2 ON:  " + str(chE2on_data)
print "CH3 ON:  " + str(chE3on_data)
print "CH1 OFF: " + str(chE1off_data)
print "CH2 OFF: " + str(chE2off_data)
print "CH3 OFF: " + str(chE3off_data)
print " "
print "Channel F:"
print "CH1 ON:  " + str(chF1on_data)
print "CH2 ON:  " + str(chF2on_data)
print "CH3 ON:  " + str(chF3on_data)
print "CH1 OFF: " + str(chF1off_data)
print "CH2 OFF: " + str(chF2off_data)
print "CH3 OFF: " + str(chF3off_data)
print " "

def stateSwitch(set,channel,power):
	if set == "A":
		if channel == "1":
			if power == "1":
				rfTX(chA1on_data)
			else:
				rfTX(chA1off_data)
		if channel == "2":
                        if power == "1":
                                rfTX(chA2on_data)
                        else:
                                rfTX(chA2off_data)
		if channel == "3":
                        if power == "1":
                                rfTX(chA3on_data)
                        else:
                                rfTX(chA3off_data)
	if set == "B":
                if channel == "1":
                        if power == "1":
                                rfTX(chB1on_data)
                        else:
                                rfTX(chB1off_data)
                if channel == "2":
                        if power == "1":
                                rfTX(chB2on_data)
                        else:
                                rfTX(chB2off_data)
                if channel == "3":
                        if power == "1":
                                rfTX(chB3on_data)
                        else:
                                rfTX(chB3off_data)
	if set == "C":
                if channel == "1":
                        if power == "1":
                                rfTX(chC1on_data)
                        else:
                                rfTX(chC1off_data)
                if channel == "2":
                        if power == "1":
                                rfTX(chC2on_data)
                        else:
                                rfTX(chC2off_data)
                if channel == "3":
                        if power == "1":
                                rfTX(chC3on_data)
                        else:
                                rfTX(chC3off_data)
	if set == "D":
                if channel == "1":
                        if power == "1":
                                rfTX(chD1on_data)
                        else:
                                rfTX(chD1off_data)
                if channel == "2":
                        if power == "1":
                                rfTX(chD2on_data)
                        else:
                                rfTX(chD2off_data)
                if channel == "3":
                        if power == "1":
                                rfTX(chD3on_data)
                        else:
                                rfTX(chD3off_data)
	if set == "E":
                if channel == "1":
                        if power == "1":
                                rfTX(chE1on_data)
                        else:
                                rfTX(chE1off_data)
                if channel == "2":
                        if power == "1":
                                rfTX(chE2on_data)
                        else:
                                rfTX(chE2off_data)
                if channel == "3":
                        if power == "1":
                                rfTX(chE3on_data)
                        else:
                                rfTX(chE3off_data)
	if set == "F":
                if channel == "1":
                        if power == "1":
                                rfTX(chF1on_data)
                        else:
                                rfTX(chF1off_data)
                if channel == "2":
                        if power == "1":
                                rfTX(chF2on_data)
                        else:
                                rfTX(chF2off_data)
                if channel == "3":
                        if power == "1":
                                rfTX(chF3on_data)
                        else:
                                rfTX(chF3off_data)
	if set == "X":
		rfTX("X")


def rfTX(inputString):
	shortDelay = 0.000581
        longDelay  = 0.001585

	if inputString == "X":
		GPIO.output(txPin,1)
                time.sleep(0.01)
		GPIO.output(txPin,0)
                time.sleep(0.01)
	else:
		inputString2 = inputString
		repeat = 4
		while repeat > 0:
			count = len(inputString)
			GPIO.output(txPin,0)
			time.sleep(0.00999)
			while count > 0:
				bit = inputString[0]
				if bit == "1":
					GPIO.output(txPin,1)
					time.sleep(longDelay)
					GPIO.output(txPin,0)
					time.sleep(shortDelay)
				else:
					GPIO.output(txPin,1)
	                                time.sleep(shortDelay)
	                                GPIO.output(txPin,0)
	                                time.sleep(longDelay)
				inputString = inputString[1:]
				count -= 1
			repeat -= 1
			inputString = inputString2

print "WAITING FOR FIRST COMMAND..."

while True:
	com = commandCheck()

	if freqJam == 1:
		stateSwitch("X","X","X")

	if not com == "NULL":		
		print "COMMAND RECEIVED: " + str(com)
		type = com[0]

		if type == "R":
			set = com[2]
			channel = com[3]
			power = com[5]
			stateSwitch(set,channel,power)

		elif type == "M":
			message = com[2:]
			print "MESSAGE: " + message
		elif type == "J":
			message = com[2:]
			if message == "2":
				print "JAMMING disabled."
				freqJam = 0
			if message == "1":
				print "JAMMING enabled."
				freqJam = 1
		else:
			print "ERROR || Cannot parse command!"
