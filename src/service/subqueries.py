import pandas as pd
import json, sys, os, shutil
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.append(grand_parent_dir)

import utility.helper.reportgenerator as reportgenerator
from utility.log.util import logger, log
from dateutil.relativedelta import *
import glob
import utility.helper.emailer as emailer
from dao.jikan_dao import get_movies_by_genre, get_jikan_genre, get_jikan_producer
from jikanpy import Jikan
jikan = Jikan()
from colorama import Fore, Style

from utility.helper.printer import colored_print


class SubQueries:
    def execute(self, app_config, name, query_config, filters, use_email, recepient_list):
        getattr(self, name)(app_config, name, query_config, filters, use_email, recepient_list)
        if use_email:
            print('Sending reports to email.')
            files = glob.glob('output/'+name+'*.csv')
            print('{} files to email {}'.format(name, files))
            if len(files) > 0:
                emailer.send_report(app_config, name, 'SUCCESS', files, recepient_list)
            else:
                print('ERROR: no files generated for the report. ')
                log('ERROR', 'no files generated for the report. ')
        pass

    def get_movies_by_field(self, app_config, name, query_config, filters, use_email, recepient_list):
        genre = get_jikan_genre()
        print(genre)
        movies = get_movies_by_genre('Action')
        print(movies)
        search_result = jikan.search('anime', 'Mushishi', page=2)
        print(pd.DataFrame(v) for k,v in search_result.items())
        winter_2018_anime = jikan.seasons(year=2018, season='winter')
    
    def get_genre_list(self, app_config, name, query_config, filters, use_email, recepient_list):
        genre = get_jikan_genre()
        data = genre["data"]
        genre_list = [obj['name'].strip() for obj in data]
        print(colored_print(f'Available list of genres are as follows:', Fore.MAGENTA))
        for i, item in enumerate(genre_list, start=1):
            color = Fore.BLUE if i%2 == 0 else Fore.GREEN
            print(colored_print(f"{i}. ", Fore.BLACK) + colored_print(f"{item}", Fore.MAGENTA))
        return genre_list
        
           
    
# exact match
# get by genre
# get by name
# get by year
# get by director
# get by actor
# get by rating 





        

