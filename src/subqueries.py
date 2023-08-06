import datetime
from datetime import timedelta
import calendar
import utility.helper.reportgenerator as reportgenerator
from utility.log.util import logger, log
from dateutil.relativedelta import *
import glob
import utility.helper.emailer as emailer


class SubQueries:

    def execute(self, app_config, name, query_config, paramDict):
        getattr(self, name)(app_config, name, query_config, paramDict)
        if app_config['use_email'].data == 'True':
            print('Sending reports to email.')
            files = glob.glob('output/'+name+'*.csv')
            print('{} files to email {}'.format(name, files))
            if len(files) > 0:
                emailer.send_report(app_config, name, 'SUCCESS', files)
            else:
                print('ERROR: no files generated for the report. ')
                log('ERROR', 'no files generated for the report. ')
        pass

    def query(self, app_config, name, query_config, paramDict):
        query = query_config['query']
        log('INFO', "subquery: {}".format(query))
        

