from os import listdir, path
#path = "E:\\Productivity\\Documents\\sdrowssap\\Rinaldo"
def Reader(user, key, dir):
    print("exit - To go mainmenu")
    message_list = []
    for no, files in enumerate(listdir(dir)):
        if files.endswith(".txt"):
            message_list.append(files)
            # Prints only text file present in My Folder
            print(files[:-4], " >> " ,no)
    selection = input("Please enter your selection : ")
    try:
        selection = int(selection)
        if (len(message_list) >= selection) and len(message_list) >= 0:
            dir = path.join(dir, message_list[selection])
        else:
            print("Invalid selection")
        read_file = open(dir, "rb")
        read_token = read_file.read()
        read_file.close()
        decoded = user.decrypt(read_token)
        decoded = decoded.decode()
        print(decoded)
    except:
        pass