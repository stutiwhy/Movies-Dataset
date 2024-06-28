import pandas as pd
from exceptions import DataCleaningError, MissingColumnError

def clean_data(df):

    if df.empty:
        raise DataCleaningError("Data is empty.") # exception handling for if the data is empty.

    # list with names of required columns so we can raise exception if all columns are not there
    required_columns = ["name","year","movie_rated","run_length","genres","release_date","rating","num_raters","num_reviews"]
    for col in required_columns:
        if col not in df.columns:
            raise MissingColumnError(col)

    df.drop_duplicates(inplace = True) # removing all the redundant data from the dataset

    df.drop(['review_url'], axis = 1, inplace = True)

    print("Data cleaned successfully!")

    return df

# print(df['rating'].value_counts())

# # print(df.groupby('year').index().values())
# # 1915 - 2020

# print(df.shape)
# # (1392, 9)

# print(df.describe)

# print(df.genres.describe)

# # agegroup = df.groupby('movie_rated').count()

# # plt.figure(figsize=(10,10))
# # plt.plot(agegroup, 'g--')
# # plt.xlabel('Age categories')
# # plt.ylabel('Number of movies')
# # st.pyplot(plt)

# yeargroups = df['year'].unique()

# print(yeargroups)