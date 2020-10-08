import os
import random
import base64
import time

e_fname = "dump"
d_fname = None

while (True):
	os.system("title Login")
	os.system("cls")
	uname = input("User: ")
	pw = input("Pass: ")

	if (uname == "klump" and pw == "123"):
		os.system("cls")
		break
	else:
		pass
		os.system("cls")


def py_encrypt(key, msg, id):
	encrypted = []
	result = ""
	for i, c in enumerate(msg):
		key_c = ord(key[i % len(key)])
		msg_c = ord(c)
		msg_c = msg_c - key_c + id
		encrypted.append(chr((msg_c + key_c) % 127))
		result = ''.join(encrypted)
	return result


def py_decrypt(key, encrypted, id):
	msg = []
	for i, c in enumerate(encrypted):
		key_c = ord(key[i % len(key)])
		enc_c = ord(c)
		#print("ID: " + str(id))
		enc_c = enc_c + key_c - id
		msg.append(chr((enc_c - key_c) % 127))
		result = ''.join(msg)
	return result


def decrypt(key, string):
	t_start = time.process_time()
	# print("string: " + string)
	strId = string[:1]  # string identifier
	# print("strId CHR: " + strId)
	print("strId: " + str(strId))

	strId = ord(strId)
	strId = strId % 127

	string = string[1:]
	# print("string[1:]: " + string)

	_strResDec = ""
	for wrd in string:
		try:
			c = ord(wrd) - strId % 18
			try:
				c = chr(c)
			except:
				c = str(c)
			_strResDec += c
		except:
			c = int(wrd) - strId % 18
			try:
				c = chr(c)
			except:
				c = str(c)
			_strResDec += c
		#print("Strd " , strId)
		#print("Strd %", strId % 18)
		#print("RESULT | " + _strResDec)
	for char in _strResDec:
		#print("char: " + char)
		charInt = ord(char)
		charInt = charInt + strId
		string = _strResDec + chr(charInt)
		#print("string: " + string)
	string = py_decrypt(key, string, strId)
	#print("STRING: " + string)

	final = ""
	str_num = ""
	
	#errMsg_times = 0
	passed = True
	for num in string:
		if(passed == True):
			#print("num: " + num)
			if (num != ","):
				str_num = str_num + num
				#print(str_num)
			else:
				#print("str_num: " + str_num)
				try:
					charInt = int(str_num) + 13
					passed = True
				except:
					print("Decryption has failed")
					passed = False
				if(passed == True):
					#print("charInt: " + str(charInt))
					charStr = chr(charInt)
					final = final + charStr
					str_num = ""
	if(passed == True):

		# CMD CODE EXEC DOES NOT WORK - TO MUCH WORK TO DO

		codeExec = ""
		for car in final:
			# Get CMD code execute
			# Example code &* ECHO HELLO WORLD! *&
			if(car == "&"):
				if(car == "*"):
					# Check if code ends
					if(car == "*"):
						if(car == "&"):
							# Creates possible entry for new code in same string
							codeExec = ""
						else:
							codeExec += car
					else:
						codeExec += car
		#print("Codeexec: " + codeExec)
		final = final.replace("%S%", " ")
		print("\nFinal: " + final)
		print("\nText has been saved to --> output.txt")
		if('.' in d_fname):
			f = open(d_fname, "w")
		else:
			f = open("output.txt", "w")
		f.write(final)
		f.close()
		t_end = time.process_time() - t_start
		print("\r\n[----- Used " + str(t_end) + " seconds -----]")


def try_encryption(key, string, inputStr, strId):
	result = True
	print("Trying")
	os.system("title Trying Hash...")
	_strResDec = ""
	for wrd in string:
		try:
			c = ord(wrd) - strId % 18
			try:
				c = chr(c)
			except:
				c = str(c)
			_strResDec += c
		except:
			c = int(wrd) - strId % 18
			try:
				c = chr(c)
			except:
				c = str(c)
			_strResDec += c
		#print("RESULT | " + _strResDec)
	for char in _strResDec:
		# print("char: " + char)
		charInt = ord(char)
		charInt = charInt + strId
		string = _strResDec + chr(charInt)
		#print("string: " + string)
	string = py_decrypt(key, string, strId)
	#print("STRING: " + string)
	final = ""
	str_num = ""
	charInt = 0
	os.system("title Trying Hash...")
	for num in string:
		print("num: " + num)
		if (num != ","):
			str_num = str_num + num
			print(str_num)
		else:
			#print("str_num: " + str_num)
			try:
				charInt = int(str_num) + 13
			except ValueError:
				print("Restarting")
				# os.system("pause")
				os.system("title Restarting Encryption")
				time.sleep(3)
				os.system("cls")
				print("Found Error In Hash. Restarting Encryption")
				time.sleep(3)
				result = False
			#print("charInt: " + str(charInt))
			charStr = chr(charInt)
			final = final + charStr
			str_num = ""
			return result


def encrypt(key, string):
	t_start = time.process_time()
	inputStr = string
	os.system("title Encrypting")
	strId = random.randint(33, 126)
	#print("strId: " + str(strId))
	print("strId CHR: " + chr(strId))
	print("Encrypting String...")
	final = ""
	for char in string:
		#print("char: " + char)
		charInt = ord(char)
		charInt = charInt - 13
		final = final + str(charInt) + ","
		#print("NUM FINAL: " + final)

	final = py_encrypt(key, final, strId)
	result = ""
	for wrd in final:
		try:
			c = ord(wrd) + (strId % 18)
			try:
				c = chr(c)
			except:
				c = str(c)
			result += c
		except:
			c = int(wrd) + (strId % 18)
			try:
				c = chr(c)
			except:
				c = str(c)
			result += c
		#print("Strd " , strId)
		#print("Strd %", strId % 18)
	final = result
	try_enc = try_encryption(key, final, inputStr, strId)
	if (try_enc == False):
		encrypt(key, string)
	
	f = open(e_fname + ".alc", "wb")

	strId = chr(strId % 127)
	final_bytes = bytes(strId + final, "utf-8")
	f.write(final_bytes)
	f.close()
	print("\n\nBytes {" + str(final_bytes) + "}\n")
	print("\nFinal: " + final)
	print("\nHash has been saved to --> dump.alc")
	t_end = time.process_time() - t_start
	print("\r\n[----- Used " + str(t_end) + " seconds -----]")
	# os.system("cls")


def ocr(path, serialize):
	if (serialize == True):
		with open(path, "rb") as f:
			read = base64.b64encode(f.read())
			result = read.decode("utf-8")
	else:
		with open(path, "r") as f:
			result = f.read()
	# print("IMAGE: " + str(result))
	return result


while (True):
	os.system("title Alpha Crypt")
	eod = input("Encrypt Or Decrypt[E/D]: ")
	key = "12#obj84+\\"
	if (eod.lower() == "exit"):
		os.system("cls")
		exit(1)
	if (eod.lower() == "e"):
		isFileOrString = input("File or String?[F/S]: ")
		if (isFileOrString.lower() == "f"):
			file = input("File: ")
			while (True):
				serialized = input("Serialized object[True/False]: ")
				serialized = serialized.lower()
				if (serialized == "true" or serialized == "false"):
					break

			if (serialized == "true"):
				string = str(ocr(file, True))
			else:
				string = str(ocr(file, False))
			os.system("cls")
			e_fname = file
			encrypt(key, string)
		else:
			string = input("String: ")
			os.system("cls")
			encrypt(key, string)
	if (eod.lower() == "d"):
		os.system("cls")
		fIn = input(".alc File Name: ")
		d_fname = fIn
		fIn = fIn + ".alc"
		print(fIn)
		if (os.path.isfile(fIn)):
			f = open(fIn, "rb")
			read = f.read()
			try:
				read = read.decode("utf-8")
			except:
				print("Could Not Decode Cipher")
			decrypt(key, read)
		else:
			print("Can't Find File")
			os.system("pause")