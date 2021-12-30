from os import listdir, path
from time import sleep
import tkinter
from tkinter import ttk
from tkinter import messagebox
from clearscreen import clean_shell, clear_clipboard
from pyperclip import copy as clipcopier
from threading import Thread
# path = "E:\\Productivity\\Documents\\sdrowssap\\Rinaldo"
def Reader(password, mydirectory):
    # clean_shell()
    global select_pass_text, directory, combo_box, text_box, open_encrypter_gui
    directory = mydirectory
    select_pass_text = 1
    # def select_drop(num):
    #     global select_pass_text
    #     select_pass_text = num
    def exit_func():
        global open_encrypter_gui, select_pass_text
        select_pass_text = 3
        open_encrypter_gui.destroy()
    def clip_ask_fun(ask):
        global clip_ask
        clip_ask = ask
    my_list = []
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui.title("Open Encrypter")
    open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width="700", height="300")
    open_encrypter_gui_canvas.grid(columnspan=3, rowspan=3)
    var = tkinter.IntVar()
    welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Select your data", 
        relief="flat", font=("Arial", 25), padx=10)
    welcome_open_encrypter.grid(row=0, column=1)
    passwords_radio = tkinter.Radiobutton(open_encrypter_gui, variable=var, text="Passwords", font=("Arial", 18), value=1, command=lambda: select_drop(1))
    passwords_radio.grid(row=1, column=0)
    text_radio = tkinter.Radiobutton(open_encrypter_gui, variable=var, text="Texts", font=("Arial", 18), value=2, command=lambda: select_drop(2))
    text_radio.grid(row=1, column=1)
    # print("Press 1 >> Passwords\nPress 2 >> Plain Text\nPress 3 >> Quit")
    # select_pass_text = input("\nEnter your selection, Defualt(Passwords) : ")
    clip_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Copy to Clipboard", command=lambda: butn_decrypt("y"))
    clip_btn.grid(row=4, column=2)
    show_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Show Everything", command=lambda: butn_decrypt("n"))
    show_btn.grid(row=4, column=1)
    exit_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Exit", command=lambda: exit_func())
    exit_btn.grid(row=4, column=0)
    combo_box = ttk.Combobox(open_encrypter_gui, width=40, font=("Arial", 18), values=my_list)
    open_encrypter_gui.option_add('*TCombobox*Listbox.font', ("Arial", 18))
    combo_box.grid(row=2, columnspan=3)
    text_box = tkinter.Text(open_encrypter_gui, height=10, width=60, padx=10, pady=10, font=("Arial", 14))
    text_box.grid(row=3, columnspan=3)
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
                my_values.append(files[:-4])
            # print("exit - To go mainmenu")
            # selection = input("Please enter your selection : ")
        #  print(my_values)
        combo_box["values"] = my_values
    def butn_decrypt(clip_ask):
        try:
            dir = path.join(directory, combo_box.get() + ".bin")
            from decrypt import Decrypter
            decoded = Decrypter(combo_box.get(), private_key, directory, password)
            # clip_ask = input("Do you want to copy this to clipboard (Y or n) : ")
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
                print_password = f"\nPassword : {password_obtained}"
                state_text = "Password"
            else:
                state_text = "text"
                pass
            if clip_ask.lower() == "n":
                if select_pass_text == 1:
                    text_box.insert(tkinter.END, decoded)
                    text_box.insert(tkinter.END, print_password)
                else:
                    text_box.insert(tkinter.END, decoded)
            else:
                text_box.insert(tkinter.END, decoded)
                if select_pass_text == 1:
                    decoded = password_obtained
                clipcopier(decoded)
                clipclear_thread = Thread(target=clear_clipboard)
                clipclear_thread.start()
                text_box.insert(tkinter.END, f"\nThe {state_text} is copied into the clipboard use it within 45 Seconds !!!\n")
            text_box.insert(tkinter.END, "\n\nThe screen will be cleared within 30 Seconds!!!\n")
            def clear_text_box():
                global text_box
                sleep(30)
                text_box.delete(1.0, "end")
            clear_text_box_thread = Thread(target=clear_text_box)
            clear_text_box_thread.start()
            # open_encrypter_gui.destroy()
            open_encrypter_gui.mainloop()
        except:
            pass