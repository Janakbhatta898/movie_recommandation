

import streamlit as st
import pandas as pd
import pickle
import requests
import time



import numpy as np



def get_poster(movie_id):
    reponse=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d3628cc9d8be3b843f3f2a99c6552459")
    data=reponse.json()
    poster="https://image.tmdb.org/t/p/original/"+data['poster_path']
    return poster


movies_new=pickle.load(open('movies_new.pkl','rb'))
movies=pd.DataFrame(movies_new)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    # index of whole data set not just so we did masking

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # we take the firs 9 movie which are similar to the user choice and sorted on the basis of similarity score

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:5]
    recommended_movies=[]
    recommended_poster=[]

    for i in movie_list:

        recommended_poster.append(get_poster(movies.iloc[i[0]].id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies,recommended_poster
st.title("Recommendation system")
st.badge("choose ")
movie=st.selectbox('Select Movies',movies['title'].values)

if st.button("recommend"):

    movie_recommended,poster_recommended=recommend(movie)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.header(movie_recommended[0])
        st.image(poster_recommended[0])
    with col2:
        st.header(movie_recommended[1])
        st.image(poster_recommended[1])
    with col3:
        st.header(movie_recommended[2])
        st.image(poster_recommended[2])
    with col4:
        st.header(movie_recommended[3])
        st.image(poster_recommended[3])



    st.badge("success ")

