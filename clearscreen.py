def clean_shell():
    from os import system, name
    if name == 'nt':
        scr = system('cls')
    else:
        scr = system('clear')
