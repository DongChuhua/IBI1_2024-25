#input three possible splice donor/acceptor	combinations (GTAG,	GCAG, ATAC)	
#output different file with different name(GTAG_spliced_genes.fa, GCAG_spliced_genes.fa, ATAC_spliced_genes.fa)

#for each combination
#read the file line by line
# if the line starts with ">", find the gene_name
# if the line does not start with ">", append the sequence into one line
#split the introns of each seq of the gene
#count the number of introns
#write the gene_name and sequence into the new file

import re


#define the function to cut introns from the sequence
def cut_introns(seq, donor, acceptor):
    introns = []
    donor_sites = [m.start() for m in re.finditer(donor, seq)] #find all the start of donor_sites, store in list
    for i in donor_sites:
        A = re.search(acceptor, seq[i+2:]) #find all the acceptor 
        if A:
            new_introns = seq[i:A.start()+2+i+2]
            introns.append(new_introns) 
    return introns



#input
combination = str(input("Enter the splice donor/acceptor combination (GTAG, GCAG, ATAC): "))
#create a dictionary to store the different combination
donor_acceptor = {'GTAG': ('GT', 'AG'), 'GCAG': ('GC', 'AG'), 'ATAC': ('AT', 'AC')}
donor, acceptor = donor_acceptor[combination]
#ensure the validity of the input
if combination not in donor_acceptor:
    print("Invalid combination!")
    exit()


#initialize the variables
seq = ''
gene_name = ''
total_introns = []


if combination in donor_acceptor:
    with open ('tata_genes.fa', "r") as file, open(f'{combination}_spliced_genes.fa', "w") as out:
        #read line by line
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if seq: 
                    total_introns = cut_introns(seq, donor, acceptor)  #cut the introns from the sequence
                    # go through each intron in the total_introns list          
                    for one_intron in total_introns:
                        if gene_name and re.search(r'TATA[AT]A[AT]', one_intron):
                            TATA_count = str(len(re.findall(r'TATA[AT]A[AT]', one_intron))) #count the number of TATA box sequence
                            out.write('>' + gene_name[0] + ' number_of_TATA_box:' + TATA_count + '\n' + one_intron + '\n')
                        
                    gene_name = ''#reset the gene name for the next gene
                    seq = '' #reset the sequence for the next gene
                    total_introns = [] #reset
                gene_name = re.findall(r'>(\S+)', line)
            else: # for the sequence part
                seq += line.strip()
        
        # check the last gene in the file
        total_introns = cut_introns(seq, donor, acceptor)  #cut the introns from the sequence                     
        for one_intron in total_introns:
            if gene_name and re.search(r'TATA[AT]A[AT]', one_intron):
                TATA_count = str(len(re.findall(r'TATA[AT]A[AT]', one_intron))) #count the number of TATA box sequence
                out.write('>' + gene_name[0] + ' number_of_TATA_box:' + TATA_count + '\n' + one_intron + '\n')  
    

  
        
                    



