import configparser
from jproperties import Properties

import json, sys, os, shutil
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.append(grand_parent_dir)
import argparse

import colorama
from colorama import Fore, Style
from pathlib import Path

from utility.log.util import logger, log
from datetime import datetime 
from utility.helper.printer import colored_print 

class ConfigUtil:
    def __init__(self, argv):
        print(argv)
        if argv.config:
            self.file_path = argv.config
            if not self.file_path.endswith('.properties') or not self.file_path.endswith('.ini'):
                log('ERROR', f'Wrong config file location entered')
                # exit(-1)
        else:
            self.file_path = os.path.join(grand_parent_dir, 'utility/config/config.properties')
        log('INFO', f'config file location: {self.file_path}')
        
        self.type = Path(self.file_path).suffix
        match self.type:
            case '.ini':
                self.config = configparser.ConfigParser()
            case '.properties':
                self.config = Properties()
            case _:
                log('ERROR', f'Config not supported "{self.type}"')
                # exit(-1)
        
    def read_properties(self):
        match self.type:
            case '.ini':
                self.read_ini_properties() 
            case '.properties':
                self.read_properties()
            case _:
                log('ERROR', f'Config not supported "{self.type}"')
                # exit(-1)
                
    def read_ini_properties(self):
        self.config.read(self.file_path)
        
    def read_properties(self):
        try:
            with open(self.file_path, "rb") as config_file:
                self.config.load(config_file)
            return self.config
        except Exception as e:
            logger.exception('Error reading config file or config file not present.')
            log('ERROR', f'Program exiting with failure {datetime.now()}')
            # exit(-1)
        
    def get_property(self, section, key):
        match self.type:
            case '.ini':
                return self.get_ini_properties(section, key) 
            case '.properties':
                return self.get_properties(f'{section}_{key}')
            case _:
                log('ERROR', f'Config not loaded {datetime.now()}')
                # exit(-1) 
                
    def get_ini_properties(self, section, key):
        return self.config.get(section, key)
    
    def get_properties(self, key):
        val = self.config.get(key).data
        print(val)
        return val
    
    def set_property(self, section, key, val):
        match self.type:
            case '.ini':
                self.set_ini_properties(section, key, val) 
            case '.properties':
                self.set_properties(f'{section}_{key}', val)
            case _:
                log('ERROR', f'Config not loaded {datetime.now()}')
                exit(-1) 
                
    def set_ini_properties(self, section, key, val):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, val)
    
    def set_properties(self, key, val):
        self.config[key] = val
    
    def read_query_config(self):
        try:
            report_path = self.get_property('report_config', 'path')
            self.config_file_location = os.path.join(grand_parent_dir, report_path)
            with open(self.config_file_location, 'rb') as f:
                reports_config = json.load(f)
                f.close()
        except Exception:
            logger.exception('Error reading query file or query file not present. {datetime.now()}')
            log('ERROR', f'Program exiting with failure {datetime.now()}')
            exit(-1)
        return reports_config
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script with logging on/off argument")
    parser.add_argument("--enable-logging", action="store_true", help="Enable logging")
    parser.add_argument("--config", action="store_true", help="Pass config path")

    args = parser.parse_args()
    file_path = "utility/config/config.properties"  # Update with your file path
    section_name = "email_config"  # Update with your section name
    property_name = "supported_domain"  # Update with your property name

    config_util = ConfigUtil(args)
    config_util.read_properties()

    try:
        value = config_util.get_property(section_name, property_name)
        print(f"{property_name} = {value}")
    except configparser.NoSectionError:
        print(f"Section '{section_name}' not found in the configuration file.")
    except configparser.NoOptionError:
        print(f"Property '{property_name}' not found in section '{section_name}'.")
