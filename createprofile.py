def Create_Profifle():
    from os import getcwd, mkdir, path, makedirs
    from time import sleep
    from pyperclip import copy as clipcopier
    from threading import Thread
    from clearscreen import clear_clipboard
    from getpass import getpass
    user_name = str(input("Please Enter the User Name : "))
    user_name_copy = user_name
    cwd = getcwd()
    user_directory = path.join(cwd ,".users")
    check = path.isdir(user_directory)
    if check == False:
        mkdir(user_directory)
    else:
        pass
    directory = path.join(user_directory, user_name)
    check = path.isdir(directory)
    def password_collect():
        while True:
            password_1 = getpass("\nPlease Enter your Master Password : ")
            if len(password_1) > 7:
                password_2 = getpass("\nPlease Enter your Master Password Again: ")
                if password_1 == password_2:
                    break
                else:
                    print("Sorry, Please enter the same password!")
            else:
                print("Your Password should have minimum 8 letters!")
        return password_2
    if check == False:
        try:
            makedirs(directory, exist_ok = True)
            mkdir(directory + '/.text')
            mkdir(directory + '/.passwords')
            master_password = password_collect()
            from generatekey import Generate_RSA
            Generate_RSA(master_password, directory)
            print("New user {} has been created successfully".format(user_name_copy))
            sleep(10)
        except OSError as error:
            print("Operation failed due to some unexpected error!!!")
            sleep(10)
    else:
        print("Sorry {} user already exist!!".format(user_name_copy))
        sleep(10)

if __name__ == '__main__':
    Create_Profifle()