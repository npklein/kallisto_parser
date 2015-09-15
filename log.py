import sys
from time import strftime

def log(linenum, idstr='', message='', info=''):
    if type(linenum) is str: # log short message only
        print(linenum)
        sys.stdout.flush()
    else:
        fields = []
        fields.append(strftime('%Y-%m-%d %H:%M:%S'))
        fields.append(str(linenum) + ':' + idstr)
        fields.append(str(message))
        fields.append(str(info))
        print('\t'.join(fields))
        sys.stdout.flush()
