#! Python3
# transform_the.py holds Edelweiss to SAILS transformer functions
# superseded by transforms.py

def titleReformat(title):
    """ formats the title to enable alpha sorting in SAILS """
    new_title = title
    if title[:4].lower() == 'the ':
        new_title = title[4:] + ", The"
    if title[:2].lower() == 'a ':
        new_title = title[2:] + ", A"
    return(new_title)

def book_format_encode(format):
    """ returns SAILS format code based on text format name
        Hardcover = 2, Trade Paper = 3
        does this need to support more formats? Audio? """
    fcode = 2
    if format.lower() == "trade paper":
        fcode = 3
    return(fcode)

titles = ['The Market Gardener', 'A Farewell to Arms', 'Men Explain Things To Me', 'A Confederacy of Dunces', 'The Mansplainer', 'a Warning']
for title in titles:
    print('\"' + title + '\" becomes \"' + titleReformat(title)+ '\"')

