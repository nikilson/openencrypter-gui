from cryptography.fernet import Fernet
from os import getcwd, path
from time import sleep
from clearscreen import clean_shell
user_name = ""
user_key = ""
new_user = ""
directory = getcwd()
def main_login():
    global user_name, user_key, new_user, directory, status, log_status
    #global user_name, user_key, new_user, directory
    def main():
        global user_name, user_key, new_user, directory, status, log_status
        print("exit << Go back to main")
        user_name = str(input("User Name : "))
        if user_name == "exit":
            status = False
        user_key = str(input("Key : "))
        # user_name = 'Test'
        user_name_copy = user_name
        directory = path.join(directory, user_name)
        check = path.isdir(directory)
        if check == False:
            print("User not available!!!")
            #status = False
        else:
            pass
        try:
            new_user = Fernet(user_key)
            valid_file = path.join(directory, 'validator.txt')
            valid_file = open(valid_file, 'rb')
            token_key = valid_file.read()
            valid_file.close()
        except:
            key_got = 0
        try:
            key_got = new_user.decrypt(token_key)
            key_got = key_got.decode()
        except:
            key_got = 0
        if key_got == user_key:
            clean_shell()
            print("Login Successfull!!!")
            log_status = True
            status = False
        else:
            clean_shell()
            log_status = False
            print("Incorrect key!!")
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
            writedata.datawriter(new_user, user_key, directory)
        elif select == '2':
            import readdata
            readdata.Reader(new_user, user_key, directory)
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
