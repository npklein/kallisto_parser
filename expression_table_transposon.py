# Niek de Klein
# 13/09/2015
import os

kallisto_rootdir = '/Users/NPK/UMCG/projects/PRO-seq_pipeline/PROseq_cd4_jurkat/gm/kallisto/'
combined_tpm = open(os.path.join(kallisto_rootdir, 'tpm_combined.tsv'),'w')
combined_est_counts = open(os.path.join(kallisto_rootdir, 'est_counts_combined.tsv'),'w')
add_header = True
for root, dirs, files in os.walk(kallisto_rootdir):
    for filename in files:
        if not filename == 'abundance.tsv':
            continue
        samplename = root.replace(kallisto_rootdir,'')
        header = ''
        tpm = samplename
        est_counts = samplename
        with open(os.path.join(root,filename)) as kallisto_file:
            kallisto_file.readline()
            for line in kallisto_file:
                header += '\t'+line.split('\t')[0]
                tpm += '\t'+line.strip().split('\t')[4]
                est_counts += '\t'+line.split('\t')[3]
            if add_header:
                combined_tpm.write(header+'\n')
                combined_est_counts.write(header+'\n')
                add_header = False
            combined_tpm.write(tpm+'\n')
            combined_est_counts.write(est_counts+'\n')
combined_tpm.close()
combined_est_counts.close()