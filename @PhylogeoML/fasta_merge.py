import os

def merge_fasta_files(folder_path, output_file):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    fasta_sequences = []

    # Open all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is in FASTA format
        if filename.endswith(".fasta") or filename.endswith(".fa"):
            with open(file_path, 'r') as fasta_file:
                fasta_data = fasta_file.read()
                fasta_sequences.append(fasta_data)
    
    # Write the merged sequences to the output file
    with open(output_file, 'w') as output_fasta:
        output_fasta.write('\n'.join(fasta_sequences))

    print("Merging FASTA files completed.")

# Specify the target folder path and the output file name
target_folder = "Genetic/Raw"
output_file = "Genetic/merged_sequences.fasta"

merge_fasta_files(target_folder, output_file)
