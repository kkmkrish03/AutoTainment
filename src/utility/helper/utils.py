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
    