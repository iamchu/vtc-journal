# minimalist journaling app
# * handle multiple lines
# + change file name for day only and separate appending and etc by time that entry was created.
# don't ask for appending if file already exists, just append already to the damn thing!

import os
import time

def createTxt():
	user_input = ""
	# wb+: w for writing permission. b is to specify that its a binary file. the + is to create if it doesnt exists
	# if file already exists:
	if(os.path.isfile(time.strftime("%d-%m-%Y"))):
		print "File already exists. Will append entry."
		my_file = open(time.strftime("%d-%m-%Y"), "ab+")
		is_appending = True
	# if file does not exists yet
	else: 
		my_file = open(time.strftime("%d-%m-%Y"), "wb+")
		is_appending = False
	return is_appending, my_file

def writeToFile(is_appending, my_file):

	if(is_appending):
		print "Appending for file " + time.strftime("%d/%m/%Y") + ":"

	print "Entry for " + time.strftime("%d/%m/%Y") + ":"

	lines = []
	while True:
	    line = raw_input()
	    if line:
	        lines.append(line)
	    else:
	        break
	user_entry = '\n'.join(lines)

	if(is_appending):
		user_entry = "\n\n" + user_entry

	my_file.write(user_entry)
	my_file.close()

	print "Sucess. Now exiting app..."
	messageExit()

def messageExit():
	print "Exited application."

def main():
	is_appending, my_file = createTxt()
	writeToFile(is_appending, my_file)

main()