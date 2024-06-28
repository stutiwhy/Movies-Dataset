import pandas as pd
import matplotlib.pyplot as plt
from exceptions import FileHandlingError
from file_handling import load_clean_data

def plot_movies_by_genre_over_time(df):
    # making sure rel_date is datetime type because for some reason it does not like staying that way even after doing it in data cleaning
    df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce') 
    
    # extracting year from rel_date
    df['year'] = df['rel_date'].dt.year

    # splitting genres of movies which have multiple genres in their genres column into list and creates unique genre columns
    df['genres'] = df['genres'].str.split(';')
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

def plot_genre_ratings_bar(df):
    # Explode genres if they are in a list or separated by commas
    df['genres'] = df['genres'].str.split(';')
    df_exploded = df.explode('genres')

    # Group by genre and calculate average rating
    genre_avg_ratings = df_exploded.groupby('genres')['rating'].mean().sort_values(ascending=False)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(genre_avg_ratings.index, genre_avg_ratings, color='#CBC3E3', edgecolor='grey')
    plt.title('Average Ratings by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    return plt
    
def plot_ratings_vs_raters(df):
    plt.figure(figsize=(10, 6))
    
    # Plotting
    plt.scatter(df['num_raters'], df['rating'], color='#9370DB', alpha=0.3,edgecolor='grey')
    
    # Set labels and title
    plt.title('Ratings vs Number of Raters')
    plt.xlabel('Number of Raters')
    plt.ylabel('Rating')
    
    # Format x-axis to display integers without scientific notation
    plt.ticklabel_format(style='plain', axis='x')
    
    plt.tight_layout()
    
    return plt

def plot_runtime_vs_year(df):
    # Convert 'rel_date' to datetime if not already
    df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce')

    # Extract year from 'rel_date' column
    df['year'] = df['rel_date'].dt.year

    # Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['year'], df['run_length'], alpha=0.3, color='#9370DB',edgecolor='grey')

    # Adding titles and labels
    plt.title('Runtime of Movies Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Runtime (minutes)')

    # Tidy up the layout
    plt.tight_layout()

    return plt

def plot_ratings_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating'].dropna(), bins=20, color='#CBC3E3', edgecolor='grey')
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()
    return plt

def plot_runtime_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['run_length'].dropna(), bins=20, color='#CBC3E3', edgecolor='grey')
    plt.title('Distribution of Movie Runtimes')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    return plt

def plot_movies_by_decade(df):
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


# def main(): 
#     try:
#         df = load_clean_data("clean_movie_data.csv")
#         print("Data loaded successfully!")

#         # Get the figures from each plot function
#         fig = plot_movies_by_genre_over_time(df)
#         fig.show()
#         # fig = plot_genre_ratings_bar(df)
#         # fig = plot_ratings_vs_raters(df)
#         # fig = plot_genres_vs_runtime(df)
#         # fig.show()
#         fig1 = plot_runtime_vs_year(df)
#         fig1.show()
#         fig2 = plot_ratings_distribution(df)
#         fig2.show()
#         fig3 = plot_runtime_distribution(df)
#         fig3.show()
#         fig4 = plot_movies_by_decade(df)
#         fig4.show()

#     except FileNotFoundError:
#         raise FileHandlingError("Clean data file not found.")
#     except pd.errors.EmptyDataError:
#         raise FileHandlingError("Loaded data file is empty.")
#     except Exception as e:
#         raise FileHandlingError(f"An error occurred: {e}")

# main()