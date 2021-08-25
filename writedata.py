def password_collect_service():
    from getpass import getpass
    while True:
        password_1 = getpass("\nPlease Enter your Password : ")
        password_2 = getpass("\nPlease Enter your Password Again: ")
        if password_1 == password_2:
            break
        else:
            print("Sorry, Please enter the same password!")
    return password_2
def create_password():
    service_name = input("Service Name or URL : ")
    user_name_service = input("User Name : ")
    clt_password = password_collect_service()
    message = f"{service_name}|service ends the user is :{user_name_service}|user ends the password is :{clt_password}"
    return message
def datawriter(user_name, user_key, directory):
    from clearscreen import clean_shell
    from os import getcwd, path
    clean_shell()
    cwd = getcwd()
    cwd = path.join(cwd, ".users")
    cwd = path.join(cwd, user_name)
    key_path = path.join(cwd, ".keys")
    pass_store_path = path.join(cwd, ".passwords")
    text_store_path = path.join(cwd, ".text")
    #print(cwd, key_path, pass_store_path)
    title = str(input("Enter the title : "))
    check_password = False
    check_password = input(f"Do you want to save {title} as a password!! Default No (Y or n) : ")
    if check_password.lower() == "y":
        store_path = pass_store_path
        message = create_password()
    else:
        message = str(input("Enter the mesaage : "))
        store_path = text_store_path
    clean_shell()
    #try:
    from encrypter import Encrypter
    #print(key_path)
    Encrypter(title, message, key_path + '/public.key', store_path)
    #enc_msg = user.encrypt(message.encode('utf-8')
    print("Message has been written successfully!!!")
    # except e as a Exception:
    #     print(e)
    #     print("Please try again!!!")

