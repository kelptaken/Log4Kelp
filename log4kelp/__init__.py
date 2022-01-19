# ---               |   ---
# Log4Kelp          |   This is a logging library
# by KelpTaken      |   for my internal projects.
# ---               |   ---

import colorama
import platform

if platform.system == 'Windows':
    colorama.init(convert=True)
else:
    colorama.init()

class Logger: # basic visual logger

    def Info(text):
        print(f'- {text}')

    def Warn(text):
        print(f'{colorama.Fore.YELLOW}[!] {colorama.Fore.RESET} {text}')

    def Error(text):
        print(f'{colorama.Fore.RED}[!!]{colorama.Fore.RESET} {text}')

class Suffix: # ( ͡° ͜ʖ ͡°) my upcoming project

    def Info(text):
        print(f'{colorama.Fore.GREEN}>>{colorama.Fore.RESET} {text}')
    
    def Warn(text):
        print(f'{colorama.Fore.YELLOW}! {colorama.Fore.RESET} {text}')

    def Error(text):
        print(f'{colorama.Fore.RED}{colorama.Style.BRIGHT}!!{colorama.Fore.RESET}{colorama.Style.RESET_ALL} {text}')

    def Loading(text):
        print(f'{colorama.Fore.YELLOW}⛾ {colorama.Fore.RESET} {text}')
    
def Custom(prefix, color, text):
    if color == 'red':
        print(f'{colorama.Fore.RED}{prefix}{colorama.Fore.RESET} {text}')
    elif color == 'green':
        print(f'{colorama.Fore.GREEN}{prefix}{colorama.Fore.RESET} {text}')
    elif color == 'yellow':
        print(f'{colorama.Fore.YELLOW}{prefix}{colorama.Fore.RESET} {text}')
    elif color == 'blue':
        print(f'{colorama.Fore.BLUE}{prefix}{colorama.Fore.RESET} {text}')
    elif color == 'white':
        print(f'{colorama.Fore.WHITE}{prefix}{colorama.Fore.RESET} {text}')
    elif color == 'black':
        print(f'{colorama.Fore.BLACK}{prefix}{colorama.Fore.RESET} {text}')
    else:
        print(f'{colorama.Fore.WHITE}{prefix}{colorama.Fore.RESET} {text}')