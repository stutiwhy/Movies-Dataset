import pandas as pd
import matplotlib.pyplot as plt
from exceptions import FileHandlingError, PlottingError
from file_handling import load_clean_data

def plot_movies_by_genre_over_time(df):
    try:
        # making sure rel_date is datetime type because for some reason it does not like staying that way even after doing it in data cleaning
        df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce') 
        
        # extracting year from rel_date
        df['year'] = df['rel_date'].dt.year

        # splitting genres of movies which have multiple genres in their genres column into list and creates unique genre columns
        df['genres'] = df['genres'].str.split(', ')
        df_exploded = df.explode('genres')

        movies_by_genre_year = df_exploded.groupby(['year', 'genres']).size().reset_index(name='count')

        fig, ax = plt.subplots(figsize=(12, 7))

        genres = movies_by_genre_year['genres'].unique()
        for genre in genres:
            data = movies_by_genre_year[movies_by_genre_year['genres'] == genre]
            ax.plot(data['year'], data['count'], marker='o', label=genre, linewidth=2)

        plt.title('Number of Movies by Genre Over Time')
        plt.xlabel('Year')
        plt.ylabel('Number of Movies') 
        plt.legend(title='Genre', bbox_to_anchor=(1, 1))
        plt.tight_layout()

        return plt
    except Exception as e:
        raise PlottingError(f"An error occurred while plotting movies by genre over time: {e}")

def plot_genre_ratings_bar(df):
    try:
        df['genres'] = df['genres'].str.split(', ')
        df_exploded = df.explode('genres')

        genre_avg_ratings = df_exploded.groupby('genres')['rating'].mean().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        plt.bar(genre_avg_ratings.index, genre_avg_ratings, color='#CBC3E3', edgecolor='grey')
        plt.title('Average Ratings by Genre')
        plt.xlabel('Genre')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        return plt
    
    except KeyError as e:
        raise PlottingError(f"KeyError: {e}. Ensure 'genres' and 'rating' columns exist.")
    except Exception as e:
        raise PlottingError(f"An error occurred during plotting: {e}")

def plot_ratings_vs_raters(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['num_raters'], df['rating'], color='#9370DB', alpha=0.3, edgecolor='grey')
        plt.title('Ratings vs Number of Raters')
        plt.xlabel('Number of Raters')
        plt.ylabel('Rating')
        plt.ticklabel_format(style='plain', axis='x')
        plt.tight_layout()

        return plt

    except KeyError as e:
        raise PlottingError(f"KeyError: {e}. Ensure 'num_raters' and 'rating' columns exist.")
    except Exception as e:
        raise PlottingError(f"An error occurred during plotting: {e}")

def plot_runtime_vs_year(df):
    try:
        df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce')
        df['year'] = df['rel_date'].dt.year

        plt.figure(figsize=(10, 6))
        plt.scatter(df['year'], df['run_length'], alpha=0.3, color='#9370DB', edgecolor='grey')
        plt.title('Runtime of Movies Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Runtime (minutes)')
        plt.tight_layout()

        return plt

    except KeyError as e:
        raise PlottingError(f"KeyError: {e}. Ensure 'year' and 'run_length' columns exist.")
    except Exception as e:
        raise PlottingError(f"An error occurred during plotting: {e}")

def plot_ratings_distribution(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(df['rating'].dropna(), bins=20, color='#CBC3E3', edgecolor='grey')
        plt.title('Distribution of Movie Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.tight_layout()

        return plt

    except KeyError as e:
        raise PlottingError(f"KeyError: {e}. Ensure 'rating' column exists.")
    except Exception as e:
        raise PlottingError(f"An error occurred during plotting: {e}")

def plot_runtime_distribution(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(df['run_length'].dropna(), bins=20, color='#CBC3E3', edgecolor='grey')
        plt.title('Distribution of Movie Runtimes')
        plt.xlabel('Runtime (minutes)')
        plt.ylabel('Frequency')
        plt.tight_layout()

        return plt

    except KeyError as e:
        raise PlottingError(f"KeyError: {e}. Ensure 'run_length' column exists.")
    except Exception as e:
        raise PlottingError(f"An error occurred during plotting: {e}")

def plot_movies_by_decade(df):
    try:
        plt.figure(figsize=(10, 6))
        df['year'] = pd.to_datetime(df['rel_date'], errors='coerce').dt.year
        df['decade'] = (df['year'] // 10) * 10
        movies_by_decade = df['decade'].value_counts().sort_index()
        plt.bar(movies_by_decade.index, movies_by_decade, color='#CBC3E3', edgecolor='grey')
        plt.title('Number of Movies by Decade')
        plt.xlabel('Decade')
        plt.ylabel('Number of Movies')
        plt.xticks(rotation=45)
        plt.tight_layout()

        return plt

    except KeyError as e:
        raise PlottingError(f"KeyError: {e}. Ensure 'rel_date' column exists and is properly formatted.")
    except Exception as e:
        raise PlottingError(f"An error occurred during plotting: {e}")
    
def plot_raters_by_genre_bar(df):
    try:
        # Explode the genres if they are in a list or separated by semicolons
        df['genres'] = df['genres'].str.split(', ')
        df_exploded = df.explode('genres')

        # Group by genre and calculate the average number of raters
        genre_avg_raters = df_exploded.groupby('genres')['num_raters'].mean().sort_values(ascending=False)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(genre_avg_raters.index, genre_avg_raters, color='#CBC3E3', edgecolor='grey')
        plt.title('Average Number of Raters by Genre')
        plt.xlabel('Genre')
        plt.ylabel('Average Number of Raters')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        return plt
    except Exception as e:
        raise PlottingError(f"An error occurred while plotting raters by genre: {e}")

# def main():
#     try:
#         df = load_clean_data("clean_movie_data.csv")
#         print("Data loaded successfully!")

#         fig1 = plot_movies_by_genre_over_time(df)
#         fig1.show()
#         fig2 = plot_genre_ratings_bar(df)
#         fig2.show()
#         fig3 = plot_ratings_vs_raters(df)
#         fig3.show()
#         fig4 = plot_runtime_vs_year(df)
#         fig4.show()
#         fig5 = plot_ratings_distribution(df)
#         fig5.show()
#         fig6 = plot_runtime_distribution(df)
#         fig6.show()
#         fig7 = plot_movies_by_decade(df)
#         fig7.show()

#     except FileNotFoundError:
#         raise FileHandlingError("Clean data file not found.")
#     except pd.errors.EmptyDataError:
#         raise FileHandlingError("Loaded data file is empty.")
#     except Exception as e:
#         raise FileHandlingError(f"An error occurred: {e}")

# main()
