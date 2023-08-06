from utility.helper.validator import is_string_valid_boolean, is_string_true_or_yes, validate_email
import colorama
from colorama import Fore, Style
from utility.helper.printer import colored_print

STAR_LINE = '\n**************************************************************************************************************'

def is_use_email():
    while True:
        use_email = input(colored_print('Send report via email(True/False): ', Fore.GREEN))
        if is_string_valid_boolean(use_email):
            return is_string_true_or_yes(use_email)
        else:
            print(colored_print(f"Sorry, not sure what that was. (y/N) ", Fore.YELLOW))

def get_email(use_email, domain):
    if use_email:
        while True:
            recepient_list = input(colored_print('Enter single or multiple (comma separated) email id(s): ', Fore.GREEN))
            try:
                validate_email(recepient_list, domain)
                return recepient_list
            except Exception:
                print(colored_print(f"Sorry, the email format was not correct, please reenter or quit (q).", Fore.YELLOW))
                
def get_movie_report_type(reports_config):
    print(colored_print(STAR_LINE, Fore.CYAN))
    print(colored_print(STAR_LINE, Fore.MAGENTA))
    print(colored_print('\nPlease select report to generate from below(use name for selection):\n', Fore.MAGENTA))
    # print(colored_print('For Information on below report, refer to Wiki: https://test/l/c/Ddmu4oX1 \n', Fore.MAGENTA))
    movie_map = {}
    for (i, (name, conf)) in enumerate(reports_config.items(), start=1):
        conf_name = conf['name']
        movie_map[f"{i}"] = name
        print(colored_print(f'[{i}] name: {conf_name} ', Fore.CYAN))
    print(colored_print(STAR_LINE, Fore.MAGENTA))
    print(colored_print(STAR_LINE, Fore.CYAN))
    selected_name = input(colored_print('Enter report number to execute: ', Fore.GREEN)).strip()
    selected_name = movie_map[selected_name]
    selected_report_config = reports_config.get(selected_name)
    return selected_name, selected_report_config
