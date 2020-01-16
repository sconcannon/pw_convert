#! python3
# settings for pw_convert

def set_mapping():
    mapping =   {'A': 'itemid',
            'B': 'pubid',
            'C': 'format',
            'D': 'release',
            'E': 'isbn13',
            'F': 'Title',
            'G': 'Subtitle',
            'H': 'Series',
            'I': 'Author',
            'J': 'authorcity',
            'K': 'authorstate',
            'L': 'PubDate',
            'M': 'discount',
            'N': 'usprice',
            'O': 'BISAC',
            'P': 'upc',
            'Q': 'trimsize',
            'R': 'pagecnt',
            'S': 'printrun',
            'T': 'imprint',
            'U': 'category',
            'V': 'catalogpage',
            'W': 'catalogcopy',
            'X': 'local',
            'Y': 'notes',
            'Z': 'catalogname',
            'AA': 'ordering'}
    return mapping;

def pub_code_mapping():
    vendor_mapping = [{'ew_code':'UOTP','sails_code':0,'disc':0.4,'name':'UToronto Press'},
                      {'ew_code':'11NS', 'sails_code': 71, 'disc': 0.4,'name':'Penn State UP'},
                      {'ew_code':'BLOA', 'sails_code': 6, 'disc': 0.47,'name':'Bloomsbury'},
                      {'ew_code':'MM', 'sails_code': 6, 'disc': 0.47,'name':'Bloomsbury'},
                      {'ew_code':'XTBR', 'sails_code': 6, 'disc': 0.47,'name':'Bloomsbury'},
                      {'ew_code':'HXN', 'sails_code': 7, 'disc': 0.5,'name':'Capstone'},
                      {'ew_code':'FIRE', 'sails_code': 48, 'disc': 0.4,'name':'Firefly'}]
    return vendor_mapping

def seasonName():
    return 'Spring 2020'

def format_code_mapping_text():
    formats = {1: ['unknown'],
               2: ['hardback', 'hardcover', 'hard cover', 'cloth'],
               3: ['trade paper', 'trade', 'paperback'],
               4: ['mass market paperback'],
               5: ['board book'],
               6: ['paper over board'],
               7: ['calendar-wall'],
               8: ['calendar-desk'],
               9: ['map-wall'],
               10: ['map-folded'],
               11: ['spiral bound'],
               12: ['catalog'],
               13: ['display-filled'],
               14: ['display-empty'],
               15: ['pack'],
               16: ['boxed set'],
               17: ['slip case'],
               18: ['deck'],
               19: ['dvd'],
               20: ['cd'],
               21: ['poster-wall'],
               22: ['laminated card'],
               23: ['globe'],
               24: ['action figure'],
               25: ['sticker book'],
               26: ['game/board game'],
               27: ['large print paperback'],
               28: ['large print hardback'],
               29: ['greeting card'],
               30: ['journal'],
               31: ['sketchbook - mixed assortment'],
               32: ['pen/pencil loop'],
               33: ['address book'],
               34: ['sketchbook - soft cover'],
               35: ['sketchbook-general'],
               36: ['sketchbook - hardcover'],
               37: ['sketchbook - wirebound'],
               38: ['kit'],
               39: ['toy'],
               40: ['puzzle'],
               41: ['planner'],
               42: ['paper & cd'],
               43: ['hardback & cd'],
               44: ['hardback & dvd'],
               45: ['bag'],
               46: ['writing set'],
               47: ['calendar - other'],
               48: ['wirebound'],
               49: ['board game'],
               50: ['comics - single issue'],
               51: ['notecards'],
               52: ['baby board books'],
               53: ['thick soft cover'],
               54: ['bath book'],
               55: ['big book'],
               56: ['bundle'],
               57: ['card game'],
               58: ['doll'],
               59: ['plush toy'],
               60: ['puppet'],
               61: ['board book (soft)'],
               62: ['playing cards'],
               63: ['tarot cards'],
               64: ['mixed media'],
               65: ['novelty book'],
               66: ['e-pub'],
               67: ['pamphlet'],
               68: ['inflatable toy'],
               69: ['3-d model'],
               70: ['counter pack'],
               71: ['notebook-general'],
               72: ['paper placemat'],
               73: ['post cards'],
               74: ['stationary'],
               75: ['galley']}

    return formats

def format_code_mapping_ew():
    formats = {
        'BB':2, # hardcover
        'BC':3, # paperback
        'BD':1,
        'BE':11, #spiral-bound
        'BH':5, #board book
        'XC':13, # display-filled
    }
    return formats