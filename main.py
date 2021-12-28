def main_menu():
    import tkinter
    global open_encrypter_gui
    open_encrypter_gui = tkinter.Tk()
    open_encrypter_gui.geometry("700x450")
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
        from liveenc import live_main
        open_encrypter_gui.destroy()
        live_main()
    # def select_mode_method(x):
    #     global select_mode, open_encrypter_gui
    #     select_mode = x
    #     print(select_mode)
        # open_encrypter_gui.destroy()
    welcome_open_encrypter = tkinter.Label(open_encrypter_gui, text="Welcome to Open Encrypter!!!\n", 
        relief="flat", font=("Arial", 22))
    home_b1 = tkinter.Button(open_encrypter_gui, width=30, padx=2, pady=2, font=("Arial", 18), text="Login", command=(lambda: main_login1()))
    home_b2 = tkinter.Button(open_encrypter_gui, width=30, padx=2, pady=2, font=("Arial", 18), text="Register New Profile", command=(lambda: Create_Profifle1()))
    home_b3 = tkinter.Button(open_encrypter_gui, width=30, padx=2, pady=2, font=("Arial", 18), text="Live Encryption", command=(lambda: live_main1()))
    home_b4 = tkinter.Button(open_encrypter_gui, width=30, padx=2, pady=2, font=("Arial", 18), text="Quit", command=(lambda: quit()))
    welcome_open_encrypter.pack()
    home_b1.pack()
    home_b2.pack()
    home_b3.pack()
    home_b4.pack()
    open_encrypter_gui.mainloop()
    # Finish

if __name__ == '__main__':
    main_menu()