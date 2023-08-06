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
    while True:
        print(colored_print(STAR_LINE, Fore.CYAN))
        print(colored_print(STAR_LINE, Fore.MAGENTA))
        print(colored_print('\nPlease select report to generate from below(use name for selection):\n', Fore.MAGENTA))
        # print(colored_print('For Information on below report, refer to Wiki: https://test/l/c/Ddmu4oX1 \n', Fore.MAGENTA))
        movie_map = {}
        movie_desc = {}
        movie_name = {}
        for (i, (name, conf)) in enumerate(reports_config.items(), start=1):
            conf_name = conf['name']
            movie_name[f"{i}"] = conf_name 
            movie_map[f"{i}"] = name
            movie_desc[f"desc{i}"] = conf["desc"]
            print(colored_print(f'{i}.) {conf_name} (type "desc{i}" for describing the report)', Fore.CYAN))
        print(colored_print(STAR_LINE, Fore.MAGENTA))
        print(colored_print(STAR_LINE, Fore.CYAN))
        selected_name = input(colored_print('Enter report number to execute: ', Fore.GREEN)).strip()
        if selected_name.isdigit():
            return movie_map[selected_name], reports_config.get(movie_map[selected_name]), movie_name.get(selected_name)
        else:
            selected_name = f'Description: {movie_desc[selected_name]}'
            print(colored_print(selected_name, Fore.CYAN))
            
def get_valid_fields_for_filter(selected_name, selected_report_config):
    filters = {}
    filter_map = {}
    remember = [f"Movie Report Name: {selected_name}", "____Filters:"]
    while True:
        if 'valid_inputs' in selected_report_config and len(selected_report_config['valid_inputs']) > 0:
            print(colored_print(f'Please select the filters from the list below:', Fore.CYAN))
            for (i, param) in enumerate(selected_report_config['valid_inputs'], start=1):
                pf = param.split(':')
                filter_map[f'{i}'] = pf[0]
                if len(pf) == 2:
                    print(colored_print(f'{i}) {pf[0]} ({pf[1]}) ', Fore.GREEN))
                else:
                    print(colored_print(f'{i}) {pf[0]} ', Fore.GREEN))
            param_value = input(colored_print('Enter filter number to execute (enter "q" to skip filter): ', Fore.GREEN)).strip()    
            if 'q' == param_value.lower():
                break
            param_value = filter_map.get(param_value)
            if param_value and param_value in filters:
                print(colored_print(f'Filter{param_value} already present, please choose anther filter:', Fore.YELLOW))
            elif param_value:
                param_data = input(colored_print(f'Enter filter({param_value}) value for match: ', Fore.GREEN)).strip()  
                filters[param_value] = param_data
            else:
                print(colored_print(f'Not sure what was that. ', Fore.GREEN))
            more = input(colored_print(f'Do you wish to add more filters (True/False): ', Fore.GREEN)).strip()    
            if not is_string_true_or_yes(more):
                break
    for k, v in filters.items():
        remember.append(f'________{k}: {v}')
    print(*remember, sep='\n') 
    return filters         
            
        
