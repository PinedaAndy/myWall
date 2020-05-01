import tkinter as tk 
import tmdbsimple as tmdb
#import search_display as sd

tmdb.API_KEY = 'bf2db7d8063307bdcc241c3919c45564'

# holds the homescreen 

class home_screen():

    def __init__(self,*args,**kwargs):
        
        self.canvas()
    
        #creates search entry option and takes in search 
        self.search_name = tk.StringVar()
        self.search = tk.Entry(self.root, bg = 'white', bd = 3, textvariable = self.search_name)
        self.search.place(x = 27, y = 22 , height = 44, width = 208)
        self.search_name = self.search.get()

        ## Search button 
        search_button = tk.Button(self.root,text = 'Enter', bg = '#A4DFAA', command = 'NADA') #takes the search name and calles the search display 
        search_button.place(x = 246, y = 22, height = 44 , width = 103)
        

        # Movies Frames 
        main_display = tk.Frame(self.root,bg = 'pink')
        main_display.place(x = 27, y = 91 , height = 513, width= 322)

        ### Print Search hold into the frame for movies 


        self.root.mainloop()
        


    # Stores the main canvas display for the screen 

    def canvas(self):

        self.root = tk.Tk()
        
        #title of application 
        self.root.title('myWall')

        #variables 
        self.search_name = '' #name of the movie 
        #self.search_display = sd 

        #controls canvas size 
        self.height = 667 
        self.width = 375

        #creates canvas 
        self.main_canvas = tk.Canvas(self.root, height = self.height, width = self.width, bg = '#100B20')
        self.main_canvas.pack()


        
       



if __name__ == "__main__":
    home = home_screen()
    home
