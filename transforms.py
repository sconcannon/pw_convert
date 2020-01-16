#! Python3
# transforms.py holds Edelweiss to SAILS transformer functions
import settings
from datetime import datetime

def titleReformat(title):
    """ formats the title to enable alpha sorting in SAILS """
    new_title = title.strip()
    if title[:4].lower() == 'the ':
        new_title = title[4:] + ", The"
    if title[:2].lower() == 'a ':
        new_title = title[2:] + ", A"
    return(new_title)

def book_format_encode(format):
    """ returns SAILS format code based on text format name
        Hardcover = 2, Trade Paper = 3
        does this need to support more formats? Audio? """
    fcode = 1
    if format == 'BC':
        fcode = 3
    elif format == 'BB':
        fcode = 2
    else:
        mapping = settings.format_code_mapping_ew()
        if format in mapping:
            fcode=mapping[format]
    return(fcode)

def pub(source):
    mapping = settings.pub_code_mapping()
    source = source.strip()
    pubDetails = next((item for item in mapping if item["ew_code"] == source), None)
    if pubDetails:
        return pubDetails
    else:
        pubDetails = {'ew_code': 'UNKN', 'sails_code': 99, 'disc': 0.4,'name':'Pub Not Found'}
        return pubDetails

def date_format(source):
    return datetime.strptime(source, '%m/%d/%Y').strftime('%m/%d/%Y')

def printRun(source):
    if source == 'N/A':
        return ''
    else:
        return source



