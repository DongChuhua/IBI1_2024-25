# Find the length of the largest possible intron in a DNA sequence. The intron must start with GT and end with AG.
import re

def find_largest_intron(seq):
    max_length = 0
    GT_positions = []
    AG_positions = []
    largest_intron = ""
    
    # Find all GT positions (splice donor sites)
    GT_positions =  [m.start() for m in re.finditer('GT', seq)]
    
    # Find all AG positions (splice acceptor sites)
    AG_positions = [m.start() for m in re.finditer('AG', seq)]
    
    # Check all possible GT-AG pairs where GT comes before AG
    for GT in GT_positions:
        for AG in AG_positions:
            if AG > GT + 1:  # AG must be after GT with at least one base in between
                intron_length = AG - GT + 2  # +2 to include both dinucleotides
                if intron_length > max_length:
                    max_length = intron_length
                    largest_intron = seq[GT:AG + 2]
    return max_length, largest_intron


#  test cases
test_sequences = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
max_length, largest_intron = find_largest_intron(test_sequences)
print('The largest intron is: ' + largest_intron)
print ('The length of the largest intron is ' + str(max_length))