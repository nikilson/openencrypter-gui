from os import listdir, path, remove
from clearscreen import clean_shell
def text_deleter(user, key, directory):
    clean_shell()
    print("Press 1 >> Passwords\nPress 2 >> Plain Text\nPress 3 >> Quit")
    select_pass_text = input("\nEnter your selection, Defualt(Quit) : ")
    try:
        select_pass_text = int(select_pass_text)
    except:
        select_pass_text = 0
    if select_pass_text == 1:
        directory = path.join(directory, ".passwords")
    elif select_pass_text == 2:
        directory = path.join(directory, ".text")
    else:
        directory = "exit"
    message_list = []
    if directory != "exit":
        for file_det in listdir(directory):
            if file_det.endswith(".bin"):
                message_list.append(file_det)
        for no, files in enumerate(message_list):      
            # Prints only text file present in My Folder
            print(files[:-4], " >> " ,no)
        print("exit - To go mainmenu from REMOVING data")
        selection = input("Please enter your selection : ")
    try:
        selection = int(selection)
        if (len(message_list) >= selection) and len(message_list) >= 0:
            dir = path.join(directory, message_list[selection])
            ask_sure_delete = input("Do you really want delete {} ?? (yes or no) : ".format(message_list[selection][:4]))
            if ask_sure_delete.lower() == "yes":
                remove(dir)
                print("\nText {} has been removed successfully!!!".format(message_list[selection][:4]))
            else:
                print("\nThe process is reverted!!")
        else:
            print("Invalid selection")
    except:
        pass