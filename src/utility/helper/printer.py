import colorama
from colorama import Fore, Style
colorama.init()

def colored_print(text, color):
    # Print colored text
    return f'{color} {text} {Style.RESET_ALL}'
    
    