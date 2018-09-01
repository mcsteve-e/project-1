import EBox
import sys
import os
import traceback

def encryptFile(filename):
	if not filename.endswith(".txt"):
		print("The name of the file must end in .txt")
		return
	if not os.path.isfile(filename):
		print("This file does not exist")
		return
	else:
		newfilename = filename[0:-4] + "-encrypted.txt"
		ebox.restart()
		with open(filename) as f:
			text = f.read()
		fnew = open(newfilename, "w")
		for line in text.split("\n"):
			encline = ebox.encrypt(line)
			fnew.write(encline)
		fnew.close()

def decryptFile(filename):
	if not filename.endswith(".txt"):
		print("The name of the file must end in .txt")
		return
	if not os.path.isfile(filename):
		print("This file does not exist")
		return
	else:
		if filename.endswith("-encrypted.txt"):
			newfilename = filename[0:-14] + "-decrypted.txt"
		else:
			newfilename = filename[0:-4] + "-dcrypted.txt"
		ebox.restart()
		with open(filename) as f:
			text = f.read()
		fnew = open(newfilename, "w")
		for line in text.split("\n"):
			encline = ebox.decrypt(line)
			fnew.write(encline)
		fnew.close()

password = ""          #input("Enter your password:")

ebox = EBox.EBox()
mode = "encrypt"
level = 0

while (True):
	try:
		line = input("? ")
		if line == "quit": break
		if line.startswith("e "):
			if password == "":
				password = input("Enter your password:")
				ebox.set_password(password) 
			print(ebox.encrypt(line[2:]))
		elif line.startswith("ef"):
			if password == "":
				password = input("Enter your password:")
				ebox.set_password(password) 
			mode = "encrypt"
			ebox.reset("encrypt", level)
			encryptFile(line[3:])
		elif line.startswith("d "):
			if password == "":
				password = input("Enter your password:")
				ebox.set_password(password) 
			print(ebox.decrypt(line[2:]))
		elif line.startswith("df"):
			if password == "":
				password = input("Enter your password:")
				ebox.set_password(password) 
			mode = "decrypt"
			ebox.reset("decrypt", level)
			decryptFile(line[3:])
		elif line == "reset":
			ebox.reset(mode, level)
		elif line == "mode encrypt":
			ebox.reset("encrypt", level)
			mode = "encrypt"
		elif line == "mode decrypt":
			ebox.reset("decrypt", level)
			mode = "decrypt"
		elif line.startswith("level "):
			level = int(line[6:])
			ebox.reset(mode, level)
		elif line.startswith("password "):
			ebox.set_password(line[9:])
		elif line == "status":
			retval = ebox.get_status()
			print("Mode:",retval[0])
			print("Level:", retval[1])
			print("password length:",retval[2])
			print("Number of chars processed since last reset:",retval[3])
		elif line == "help":
			print("e ....   -- encrypt a line")
			print("ef filename -- encrypt a whole file")
			print("d ....   -- decrypt a line")
			print("df filename -- decrypt a whole file")
			print("reset -- reset the system, clear out the number of characters processed")
			print("mode encrypt -- start encryption")
			print("mode decrypt -- start decryption")
			print("password ... -- change the password")
			print("level ... -- set the level (must be 0 or 1)")
			print("status -- get information about the system") 
			print("quit -- quit this application")
		elif line.startswith("debug"):
			if line == "debug":
				ebox._debug = True
			elif line == "debug off":
				ebox._debug = False
			elif line == "debug on":
				ebox._debug = True
		elif line.startswith("#"):
			print(eval(line[1:]))
		elif line.startswith("!"):
			os.system(line[1:])
		else:
			print("Unknown command!")
	except Exception as e:
		tb = traceback.format_exc()
		print("Caught a run-time error and recovered from it.")
		print(e.__class__.__name__, end=", ")
		print(e)
		print(tb)
		


		