<h1  align="center"> aPhyloGeoML </h1>

<h2  align="center"> Bioinformatics Project: Prediction of Climate-Related Protein Mutations </h2>

This project aims to develop a machine learning model capable of predicting potential future mutations in protein sequences due to climate changes. To achieve this, we use climate data and protein sequences, preprocessing and encoding them into a suitable format for machine learning.

# 📁 Project Structure

The project is organized as follows:

- Programs: This folder contains four dedicated Python programs for preprocessing climate data using variation and correlation, merging FASTA files, and encoding protein sequences into a "one-hot" format.

- 🔎 Data collection: This folder contains the steps involved in gathering climatic and genetic data. It includes scripts for harvesting protein sequences from NCBI data base. Each sequence is associated with a date and/or location, and this information is used to collect climate data from the NASA site using another script that automates the process.

- ⛅ Climatic: This folder holds CSV-format climate data files required for our analysis. The initial data file is called "nasa_data_final.csv".

- 🧬 Genetic: This folder contains FASTA files of protein sequences, as well as the resulting files from preprocessing. All the initial sequences are contained in the "raw" folder.

# ✔️ Prerequisites

Before running the programs, ensure you have the following Python libraries installed:

- pandas
- numpy
- tkinter
- seaborn
- matplotlib
- To install these libraries, you can use the command `pip install library_name`.

# 🚀 Running the Programs

 1️⃣ Normalization and Filtering of Climate Data

- Run the `normalization_variance.py` program.
- You will be prompted to enter a variance threshold for filtering climate columns.
- The data will be normalized, and columns with low variance will be filtered.
- The resulting file will be saved in Excel format in the `Climatic` folder.

 2️⃣ Study of the correlation between attributes

- Run the `correlation.py` program.
- The program will compute the corelation between all the parameters contained in the excel file.
- You can also see on the ouptup consol the different pairs of highly corelated parameters.
- A plot pop-up window will appear showing the corelation matrix of the parameters.

 3️⃣ Merging FASTA Files

- Place the FASTA files of protein sequences in the `Genetic/Raw` folder.
- Run the `fasta_merge.py` program to merge the files into a single FASTA file.
- The merged file will be saved as `sequences_merged.fasta` in the `Genetic` folder.

 4️⃣ "One Hot" Encoding of Protein Sequences

- Run the `encoding_from_fasta.py` program to read the merged FASTA file and perform "one-hot" encoding.
- The result will be saved in an Excel file named `encoded_protein_sequences.xlsx`.

# 📝 Notes

This project is still in its early stages and is currently focused on data preprocessing. The next steps will involve studying the correlation between climate parameters and protein sequences to establish a third layer of data filtering. Once data preprocessing is complete, the next phase will involve training a machine learning model to predict climate-related protein mutations.

Feel free to add additional sections to this README as the project develops, such as specific dependencies, achieved results, and future directions.

This README will provide users with an overview of the project, instructions on how to run the programs, and information about the data structure. Remember to update it as the project progresses.

# 📧 Contact 

Please email us at : <Nadia.Tahiri@USherbrooke.ca> for any question or feedback.
