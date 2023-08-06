import logging
import os
import sys
import json_log_formatter
from logging.handlers import RotatingFileHandler

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.append(grand_parent_dir)

import colorama
from colorama import Fore, Style
colorama.init()

formatter = json_log_formatter.JSONFormatter()
filename = '../logs/AutoTainMent.json'
os.makedirs(os.path.dirname(filename), exist_ok=True)
json_handler = RotatingFileHandler(filename, maxBytes=20971520, backupCount=5)
json_handler.setFormatter(formatter)

console_formatter = logging.Formatter("%(name)s - :%(levelname)s: - %(message)s")
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(console_formatter)

logger = logging.getLogger(f'{Fore.RED} AUTO-TAIN-MENT {Style.RESET_ALL}')
logger.addHandler(json_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

def setup_logging(enable_logging):
    log_level = logging.DEBUG if enable_logging else logging.ERROR
    logger.setLevel(log_level)
    console_handler.setLevel(log_level)

def log(level, message):
    "Automatically log the current function details."
    import inspect
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    colors = {
        'INFO': Fore.BLUE,
        'DEBUG': Fore.WHITE,
        'ERROR': Fore.RED,
        'WARNING': Fore.YELLOW,
        '*': Fore.BLACK,
    }
    color = colors.get(level, Fore.RESET)
    if level == 'INFO':
        inf_msg = "%s in %s:%i :: %s" % (
            func.co_name, 
            func.co_filename.rsplit(sep='/',maxsplit=1)[0], 
            func.co_firstlineno,
            message
        )
        logger.info(f'{color} {inf_msg} {Style.RESET_ALL}')
    elif level == 'DEBUG':  
        dbg_msg = "%s in %s:%i :: %s" % (
            func.co_name, 
            func.co_filename.rsplit(sep='/',maxsplit=1)[1], 
            func.co_firstlineno,
            message
        )  
        logger.debug(f'{color} {dbg_msg} {Style.RESET_ALL}')
    elif level == 'ERROR': 
        err_msg = "%s in %s:%i :: %s"  % (
            func.co_name, 
            func.co_filename.rsplit(sep='/',maxsplit=1)[1], 
            func.co_firstlineno,
            message
        )   
        logger.error(f'{color} {err_msg} {Style.RESET_ALL}')
    elif level == 'WARNING': 
        war_msg = "%s in %s:%i :: %s"  % (
            func.co_name, 
            func.co_filename.rsplit(sep='/',maxsplit=1)[1], 
            func.co_firstlineno,
            message
        )   
        logger.warning(f'{color} {war_msg} {Style.RESET_ALL}')
    else:
        color = colors.get('*', Fore.RESET)
        msg_log = "%s in %s:%i :: %s" % (
            func.co_name, 
            func.co_filename.rsplit(sep='/',maxsplit=1)[1], 
            func.co_firstlineno,
            message
        )
        print(f'{color} {msg_log} {Style.RESET_ALL}')
    pass
    