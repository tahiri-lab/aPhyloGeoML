import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog

# Function to normalize data
def normalize_data(data):
    normalized_data = []
    
    for column in data.T:
        min_val = np.nanmin(column)
        max_val = np.nanmax(column)
        
        if pd.isna(min_val) or pd.isna(max_val) or min_val == max_val:
            normalized_column = np.full(column.shape, 0.5)
        else:
            normalized_column = (column - min_val) / (max_val - min_val)
        
        normalized_data.append(normalized_column)
    
    return np.array(normalized_data).T

# Function to filter columns with low variance
def filter_low_variance_columns(data_frame, threshold):
    normalized_variances = data_frame.apply(lambda col: np.var(col), axis=0)
    selected_columns = normalized_variances[normalized_variances >= threshold].index
    return data_frame[selected_columns]

# Ask the user to enter the threshold using a dialog window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Use a simple dialog window to get the threshold
threshold = simpledialog.askfloat("Variance Threshold", "Please enter the variance threshold:")

# If the user clicks Cancel, exit the program
if threshold is None:
    print("Operation cancelled.")
else:
    climatic_data_file_path = 'Climatic\Climatic_Data.csv'
    climatic_data = pd.read_csv(climatic_data_file_path, sep=';')

    # Replace missing data labeled as "-999" into Nan (missing value)
    climatic_data.replace(-999, np.nan, inplace=True)

    climatic_data = climatic_data.apply(pd.to_numeric, errors='coerce')

    normalized_data = normalize_data(climatic_data.values)
    normalized_data_df = pd.DataFrame(normalized_data, columns=climatic_data.columns)

    initial_dimensions = normalized_data_df.shape

    # Filter columns with low variance
    filtered_data = filter_low_variance_columns(normalized_data_df, threshold)
    filtered_dimensions = filtered_data.shape

    excel_output_file_path = "Climatic/normalized_and_filtered_climatic_data.xlsx"
    filtered_data.to_excel(excel_output_file_path, index=False)

    print("Initial dimensions before variance reduction:", initial_dimensions)
    print("Dimensions after variance reduction:", filtered_dimensions)
    print(f"Normalized and filtered data has been saved to the file '{excel_output_file_path}'.")
