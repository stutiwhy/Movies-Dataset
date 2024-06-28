import pandas as pd
import matplotlib.pyplot as plt
from exceptions import FileHandlingError, MissingColumnError
from file_handling import load_clean_data

def plot_movies_by_genre_over_time(df):
    # Convert 'rel_date' to datetime if not already
    df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce')

    if 'genres' and 'rel_date' not in df.columns:
        raise MissingColumnError("The DataFrame does not contain the necessary columns.")

    # Extract year from 'rel_date' column
    df['year'] = df['rel_date'].dt.year

    # Explode genres if they are in a list or separated by commas
    df['genres'] = df['genres'].str.split('; ')
    df_exploded = df.explode('genres')

    # Group by year and genres, count movies
    movies_by_genre_year = df_exploded.groupby(['year', 'genres']).size().reset_index(name='count')

    # Plotting with increased figure size
    fig, ax = plt.subplots(figsize=(12, 7))  # Adjust width and height as needed

    # Plotting each genre as a separate line plot
    genres = movies_by_genre_year['genres'].unique()
    for genre in genres:
        data = movies_by_genre_year[movies_by_genre_year['genres'] == genre]
        ax.plot(data['year'], data['count'], marker='o', label=genre, linewidth=2)

    plt.title('Number of Movies by Genre Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.legend(title='Genre', bbox_to_anchor=(1, 1))
    
    # Apply tight layout on the figure, not on ax
    fig.tight_layout()
    
    plt.show()
    # return fig

def plot_genre_ratings_bar(df):
    try:
        # Check if 'genres' and 'rating' columns are present
        if 'genres' not in df.columns or 'rating' not in df.columns:
            raise MissingColumnError("The DataFrame does not contain the necessary columns.")

        # Explode genres if they are in a list or separated by commas
        df['genres'] = df['genres'].str.split('; ')
        df_exploded = df.explode('genres')

        # Group by genre and calculate average rating
        genre_avg_ratings = df_exploded.groupby('genres')['rating'].mean().sort_values(ascending=False)

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        genre_avg_ratings.plot(kind='bar', ax=ax, color='skyblue')

        ax.set_title('Average Ratings by Genre')
        ax.set_xlabel('Genre')
        ax.set_ylabel('Average Rating')
        ax.grid(True)
        ax.set_xticklabels(genre_avg_ratings.index, rotation=45, horizontalalignment='right')  # Rotate x-axis labels for better readability
        plt.tight_layout()

        plt.show()
        # return fig

    except MissingColumnError as e:
        print(f"Missing column error: {e}")
        return None

    except Exception as e:
        print(f"An error occurred in plot_genre_ratings_bar: {e}")
        return None
    
def plot_ratings_vs_raters(df):
    # Check if necessary columns are present
    if 'rating' not in df.columns or 'num_raters' not in df.columns:
        raise ValueError("The DataFrame does not contain the necessary columns 'rating' or 'num_raters'.")
    
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotting
    ax.scatter(df['num_raters'], df['rating'], color='blue', alpha=0.5)
    
    # Set labels and title
    ax.set_title('Ratings vs Number of Raters')
    ax.set_xlabel('Number of Raters')
    ax.set_ylabel('Rating')
    
    # Format x-axis to display integers without scientific notation
    ax.xaxis.get_major_formatter().set_scientific(False)
    ax.xaxis.get_major_formatter().set_useOffset(False)
    
    fig.tight_layout()
    
    plt.show()
    # return fig

def plot_genres_vs_runtime(df):
    try:
        if 'genres' not in df.columns or 'run_length' not in df.columns:
            raise MissingColumnError("The DataFrame does not contain the necessary columns 'genres' or 'run_length'.")
        
        if df.empty:
            raise ValueError("DataFrame is empty after processing.")

        # Group by genres and calculate mean or sum of run_length
        genre_stats = df.groupby('genres')['run_length'].mean()  # Change to .sum() for total runtime
        
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plotting
        genre_stats.plot(kind='bar', color='skyblue', ax=ax)
        
        # Set labels and title
        ax.set_title('Average Runtime of Movies by Genre')
        ax.set_xlabel('Genre')
        ax.set_ylabel('Average Runtime (minutes)')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y')
        
        fig.tight_layout()

        plt.show()
        
        # return fig

    except MissingColumnError as e:
        print(f"Missing column error: {e}")
        return None

    except ValueError as e:
        print(f"Value error: {e}")
        return None

    except Exception as e:
        print(f"An error occurred in plot_genres_vs_runtime: {e}")
        return None

def main():
    try:
        # Load the cleaned data
        df = load_clean_data("clean_movie_data.csv")
        print("Data loaded successfully!")

        # Get the figures from each plot function
        plot_movies_by_genre_over_time(df)
        plot_genre_ratings_bar(df)
        plot_ratings_vs_raters(df)
        plot_genres_vs_runtime(df)
        
        # Optionally show the plots (useful for interactive sessions)
        # plt.show()

    except FileNotFoundError:
        raise FileHandlingError("Clean data file not found.")
    except pd.errors.EmptyDataError:
        raise FileHandlingError("Loaded data file is empty.")
    except Exception as e:
        raise FileHandlingError(f"An error occurred: {e}")

main()
