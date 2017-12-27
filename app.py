# minimalist journaling app
# change file name for day only and separate appending and etc by time that entry was created.
import os
import time

def returnTimeNow(separator):
	return time.strftime("%d-%m-%Y") + "_" + time.strftime("%Hh%M")

def checkForFileAndReturnAppropriateInput(user_input):
	if(user_input == "A" or user_input == "a"):
		# append data to file...
		return open(time.strftime("%d-%m-%Y") + "_" + time.strftime("%Hh%M"), "ab+")
	elif(user_input == "O" or user_input == "o"):
		# overwrite the file...
		return open(time.strftime("%d-%m-%Y") + "_" + time.strftime("%Hh%M"), "wb+")
	elif(user_input == "N" or user_input == "n"):
		# do nothing and exit app
		return None
	else:
		checkForFileAndReturnAppropriateInput(user_input)

def createTxt():
	user_input = ""
	# wb+: w for writing permission. b is to specify that its a binary file. the + is to create if it doesnt exists
	# if file already exists:
	if(os.path.isfile(time.strftime("%d-%m-%Y") + "_" + time.strftime("%Hh%M"))):
		print "File already exists. Would you like to (A)ppend data, (O)verwrite it or do (N)othing?"
		user_input = raw_input()
		my_file = checkForFileAndReturnAppropriateInput(user_input)
	# if file does not exists yet
	else: 
		my_file = open(time.strftime("%d-%m-%Y") + "_" + time.strftime("%Hh%M"), "wb+")
	return user_input, my_file

def writeToFile(user_input, my_file):
	print "Entry for " + time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M") + ":"
	user_entry = raw_input()
	if(user_input == "A" or user_input == "a"):
		user_entry = "\n" + user_entry
	my_file.write(user_entry)
	my_file.close()
	print "Sucess. Now exiting app..."
	messageExit()


def messageExit():
	print "Exited application."

def main():
	user_input, my_file = createTxt()
	if(user_input == "N" or user_input == "n"):
		messageExit()
	else:
		writeToFile(user_input, my_file)

main()