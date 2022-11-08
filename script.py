import json


def convert_dna_to_rna(dna_sequence) -> str:
    """
      Function that converts input DNA sequence,
      given as a string, to RNA sequence, 
      returned as a string as well. 
    """

    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence


def convert_rna_to_protein(rna_sequence) -> str:
    """
      Function that converts input RNA sequence, 
      given as a string, to protein sequence, 
      returned as a string as well.
      
      The genetic code which translates RNA to 
      protein is stored in file "genetic_code.json", 
      which is stored in ./data directory
    """

    # load genetic code from file
    with open('./data/genetic_code.json', 'r') as json_file:
        genetic_code = json.load(json_file)

    # initialize protein sequence
    protein = ""

    # fill protein sequence with amino acids, 
    # translated from RNA sequence
    for base in range(0, len(rna_sequence), 3):
        codon = rna_sequence[base:base+3]
        if len(codon) == 3:
            protein += genetic_code[codon[0]][codon[1]][codon[2]]
    
    return protein
