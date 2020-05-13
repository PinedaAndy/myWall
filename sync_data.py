import tmdbsimple as tmdb
tmdb.API_KEY = 'bf2db7d8063307bdcc241c3919c45564'
  
def search_movie_name(name):
    search = tmdb.Search()
    search.movie(query = name)

    #Showing search results and letting you select a movie or tv show 
    #used a dictonary to store title as key and ID as value 
        
    search_hold = [] 

    
    for s in search.results:

        #Gathers general information about the movie 
        title = s["title"]
        title_id = s["id"]
        poster_path = s["poster_path"]
        overview = s["overview"]
        release_date = s['release_date']


        
        #gets the trailer link and creates a youtube link to trailer
        #if no trailer is found 'NaN' will be assigned to variable

        movie = tmdb.Movies(title_id)
        video_details = movie.videos()

        youtube = 'https://www.youtube.com/watch?v='

        try:
            key = video_details['results'][0]['key'] #unique youtube key for video
            youtube_key = youtube + key #creates the link 
        except:
            youtube_key = 'NaN' 



        #creates a list with movie information 
        movie = [title_id,title,release_date,poster_path,youtube_key,overview]

        #appends the movie info to the search list
        search_hold.append(movie)
        
          
        
    
    #returns a list of results 
    return search_hold
    

if __name__ == "__main__":
    pass 