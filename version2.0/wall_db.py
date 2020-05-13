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
    def __init__(self, id, title, genre, release_date, overview, poster_image="", trailer_link=""):
        self.id = id
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.poster_image = poster_image
        self.trailer_link = trailer_link

    #def get_image(self):
        

    #def get_trailer_link(self):
        
class Wall:
    """ The list of movies the user wants to watch. 
    
    Attributes:
        watched (list): the list of watched movies (Movie obj)
        intended (list): the list of movies to be watched (Movie obj)"""
    
    def __init__(self):
        
        self.watched = []
        self.intended = []

        # headers of movies.csv: id, watched, title, genre, , release_date, overview, poster_path, trailer_link
        # load data of movies already saved
        movies = pd.read_csv("./movies.csv")

        # sort movies by whether they were watched or not
        for movie in movies:
            id, title, genre, release_date, overview, poster_image, trailer_link = [movie['id'], movie['title'], movie['genre'], movie['release_date'], movie['overview'], movie['poster_image'], movie['trailer_link']]

            if movie['watched'] == 1:
                self.watched.append(Movie(id, title, genre, release_date, overview, poster_image, trailer_link))
            elif movie['watched'] == 0:
                self.intended.append(Movie(id, title, genre, release_date, overview, poster_image, trailer_link))


    #def get_recommendations(self, movie_id):


    def add_to_watched(self, movie_id):
        """ Adds movie to watched list and removes it from intended list using id of movie"""
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

    def recompile_list(self):
        columns = ['id', 'title', 'genre', 'release_date', 'overview', 'poster_image', 'trailer_link']

        movies = self.watched.append(self.intended)
        df = pd.DataFrame(data = movies)
        df.to_csv(columns = columns)

            



def search_tmdb(my_query):
    """ Searches tmdb by title. 
    Returns:
        results_list: a list of search results with video """
    search = tmdb.Search()
    response  = search.movie(query = my_query)
    results_list = []
    for movie in search.results:
        movie_id = movie['id']
        data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb.API_KEY}&append_to_response=videos,images")
        parsed_data = data.json()
        time.sleep(1)

        # sort out desired metadata
        id, title, genre, release_date, overview = [parsed_data['id'], parsed_data['title'], parsed_data['genres'][0]['name'], parsed_data['release_date'][:3], parsed_data['overview']]

        # make video link
        link = ""
        if parsed_data['videos'] is not None:
            # get video data
            video_data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={tmdb.API_KEY}")
            parsed_video_data = video_data.json()

            for result in parsed_video_data['results']:
                # filter for exclusively trailers and teasers; only supports youtube videos
                if (result['type'] in ['Trailer', 'Teaser']) and (result['site'] == 'Youtube'):
                    key = result['key']
                    link = f"https://www.youtube.com/watch?v={key}"
                    break
            
        
        
        results_list.append(Movie(id, title, genre, release_date, overview, trailer_link = link))
        time.sleep(1)
    return results_list



def get_recommendations(movie_id):
    data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={tmdb.API_KEY}&append_to_response=videos,images")
    parsed_data = data.json()

    recommendations = []

    for movies in parsed_data:
        id, title, genre, release_date, overview = [parsed_data['id'], parsed_data['title'], parsed_data['genres'][0]['name'], parsed_data['release_date'][:3], parsed_data['overview']]
        link = ""
        # make video link
        if parsed_data['videos'] is not None:
            # get video data
            video_data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={tmdb.API_KEY}")
            parsed_video_data = video_data.json()

            for result in parsed_video_data['results']:
                # filter for exclusively trailers and teasers; only supports youtube videos
                if (result['type'] in ['Trailer', 'Teaser']) and (result['site'] == 'Youtube'):
                    key = result['key']
                    link = f"https://www.youtube.com/watch?v={key}"
                    break

        recommendations.append(Movie(id, title, genre, release_date, overview, trailer_link = link))
    return recommendations


if __name__ == "__main__":
    wall = Wall()
    wall.intended = search_tmdb("The Third Man")[0]
    wall.recompile_list()
    print(str(get_recommendations(1092)))
    time.sleep(30)