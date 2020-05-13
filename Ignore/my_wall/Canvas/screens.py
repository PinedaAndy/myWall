# Contains all the screens and object that are callable onto a canvas
# an easier way of just designing the project without having to repeat code 

import os
import tkinter as tk
import tmdbsimple as tmdb
from PIL import Image 
from PIL import ImageTk


tmdb.API_KEY = 'bf2db7d8063307bdcc241c3919c45564'





















# Holds the different screens and widgets for the application 

class Screens():


    def __init__(self,*args,**kwargs):
        self.canvas()
        self.menu()
        self.my_frame()
       

        self.root.mainloop()
    





    #Main Screen canvas 

    def canvas(self,*kwargs):

        self.root = tk.Tk()
        
        #title of application 
        self.root.title('myWall')

        #variables 
        self.search_name = '' #name of the movie 
        #self.search_display = sd 

        #controls canvas size 
        self.height = 435
        self.width = 630

        #creates canvas 
        self.main_canvas = tk.Canvas(self.root, height = self.height, width = self.width, bg = '#000000', bd = 0)
        self.main_canvas.pack()

       
        
    



    # Menu with 
    #   Home - Takes you to home screen 
    #   Search - takes you to search for a new movie 
    #   Watched - Takes you to watched 

    def menu(self):
    
        # Background button blur 
        #image = Image.open("/Users/Professional/Desktop/my_wall/Resources/Menu/home_button.png") #opens the button blur vector image (*Book Dark Sketch Concept)
        #photo = ImageTk.PhotoImage(image)

        #Button Frame 

        #home button
        self.home_button = tk.Button(self.root,text = 'HOME')
        self.home_button.place(width = 100, height = 25, x = 28, y = 402)
        
        
        #Search button
        self.search_button = tk.Button(self.root,text = 'SEARCH')
        self.search_button.place(width = 100, height = 25, x = 143, y = 402)
        

        #Watched button
        self.home_button = tk.Button(self.root,text = 'WATCHED')
        self.home_button.place(width = 100, height = 25, x = 258, y = 402)
      



    ## SEARCH BAR 
    ## NEEDS WORK
        ## - Needs to be able to search and change to the canvas with the search results 
    def search_bar(self):
        #displays a search bar at the top to search within menu 

        # Search entry
        search_bar = tk.Entry(self.root)
        search_bar.place(x = 33, y = 17)
        search_bar.get()

        #search label text
        self.search_bar_entery = tk.Button(text = 'Enter') #Searchs the current frame in list 
        self.search_bar_entery.place(x=268 ,y=20)
        
        

















    # Displays users main frame where all movies are stored 
    def my_frame(self,**kwargs):

        #Uses class for the movie database 
        self.data = Database()

        #creats a scrollbar for canvas 
            # -- NEEDS WORK 
            #--------NEEDS TO scroll through movies in canvas 
            # -------- Maybe try creating a list box with label with backgrounds for each one 
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.place(x=600)

        #creats a canvas for the main frame 
        my_canvas = tk.Canvas(width = 603, height = 380, yscrollcommand = scrollbar.set)
        my_canvas.place(x = 14, y = 12)

        
        
        #optional arguements 
        
        job = 'none' #what to display on the canvas, default is intended to watch list 
        user_search = '' #what the user is searching in list


        path  = open('/Users/Professional/Desktop/my_wall/intended.txt','r')
        image_path = 'https://image.tmdb.org/t/p/original/' #image path to add to jpg of poster link to display poster image for movie id 

        # Default Size, stays the same 
        height = 72
        width  = 58

        # Location, Changes per row and section 
        position_x = 26
        position_y = 20



        x = 0

        while x <= 28:
          
            if x % 7 == 0:

                position_x = 26
                position_y += 80 

        
            else:

                id_placement_1 = tk.Canvas(my_canvas, width = width, height = height, bg = 'red')
                id_placement_1.place(x=position_x,y=position_y)
                

                position_x += 100

            x +=1 

                



 

        


            

            

                























        


#Functions to acess movie database for application 

class Database():

    def __init__(self):
        pass


    #Seaarches for a movie in the the movie database 
    # ----- NEEDS WORK 
    def search(self,name):
        search = tmdb.Search()
        search.movie(query = name)

        #Showing search results and letting you select a movie or tv show 
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



    # Prints your collection of selected movie from list 

    def my_list(self,**kwargs):
        
        list = ''

        intended_list = []
        watched_list = []

        movies = open('/Users/Professional/Desktop/my_wall/intended.txt','r')
        watched = open('/Users/Professional/Desktop/my_wa/watched.txt','r')


        for movie in movies:
            movie = movie.rstrip()
            intended_list.append(movie)

        for movie in watched: 
            movie = movie.rstrip()
            watched_list.append(movie)


        # Lets user pick type of list to return
        # default returns a tupile of both the list 

        if list  == 'intended':
            return intended_list
        elif list == 'watched':
            return watched
        elif list == 'both':
            return intended_list,watched_list
        else:
            return intended_list,watched_list
       

    






























    
if __name__ == "__main__":
    screens = Screens()
    screens