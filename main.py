def main_menu():
    global inv, select_mode
    inv = False
    print("Enter 1 >> Login \nEnter 2 >> Register new profile \nEnter 3 >> Live encryption\nEnter 4 >> Quit")
    select_mode = input("Please enter your selection : ")
    try:
        select_mode = int(select_mode)
    except:
        select_mode = 0
    if select_mode == 1:
        import login
        login.main_login()
    elif select_mode == 2:
        try:
            del createprofile
        except:
            pass
        import createprofile
    elif select_mode == 3:
        from liveenc import live_main
        live_main()
    elif select_mode == 4:
        quit()
    else:
        inv = True
if __name__ == '__main__':
    from clearscreen import clean_shell
    inv = False
    while True:
        clean_shell()
        if inv:
            print("Sorry, Invalid selection!!")
        main_menu()
        select_mode = 0
        