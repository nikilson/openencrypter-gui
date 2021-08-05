def datawriter(user, user_key, dir):
    title = str(input("Enter the title : "))
    message = str(input("Enter the mesaage : "))
    try:
        enc_msg = user.encrypt(message.encode('utf-8'))
        if title != "validator":
            title += ".txt"
            from os import path
            dir = path.join(dir, title)
            message_file = open(dir, "wb")
            message_file.write(enc_msg)
            message_file.close()
        print("Message has been written successfully!!!")
    except:
       print("Please try again!!!")

