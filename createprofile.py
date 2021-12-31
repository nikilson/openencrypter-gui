def Create_Profifle():
    from os import getcwd, mkdir, path, makedirs
    from time import sleep
    from pyperclip import copy as clipcopier
    from threading import Thread
    from clearscreen import clear_clipboard
    import tkinter
    from tkinter import messagebox
    #global check, user_name_copy
    #check = True
    def main_local():
        global check, user_name_copy, user_name, user_name_input, user_key_input, user_key_input2, user_name, password_1, password_2
        def go_back():
            global open_encrypter_gui, status
            open_encrypter_gui.destroy()
            status = False
            from main import main_menu
            main_menu()
        def submit():
            global open_encrypter_gui, user_name_input, user_key_input, user_name, password_1, user_key_input2, password_2
            user_name = user_name_input.get()
            password_1 = user_key_input.get()
            password_2 = user_key_input2.get()
            open_encrypter_gui.destroy()
            # print(user_name, user_key)
        global open_encrypter_gui, check
        open_encrypter_gui = tkinter.Tk()
        open_encrypter_gui.title("Open Encrypter")
        my_icon = path.join("assets", "key.png")
        my_icon = tkinter.PhotoImage(file = my_icon)
        open_encrypter_gui.iconphoto(False, my_icon)
        open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width ="600", height="400")
        # open_encrypter_gui.geometry("700x450")
        open_encrypter_gui_canvas.grid(columnspan=3, rowspan=4)
        welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Register New Profile", 
            relief="flat", font=("Arial", 25))
        user_name_label = tkinter.Label(open_encrypter_gui, text="User Name", relief="flat", font=("Arial", 22))
        user_name_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 18))
        user_key_label = tkinter.Label(open_encrypter_gui, text="Password", relief="flat", font=("Arial", 22))
        user_key_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 18), show="*")
        user_key_label2 = tkinter.Label(open_encrypter_gui, text=" Re Enter Password", relief="flat", font=("Arial", 22))
        user_key_input2 = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 18), show="*")
        quit_button = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="white", width=10, padx=2, pady=2, font=("Arial", 18), text="Quit", command=lambda: quit())
        go_back_button = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="white", width=10, padx=2, pady=2, font=("Arial", 18), text="Back", command=lambda: go_back())
        submit_button = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="white", width=10, padx=2, pady=2, font=("Arial", 18), text="Submit", command=lambda: submit())
        welcome_open_encrypter.grid(row=0, column=1)
        user_name_label.grid(row=1, column=0)
        user_name_input.grid(row=1, column=1, columnspan=2)
        user_key_label.grid(row=2, column=0)
        user_key_input.grid(row=2, column=1, columnspan=2)
        user_key_label2.grid(row=3, column=0)
        user_key_input2.grid(row=3, column=1, columnspan=2)
        quit_button.grid(row=4, column=0)
        go_back_button.grid(row=4, column=1)
        submit_button.grid(row=4, column=2)
        open_encrypter_gui.mainloop()   
        # check = path.isdir(directory)
        
    while True:
        main_local()
        if len(password_1) > 7:
            if password_1 == password_2:
                user_name_copy = user_name
                cwd = getcwd()
                user_directory = path.join(cwd ,".users")
                directory = path.join(user_directory, user_name)
                check = path.isdir(directory)
                # print(user_directory, user_name)
                if check == False:
                    try:
                        mkdir(user_directory)
                    except:
                        pass
                else:
                    messagebox.showwarning("User Exists", message="Sorry {} user already exist!!".format(user_name_copy))
                    continue
                break
            else:
                messagebox.showerror("Incorrect Password", message="Sorry, Please enter the same password!")
        else:
            messagebox.showwarning("Invalid Password", message="Your Password should have minimum 8 letters!")
    if check == False:
        # print(check)
        try:
            makedirs(directory, exist_ok = True)
            mkdir(directory + '/.text')
            mkdir(directory + '/.passwords')
            master_password = password_2
            from generatekey import Generate_RSA
            Generate_RSA(master_password, directory)
            messagebox.showinfo("User Created", message="New user {} has been created successfully".format(user_name_copy))
        except OSError as error:
            messagebox.showerror("Unkown Error", message="Operation failed due to some unexpected error!!!")
    else:
        messagebox.showwarning("User Exists", message="Sorry {} user already exist!!".format(user_name_copy))

if __name__ == '__main__':
    Create_Profifle()