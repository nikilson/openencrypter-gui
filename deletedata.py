from os import listdir, path, remove, getcwd
from tkinter import messagebox
import tkinter
from tkinter import ttk
# from clearscreen import clean_shell
def exit_func():
    global open_encrypter_gui, select_pass_text
    select_pass_text = 3
    open_encrypter_gui.destroy()
def text_deleter(user, key, directory):
    # clean_shell()
    global mydirectory, combo_box, open_encrypter_gui
    mydirectory = directory
    my_list = []
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui.title("Open Encrypter")
    Tk_Width = 680  
    Tk_Height = 300

    #calculate coordination of screen and window form
    x_Left = int(open_encrypter_gui.winfo_screenwidth()/2 - Tk_Width/2)
    y_Top = int(open_encrypter_gui.winfo_screenheight()/2 - Tk_Height/2)
     
    # Write following format for center screen
    open_encrypter_gui.geometry( "%dx%d+%d+%d" % (Tk_Width, Tk_Height, x_Left, y_Top))
    open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width="700", height="300")
    open_encrypter_gui_canvas.grid(columnspan=3, rowspan=4)
    var = tkinter.IntVar()
    welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Delete Data", 
        relief="flat", font=("Arial", 25), padx=10)
    welcome_open_encrypter.grid(row=0, column=0)
    passwords_radio = tkinter.Radiobutton(open_encrypter_gui, variable=var, text="Passwords", font=("Arial", 18), value=1, command=lambda: select_drop(1))
    passwords_radio.grid(row=1, column=0)
    text_radio = tkinter.Radiobutton(open_encrypter_gui, variable=var, text="Texts", font=("Arial", 18), value=2, command=lambda: select_drop(2))
    text_radio.grid(row=1, column=1)
    combo_box = ttk.Combobox(open_encrypter_gui, width=40, font=("Arial", 18), values=my_list)
    open_encrypter_gui.option_add('*TCombobox*Listbox.font', ("Arial", 18))
    combo_box.grid(row=2, columnspan=2, column=0)
    submit_pass_btn = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Submit", command=lambda: delete_button())
    exit_btn = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=20, padx=2, pady=2, font=("Arial", 18), text="Exit", command=lambda: exit_func())
    submit_pass_btn.grid(row=3, column=1)
    exit_btn.grid(row=3, column=0)
    def select_drop(num):
        global select_pass_text, directory, message_list, my_values, combo_box, mydirectory, combo_box
        select_pass_text = num
        directory = getcwd()
        directory = path.join(directory, ".users")
        directory = path.join(directory, user)
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
        # print(my_values)
        combo_box["values"] = my_values

    def delete_button():
        global directory, combo_box, open_encrypter_gui
        try:
            dir = path.join(directory, combo_box.get() + ".bin")
            res = messagebox.askquestion("Exit Application", message=f"Do you really want to delete {combo_box.get()}!!!")
            if res == "yes":
                remove(dir)
                messagebox.showinfo("Deleted", message="Text {} has been removed successfully!!!".format(message_list[selection][:4]))
            else:
                messagebox.showinfo("Return", message="Returning to main application")
        except:
            pass
    open_encrypter_gui.mainloop()

if __name__ == '__main__':
    my_secret_key = "E:\\Productivity\\Projects\\Coding\\Python\\openencrypter-gui\\.users\\rinaldo\\.keys\\private.key"
    text_deleter("rinaldo", my_secret_key, "E:\\Productivity\\Projects\\Coding\\Python\\openencrypter-gui")