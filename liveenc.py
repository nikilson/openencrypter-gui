from cryptography.fernet import Fernet
from time import sleep
# from clearscreen import clean_shell
from pyperclip import copy as clipcopier
from threading import Thread
from clearscreen import clear_clipboard
# from getpass import getpass
import tkinter
from tkinter import messagebox


user_name = ""
user_key = ""
def login_live():
    global my_text_input, my_hash_input, new_user
    # clean_shell()
    # print("press 1 for ENCRYPT\npress 2 for DECRYPT\npress 3 for EXIT\n")
    # ask_dec = input("\nPlease enter your selection : ")
    open_encrypter_gui_login = tkinter.Tk()
    open_encrypter_gui_login.title("Open Encrypter")
    Tk_Width = 1100 
    Tk_Height = 700

    #calculate coordination of screen and window form
    x_Left = int(open_encrypter_gui_login.winfo_screenwidth()/2 - Tk_Width/2)
    y_Top = int(open_encrypter_gui_login.winfo_screenheight()/2 - Tk_Height/2)
     
    # Write following format for center screen
    open_encrypter_gui_login.geometry( "%dx%d+%d+%d" % (Tk_Width, Tk_Height, x_Left, y_Top))
    open_encrypter_gui_login_canvas = tkinter.Canvas(open_encrypter_gui_login, width ="1100", height="700")
    open_encrypter_gui_login_canvas.grid(columnspan=4, rowspan=5)

    title_name_label = tkinter.Label(open_encrypter_gui_login, text="Live Encryption", relief="flat", font=("Arial", 25))
    my_text_label = tkinter.Label(open_encrypter_gui_login, text="Plain Text", relief="flat", font=("Arial", 16))
    my_text_input = tkinter.Text(open_encrypter_gui_login, bd=1, height=10, width=45, font=("Arial", 16))
    my_hash_label = tkinter.Label(open_encrypter_gui_login, text="Encrypted Hash", relief="flat", font=("Arial", 16))
    my_hash_input = tkinter.Text(open_encrypter_gui_login, bd=1, height=10, width=45, font=("Arial", 16))
    decrypt_btn = tkinter.Button(open_encrypter_gui_login, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Decrypt", command=lambda: live_decrypt_text())
    encrypt_btn = tkinter.Button(open_encrypter_gui_login, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Encrypt", command=lambda: live_encrypt_text())
    clear_btn = tkinter.Button(open_encrypter_gui_login, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Clear", command=lambda: clear_text())
    logout_btn = tkinter.Button(open_encrypter_gui_login, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Logout", command=lambda: go_back(open_encrypter_gui_login))
    title_name_label.grid(row=0, columnspan=4)
    my_text_label.grid(row=1, column=0)
    my_text_input.grid(row=1, column=1, columnspan=2, rowspan=2)
    my_hash_label.grid(row=3, column=0)
    my_hash_input.grid(row=3, column=1, columnspan=2, rowspan=2)
    decrypt_btn.grid(row=1, column=3)
    encrypt_btn.grid(row=2, column=3)
    clear_btn.grid(row=3, column=3)
    logout_btn.grid(row=4, column=3)

    open_encrypter_gui_login.mainloop()

def clear_text():
    global my_text_input, my_hash_input
    my_text_input.delete(1.0, "end")
    my_hash_input.delete(1.0, "end")

def live_encrypt_text():
    global new_user
    global my_text_input, my_hash_input
    plain_text = my_text_input.get(1.0, "end")
    gen_hash = new_user.encrypt(plain_text.encode('utf-8'))
    # print("Please note your encrypted message within 20 Seconds >>  {}".format(gen_hash.decode()))
    messagebox.showinfo("Copied", "Your hash is copied into the clipboard!!!")
    clipcopier(gen_hash.decode())
    my_hash_input.delete(1.0, "end")
    my_hash_input.insert(tkinter.END, gen_hash.decode())
    # sleep(20)
    # clipclear_thread = Thread(target=clear_clipboard)
    # clipclear_thread.start()
    # except:
    #     print("Sorry, The key is Invalid")
    #     sleep(5)
def live_decrypt_text():
    global my_text_input, my_hash_input, new_user
    try:
        read_token = my_hash_input.get(1.0, "end")
        read_token = read_token.encode()
        decoded = new_user.decrypt(read_token)
        decoded = decoded.decode()
        my_text_input.delete(1.0, "end")
        my_text_input.insert(tkinter.END, decoded)
        clipcopier(decoded)
        clipclear_thread = Thread(target=clear_clipboard)
        clipclear_thread.start()
        messagebox.showinfo("Copied!", message="The text is copied into the clipboard use it within 45 Seconds !!!")

    except Exception as e:
        print(e)
        messagebox.showerror("Wrong Hash!", message="Sorry, The Hash is Invalid!!!")

def generate_key():
    global gen_key_input
    key = Fernet.generate_key()
    # print("\nPlease Note down your private key within 30 Seconds!!!  {}".format(key.decode()))
    gen_key_input.insert(tkinter.END, key.decode())
    clipcopier(key.decode())
    messagebox.showinfo("Copied", message="Your key is copied into the clipboard!!!")
    # clear_text_box(gen_key_input)

def go_back(open_encrypter_gui):
    global status
    open_encrypter_gui.destroy()
    status = False
    from main import main_menu
    main_menu()

def clear_text_box(text_box):
    # global text_box
    clear_text_box_thread = Thread(target=lambda: text_box.delete(1.0, "end"))    
    sleep(30)
    clear_text_box_thread.start()

def live_main():
    global status, open_encrypter_gui, gen_key_input, user_key_input
    # clean_shell()
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui.title("Open Encrypter")
    Tk_Width = 1000 
    Tk_Height = 400

    #calculate coordination of screen and window form
    x_Left = int(open_encrypter_gui.winfo_screenwidth()/2 - Tk_Width/2)
    y_Top = int(open_encrypter_gui.winfo_screenheight()/2 - Tk_Height/2)
     
    # Write following format for center screen
    open_encrypter_gui.geometry( "%dx%d+%d+%d" % (Tk_Width, Tk_Height, x_Left, y_Top))
    open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width ="1000", height="400")
    open_encrypter_gui_canvas.grid(columnspan=3, rowspan=4)
    title_name_label = tkinter.Label(open_encrypter_gui, text="Live Encryption", relief="flat", font=("Arial", 25))
    login_key_label = tkinter.Label(open_encrypter_gui, text="Enter Your Key", relief="flat", font=("Arial", 18))
    gen_key_btn = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Generate Key", command=lambda: generate_key())
    login_key_btn = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Login With key", command=lambda: login_btn_func())
    exit_pass_btn = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Exit", command=lambda: go_back(open_encrypter_gui))
    gen_key_input = tkinter.Text(open_encrypter_gui, bd=1, height=1, width=45, font=("Arial", 16))
    user_key_input = tkinter.Entry(open_encrypter_gui, bd=1, width=45, font=("Arial", 16), show="*")
    title_name_label.grid(row=0, columnspan=3)
    gen_key_btn.grid(row=1, column=0)
    gen_key_input.grid(row=1, column=1, columnspan=2)
    login_key_label.grid(row=2, column=0)
    user_key_input.grid(row=2, column=1, columnspan=2)
    login_key_btn.grid(row=3, column=2)
    exit_pass_btn.grid(row=3, column=0)
    open_encrypter_gui.mainloop()
    # print("press 1 >> GENERATE KEY\npress 2 >> LOGIN\npress 3 >> MAINMENU")
    # ask_mode = input("\nPlease enter your selection : ")

def login_btn_func():
    global user_key_input, open_encrypter_gui, new_user
    key_input = user_key_input.get()
    # key_input = input("Please enter your secret key : ")
    try:
        new_user = Fernet(key_input)
        open_encrypter_gui.destroy()
        log_sts = login_live()

    except Exception as e:
        # print(e)
        messagebox.showerror("Invalid Key", message="Sorry, Invalid Key!!!")
if __name__ == '__main__':
    live_main()