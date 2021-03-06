def main_menu():
    import tkinter
    global open_encrypter_gui
    from os import path
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui.title("Open Encrypter")
    Tk_Width = 700
    Tk_Height = 450

    #calculate coordination of screen and window form
    x_Left = int(open_encrypter_gui.winfo_screenwidth()/2 - Tk_Width/2)
    y_Top = int(open_encrypter_gui.winfo_screenheight()/2 - Tk_Height/2)
     
    # Write following format for center screen
    open_encrypter_gui.geometry( "%dx%d+%d+%d" % (Tk_Width, Tk_Height, x_Left, y_Top))
    # my_icon = path.join("assets", "key.png")
    # my_icon = tkinter.PhotoImage(file = my_icon)
    # open_encrypter_gui.iconphoto(False, my_icon)
    open_encrypter_gui_canvas = tkinter.Canvas(open_encrypter_gui, width="700", height="450")
    open_encrypter_gui_canvas.grid(rowspan=5)
    def Create_Profifle1():
        global open_encrypter_gui
        from createprofile import Create_Profifle
        open_encrypter_gui.destroy()
        Create_Profifle()
    def main_login1():
        global open_encrypter_gui
        from login import main_login
        open_encrypter_gui.destroy()
        main_login()
    def live_main1():
        global open_encrypter_gui
        #messagebox.showinfo("Under Development", "This feature will be added in the upcomming build!!")
        from liveenc import live_main
        open_encrypter_gui.destroy()
        live_main()
    def main_quit():
        global open_encrypter_gui
        open_encrypter_gui.destroy()
        quit()
    # def select_mode_method(x):
    #     global select_mode, open_encrypter_gui
    #     select_mode = x
    #     print(select_mode)
        # open_encrypter_gui.destroy()
    welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Welcome to Open Encrypter!!!", 
        relief="flat", font=("Arial", 22))
    home_b1 = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Login", command=(lambda: main_login1()))
    home_b2 = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Register New Profile", command=(lambda: Create_Profifle1()))
    home_b3 = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Live Encryption", command=(lambda: live_main1()))
    home_b4 = tkinter.Button(open_encrypter_gui, bg="#20bebe", fg="black", width=30, padx=2, pady=2, font=("Arial", 18), text="Quit", command=(lambda: main_quit()))
    welcome_open_encrypter.grid(row=0)
    home_b1.grid(row=1)
    home_b2.grid(row=2)
    home_b3.grid(row=3)
    home_b4.grid(row=4)

    # Some keyboard bindings

    open_encrypter_gui.bind("<Return>", lambda event: main_login1())
    open_encrypter_gui.bind("<Escape>", lambda event: main_quit())
    open_encrypter_gui.focus_force()
    open_encrypter_gui.mainloop()
    # Finish

if __name__ == '__main__':
    main_menu()