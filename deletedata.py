from os import listdir, path, remove
from clearscreen import clean_shell
def text_deleter(user, key, dir):
    clean_shell()
    print("exit - To go mainmenu")
    message_list = []
    for file_det in listdir(dir):
        if file_det.endswith(".txt") and (file_det != "validator.txt"):
            message_list.append(file_det)
    for no, files in enumerate(message_list):      
        # Prints only text file present in My Folder
        print(files[:-4], " >> " ,no)
    selection = input("Please enter your selection : ")
    try:
        selection = int(selection)
        if (len(message_list) >= selection) and len(message_list) >= 0:
            dir = path.join(dir, message_list[selection])
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