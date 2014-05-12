#/////////////////////////////////////////////
#
#   Wireless AC Control Software 1.4 (beta)
#   by Connor Nishijima and Andrew Neal
#
#/////////////////////////////////////////////

directory = "/home/pi/wac2/"

def commandCheck():
	f = open(directory + "command","r")
	command = f.read().strip("\n")
	f.close
	if not command == "":
		return command
		print "RECEIVED COMMAND: " + str(command)
	else:
		return null

while True:
	commandCheck()
