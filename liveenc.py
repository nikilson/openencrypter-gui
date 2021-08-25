from cryptography.fernet import Fernet
from time import sleep
from clearscreen import clean_shell
from pyperclip import copy as clipcopier
from threading import Thread
from clearscreen import clear_clipboard
from getpass import getpass
user_name = ""
user_key = ""
def login_live(new_user):
    clean_shell()
    print("press 1 for ENCRYPT\npress 2 for DECRYPT\npress 3 for EXIT\n")
    ask_dec = input("\nPlease enter your selection : ")
    try:
        ask_dec = int(ask_dec)
    except:
        ask_dec = 0
    if ask_dec == 1:
        login_status = True
        # try:
        plain_text = input("\nPlease enter the text you want to ENCRYPT : ")
        gen_hash = new_user.encrypt(plain_text.encode('utf-8'))
        print("Please note your encrypted message within 20 Seconds >>  {}".format(gen_hash.decode()))
        print("\nYour hash is copied into the clipboard!!!")
        clipcopier(gen_hash.decode())
        sleep(20)
        # clipclear_thread = Thread(target=clear_clipboard)
        # clipclear_thread.start()
        # except:
        #     print("Sorry, The key is Invalid")
        #     sleep(5)
    elif ask_dec == 2:
        login_status = True
        try:
            read_token = input("\nPlease enter your hash or encrypted text : ")
            read_token = read_token.encode()
            decoded = new_user.decrypt(read_token)
            decoded = decoded.decode()
            clip_ask = input("Do you want to copy this to clipboard Default - No (Y or n) : ")
            if clip_ask.lower() == "y":
                clipcopier(decoded)
                clipclear_thread = Thread(target=clear_clipboard)
                clipclear_thread.start()
                print("The text is copied into the clipboard use it within 45 Seconds !!!")
                sleep(10)
            else:
                print("\nNote the text within 45 Seconds")
                print(decoded)
                sleep(45)
        except:
            print("\nSorry, The key is Invalid")
            sleep(5)
    elif ask_dec == 3:
        login_status = False
    else:
        login_status = True
        print("\nInvalid selection!!!")
    return login_status
def generate_key():
    key = Fernet.generate_key()
    print("\nPlease Note down your private key within 30 Seconds!!!  {}".format(key.decode()))
    print("\nYour key is copied into the clipboard!!!")
    clipcopier(key.decode())
    sleep(30)
    live_main()
def live_main():
    global status
    def main():
        global status
        clean_shell()
        print("press 1 >> GENERATE KEY\npress 2 >> LOGIN\npress 3 >> MAINMENU")
        ask_mode = input("\nPlease enter your selection : ")
        try:
            ask_mode = int(ask_mode)
        except:
            ask_mode = 0
        if ask_mode == 1:
            generate_key()
        elif ask_mode == 2:
            clean_shell()
            key_input = input("Please enter your secret key : ")
            try:
                new_user = Fernet(key_input)
                while True:
                    log_sts = login_live(new_user)
                    if log_sts == False:
                        break
                    else:
                        pass
            except:
                sleep(4)
                print("Sorry, Try again!!!")
        elif ask_mode == 3:
            status = False
        else:
            print("Invalid selection!!!")
            sleep(3)
    status = True
    while status == True:
        if status == False:
            break
        else:
            pass
        main()

if __name__ == '__main__':
    live_main()