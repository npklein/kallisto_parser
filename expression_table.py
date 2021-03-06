# Niek de Klein
# 13/09/2015
import os
import sys
kallisto_rootdir = '/Users/NPK/UMCG/projects/PRO-seq_pipeline/PROseq_cd4_jurkat/gm/kallisto/'
combined_tpm = open(os.path.join(kallisto_rootdir, 'tpm_combined.tsv'),'w')
combined_est_counts = open(os.path.join(kallisto_rootdir, 'est_counts_combined.tsv'),'w')
add_header = True

table = {}
header = ''
for root, dirs, files in os.walk(kallisto_rootdir):
    for filename in files:
        if not filename == 'abundance.tsv':
            continue
        samplename = root.replace(kallisto_rootdir,'')
        header += '\t'+samplename
        with open(os.path.join(root,filename)) as kallisto_file:
            kallisto_file.readline()
            for line in kallisto_file:
                line = line.strip().split('\t')
                if line[0] not in table:
                    table[line[0]] = [[line[3], line[4]]]
                else:
                    table[line[0]].append([line[3],line[4]])
combined_tpm.write(header)
combined_est_counts.write(header)
for gene in table:
    combined_est_counts.write('\n'+gene)
    combined_tpm.write('\n'+gene)
    for sample in table[gene]:
        combined_est_counts.write('\t'+sample[0])
        combined_tpm.write('\t'+sample[1])
combined_tpm.close()
combined_est_counts.close()
