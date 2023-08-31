import pandas as pd
import numpy as np

# Path to the FASTA file containing protein sequences
fasta_file_path = "Genetic/merged_sequences.fasta"

protein_sequences = []

with open(fasta_file_path, 'r') as f:
    lines = f.readlines()
    protein_sequence = ""
    for line in lines:
        if line.startswith(">"):  # Sequence header line
            if protein_sequence:  # Check if a sequence is already being read
                protein_sequences.append(protein_sequence)
                protein_sequence = ""
        else:
            protein_sequence += line.strip()

    if protein_sequence:  # For the last sequence in the file
        protein_sequences.append(protein_sequence)

# Find all unique amino acids (including padding character)
amino_acids = set(''.join(protein_sequences))

# "One hot" encoding of protein sequences
def encode_one_hot(sequence):
    encoding = np.zeros((len(sequence), len(amino_acids)), dtype=int)
    for i, aa in enumerate(sequence):
        encoding[i, list(amino_acids).index(aa)] = 1
    return encoding

protein_sequences_encoded = [encode_one_hot(seq) for seq in protein_sequences]

# Write the encoded protein sequences to an Excel file
df = pd.DataFrame({'Protein Sequences': protein_sequences_encoded})
df.to_excel('Genetic/protein_sequences_encoded.xlsx', index=False)

print("Protein sequences have been extracted from the FASTA file, encoded in 'one hot' (including padding character), and saved to the 'protein_sequences_encoded.xlsx' file.")
