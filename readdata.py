from os import listdir, path
from clearscreen import clean_shell, clear_clipboard
from pyperclip import copy as clipcopier
from threading import Thread
#path = "E:\\Productivity\\Documents\\sdrowssap\\Rinaldo"
def Reader(user, key, dir):
    clean_shell()
    print("exit - To go mainmenu")
    message_list = []
    for file_det in listdir(dir):
        if file_det.endswith(".txt") and (file_det != "validator.txt"):
            message_list.append(file_det)
    for no, files in enumerate(message_list):      
        # Prints only text file present in My Folder
        print(files[:-4], " >> " ,no)
    selection = input("Please enter your selection : ")
    try:
        selection = int(selection)
        if (len(message_list) >= selection) and len(message_list) >= 0:
            dir = path.join(dir, message_list[selection])
        else:
            print("Invalid selection")
        read_file = open(dir, "rb")
        read_token = read_file.read()
        read_file.close()
        decoded = user.decrypt(read_token)
        decoded = decoded.decode()
        clip_ask = input("Do you want to copy this to clipboard Default - No (Y or n) : ")
        if clip_ask.lower() == "y":
            clipcopier(decoded)
            clipclear_thread = Thread(target=clear_clipboard)
            clipclear_thread.start()
            print("The text is copied into the clipboard use it within 45 Seconds !!!")
        else:
            print(decoded)
    except:
        pass