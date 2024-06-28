import streamlit as st
import pandas as pd
from PIL import Image
import base64
import matplotlib.pyplot as plt
from plotting import plot_movies_by_genre_over_time, plot_genre_ratings_bar, plot_ratings_vs_raters, plot_runtime_vs_year, plot_ratings_distribution, plot_runtime_distribution, plot_movies_by_decade, plot_raters_by_genre_bar
from file_handling import load_clean_data, save_clean_data
from exceptions import FileHandlingError, PlottingError

# Load and preprocess the data
try:
    df = load_clean_data('clean_movie_data.csv')
    df['rel_date'] = pd.to_datetime(df['rel_date'], errors='coerce')
    df['year'] = df['rel_date'].dt.year
except FileNotFoundError:
    raise FileHandlingError("Clean data file not found.")
except pd.errors.EmptyDataError:
    raise FileHandlingError("Loaded data file is empty.")
except Exception as e:
    raise FileHandlingError(f"An error occurred while loading the data: {e}")

# Function to get base64 string of image file
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        raise FileHandlingError(f"An error occurred while encoding the image: {e}")

# Function to set background image
def set_background(png_file):
    try:
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
            padding: 20px;
        }
        .stApp .main {
            background-color: rgba(30, 30, 30, 0.9);
            padding: 20px;
        }
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .stApp p {
            font-size: 18px;
            color: white;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }
        </style>''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        raise PlottingError(f"An error occurred while setting the background: {e}")

# Set the background image
set_background('movie-back.png')

# Function for basic analysis
def basic_analysis():
    st.title('Movies Dataset Analysis')

    st.header('An EDA')
    st.subheader('Introduction:')
    st.write(
        "This project uses Matplotlib and Streamlit to analyze a dataset of movies, focusing on understanding the factors contributing to their success. By examining movie data, we gain insights into audience preferences, make informed business decisions, and identify trends in popular cinematic themes. This analysis also sheds light on the economic impact of the film industry and explores cultural influences in media. Essentially, it's about leveraging data to uncover valuable insights into what resonates with audiences in movies."
    )
    st.markdown('<hr>', unsafe_allow_html=True)

    # Top 10 highest rated movies
    st.subheader('Top 10 Highest Rated Movies:')
    try:
        df = pd.read_csv('clean_movie_data.csv')
        top_10 = df.sort_values('rating', axis=0, ascending=False).head(10)
        st.dataframe(top_10, hide_index=True)
    except FileNotFoundError:
        raise FileHandlingError("Clean data file not found.")
    except pd.errors.EmptyDataError:
        raise FileHandlingError("Loaded data file is empty.")
    except Exception as e:
        raise FileHandlingError(f"An error occurred while fetching the top 10 highest rated movies: {e}")

    # Top 10 lowest rated movies
    st.subheader('Top 10 Lowest Rated Movies:')
    try:
        last_10 = df.sort_values('rating', axis=0, ascending=True).head(10)
        st.dataframe(last_10, hide_index=True)
    except Exception as e:
        raise FileHandlingError(f"An error occurred while fetching the top 10 lowest rated movies: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    # Data visualization introduction
    st.subheader('Data Visualization:')
    st.write(
        'Data visualization is a critical aspect of data analysis because it allows for the representation of complex data in a visual format. Visualizations make it easier to identify patterns, trends, and outliers in the data, facilitating better decision-making.'
    )
    st.markdown('<hr>', unsafe_allow_html=True)

    # Plotting visualizations
    try:
        g1 = plot_runtime_distribution(df)
        st.pyplot(g1)
        st.write('fig.1 : Runtime Histogram')
    except PlottingError as e:
        st.write(f"An error occurred while plotting runtime distribution: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        g2 = plot_ratings_distribution(df)
        st.pyplot(g2)
        st.write('fig.2 : Ratings Histogram')
    except PlottingError as e:
        st.write(f"An error occurred while plotting ratings distribution: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        g3 = plot_genre_ratings_bar(df)
        st.pyplot(g3)
        st.write('fig.3 : Genre by Ratings Bar Graph')
    except PlottingError as e:
        st.write(f"An error occurred while plotting genre ratings bar graph: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        df = load_clean_data('clean_movie_data.csv')
        g8 = plot_raters_by_genre_bar(df)
        st.pyplot(g8)
        st.write('fig.4 : Average Number of Raters by Genre Bar Graph')
    except PlottingError as e:
        st.write(f"An error occurred while plotting raters by genre: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        g4 = plot_ratings_vs_raters(df)
        st.pyplot(g4)
        st.write('fig.4 : Ratings by Number of Raters Scatter Plot')
    except PlottingError as e:
        st.write(f"An error occurred while plotting ratings vs number of raters: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        g5 = plot_runtime_vs_year(df)
        st.pyplot(g5)
        st.write('fig.5 : Runtime by Year Scatter Plot')
    except PlottingError as e:
        st.write(f"An error occurred while plotting runtime vs year: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        g6 = plot_movies_by_decade(df)
        st.pyplot(g6)
        st.write('fig.6 : Movies by Decade Bar Graph')
    except PlottingError as e:
        st.write(f"An error occurred while plotting movies by decade: {e}")

    st.markdown('<hr>', unsafe_allow_html=True)

    try:
        df = load_clean_data('clean_movie_data.csv')
        g7 = plot_movies_by_genre_over_time(df)
        st.pyplot(g7)
        st.write('fig.7 : Number of Movies Growth by Genre Over Time Line Plot')
    except PlottingError as e:
        st.write(f"An error occurred while plotting movies by genre over time: {e}")

# Function for search
def search():
    st.title('Search For Movies')

    st.header('Choose a genre to search for movies : ')
    selected_genre = st.selectbox('Select Genre:', {'Action', 'War', 'Sport', 'Thriller', 'Drama', 'Biography', 'Comedy', 'Animation', 'Adventure', 'Romance', 'Mystery', 'Crime', 'Music', 'Horror', 'Western', 'Sci-Fi', 'History'})

    # Filter the dataframe based on selected_genre
    try:
        filtered_df = df[df['genres'].apply(lambda genres: selected_genre in genres)]
        if filtered_df.empty:
            st.write(f"No movies found for genre '{selected_genre}'.")
        else:
            st.write(f"Movies in genre '{selected_genre}':")
            st.dataframe(filtered_df[['name', 'genres']], hide_index=True)
    except Exception as e:
        raise PlottingError(f"An error occurred while searching for movies by genre : {e}")

    unique_years = sorted(df['year'].unique())
    selected_year = st.selectbox('Select Year', unique_years)

    # Filter the dataframe based on selected_genre and year
    try:
        filtered_df = df[
            (df['genres'].apply(lambda genres: selected_genre in genres)) &
            (df['year'] == selected_year)
        ]

        if filtered_df.empty:
            st.write(f"No movies found for genre '{selected_genre}' in the year {selected_year}.")
        else:
            st.write(f"Movies in genre '{selected_genre}' from {selected_year}:")
            st.dataframe(filtered_df[['name', 'genres', 'year']], hide_index=True)
    except Exception as e:
        raise PlottingError(f"An error occurred while searching for movies by genre and year : {e}")

# Sidebar selection
st.sidebar.title('Make Your Choice')
ch = st.sidebar.selectbox('Select page : ', {'Movie Dataset Analysis', 'Search For Movies'})

# Main content based on selection
if ch == 'Movie Dataset Analysis':
    basic_analysis()
elif ch == 'Search For Movies':
    search()
