import pandas as pd

def create_summary_txt(df, file_path):
    total_movies = len(df)
    df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce') 
    df['year'] = df['rel_date'].dt.year
    time_span = f"{df['year'].min()} - {df['year'].max()}"
    
    highest_rated_movie = df.loc[df['rating'].idxmax()]['name']
    lowest_rated_movie = df.loc[df['rating'].idxmin()]['name']
    longest_runtime_movie = df.loc[df['run_length'].idxmax()]['name']
    shortest_runtime_movie = df.loc[df['run_length'].idxmin()]['name']
    most_rated_movie = df.loc[df['num_raters'].idxmax()]['name']
    least_rated_movie = df.loc[df['num_raters'].idxmin()]['name']

    df['genres'] = df['genres'].str.strip().str.split(';')
    df_exploded = df.explode('genres')
    most_common_genre = df_exploded['genres'].value_counts().idxmax()
    least_common_genre = df_exploded['genres'].value_counts().idxmin()

    year_most_movies = df['year'].value_counts().idxmax()
    year_fewest_movies = df['year'].value_counts().idxmin()

    avg_rating = df['rating'].mean()
    avg_runtime = df['run_length'].mean()

    top_5_common_genres = df_exploded['genres'].value_counts().head(5).index.tolist()
    top_5_longest_movies = df.nlargest(5, 'run_length')['name'].tolist()
    top_5_highest_rated_movies = df.nlargest(5, 'rating')['name'].tolist()

    with open(file_path, 'w') as file:
        file.write(f"Summary of Movie Dataset\n\n")
        file.write(f"{'-'*30}\n\n")
        file.write(f"Total Number of Movies: {total_movies}\n")
        file.write(f"Time Span Covered: {time_span}\n\n")

        file.write(f"Highest Rated Movie: {highest_rated_movie} - {df.loc[df['rating'].idxmax()]['rating']:.1f}\n")
        file.write(f"Lowest Rated Movie: {lowest_rated_movie} - {df.loc[df['rating'].idxmin()]['rating']:.1f}\n\n")

        file.write(f"Longest Runtime Movie: {longest_runtime_movie} - {df.loc[df['run_length'].idxmax()]['run_length']} minutes\n")
        file.write(f"Shortest Runtime Movie: {shortest_runtime_movie} - {df.loc[df['run_length'].idxmin()]['run_length']} minutes\n\n")

        file.write(f"Most Rated Movie: {most_rated_movie} - {df.loc[df['num_raters'].idxmax()]['num_raters']}\n")
        file.write(f"Least Rated Movie: {least_rated_movie} - {df.loc[df['num_raters'].idxmin()]['num_raters']}\n\n")

        file.write(f"Most Common Genre: {most_common_genre}\n")  # Include the most common genre
        file.write(f"Least Common Genre: {least_common_genre}\n\n")

        file.write(f"Year with Most Movies Released: {year_most_movies} - {df['year'].value_counts().max()}\n")
        file.write(f"Year with Fewest Movies Released: {year_fewest_movies} - {df['year'].value_counts().min()}\n\n")

        file.write(f"Average Movie Rating: {avg_rating:.2f}\n")
        file.write(f"Average Movie Runtime: {avg_runtime:.2f} minutes\n\n")

        file.write(f"Top 5 Most Common Genres: {', '.join(top_5_common_genres)}\n")
        file.write(f"Top 5 Longest Movies: {', '.join(top_5_longest_movies)}\n")
        file.write(f"Top 5 Highest Rated Movies: {', '.join(top_5_highest_rated_movies)}\n")

df = pd.read_csv('clean_movie_data.csv')
create_summary_txt(df, 'movie_summary.txt')
