# read seq1, seq2 
# read BLOSUM62 matrix
# for each aa, find the scores and add up

#import the libraries
from Bio.Align import substitution_matrices

# read the seq in FASTA format
def read_fasta(fasta_file):
    seq = ''
    with open(fasta_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                seq += line.strip()
    return seq

# percentage identity
def percentage_identity(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:				
            count += 1
    return count / len(seq1) * 100	

# BLOSUM score
def BLOSUM_score(seq1, seq2):
    score = 0
    blosum62 = substitution_matrices.load("BLOSUM62")
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62.get((aa1, aa2), -4)  
    return score


# run the function, make the comparisons
human_seq = read_fasta('human.fa')
mouse_seq = read_fasta('mouse.fa')
random_seq = read_fasta('random.fa')

print (f'percentage identity of human and mouse is {percentage_identity(human_seq, mouse_seq)}')
print (f'percentage identity of human and random is {percentage_identity(human_seq, random_seq)}')
print (f'percentage identity of mouse and random is {percentage_identity(mouse_seq, random_seq)}')
print (f'alignment score of human and mouse is {BLOSUM_score(human_seq, mouse_seq)}')
print (f'alignment score of human and random is {BLOSUM_score(human_seq, random_seq)}')
print (f'alignment score of human and random is {BLOSUM_score(mouse_seq, random_seq)}') 
