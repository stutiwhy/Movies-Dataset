import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from one import plot_average_rating_by_rating, plot_genre_distribution, plot_rating_vs_raters


def main():
    st.title('Movie Dataset Analysis Dashboard')


    st.sidebar.title('Choose Visualization')
    visualization_option = st.sidebar.selectbox(
        'Select a visualization',
        ('Average Rating by Movie Rating', 'Genre Distribution', 'Rating vs. Number of Raters')
    )

    # Load data (sample)
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

    if visualization_option == 'Average Rating by Movie Rating':
        st.subheader('Average Rating by Movie Rating')
        fig = plot_average_rating_by_rating(df)
        st.pyplot(fig)

    elif visualization_option == 'Genre Distribution':
        st.subheader('Genre Distribution')
        fig = plot_genre_distribution(df)
        st.pyplot(fig)

    elif visualization_option == 'Rating vs. Number of Raters':
        st.subheader('Rating vs. Number of Raters')
        fig = plot_rating_vs_raters(df)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
