import json, sys, os, shutil
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.append(grand_parent_dir)

import colorama
from colorama import Fore, Style

from utility.log.util import logger, log
from datetime import datetime 
from utility.helper.printer import colored_print 

def clean_and_recreate_output_dir():
    log('WARNING', 'Creating back up of old output directory if exist.')
    print(colored_print('WARNING: Creating back up of old output directory if exist.', Fore.MAGENTA))
    if os.path.exists('output'):
        if os.path.exists('output_backup'):
            shutil.rmtree('output_backup')
        os.rename('output', 'output_backup')
    os.makedirs('output')
     
def read_config(argv, configs):
    log('INFO', f'Starting adhoc report executor {datetime.now()}')
    config_file_location = None
    if len(argv) > 1:
        config_file_location = argv[1]
        if not config_file_location.endswith('config.properties'):
            log('ERROR', f'Wrong config file location entered')
            exit(-1)
    else:
        config_file_location = os.path.join(grand_parent_dir, 'utility/config/config.properties')
    log('INFO', f'config file location: {config_file_location}')
    try:
        with open(config_file_location, 'rb') as config_file:
            configs.load(config_file)
            config_file.close()
    except Exception:
        logger.exception('Error reading config file or config file not present.')
        log('ERROR', f'Program exiting with failure {datetime.now()}')
        exit(-1)

def read_query_config():
    try:
        config_file_location = os.path.join(grand_parent_dir, 'utility/config/query.json')
        with open(config_file_location, 'rb') as f:
            reports_config = json.load(f)
            f.close()
    except Exception:
        logger.exception('Error reading query file or query file not present.')
        log('ERROR', f'Program exiting with failure {datetime.now()}')
        exit(-1)
    return reports_config