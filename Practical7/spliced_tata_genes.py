import re

# input splice donor/acceptor combination
combination = input("Enter the splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()
if combination not in ['GTAG', 'GCAG', 'ATAC']:
    print("Invalid combination!")
    exit()

# Build regular expression pattern: first 2 bases+any character+last 2 bases
splice_pattern = re.compile(combination[:2] + r'.*?' + combination[2:])
# TATA box
tata_pattern = re.compile(r'TATA[AT]A[AT]') 

with open('tata_genes.fa', 'r') as infile, open(f'{combination}_spliced_genes.fa', 'w') as outfile:
    seq = ''
    gene_name = 'Unknown'
    
    for line in infile:
        line = line.strip()
        
        if line.startswith('>'):
            if seq:
                # Check whether there are splice sites and at least 1 TATA box
                if splice_pattern.search(seq):
                    tata_matches = tata_pattern.findall(seq)
                    if tata_matches:
                        outfile.write(f'>{gene_name} number_of_TATA_box:{len(tata_matches)}\n{seq}\n')
            
            # start a new gene
            seq = ''
            gene_name = re.search(r'gene:(\S+)', line)
        
        else:
            seq += line
    
    # check the last gene in the file
    if seq and splice_pattern.search(seq):
        tata_matches = tata_pattern.findall(seq)
        if tata_matches:
            outfile.write(f'>{gene_name} number_of_TATA_box:{len(tata_matches)}\n')
            outfile.write(f'{seq}\n')