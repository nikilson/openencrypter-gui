from cryptography.fernet import Fernet
from os import getcwd, path
from time import sleep
user_name = ""
user_key = ""
new_user = ""
directory = getcwd()
def main():
    global status, user_name, user_key, new_user, directory
    user_name = str(input("User Name : "))
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
    new_user = Fernet(user_key)
    valid_file = path.join(directory, 'validator.txt')
    valid_file = open(valid_file, 'rb')
    token_key = valid_file.read()
    valid_file.close()
    try:
        key_got = new_user.decrypt(token_key)
        key_got = key_got.decode()
    except:
        key_got = 0
    if key_got == user_key:
        print("Login Suceessfull!!!")
        status = False
    else:
        print("Incorrect key!!")
    #sleep(5)
status = True
while status == True:
    main()
while True:
    print("press 1 for WRITE new data\npress 2 for READ old data\npress 3 for QUIT")
    select = str(input("Your option : "))
    if select == '1':
        import writedata
        writedata.datawriter(new_user, user_key, directory)
    elif select == '2':
        import readdata
        readdata.Reader(new_user, user_key, directory)
    elif select == '3':
        break
    else:
        print("Retry!!!")