import pandas as pd
from random import choice
import json, sys, os, shutil
from utility.log.util import logger, log, setup_logging
from datetime import datetime
import colorama
from colorama import Fore, Style
import argparse

import rottentomatoes as rt
from imdb import Cinemagoer
import subqueries
from utility.helper.user_input import is_use_email, get_email, get_movie_report_type
from utility.helper.utils import clean_and_recreate_output_dir, read_config, read_query_config
from utility.helper.printer import colored_print

from jproperties import Properties
configs = Properties()

from jikanpy import Jikan
jikan = Jikan()
colorama.init()

# search_result = jikan.search('anime', 'Mushishi', page=2)
# print(pd.DataFrame(v) for k,v in search_result.items())
# winter_2018_anime = jikan.seasons(year=2018, season='winter')

def read_data_generate_report( report_name, report_config, paramsDict):
    log('INFO', f'Generating report {report_name} params {paramsDict}')
    try:
        subq = subqueries.SubQueries()
        subq.execute(configs, report_name, report_config, paramsDict)
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
    selected_name, selected_report_config = get_movie_report_type(reports_config)
    return reports_config, selected_name, selected_report_config
    
def main():
    reports_config, selected_name, selected_report_config = start(sys.argv, configs)
    params_dict = dict()
    if 'input' in selected_report_config and len(selected_report_config['input']) > 0:
        for param in selected_report_config['input']:
            pf = param.split(':')
            param_value = ''
            if len(pf) == 2:
                param_value = input(colored_print(f'Enter value for {pf[0]} ({pf[1]}): ', Fore.GREEN))
            else:
                param_value = input(colored_print(f'Enter value for {pf[0]}: ', Fore.GREEN))
            params_dict[pf[0]] = param_value
    if 'criteria' in selected_report_config:
        params_dict['criteria.field'] = input(colored_print('Enter field for search: ', Fore.GREEN))
        params_dict['criteria.by'] = selected_report_config['criteria']['by']
        params_dict['criteria.value'] = selected_report_config['criteria']['value'] 
    read_data_generate_report(selected_name, selected_report_config, params_dict)
    log('INFO', f'Adhoc report {selected_name} execution completed {datetime.now()}')
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