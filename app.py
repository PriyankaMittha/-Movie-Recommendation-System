import streamlit as st
import gzip
import pickle
import pandas as pd

with open("models/movie_data.pkl", "rb") as file:
    movies_dict, similarity = pickle.load(file)
movies = pd.DataFrame(movies_dict)


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommended_movies = recommend(selected_movie)

    st.write("### Recommended Movies")

    for i in range(0,10,5):

        cols = st.columns(5)

        for col, j in zip(cols, range(i,i+5)):
            if j < len(recommended_movies):

                with col:
                    st.write(recommended_movies[j])
