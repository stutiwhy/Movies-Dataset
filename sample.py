import streamlit as st
import pandas as pd
from PIL import Image
import base64
import matplotlib.pyplot as plt
from plotting import plot_ratings_vs_raters, plot_genres_vs_runtime, plot_movies_by_genre_over_time,plot_genre_ratings_bar
from file_handling import load_clean_data, save_clean_data


df = load_clean_data('clean_movie_data.csv')

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
        print(data)
        #print(base64.b64encode(data).decode())
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Text shadow for better visibility */
    }
    .stApp p {
        font-size: 18px;
        color: white; /* Paragraph text color */
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* Text shadow for better visibility */
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('WhatsApp Image 2024-06-28 at 17.51.37.jpeg')


def basic_analysis():
    st.title('MOVIE DATA ANALYSIS')

    st.header('Introduction: ')
    st.subheader('________________________________________')
    st.write('_This is a sample intro_')

    st.subheader('The top 10 highest rated movies: ')
    df = pd.read_csv('clean_movie_data.csv')
    top_10 = df.sort_values('rating', axis=0, ascending=False).head(10)
    st.write(top_10)

    last_10 = df.sort_values('rating', axis=0, ascending=False).tail(10)
    st.write(last_10)

    graph1 = plot_ratings_vs_raters(df)
    st.pyplot(graph1)

    graph2 = plot_genres_vs_runtime(df)
    st.pyplot(graph2)

    graph3 = plot_movies_by_genre_over_time(df)
    st.pyplot(graph3)

    graph4 = plot_genre_ratings_bar(df)
    st.pyplot(graph4)


def search():
    st.title('Search for movies: ')
    st.header('Choose filter to search for movies')
    st.subheader('_________________________________________')

    st.selectbox()


st.sidebar.title('Choose')
ch = st.sidebar.selectbox('Select what to view:', {'Basic movie analysis', 'Search for movies'})
if ch == 'Basic movie analysis':
    basic_analysis()

elif ch == 'Search for movies':
    search()
