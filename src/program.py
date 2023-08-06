
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
from utility.helper.user_input import is_use_email, get_email, get_movie_report_type, get_valid_fields_for_filter
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
    filters = get_valid_fields_for_filter(selected_name, selected_report_config)
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