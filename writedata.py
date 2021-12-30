import tkinter
from tkinter import messagebox

def text_writer():
    global store_path, text_store_path, text_input, submit_text_btn, exit_btn
    store_path = text_store_path
    text_input.grid(row=3, column=0, columnspan=3)
    exit_btn.grid(row=4, column=0)
    submit_text_btn.grid(row=4, column=2)
def password_collect_service():
    global user_key_input, user_key_input2, store_path, pass_store_path, message
    store_path = pass_store_path
    password_1 = user_key_input.get()
    password_2 = user_key_input2.get()
    if password_1 == password_2:
        message = password_2
    else:
        messagebox.showerror("Password Error", message="Sorry, Please enter the same password!")
def create_password():
    global service_name_input, service_name_label, submit_pass_btn, exit_btn, text_input, submit_text_btn
    try:
        submit_text_btn.pack_forget()
        text_input.pack_forget()
    except:
        pass
    service_name_label.grid(row=3, column=0)
    service_name_input.grid(row=3, column=1, columnspan=2)
    global user_key_label, user_key_label2, user_key_input, user_key_input2
    user_key_label.grid(row=4, column=0)
    user_key_input.grid(row=4, column=1, columnspan=2)
    user_key_label2.grid(row=5, column=0)
    user_key_input2.grid(row=5, column=1, columnspan=2)
    exit_btn.grid(row=6, column=0)
    submit_pass_btn.grid(row=6, column=2)
    # service_name = input("Service Name or URL : ")
    # user_name_service = input("User Name : ")
    clt_password = password_collect_service()
    message = f"{service_name}|service ends the user is :{user_name_service}|user ends the password is :{clt_password}"
    return message
def datawriter(user_name, user_key, directory):
    global store_path, text_store_path, pass_store_path, message, text_input, submit_text_btn, submit_pass_btn, exit_btn
    global service_name_input, service_name_label, user_key_label, user_key_label2, user_key_input, user_key_input2
    from clearscreen import clean_shell
    from os import getcwd, path
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width ="600", height="700")
    # open_encrypter_gui.geometry("700x450")
    open_encrypter_gui_canvas.grid(columnspan=3, rowspan=7)
    var = tkinter.IntVar()
    welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Write Data", 
        relief="flat", font=("Arial", 25))
    title_name_label = tkinter.Label(open_encrypter_gui, text="Title", relief="flat", font=("Arial", 16))
    title_name_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 16))
    passwords_radio = tkinter.Radiobutton(open_encrypter_gui, variable=var, text="Passwords", font=("Arial", 16), value=1, command=lambda: create_password())
    text_radio = tkinter.Radiobutton(open_encrypter_gui, variable=var, text="Texts", font=("Arial", 16), value=2, command=lambda: text_writer())
    service_name_label = tkinter.Label(open_encrypter_gui, text="Service Name or URL", relief="flat", font=("Arial", 16))
    service_name_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 16))
    user_key_label = tkinter.Label(open_encrypter_gui, text="Password", relief="flat", font=("Arial", 16))
    user_key_input = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 16), show="*")
    user_key_label2 = tkinter.Label(open_encrypter_gui, text=" Re Enter Password", relief="flat", font=("Arial", 16))
    user_key_input2 = tkinter.Entry(open_encrypter_gui, bd=1, width=30, font=("Arial", 16), show="*")
    submit_pass_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Write Password", command=lambda: password_collect_service())
    submit_text_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Write Text", command=lambda: text_writer())
    exit_btn = tkinter.Button(open_encrypter_gui, width=20, padx=2, pady=2, font=("Arial", 18), text="Exit", command=lambda: print("exit"))
    text_input = tkinter.Text(open_encrypter_gui, bd=1, height=15, width=40, font=("Arial", 16))
    welcome_open_encrypter.grid(row=0, column=1)
    title_name_label.grid(row=1, column=0)
    title_name_input.grid(row=1, column=1, columnspan=2)
    text_radio.grid(row=2, column=1)
    passwords_radio.grid(row=2, column=0)
    # clean_shell()
    cwd = getcwd()
    cwd = path.join(cwd, ".users")
    cwd = path.join(cwd, user_name)
    key_path = path.join(cwd, ".keys")
    pass_store_path = path.join(cwd, ".passwords")
    text_store_path = path.join(cwd, ".text")
    #print(cwd, key_path, pass_store_path)
    title = title_name_input.get()
    check_password = False
    open_encrypter_gui.mainloop()
    # check_password = input(f"Do you want to save {title} as a password!! Default No (Y or n) : ")
    # if check_password.lower() == "y":
    #     store_path = pass_store_path
    #     message = create_password()
    # else:
    #     message = str(input("Enter the mesaage : "))
    #     store_path = text_store_path
    # clean_shell()
    #try:
    # from encrypter import Encrypter
    # #print(key_path)
    # Encrypter(title, message, key_path + '/public.key', store_path)
    # #enc_msg = user.encrypt(message.encode('utf-8')
    # print("Message has been written successfully!!!")
    
    # except e as a Exception:
    #     print(e)
    #     print("Please try again!!!")
if __name__ == '__main__':
    my_secret_key = "E:\\Productivity\\Projects\\Coding\\Python\\openencrypter-gui\\.users\\rinaldo\\.keys\\private.key"
    datawriter("rinaldo", my_secret_key, "E:\\Productivity\\Projects\\Coding\\Python\\openencrypter-gui")