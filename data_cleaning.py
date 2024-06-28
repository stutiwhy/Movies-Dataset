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
        df.drop(['review_url', 'num_reviews','movie_rated'], axis=1, inplace=True, errors='ignore')
        
        # Convert run_length to minutes
        def convert_runtime_to_minutes(runtime_str):
            if isinstance(runtime_str, str):
                try:
                    hours, minutes = runtime_str.split('h ')
                    hours = int(hours)
                    minutes = int(minutes.replace('min', ''))
                    total_minutes = hours * 60 + minutes
                    return total_minutes
                except ValueError:
                    return pd.NA
            else:
                return pd.NA
        
        df['run_length'] = df['run_length'].apply(convert_runtime_to_minutes)
        
        # Function to convert release_date to datetime
        def convert_release_date(date_str):
            if isinstance(date_str, str):
                date_part = date_str.split('(')[0].strip()
                return pd.to_datetime(date_part, format='%d %B %Y', errors='coerce')
            else:
                return pd.NaT
        
        # Apply the date conversion function
        df['rel_date'] = df['release_date'].apply(convert_release_date)
        
        # Ensure 'rel_date' is in datetime format and drop invalid rows
        df = df[pd.to_datetime(df['rel_date'], errors='coerce').notna()]
        
        # Drop the original release_date column
        df.drop(['release_date'], axis=1, inplace=True)
        
        # Reorder columns
        new_columns_order = ['name', 'year', 'rel_date', 'genres', 'rating', 'run_length', 'num_raters']
        df = df.reindex(columns=new_columns_order)
        
        # Display the first few rows of the cleaned DataFrame
        print(df.head())
        print(df.dtypes)

        
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