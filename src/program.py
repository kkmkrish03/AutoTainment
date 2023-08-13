
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
from utility.helper.utils import clean_and_recreate_output_dir
from utility.helper.validator import is_string_valid_boolean, is_string_true_or_yes, validate_email
from utility.helper.printer import colored_print
import utility.config.ConfigUtil as configs

from jproperties import Properties
colorama.init()

def read_data_generate_report(config, report_name, report_config, filters, use_email, recepient_list):
    log('INFO', f'Generating report {report_name} params {filters}')
    try:
        subq = subqueries.SubQueries()
        subq.execute(config, report_name, report_config, filters, use_email, recepient_list)
        log('INFO', f'Generating report {report_name} completed, check output folder for reports.')
    except Exception:
        logger.exception(f'Generating report {report_name} failed with error. ')

def start(args):
    clean_and_recreate_output_dir()
    config = configs.ConfigUtil(args)
    config.read_properties()
    reports_config = config.read_query_config()
    use_email = is_use_email()
    recepient_list = []
    if use_email:
        recepient_list = get_email(use_email, config.get_property('email_config', 'supported_domain'))
    selected_id, selected_report_config, selected_name = get_movie_report_type(reports_config)
    return reports_config, selected_name, selected_report_config, selected_id, config, use_email, recepient_list
    
def main(args):
    while True:
        reports_config, selected_name, selected_report_config, selected_id, config, use_email, recepient_list = start(args)
        params_dict = dict()
        filters = get_valid_fields_for_filter(selected_name, selected_report_config)
        read_data_generate_report(config, selected_id, selected_report_config, filters, use_email, recepient_list)
        log('INFO', f'Adhoc report {selected_id} execution completed {datetime.now()}')
        # list of movies 
        movies = ['Welcome', 'God Fathers', 'Hera Pheri', 'Anaddi']
        print(colored_print("Hit Enter/Return to continue, (q) to quite.", Fore.BLACK))
        mood = input()
        if mood.lower() == 'q':
            break
    #random values for movies
    print(colored_print(f'Thank You!', Fore.CYAN))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script with logging on/off argument")
    parser.add_argument("--enable-logging", action="store_true", help="Enable logging")
    parser.add_argument("--config", action="store_true", help="Pass config path")
    args = parser.parse_args()
    setup_logging(args.enable_logging)
    main(args)