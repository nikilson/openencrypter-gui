import tkinter


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
welcome_open_encrypter = tkinter.Label(top, text="Welcome to Open Encrypter!!!\n",
    relief="flat", font=("Arial", 22))
welcome_open_encrypter.pack()
home_b1 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Login", command=lambda: print("Login"))
home_b1.pack()
home_b2 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Register New Profile", command=lambda: print("Register"))
home_b2.pack()
home_b3 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Live Encryption", command=lambda: print("Live"))
home_b3.pack()
home_b4 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Quit", command=lambda: print("quit"))
home_b4.pack()
my_input = tkinter.Entry(top, width=30, font=("Arial", 18), show="*")
my_input.pack()
home_b5 = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Print", command=lambda: my_print())
home_b5.pack()
my_pass = tkinter.Entry(top, width=30, font=("Arial", 18), show="*")
my_pass.pack()
home_pass = tkinter.Button(top, width=30, padx=2, pady=2, font=("Arial", 18), text="Print", command=lambda: my_print())
home_pass.pack()
top.mainloop()
