import os
import requests
import time
import csv
import json
import pandas as pd
import tkinter as tk
import tmdbsimple as tmdb

tmdb.API_KEY = 'bf2db7d8063307bdcc241c3919c45564'

class Movie:
    """ The data associated with a movie """
    def __init__(self, movie_id, title, genre, release_date, overview, poster_image="", trailer_link=""):
        self.movie_id = movie_id
        self.title = title
        self.overview = overview
        self.genre = genre
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

        # headers of movies.csv: movie_id, watched, title, genre, , release_date, overview, poster_path, trailer_link
        # load data of movies already saved
        #movies = pd.read_csv("./movies.csv") #columns = ['movie_id', 'title', 'genre', 'release_date', 'overview', 'poster_image', 'trailer_link'])
        movies = []
        with open("./movies.csv", mode = 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                movies.append(row)
        
        # sort movies by whether they were watched or not
        for movie in movies:
            movie_id, title, genre, release_date, overview, poster_image, trailer_link = [movie['movie_id'], movie['title'], movie['genre'], movie['release_date'], movie['overview'], movie['poster_image'], movie['trailer_link']]

            if movie['watched'] == 1:
                self.watched.append(Movie(movie_id, title, genre, release_date, overview, poster_image, trailer_link))
            elif movie['watched'] == 0:
                self.intended.append(Movie(movie_id, title, genre, release_date, overview, poster_image, trailer_link))


    #def get_recommendations(self, movie_id):


    def add_to_watched(self, new_movie_id):
        """ Adds movie to watched list and removes it from intended list using movie_id of movie"""
        i = 0
        while i < len(self.intended):
            if self.intended[i].movie_id == new_movie_id:
                index = i
                break
            else:
                i += 1
        self.watched.append( self.intended.pop(index) )
    
    def add_to_list(self, movie):
        movie = search_tmdb(movie.movie_id)

    def recompile_list(self):
        columns = ['movie_id', 'title', 'genre', 'release_date', 'overview', 'poster_image', 'trailer_link']

        movies = self.watched.append(self.intended)
        df = pd.DataFrame(data = movies)
        df.to_csv()

            



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
        date = parsed_data['release_date']
        year = date[0:3]
        genre_data = parsed_data['genres']
        if genre_data != []:
            genre_name = genre_data[0]
        movie_id, title, genre, release_date, overview = [parsed_data['id'], parsed_data['title'], genre_name['name'], year, parsed_data['overview']]

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
            
        
        
        results_list.append(Movie(movie_id, title, genre, release_date, overview, trailer_link = link))
        time.sleep(1)
    return results_list



def get_recommendations(movie_id):
    data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={tmdb.API_KEY}&append_to_response=videos,images")
    paged_data = data.json()
    recommendations = []
    
    parsed_data = []
    for page in paged_data['results']:
        parsed_data.append(page)



    for movies in parsed_data:
        date = movies['release_date']
        year = date[0:3]
        genre_data = movies['genre_ids']
        if genre_data != []:
            genre_name = genre_data[0]
        
        movie_id, title, genre, release_date, overview = [movies['id'], movies['title'], genre_name, year, movies['overview']]
        link = ""
        # make video link
        # get video data
        video_data = requests.get(url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={tmdb.API_KEY}")
        parsed_video_data = video_data.json()
        for result in parsed_video_data['results']:
            # filter for exclusively trailers and teasers; only supports youtube videos
            if (result['type'] in ['Trailer', 'Teaser']) and (result['site'] == 'Youtube'):
                key = result['key']
                link = f"https://www.youtube.com/watch?v={key}"
                break

        recommendations.append(Movie(movie_id, title, genre, release_date, overview, trailer_link = link))
    return recommendations


if __name__ == "__main__":
    wall = Wall()
    wall.intended.append(search_tmdb("The Great Escape")[0])
    wall.recompile_list()
    print(str(get_recommendations(1092)[0].title))      
    time.sleep(30)