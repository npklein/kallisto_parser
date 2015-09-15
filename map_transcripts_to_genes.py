#!/usr/bin/python

import sys
import os
import fnmatch
from log import log

IN_FILE = 'data/hg19.v75.cdna.all.fa'
ENST2ENSG_FILE = 'data/hg19.v75.cdna.all.enst2ensg.txt'
ENSG2ENSTS_FILE = 'data/hg19.v75.cdna.all.ensg2ensts.txt'

if __name__ == '__main__':
    
    ## create enst to ensg file
    ensgs = set()
    enst2ensg = {}
    with open(IN_FILE) as f:
        for line in f:
            if line.startswith('>'):
                split = line.split(' ')
                enst2ensg[split[0].replace('>', '')] = split[5]
                ensgs.add(split[5])
    log(str(len(enst2ensg)) + ' ENSTs, ' + str(len(ensgs)) + ' ENSGS read from ' + IN_FILE)

    ensts = sorted(list(enst2ensg.keys()))
    with open(ENST2ENSG_FILE, 'w') as f:
        for enst in ensts:
            f.write(enst + '\t' + enst2ensg[enst] + '\n')
    log(str(len(enst2ensg)) + ' ENSTs, ' + str(len(ensgs)) + ' ENSGS written to ' + ENST2ENSG_FILE)

    ## 'transpose' dict to get ensg to ensts mapping
    ensgs = sorted(list(ensgs))
    ensg2ensts = {}
    for ensg in ensgs:
        ensg2ensts[ensg] = []
    for (enst, ensg) in enst2ensg.iteritems():
        ensg2ensts[ensg].append(enst)

    with open(ENSG2ENSTS_FILE, 'w') as f:
        for ensg in ensgs:
            f.write(ensg + '\t' + '\t'.join(ensg2ensts[ensg]) + '\n')
    
    log(str(len(enst2ensg)) + ' ENSTs, ' + str(len(ensgs)) + ' ENSGS written to ' + ENSG2ENSTS_FILE)
