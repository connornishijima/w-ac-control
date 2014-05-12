#/////////////////////////////////////////////
#
#   Wireless AC Control Software 1.4 (alpha)
#   by Connor Nishijima and Andrew Neal
#
#/////////////////////////////////////////////

directory = "/home/pi/wac2/"

def commandCheck():
	f = open(directory + "command","r")
	command = f.read().strip("\n")
	f.close
	if not command == "":
		print "RECEIVED COMMAND: " + str(command)
		f = open(directory + "command","w")
		f.write("")
		f.close()
		return command
	else:
		return "NULL"

# Define code parsing ------------------------------------------
def shortParse(inputCode):
	inputCode = inputCode.replace(" ","")
        outputCode = ""
        for i in range(0, len(inputCode)):
                if inputCode[i] == "1":
                        outputCode = outputCode + "1110"
                if inputCode[i] == "0":
                        outputCode = outputCode + "1000"
        return outputCode


# IMPORT CHANNEL "ON" CODES ----------------------------------------

# SET A
f = open(directory + "rf_codes/chA/ch1on.data","r")
chA1on_data = f.read()
chA1on_data = shortParse(chA1on_data)
chA1on_data = "0000" + chA1on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chA/ch2on.data","r")
chA2on_data = f.read()
chA2on_data = shortParse(chA2on_data)
chA2on_data = "0000" + chA2on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chA/ch1on.data","r")
chA3on_data = f.read()
chA3on_data = shortParse(chA3on_data)
chA3on_data = "0000" + chA3on_data.replace('\n', '') + "00001111"
f.close()

# SET B
f = open(directory + "rf_codes/chB/ch1on.data","r")
chB1on_data = f.read()
chB1on_data = shortParse(chB1on_data)
chB1on_data = "0000" + chB1on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chB/ch2on.data","r")
chB2on_data = f.read()
chB2on_data = shortParse(chB2on_data)
chB2on_data = "0000" + chB2on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chB/ch1on.data","r")
chB3on_data = f.read()
chB3on_data = shortParse(chB3on_data)
chB3on_data = "0000" + chB3on_data.replace('\n', '') + "00001111"
f.close()

# SET C
f = open(directory + "rf_codes/chC/ch1on.data","r")
chC1on_data = f.read()
chC1on_data = shortParse(chC1on_data)
chC1on_data = "0000" + chC1on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chC/ch2on.data","r")
chC2on_data = f.read()
chC2on_data = shortParse(chC2on_data)
chC2on_data = "0000" + chC2on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chC/ch1on.data","r")
chC3on_data = f.read()
chC3on_data = shortParse(chC3on_data)
chACon_data = "0000" + chC3on_data.replace('\n', '') + "00001111"
f.close()

# SET D
f = open(directory + "rf_codes/chD/ch1on.data","r")
chD1on_data = f.read()
chD1on_data = shortParse(chD1on_data)
chD1on_data = "0000" + chD1on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chD/ch2on.data","r")
chD2on_data = f.read()
chD2on_data = shortParse(chD2on_data)
chD2on_data = "0000" + chD2on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chD/ch1on.data","r")
chD3on_data = f.read()
chD3on_data = shortParse(chD3on_data)
chD3on_data = "0000" + chD3on_data.replace('\n', '') + "00001111"
f.close()

# SET E
f = open(directory + "rf_codes/chE/ch1on.data","r")
chE1on_data = f.read()
chE1on_data = shortParse(chE1on_data)
chE1on_data = "0000" + chE1on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chE/ch2on.data","r")
chE2on_data = f.read()
chE2on_data = shortParse(chE2on_data)
chE2on_data = "0000" + chE2on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chE/ch1on.data","r")
chE3on_data = f.read()
chE3on_data = shortParse(chE3on_data)
chE3on_data = "0000" + chE3on_data.replace('\n', '') + "00001111"
f.close()

# SET F
f = open(directory + "rf_codes/chF/ch1on.data","r")
chF1on_data = f.read()
chF1on_data = shortParse(chF1on_data)
chF1on_data = "0000" + chF1on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chF/ch2on.data","r")
chF2on_data = f.read()
chF2on_data = shortParse(chF2on_data)
chF2on_data = "0000" + chF2on_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chF/ch1on.data","r")
chF3on_data = f.read()
chF3on_data = shortParse(chF3on_data)
chF3on_data = "0000" + chF3on_data.replace('\n', '') + "00001111"
f.close()

# IMPORT CHANNEL "OFF" CODES ----------------------------------------

# SET A
f = open(directory + "rf_codes/chA/ch1off.data","r")
chA1off_data = f.read()
chA1off_data = shortParse(chA1off_data)
chA1off_data = "0000" + chA1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chA/ch2off.data","r")
chA2off_data = f.read()
chA2off_data = shortParse(chA2off_data)
chA2off_data = "0000" + chA2off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chA/ch3off.data","r")
chA3off_data = f.read()
chA3off_data = shortParse(chA3off_data)
chA3off_data = "0000" + chA3off_data.replace('\n', '') + "00001111"
f.close()

# SET B
f = open(directory + "rf_codes/chB/ch1off.data","r")
chB1off_data = f.read()
chB1off_data = shortParse(chB1off_data)
chB1off_data = "0000" + chB1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chB/ch2off.data","r")
chB2off_data = f.read()
chB2off_data = shortParse(chB1off_data)
chB2off_data = "0000" + chB1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chB/ch3off.data","r")
chB3off_data = f.read()
chB3off_data = shortParse(chB3off_data)
chB3off_data = "0000" + chB3off_data.replace('\n', '') + "00001111"
f.close()

# SET C
f = open(directory + "rf_codes/chC/ch1off.data","r")
chC1off_data = f.read()
chC1off_data = shortParse(chC1off_data)
chC1off_data = "0000" + chC1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chC/ch2off.data","r")
chC2off_data = f.read()
chC2off_data = shortParse(chC2off_data)
chC2off_data = "0000" + chC2off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chC/ch3off.data","r")
chC3off_data = f.read()
chC3off_data = shortParse(chC3off_data)
chC3off_data = "0000" + chC3off_data.replace('\n', '') + "00001111"
f.close()


# SET D
f = open(directory + "rf_codes/chD/ch1off.data","r")
chD1off_data = f.read()
chD1off_data = shortParse(chD1off_data)
chD1off_data = "0000" + chD1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chD/ch2off.data","r")
chD2off_data = f.read()
chD2off_data = shortParse(chD2off_data)
chD2off_data = "0000" + chD2off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chD/ch3off.data","r")
chD3off_data = f.read()
chD3off_data = shortParse(chD3off_data)
chD3off_data = "0000" + chD3off_data.replace('\n', '') + "00001111"
f.close()


# SET E
f = open(directory + "rf_codes/chE/ch1off.data","r")
chE1off_data = f.read()
chE1off_data = shortParse(chE1off_data)
chE1off_data = "0000" + chE1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chE/ch2off.data","r")
chE2off_data = f.read()
chE2off_data = shortParse(chE2off_data)
chE2off_data = "0000" + chE2off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chE/ch3off.data","r")
chE3off_data = f.read()
chE3off_data = shortParse(chE3off_data)
chE3off_data = "0000" + chE3off_data.replace('\n', '') + "00001111"
f.close()


# SET F
f = open(directory + "rf_codes/chF/ch1off.data","r")
chF1off_data = f.read()
chF1off_data = shortParse(chF1off_data)
chF1off_data = "0000" + chF1off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chF/ch2off.data","r")
chF2off_data = f.read()
chF2off_data = shortParse(chF2off_data)
chF2off_data = "0000" + chF2off_data.replace('\n', '') + "00001111"
f.close()

f = open(directory + "rf_codes/chF/ch3off.data","r")
chF3off_data = f.read()
chF3off_data = shortParse(chF3off_data)
chF3off_data = "0000" + chF3off_data.replace('\n', '') + "00001111"
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

