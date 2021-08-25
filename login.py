#from cryptography.fernet import Fernet
from decrypt import Decrypter
from os import getcwd, path
from time import sleep
from clearscreen import clean_shell
from getpass import getpass
user_name = ""
user_key = ""
new_user = ""
directory = getcwd()

def main_login():
    global user_name, user_key, new_user, directory
    global status, log_status, key_directory, key_got, token_key
    #global user_name, user_key, new_user, directory
    def main():
        global user_name, user_key, new_user, directory, status
        global log_status, key_directory, key_got, token_key
        clean_shell()
        print("exit << Go back to main")
        user_name = str(input("User Name : "))
        if user_name == "exit":
            status = False
        user_key = str(getpass("Password : "))
        # user_name = 'Test'
        user_name_copy = user_name
        directory = path.join(directory ,".users")
        directory = path.join(directory, user_name)
        key_directory = path.join(directory, ".keys")
        check = path.isdir(directory)
        if check == False:
            print("User not available!!!")
            #status = False
        else:
            pass
        try:
            #new_user = Fernet(user_key)
            #valid_file = path.join(key_directory, 'validator.bin')
            #master_password = password_collect()
            key_got = Decrypter("validator", key_directory + "/private.key", 
                key_directory, user_key)
            valid_file = open(key_directory + "/private.key", 'rb')
            token_key = valid_file.read().decode()
            #valid_file.close()
            #key_got = 1
        except:
            #print("Incorrect password")
            try:
                print("Incorrect key!!")
                valid_file = open(key_directory + "/private.key", 'rb')
                token_key = valid_file.read().decode()
                key_got = 0
            except:
                key_got = 0
                token_key = None
        if key_got == token_key:
            clean_shell()
            print("Login Successfull!!!")
            log_status = True
            status = False
        else:
            sleep(4)
            clean_shell()
            log_status = False
            directory = getcwd()
    #sleep(5)
    status = True
    while status == True:
        main()
    while log_status:
        print("press 1 for WRITE new data\npress 2 for READ old data\npress 3 for REMOVE old data\npress 4 for QUIT")
        select = str(input("Your option : "))
        if select == '1':
            import writedata
            writedata.datawriter(user_name, user_key, directory)
        elif select == '2':
            import readdata
            readdata.Reader(user_key, directory)
        elif select == '3':
            import deletedata
            deletedata.text_deleter(new_user, user_key, directory)
        elif select == '4':
            break
        else:
            print("Retry!!!")
    return status
if __name__ == '__main__':
    main_login()
