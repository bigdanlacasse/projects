"""
 Included for importability
"""
from pprint import pprint

def dump(thing, label=None):
    width = 100
    footer = '\n' + ('-' * width)

    if label is not None:
        pw = (width - len(str(label)) - 2) / 2
        divider = '-' * pw
        print divider + ' ' + label + ' ' + divider
    else:
        print footer
    
    try:
        pprint(thing)
    except:
        try:
            pprint(repr(thing))
        except Exception as e:
            print 'Couldn\'t dump that obj: ' + e.message
    print footer