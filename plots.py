# Importing  modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_average_rating_by_rating(df):
    ratings = df['movie-rated'].unique()
    avg_ratings = df.groupby('movie-rated')['rating'].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(avg_ratings.index, avg_ratings.values, color='blue')
    plt.title('Average Rating by Movie Rating')
    plt.xlabel('Movie Rating')
    plt.ylabel('Average Rating')
    plt.ylim(0, 10)  
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt


def plot_genre_distribution(df):
    genres = df['genres'].str.split('; ', expand=True).stack().value_counts()

    plt.figure(figsize=(10, 6))
    genres.plot(kind='bar', color='purple')
    plt.title('Distribution of Movie Genres')
    plt.xlabel('Genres')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt


def plot_rating_vs_raters(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['rating'], df['num_raters'], color='green', alpha=0.5)
    plt.title('Rating vs. Number of Raters')
    plt.xlabel('Rating')
    plt.ylabel('Number of Raters')
    plt.tight_layout()

    return plt


def main():
#sample
    df = pd.DataFrame({
        'name': ['The Dark Knight', 'Inception', 'The Matrix', 'The Lord of the Rings', 'The Dark Knight Rises'],
        'year': [2008, 2010, 1999, 2001, 2012],
        'movie-rated': ['PG-13', 'PG-13', 'R', 'PG-13', 'PG-13'],
        'run_length': ['2h 32min', '2h 28min', '2h 16min', '2h 58min', '2h 44min'],
        'genres': ['Action; Crime; Drama;', 'Action; Adventure; Sci-Fi;', 'Action; Sci-Fi;', 'Action; Adventure; Drama;', 'Action; Adventure;'],
        'release_date': ['18 July 2008 (USA)', '16 July 2010 (USA)', '31 March 1999 (USA)', '19 December 2001 (USA)', '20 July 2012 (USA)'],
        'rating': [9.0, 8.8, 8.7, 8.8, 8.4],
        'num_raters': [2224522, 1981675, 1619761, 1609165, 1470329],
        'num_reviews': [6836, 3820, 4281, 5365, 2979]
    })

  
    fig = plot_average_rating_by_rating(df)
    plt.show()

    fig = plot_genre_distribution(df)
    plt.show()

    fig = plot_rating_vs_raters(df)
    plt.show()

if __name__ == "__main__":
    main()
