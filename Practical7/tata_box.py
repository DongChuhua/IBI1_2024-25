
import re 

#read the input file and write the output file
#read line by line
#for the line that starts with >
     #find the information afer the 'gene:' and before the next space
#for the line that does not start with >
     #it is part of the sequence, so add it to the seq variable
#when the line starts with > again, 
     #check if the seq variable contains the TATA box, if it does, outwrite
     #reset the seq variable and gene name for the next gene
#when the end of the file is reached, check if the seq variable contains the TATA box, if it does, outwrite


# read the input file and write the output file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file, open('tata_genes.fa', 'w') as out:
    #plict the new file in two parts, one for the gene name and one for the sequence
    seq = '' 
    gene_name = ''      
   
    #read the file line by line
    #if the line starts with >, find the information afer the 'gene:' and before the next space, set as the gene_name part
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if gene_name and re.search(r'TATA[AT]A[AT]', seq):
                out.write('>' + gene_name[0] + '\n' + seq + '\n')
                gene_name = ''#reset the gene name for the next gene
            seq = ''#reset the sequence for the next gene

            gene_name = re.findall(r'gene:(\S+)', line)
        
        #if the line does not start with >, it is part of the sequence, so add it to the seq variable    
        else:
            seq += line.strip()
    
    # check the last gene in the file
    if gene_name and re.search(r'TATA[AT]A[AT]', seq):
        out.write('>' + gene_name[0] + '\n' + seq + '\n')
                
                
                
               


                
                
                
                
                
                
    
            


