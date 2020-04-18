import tmdbsimple as tmdb
import os 

# fix this
tmdb.API_KEY = 'bf2db7d8063307bdcc241c3919c45564'

"""

Searches the The Movie Database for a movie with the titled entered by the user
or similar 

"""
class Search:
    

    def __init__(self,movie):
        self.movie = movie
    
    
    def search(self,name):
        search = tmdb.Search()
        response = search.movie(query = name)

        #Showing search results and letting you select a movie
        #used a dictonary to store title as key and ID as value 
        
        search_hold = {}
        
        count = 1 
        for s in search.results:
            title = s["title"]
            title_id = s["id"]

            search_hold[count] = []
            search_hold[count].append(title)
            search_hold[count].append(title_id)
            count += 1
            
          
        #returns search results in a dictonary 
        return search_hold

    def selection(self,dict):
        
        selection = int(input('Select a movie: ')) 

        if selection in dict.keys():
            movie_id = dict[selection][1]
            title = str(dict[selection][0])
            self.movie = tmdb.Movies(int(movie_id))
            
            print("\n")

            return movie_id, self.movie, title


        else:
            print("Movie Not Found")



"""

Users personal collection of saved movies that they intend to watch 
works by saving the movies designated Id number given by TMDB

"""

class MyCollection:

    def __init__(self):
        self.mycollection = {'user':None, 'intended':{'id_num':[]}, 'watched':{'id_num':[]} }
        self.movie = tmdb.Movies()
        self.id = 630
        
  
    def check(self,id_num):

        """
        Opens your list of movies you intend to watch. Movies are saved by ID numbers 
        to a text file named intended.txt 

        If movie id number is already in the intended.txt file then a print statement 
        will print letting you know that the selected movie is already in your list 
        else it'll add the new id number to your intended to watch list
        """


        #Checks for duplicte id's in your list so you cant have the same movie added more than once
        # creates a keys from the id's then turns into a list without any duplicate values

        current_list_dict = {}
        with open('intended.txt') as id_list:
            for number in id_list:
                number = number.rstrip()
                current_list_dict[number] = ''

        current_list = list(dict.fromkeys(current_list_dict))



        ## Checks to see if you already have the movie added on your list
        ## else it appends the new id to your collections list 

        id_num = str(id_num)

        if id_num in current_list:
            if id_num in self.mycollection['intended']['id_num']: # checks to see if id number is already in self.mycollection dictonary 
                return True,current_list
        else: 
            return False, current_list


    def add_intended(self,id_num):

        # Does a quick check to see if movie is already in your list 
        # False == Not in list, True == in list
        m = MyCollection()
        prompt = m.check(id_num)


        if prompt == True:
            return(print('Movie is already in list', '(', str(id_num), ')'))
        else: 
            self.mycollection['intended']['id_num'].append(id_num)

            path = open('intended.txt','a')
            id_num = str(id_num) + '\n'
            path.write(id_num)
            print('Movie Succesffuly added')
            
    

    def my_list(self):

        mycollection = self.mycollection

        intended_list = []
        watched_list = []

        movies = open('intended.txt','r')
        watched = open('watched.txt','r')

        for movie in movies:
            movie = movie.rstrip()
            intended_list.append(movie)

        for movie in watched: 
            movie = movie.rstrip()
            watched_list.append(movie)

        return intended_list,watched_list



 


####################                  
    
        
        



       
       
### Testing for Application 


user_input = str(input("Enter a movie: \n"))
s = Search(user_input)

print(s.search(user_input))
mov = s.search(user_input)
movie_id,movie,title = s.selection(mov)


c = MyCollection()
answer = str(input('Add movie to list [y/N]?: '))

if answer == 'y':
    c.add_intended(movie_id)
    prompt = c.check(movie_id)
    print(c.my_list())

else: 
    print('Not added')




intended,watched = c.my_list()

"""
Prints out user movie list by Titles
opens the intended file and assigns each id to its designated movie title

"""

path = open('intended.txt','r')
for line in path: 
    num = line.rstrip()
    movie = tmdb.Movies(num)
    response = movie.info()
    print(movie.title)


