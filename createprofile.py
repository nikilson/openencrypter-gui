from cryptography.fernet import Fernet
from os import getcwd, path, makedirs
from time import sleep
from pyperclip import copy as clipcopier
from threading import Thread
from clearscreen import clear_clipboard
key = Fernet.generate_key()
new_user = Fernet(key)
user_name = str(input("Please Enter the User Name : "))
user_name_copy = user_name
cwd = getcwd()
directory = path.join(cwd, user_name)
check = path.isdir(directory)
def createcheck(new_user, key, dir):
    password = new_user.encrypt(key)
    dir = path.join(dir, "validator.txt")
    checker = open(dir, "wb")
    checker.write(password)
    checker.close()
if check == False:
    try:
        makedirs(directory, exist_ok = True)
        print("New user {} has been created successfully".format(user_name_copy))
        print("\nPlease Note down your private key within 30 Seconds!!!  {}".format(key.decode()))
        print("\nYour key is copied into the clipboard use it within 75 Seconds!!!")
        clipcopier(key.decode())
        createcheck(new_user, key, directory)
        sleep(30)
        clipclear_thread = Thread(target=clear_clipboard)
        clipclear_thread.start()
    except OSError as error:
        print("Operation failed due to some unexpected error!!!")
        sleep(10)
else:
    print("Sorry {} user already exist!!".format(user_name_copy))
    sleep(10)

