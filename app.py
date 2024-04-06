import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    requests.get('')


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movies=[]
    for i in distances[1:6]:
        movie_id=i[0]
        #fetch poster from Api
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'How would you like to connected?',
    movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)

