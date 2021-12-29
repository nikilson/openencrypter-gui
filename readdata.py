from os import listdir, path
from time import sleep
import tkinter
from tkinter import ttk
# from clearscreen import clean_shell, clear_clipboard
from pyperclip import copy as clipcopier
from threading import Thread
# path = "E:\\Productivity\\Documents\\sdrowssap\\Rinaldo"
def Reader(password, mydirectory):
    # clean_shell()
    global select_pass_text, directory, combo_box
    directory = mydirectory
    select_pass_text = 1
    # def select_drop(num):
    #     global select_pass_text
    #     select_pass_text = num
    my_list = []
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width="700", height="300")
    open_encrypter_gui_canvas.grid(columnspan=3, rowspan=4)
    welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Select your data", 
        relief="flat", font=("Arial", 25), padx=10)
    welcome_open_encrypter.grid(row=0, column=1)
    passwords_radio = tkinter.Radiobutton(open_encrypter_gui, text="Passwords", font=("Arial", 18), value=1, command=lambda: select_drop(1))
    passwords_radio.grid(row=1, column=0)
    text_radio = tkinter.Radiobutton(open_encrypter_gui, text="Texts", font=("Arial", 18), value=2, command=lambda: select_drop(2))
    text_radio.grid(row=1, column=1)
    # print("Press 1 >> Passwords\nPress 2 >> Plain Text\nPress 3 >> Quit")
    # select_pass_text = input("\nEnter your selection, Defualt(Passwords) : ")
    clip_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Copy to Clipboard", command=lambda: print("Login"))
    clip_btn.grid(row=2, column=2)
    show_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Show Everything", command=lambda: print("Login"))
    show_btn.grid(row=2, column=1)
    exit_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Exit", command=lambda: print("Login"))
    exit_btn.grid(row=2, column=0)
    combo_box = ttk.Combobox(open_encrypter_gui, width=20, font=("Arial", 18), values=my_list)
    combo_box.grid(row=3, column=0)
    private_key = path.join(directory, ".keys")
    private_key = private_key + "/private.key"
    def select_drop(num):
        global select_pass_text, directory, message_list, my_values, combo_box
        select_pass_text = num
        directory = mydirectory
        if select_pass_text == 2:
            directory = path.join(directory, ".text")
        elif select_pass_text == 3:
            directory = "exit"
        else:
            directory = path.join(directory, ".passwords")
        message_list = []
        my_values = []
        if directory != "exit":
            for file_det in listdir(directory):
                if file_det.endswith(".bin"):
                    message_list.append(file_det)
            for no, files in enumerate(message_list):      
                # Prints only text file present in My Folder
                # print(files[:-4], " >> " ,no)
                my_values.append(files[:4])
            print("exit - To go mainmenu")
            # selection = input("Please enter your selection : ")
        combo_box["values"] = my_values
    open_encrypter_gui.mainloop()
    try:
        selection = int(selection)
        if (len(message_list) >= selection) and len(message_list) >= 0:
            dir = path.join(directory, message_list[selection])
        else:
            if directory != "exit":
                print("Invalid selection")
        from decrypt import Decrypter
        decoded = Decrypter(message_list[selection][:-4], private_key, directory, password)
        clip_ask = input("Do you want to copy this to clipboard (Y or n) : ")
        if select_pass_text == 1:
            service_loc = decoded.find("|service ends the user is :")
            service_name = decoded[:service_loc]
            #print(decoded)
            #print(service_name)
            service_len = len("|service ends the user is :") + len(service_name)
            user_loc = decoded.find("|user ends the password is :")
            user_name = decoded[service_len:user_loc]
            #print(user_name)
            service_len = service_len + len(user_name) + len("|user ends the password is :")
            password_obtained = decoded[service_len:]
            #print(password_obtained)
            decoded = f"\nService : {service_name}\nUser Name : {user_name}"
            print_password = f"Password : {password_obtained}"
            state_text = "Password"
        else:
            state_text = "text"
            pass
        if clip_ask.lower() == "n":
            if select_pass_text == 1:
                print(decoded)
                print(print_password)
            else:
                print(decoded)
        else:
            if select_pass_text == 1:
                print(decoded)
                decoded = password_obtained
            clipcopier(decoded)
            clipclear_thread = Thread(target=clear_clipboard)
            clipclear_thread.start()
            print(f"The {state_text} is copied into the clipboard use it within 45 Seconds !!!")
        print("\nThe screen will be cleared within 30 Seconds!!!")
        sleep(30)
        # clean_shell()
    except:
        pass