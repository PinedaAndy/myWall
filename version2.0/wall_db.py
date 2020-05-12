import os
import requests
import time
import json
import pandas as pd
import tkinter as tk
import tmdbsimple as tmdb

tmdb.API_KEY = 'bf2db7d8063307bdcc241c3919c45564'

class Movie:
    """ The data associated with a movie """
    def __init__(self, id, title, cast_crew, genre, production_co, poster_image, trailer_link):
        self.id = id
        self.title = title
        self.cast_crew = cast_crew
        self.poster_image = poster_image
        self.trailer_link = trailer_link

    #def get_recommendations(self):
        

    #def play_trailer(self):
     
    


class Wall:
    """The list of movies the user wants to watch."""
    
    def __init__(self):
        
        self.watched = []
        self.intended = []

        # headers of movies.csv: id, watched, title, cast_crew, poster_path, trailer_link
        # load data of movies already saved
        movies = pd.read_csv("movies.csv")

        # sort movies by whether they were watched or not
        for movie in movies:
            id, title, cast_crew, poster_image, trailer_link = movie

            if movie['watched'] == 1:
                self.watched.append(Movie(id, title, cast_crew, genre, budget, poster_image))
            elif movie['watched'] == 0:
                self.intended.append(Movie(id, title, cast_crew, genre, budget, poster_image))


    #def get_recommendations(self, movie_id):


    def add_to_watched(self, movie_id):
        """ Adds movie to watched list and removes it from intended list """
        i = 0
        while i < len(self.intended):
            if self.intended[i].id == movie_id:
                index = i
                break
            else:
                i += 1
        self.watched.append( self.intended.pop(index) )
    
    def add_to_list(self, movie):
        movie = search_tmdb(movie.id)


def search_tmdb(my_query):
    """ Searches tmdb by title """
    search = tmdb.Search()
    response  = search.movie(query = my_query)
    results_list = []
    for movie in search.results:
        movie_id = movie['id']
        data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb.API_KEY}&append_to_response=videos,images")
        parsed_data = data.json()
        results_list.append(parsed_data)
        time.sleep(1)
    return results_list




if __name__ == "__main__":
    print(str(search_tmdb("The Third Man")))
    time.sleep(30)