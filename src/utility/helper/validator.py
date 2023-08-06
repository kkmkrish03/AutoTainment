import re
from utility.log.util import logger, log
from datetime import datetime



def is_string_true_or_yes(input_string):
    return input_string.lower() in ['true', 't', 'yes', 'y']

def is_string_valid_boolean(input_string):
    return input_string.lower() in ['true', 't', 'yes', 'y', 'no', 'n', 'false', 'f']


def validate_email(recepient_list, domain):
    recepients = recepient_list.split(',')
    invalid = []
    for r in recepients:
        if domain: 
            if not r.endswith(domain) and not is_valid_email(r):
                invalid.append(r)
        else:
            if not is_valid_email(r):
                invalid.append(r)
    if len(invalid) > 0:
        invalid_emails = ','.join(invalid)
        logger.exception(f'Invalid email format: {invalid_emails}.')
        log('ERROR', f'Email validation failure {datetime.now()}')
        exit(-1)

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False