import pandas as pd
from exceptions import DataCleaningError, MissingColumnError, FileHandlingError
from file_handling import load_clean_data, save_clean_data

def clean_data():
    try:
        # Load data
        df = load_clean_data("combined.csv")
        print("Data loaded successfully!")

        # Raise exception if data is empty
        if df.empty:
            raise DataCleaningError("Data is empty.")

        # List of required columns
        required_columns = [
            "name", "year", "movie_rated", "run_length", "genres", 
            "release_date", "rating", "num_raters", "num_reviews"
        ]
        
        # Check for missing required columns
        for col in required_columns:
            if col not in df.columns:
                raise MissingColumnError(f"Missing required column: {col}")
        
        # Remove duplicates
        df.drop_duplicates(inplace=True)
        
        # Drop unnecessary columns
        df.drop(['review_url', 'num_reviews'], axis=1, inplace=True, errors='ignore')
        
        # Function to convert release_date to datetime with flexible format handling
        def convert_release_date(date_str):
            if isinstance(date_str, str):
                date_part = date_str.split('(')[0].strip()
                try:
                    return pd.to_datetime(date_part, errors='coerce')
                except ValueError as e:
                    print(f"Error parsing date: {date_part} - {e}")
                    return pd.NaT  # Return NaT (Not a Time) for invalid dates
            else:
                return pd.NaT
        
        # Apply the date conversion function
        df['rel_date'] = df['release_date'].apply(convert_release_date)
        
        # Drop rows where date conversion failed (resulting in NaT)
        df = df.dropna(subset=['rel_date'])
        
        # Drop the original release_date column
        df.drop(['release_date'], axis=1, inplace=True)
        
        # Reorder columns to move 'rel_date' next to 'year'
        new_columns_order = ['name', 'rel_date', 'genres', 'rating', 'movie_rated', 'run_length']
        df = df.reindex(columns=new_columns_order)
        
        # Display the first few rows of the cleaned DataFrame
        print(df.head())
        
        print("Data cleaned successfully!")

        # Save cleaned data to a new file (e.g., clean_movie_data.csv)
        save_clean_data(df, "clean_movie_data.csv")
        print("Cleaned data saved successfully!")
    
    except FileNotFoundError as e:
        raise FileHandlingError(f"An error occurred: File not found - {e}")

    except Exception as e:
        raise FileHandlingError(f"An error occurred: {e}")

# Call the function to clean data
clean_data()
