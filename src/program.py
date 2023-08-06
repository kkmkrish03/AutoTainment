
from random import choice
import json, sys, os, shutil
from utility.log.util import logger, log, setup_logging
from datetime import datetime
import colorama
from colorama import Fore, Style
import argparse

import rottentomatoes as rt
from imdb import Cinemagoer
import service.subqueries as subqueries
from utility.helper.user_input import is_use_email, get_email, get_movie_report_type
from utility.helper.utils import clean_and_recreate_output_dir, read_config, read_query_config
from utility.helper.validator import is_string_valid_boolean, is_string_true_or_yes, validate_email
from utility.helper.printer import colored_print

from jproperties import Properties
configs = Properties()
colorama.init()

def read_data_generate_report( report_name, report_config, filters):
    log('INFO', f'Generating report {report_name} params {filters}')
    try:
        subq = subqueries.SubQueries()
        subq.execute(configs, report_name, report_config, filters)
        log('INFO', f'Generating report {report_name} completed, check output folder for reports.')
    except Exception:
        logger.exception(f'Generating report {report_name} failed with error. ')

def start(argv, configs):
    clean_and_recreate_output_dir()
    read_config(argv, configs)  
    reports_config = read_query_config()
    use_email = is_use_email()
    if use_email:
        configs['use_email'] = 'True'
        recepient_list = get_email(use_email, '@gmail.com')
        configs['recepients'] = recepient_list
    selected_id, selected_report_config, selected_name = get_movie_report_type(reports_config)
    return reports_config, selected_name, selected_report_config, selected_id
    
def main():
    reports_config, selected_name, selected_report_config, selected_id = start(sys.argv, configs)
    params_dict = dict()
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
    read_data_generate_report(selected_id, selected_report_config, filters)
    log('INFO', f'Adhoc report {selected_id} execution completed {datetime.now()}')
    # list of movies 
    movies = ['Welcome', 'God Fathers', 'Hera Pheri', 'Anaddi']
    print(colored_print("What mood are you in", Fore.MAGENTA))
    mood = input()
    #random values for movies
    print(colored_print(f'{choice(movies)}', Fore.CYAN))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script with logging on/off argument")
    parser.add_argument("--enable-logging", action="store_true", help="Enable logging")
    args = parser.parse_args()
    setup_logging(args.enable_logging)
    main()