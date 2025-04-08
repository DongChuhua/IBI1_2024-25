def cut_sites (DNA_sequence, enzyme_sequence):
    # ensure that the enzyme sequence and DNA sequence are valid
    for i in enzyme_sequence:
        if i not in DNA_sequence:
            raise ValueError("Enzyme sequence have something beyond canonical nucleotides")
    for j in DNA_sequence:
        if j not in enzyme_sequence:
            raise ValueError("DNA sequence have something beyond canonical nucleotides")
    # identify the first position of the enzyme sequence in the DNA sequence
    cut_position = []
    for w in range(len(DNA_sequence)):
        if DNA_sequence[w:w+len(enzyme_sequence)] == enzyme_sequence:
            cut_position.append(w)
    
    return cut_position

# Example usage:
DNA_sequence = "ACGTACGTACGGTTGAAACCCTTG"
enzyme_sequence = "ACGT"
print(cut_sites(DNA_sequence, enzyme_sequence))