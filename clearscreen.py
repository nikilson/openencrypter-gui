def clean_shell():
    from os import system, name
    if name == 'nt':
        scr = system('cls')
    else:
        scr = system('clear')
def clear_clipboard():
    from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, call
    from time import sleep
    # from os import system
    sleep(45)
    #hide console
    si = STARTUPINFO()
    si.dwFlags |= STARTF_USESHOWWINDOW
    """ passing starttupinfo=si argument into subprocess.call function"""
    call('cmd /c "echo off | clip"', startupinfo=si)
    # system('cmd /c "echo off | clip"')