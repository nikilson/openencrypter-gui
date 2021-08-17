def clean_shell():
    from os import system, name
    if name == 'nt':
        scr = system('cls')
    else:
        scr = system('clear')
def clear_clipboard():
    from time import sleep
    from os import system
    sleep(45)
    system('cmd /c "echo off | clip"')