#!/usr/bin/python

import sys
import os
import fnmatch
from log import log

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('usage: python sum_transcripts.py ensg2enstsfile rootdir')
        sys.exit(-1)
    
    mappingfile = sys.argv[1]
    hash_enst2ensg = {}
    ensgs = []
    n_enst = 0
    with open(mappingfile) as f:
        for i, line in enumerate(f):
            split = line.strip().split('\t')
            ensgs.append(split[0])
            for enst in split[1:]:
                hash_enst2ensg[enst] = i
                n_enst += 1

    log(str(len(ensgs)) + ' ensgs, ' + str(n_enst) + ' ensts read from ' + mappingfile)
                
    ## find abundances.txt files under the current directory
    rootdir = sys.argv[2]
    matches = []
    for root, dirnames, filenames in os.walk(rootdir):
        for filename in fnmatch.filter(filenames, '*abundance.tsv'):
            matches.append(os.path.join(root, filename))

    ## get gene abundances by summing over corresponding transcript abundances
    for match_index, match in enumerate(matches):

        if 'data/results/' not in match:
            log(match_index, match, 'skipped')
            continue
        
        outfile = match.replace('abundance.tsv', 'abundance_ensg.tsv')
        if os.path.isfile(outfile):
            log(match_index, match, 'already processed')
            continue
        
        with open(match) as f:
            f.readline()
            gene_abundances = []
            gene_tpms = []
            for i in xrange(len(ensgs)):
                gene_abundances.append(0)
                gene_tpms.append(0)
            for line in f:
                split = line.strip().split('\t')
                enst = split[0]
                index = int(hash_enst2ensg[enst])
                try:
                    gene_abundances[index] += float(split[3])
                    gene_tpms[index] += float(split[4])
                except IndexError:
                    print len(split), index

        with open(outfile, 'w') as f:
            f.write('gene\tsum_est_counts\tsum_tpm\n')
            for i, ensg in enumerate(ensgs):
                f.write('\t'.join([ensg, str(gene_abundances[i]), str(gene_tpms[i])]) + '\n')

        log(match_index, match, 'written to', outfile)
