# importing pandas and necessary exceptions
import pandas as pd
from exceptions import FileHandlingError

def save_clean_data(data, filename="clean_movie_data.csv"): # function to save cleaned data in another clean_covid_data.csv file 
    try:
        data.to_csv(filename, index=False) # writing the data without index rows
        print(f"Saved cleaned data to {filename}")
    except Exception as e: # exception handling
        raise FileHandlingError(f"Error saving data to {filename}: {str(e)}")

def load_clean_data(filename="clean_movie_data.csv"): # function to load the clean data file that may have been saved by the function above for further analysis
    try:
        df = pd.read_csv(filename)
        if df.empty:
            raise ValueError("The .csv file is empty.") # exception handling
        return df # returning the dataset
    except FileNotFoundError as e: # even more exception handling
        raise FileHandlingError(f"File {filename} not found: {str(e)}")
    except Exception as e:
        raise FileHandlingError(f"Error loading data from {filename}: {str(e)}")