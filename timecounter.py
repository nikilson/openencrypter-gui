import tkinter
from tkinter import ttk

top = tkinter.Tk()
top.geometry("700x450")
# welcome_open_encrypter_string = tkinter.StringVar()
# welcome_open_encrypter_string.set("Welcome to Open Encrypter!!!")

#welcome_open_encrypter = tkinter.Label(top, textvariable=welcome_open_encrypter_string,
#    relief="flat")
def font_style():
    print("HI")
def my_print():
    global my_input
    print(my_input.get())
# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)
welcome_open_encrypter = tkinter.Label(top, text="Welcome to Open Encrypter!!!\n",
    relief="flat", font=("Arial", 22))
welcome_open_encrypter.pack()
home_b1 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Login", command=lambda: combo_picker())
home_b1.pack()
home_b2 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Register New Profile", command=lambda: print("Register"))
home_b2.grid()
home_b3 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Live Encryption", command= lambda: home_b2.pack_forget())
home_b3.pack()
home_b4 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Quit", command=lambda: print("quit"))
home_b4.pack()
# my_input = tkinter.Entry(top, width=30, font=("Arial", 18), show="*")
# my_input.pack()
# home_b5 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Print", command=lambda: my_print())
# home_b5.pack()
# my_pass = tkinter.Entry(top, width=30, font=("Arial", 18), show="*")
# my_pass.pack()
# home_pass = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Print", command=lambda: my_print())
# home_pass.pack()
var = tkinter.IntVar()
my_list = ["January", "Thursday", "Wednesday", "Friday"]
def list_sel(num):
    global my_list, comboExample
    if num == 1:
        comboExample["values"] = ["January", "Thursday", "Wednesday", "Friday"]
    elif num == 2:
        comboExample["values"] = ["Apple", "Mango", "Papaya", "Strawberry"]
    else:
        comboExample["values"] = ["Spiderman", "Ironman", "Thor", "Captain America"]
    # comboExample = ttk.Combobox(top, values=my_list, postcommand=lambda: print(0))
    # comboExample.pack()
def combo_picker():
    global comboExample
    print(comboExample.get())
R1 = tkinter.Radiobutton(top, text="Option 1", variable=var, value=1, command=lambda: list_sel(1))
R1.pack( anchor = tkinter.W )
R2 = tkinter.Radiobutton(top, text="Option 2", variable=var, value=2, command=lambda: list_sel(2))
R2.pack( anchor = tkinter.W )
R3 = tkinter.Radiobutton(top, text="Option 3", variable=var, value=3, command=lambda: list_sel(3))
R3.pack( anchor = tkinter.W)
comboExample = ttk.Combobox(top, width=20, font=("Arial", 18), values=my_list)
# comboExample.config(font="helv20")
top.option_add('*TCombobox*Listbox.font', ("Arial", 18))
comboExample.pack()
text_box = tkinter.Text(top, height=10, width=30, padx=10, pady=10, font=("Arial", 14))
text_box.insert(tkinter.END, "First text is hello")
text_box.insert(tkinter.END, "\nSecond text is welcome")
from time import sleep
from threading import Thread
def clear_text_box():
    global text
    sleep(5)
    text_box.delete(1.0, "end")
clear_text_box_thread = Thread(target=clear_text_box)
clear_text_box_thread.start()
text_box.pack()
top.mainloop()