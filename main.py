import base64
import os
import random
import time

e_fname = "dump"
d_fname = None


def py_encrypt(key, msg, strId):
    encrypted = []
    result = ""
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        msg_c = msg_c - key_c + strId
        encrypted.append(chr((msg_c + key_c) % 127))
        result = ''.join(encrypted)
    return result


def py_decrypt(key, encrypted, strId):
    msg = []
    for i, c in enumerate(encrypted):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        enc_c = enc_c + key_c - strId
        msg.append(chr((enc_c - key_c) % 127))
        result = ''.join(msg)
    return result


def decrypt(key, string, password):
    t_start = time.process_time()

    passKeyInt = 0
    for char in password:
        passKeyInt = passKeyInt + ord(char)

    _strResDec = ""
    for wrd in string:
        try:
            c = ord(wrd) - (passKeyInt % 18)
            try:
                c = chr(c)
            except:
                c = str(c)
            _strResDec += c
        except:
            c = int(wrd) - (passKeyInt % 18)
            try:
                c = chr(c)
            except:
                c = str(c)
            _strResDec += c

    string = py_decrypt(key, _strResDec, passKeyInt)
    # print("STRING: " + string)

    final = ""
    str_num = ""

    # errMsg_times = 0
    passed = True
    for num in string:
        if(passed == True):
            # print("num: " + num)
            if (num != ","):
                str_num = str_num + num
                # print(str_num)
            else:
                # print("str_num: " + str_num)
                try:
                    charInt = int(str_num) + 13
                    passed = True
                except:
                    print("Decryption has failed")
                    passed = False
                if(passed == True):
                    # print("charInt: " + str(charInt))
                    charStr = chr(charInt)
                    final = final + charStr
                    str_num = ""
    final = final.replace("%S%", " ")
    print("\nFinal: " + final)
    saveOutputFileName = f"{d_fname}.txt"
    if('.' in d_fname):
        saveOutputFileName = d_fname

    print(f"Save output to '{saveOutputFileName}'?")
    saveOutput = input("Save [y/N]: ")

    if(saveOutput.lower() == "y"):
        f = open(saveOutputFileName, "w")
        print(f"\nOutput has been saved to --> {saveOutputFileName}")
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
        # print("RESULT | " + _strResDec)
    for char in _strResDec:
        # print("char: " + char)
        charInt = ord(char)
        charInt = charInt + strId
        string = _strResDec + chr(charInt)
        # print("string: " + string)
    string = py_decrypt(key, string, strId)
    # print("STRING: " + string)
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
            # print("str_num: " + str_num)
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
            # print("charInt: " + str(charInt))
            charStr = chr(charInt)
            final = final + charStr
            str_num = ""
            return result


def encrypt(key, string, password):
    t_start = time.process_time()
    inputStr = string
    os.system("title Encrypting")
    print("Encrypting String...")
    final = ""
    for char in string:
        # print("char: " + char)
        charInt = ord(char)
        charInt = charInt - 13
        final = final + str(charInt) + ","
        # print("NUM FINAL: " + final)

    passKeyInt = 0
    for char in password:
        passKeyInt = passKeyInt + ord(char)

    final = py_encrypt(key, final, passKeyInt)
    result = ""
    for wrd in final:
        try:
            c = ord(wrd) + (passKeyInt % 18)
            try:
                c = chr(c)
            except:
                c = str(c)
            result += c
        except:
            c = int(wrd) + (passKeyInt % 18)
            try:
                c = chr(c)
            except:
                c = str(c)
            result += c
        # print("Strd " , strId)
        # print("Strd %", strId % 18)
    final = result
    try_enc = try_encryption(key, final, inputStr, passKeyInt)
    if (try_enc == False):
        encrypt(key, string, password)

    f = open(e_fname + ".alc", "wb")

    final_bytes = bytes(final, "utf-8")
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
    password = input("Password: ")
    key = "12#obj84+\\"
    if (eod.lower() == "exit"):
        os.system("cls")
        exit(1)
    if (eod.lower() == "e"):
        isFileOrString = input("File or String?[F/S]: ")
        if (isFileOrString.lower() == "f"):
            file = input("File: ")
            string = str(ocr(file, False))
            os.system("cls")
            e_fname = file
            encrypt(key, string, password)
        else:
            string = input("String: ")
            os.system("cls")
            encrypt(key, string, password)
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
            decrypt(key, read, password)
        else:
            print("Can't Find File")
            os.system("pause")