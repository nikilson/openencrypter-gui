#from cryptography.fernet import Fernet
def main_login():
    from decrypt import Decrypter
    from os import getcwd, path
    from time import sleep
    import writedata
    import readdata
    import deletedata
    # from clearscreen import clean_shell
    from getpass import getpass
    #global user_name, user_key, new_user, directory
    #global status, log_status, key_directory, key_got, token_key
    #global user_name, user_key, new_user, directory
    import tkinter
    from tkinter import messagebox
    global open_encrypter_main_menu_gui, directory
    global open_encrypter_gui, user_name_input, user_key_input, user_name, user_key, status, log_status
    # global user_name, user_key, new_user, directory, status
    # global log_status, key_directory, key_got, token_key
    status = True
    def kill_login():
        global log_status, open_encrypter_main_menu_gui
        open_encrypter_main_menu_gui.destroy()
        log_status = False
    def main_local():
        global user_name_input, user_key_input, open_encrypter_gui, log_status, user_name, user_key, status
        global directory
        user_name = ""
        user_key = ""
        new_user = ""
        directory = getcwd()
        open_encrypter_gui = tkinter.Tk()
        open_encrypter_gui.title("Open Encrypter")
        # my_icon1 = path.join("assets", "key.png")
        # my_icon1 = tkinter.PhotoImage(file = my_icon1)
        # open_encrypter_gui.iconphoto(False, my_icon1)
        open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width="700", height="300")
        open_encrypter_gui_canvas.grid(columnspan=3, rowspan=4)
        welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Login Menu", 
            relief="flat", font=("Arial", 25), padx=10)
        def go_back():
            global open_encrypter_gui, status
            open_encrypter_gui.destroy()
            status = False
            from main import main_menu
            main_menu()
        def submit():
            global open_encrypter_gui, user_name_input, user_key_input, user_name, user_key
            user_name = user_name_input.get()
            user_key = user_key_input.get()
            open_encrypter_gui.destroy()
            # print(user_name, user_key)
        user_name_label = tkinter.Label(open_encrypter_gui, text="User Name", relief="flat", font=("Arial", 22))
        user_name_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 18))
        user_key_label = tkinter.Label(open_encrypter_gui, text="Password", relief="flat", font=("Arial", 22))
        user_key_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 18), show="*")
        quit_button = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=10, padx=2, pady=2, font=("Arial", 18), text="Quit", command=lambda: quit())
        go_back_button = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=10, padx=2, pady=2, font=("Arial", 18), text="Back", command=lambda: go_back())
        submit_button = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=10, padx=2, pady=2, font=("Arial", 18), text="Submit", command=lambda: submit())
        welcome_open_encrypter.grid(row=0, column=1)
        user_name_label.grid(row=1, column=0)
        user_name_input.grid(row=1, column=1, columnspan=2)
        user_key_label.grid(row=2, column=0)
        user_key_input.grid(row=2, column=1, columnspan=2)
        quit_button.grid(row=3, column=0)
        go_back_button.grid(row=3, column=1)
        submit_button.grid(row=3, column=2)
        open_encrypter_gui.mainloop()
        # print("exit << Go back to main")
        user_name_copy = user_name
        directory = path.join(directory, ".users")
        directory = path.join(directory, user_name)
        key_directory = path.join(directory, ".keys")
        check = path.isdir(directory)
        if check == False:
            messagebox.showwarning("No User", message=f"User {user_name} not Found!!!")
            #status = False
        else:
            pass
        try:
            key_got = Decrypter("validator", key_directory + "/private.key", 
                key_directory, user_key)
            valid_file = open(key_directory + "/private.key", 'rb')
            token_key = valid_file.read().decode()
        except:
            try:
                messagebox.showerror("Key Error", message="Incorrect key!!")
                valid_file = open(key_directory + "/private.key", 'rb')
                token_key = valid_file.read().decode()
                key_got = 0
            except:
                key_got = 0
                token_key = None
        if key_got == token_key:
            # clean_shell()
            print("Login Successfull!!!")
            log_status = True
            status = False
        else:
            # sleep(4)
            # clean_shell()
            log_status = False
            directory = getcwd()
        #sleep(5)
    while status == True:
        main_local()
    while log_status:
        open_encrypter_main_menu_gui = tkinter.Tk()
        open_encrypter_main_menu_gui.title("Open Encrypter")
        # my_icon2 = path.join("assets", "key.png")
        # my_icon2 = tkinter.PhotoImage(file = my_icon2)
        # open_encrypter_main_menu_gui.iconphoto(False, my_icon2)
        open_encrypter_main_menu_gui_canvas = tkinter.Canvas(open_encrypter_main_menu_gui, width="700", height="450")
        open_encrypter_main_menu_gui_canvas.grid(columnspan=1, rowspan=6)
        main_menu_open_encrypter = tkinter.Label(open_encrypter_main_menu_gui, text=f"Welcome {user_name}!!", 
            relief="flat", font=("Arial", 25), padx=10)
        writedata_b = tkinter.Button(open_encrypter_main_menu_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Write Data", command=lambda: writedata.datawriter(user_name, user_key, directory))
        # print("press 1 for WRITE new data\npress 2 for READ old data\npress 3 for REMOVE old data\npress 4 for QUIT")
        readdata_b = tkinter.Button(open_encrypter_main_menu_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Read Data", command=lambda: readdata.Reader(user_key, directory))
        deletedata_b = tkinter.Button(open_encrypter_main_menu_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Delete Data", command=lambda: deletedata.text_deleter(new_user, user_key, directory))
        Logout_b = tkinter.Button(open_encrypter_main_menu_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Log out", command=lambda: kill_login())
        main_menu_open_encrypter.grid(row=0, column=0)
        readdata_b.grid(row=1, column=0)
        writedata_b.grid(row=2, column=0)
        deletedata_b.grid(row=3, column=0)
        Logout_b.grid(row=4, column=0)
        open_encrypter_main_menu_gui.mainloop()
        # select = str(input("Your option : "))
        # if select == '1':
        #     import writedata
        #     writedata.datawriter(user_name, user_key, directory)
        # elif select == '2':
        #     import readdata
        #     readdata.Reader(user_key, directory)
        # elif select == '3':
        #     import deletedata
        #     deletedata.text_deleter(new_user, user_key, directory)
        # elif select == '4':
        #     break
        # else:
        #     print("Retry!!!")
    return status
if __name__ == '__main__':
    main_login()
