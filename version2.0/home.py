import tkinter as tk





class home():



    def __init__(self):

        """ Creates the main window""" 

        #Creating the main body 
        self.root = tk.Tk() 
        self.root.geometry('448x378')


        #Creates title
        self.root.title('MyWall')



        #font used for canvas 
        self.main_font = "Adorn condensed sans"



        #Crates MyWall Label 
        self.main_mywall_label = tk.Label(text = 'My Wall', font =(self.main_font,40))
        self.main_mywall_label.place(x=154, y=68)


        #Creates the history button 
        self.history_button = tk.Button(self.root, text = 'History', command = self.history, width = 10, fg ='black')
        self.history_button.place(x= 6, y=8)

        #Creats the find button 
        self.find_button = tk.Button(self.root, text ="Find", command = self.find_frame, width = 20, height =2)
        self.find_button.place(x =140, y =138)


        #Creates the watchlist button 
        self.watch_list_button = tk.Button(self.root,text = 'Watchlist', command = self.watch_list, width = 20, height = 2)
        self.watch_list_button.place(x = 140, y= 188)


        #Creates the watched button 
        self.watched_list_button = tk.Button(self.root,text = 'Watched', command = self.watched_list, width = 20, height = 2)
        self.watched_list_button.place(x = 140, y= 238)


        #Creates the search button 
        self.search = tk.Button(self.root,text = 'Search', command = self.search_a_movie, width = 20, height = 2)
        self.search.place(x = 140, y= 288)


        self.root.mainloop()



    def find_frame(self):

        """ Find Frame to swipe through movies """ 
            #Need to work on closing windows when switching frames 

        #destroys previous window 
        self.root.destroy()


        #creates a new window 
        self.find_screen = tk.Tk()   
        self.find_screen.geometry('448x378')

        #Creates title for screen
        self.find_screen.title('MyWall')


        #Create the backbutton to the main screen
        self.backbutton = tk.Button(self.find_screen,text = "<--", command = home)
        self.backbutton.place(x =10, y =11)
        

        #creates my wall label 
        my_wall_label = tk.Label(self.find_screen, text ='My Wall',font =(self.main_font,12) )
        my_wall_label.place(x =195, y=11)


        #Creates canvas to hold poster for movie 
        self.poster_frame = tk.Frame(self.find_screen, bg ='black', width =164, height =134)
        self.poster_frame.place(x=15, y=42)


        #Overview textbox
        self.overview_textbox = tk.Text(self.find_screen, width = 34, height = 13)# state = 'disabled'
        self.overview_textbox.place(x=191, y=43)


        #aviliable on label
        aviliable_label = tk.Label(self.find_screen, text = 'Aviliable On')
        aviliable_label.place(x =60, y =176)


        #play button for trailer 
        self.play_button = tk.Button(self.find_screen, text = 'Play', width = 10, height = 3)
        self.play_button.place(x=167, y=250)



        #add to watch list button 
        add_watch_list = tk.Button(self.find_screen, text = 'Watch', height =2, width = 10)
        add_watch_list.place(x=22 , y=333)


        #like button for movies 
        like_movie = tk.Button(self.find_screen, text = 'Like', height =2, width = 10)
        like_movie.place(x=122 , y=333)

        #Dislike button for movies 
        dislike_movie = tk.Button(self.find_screen, text = 'Dislike', height =2, width = 10)
        dislike_movie.place(x=222 , y=333)

        #Watched button for movies 
        dislike_movie = tk.Button(self.find_screen, text = 'Watched', height =2, width = 10)
        dislike_movie.place(x=322 , y=333)



        self.find_screen.mainloop()

    
    def history(self):

        """Shows your history of liked and disliked movies """
        self.root.destroy()

        #Creates window 
        history = tk.Tk()
        history.geometry('448x378')
        history.title('MyWall')



        #Creates the backbutton 
        backbutton = tk.Button(history, text = "<--", command = home)
        backbutton.place(x =10, y =11)


        #creates my wall label 
        my_wall_label = tk.Label(history, text ='My Wall',font =(self.main_font,12) )
        my_wall_label.place(x =195, y=11)


        #like button to show liked history 
        like_button = tk.Button(history, text = 'Liked', width = 10)
        like_button.place(x= 121, y = 33)

        #dislike button to show disliked history
        dislike_button = tk.Button(history, text = 'Disliked', width = 10)
        dislike_button.place(x= 224, y = 33)


        #Listbox to display results 
        like_listbox = tk.Listbox(history, height =16 , width = 46)
        like_listbox.place(x=14, y = 66)


        #Remove Buttoon 
        remove_button = tk.Button(history, text = 'Remove', height =1 , width = 10)
        remove_button.place(x=171, y=343)

        

        history.mainloop()


    
    
    def watch_list(self):

        """Shows your watch list of movies """

        self.root.destroy()

        #Creates window 
        watch_list = tk.Tk()
        watch_list.geometry('448x378')
        watch_list.title('MyWall')



        #Creates the backbutton 
        backbutton = tk.Button(watch_list, text = "<--", command = home)
        backbutton.place(x =10, y =11)


        #creates my wall label 
        my_wall_label = tk.Label(watch_list, text ='My Wall',font =(self.main_font,12) )
        my_wall_label.place(x =195, y=11)



        #Listbox to display results 
        watch_list_listbox = tk.Listbox(watch_list, height =16 , width = 46)
        watch_list_listbox.place(x=14, y = 66)



        #Remove Buttoon 
        remove_button = tk.Button(watch_list, text = 'Remove', height =1 , width = 10)
        remove_button.place(x=171, y=343)

        

        watch_list.mainloop()


    def watched_list(self):

        """Shows your history of watched movies"""


        self.root.destroy()

        #Creates window 
        watched_list = tk.Tk()
        watched_list.geometry('448x378')
        watched_list.title('MyWall')



        #Creates the backbutton 
        backbutton = tk.Button(watched_list, text = "<--", command = home)
        backbutton.place(x =10, y =11)


        #creates my wall label 
        my_wall_label = tk.Label(watched_list, text ='My Wall',font =(self.main_font,12) )
        my_wall_label.place(x =195, y=11)



        #Listbox to display results 
        watched_list_listbox = tk.Listbox(watched_list, height =16 , width = 46)
        watched_list_listbox.place(x=14, y = 66)



        #Remove Buttoon 
        remove_button = tk.Button(watched_list, text = 'Remove', height =1 , width = 10)
        remove_button.place(x=171, y=343)

        

        watched_list.mainloop()



    def search_a_movie(self):

        """Lets you upload a list of movies from netflix to load onto the program"""


        self.root.destroy()

        #Creates window 
        search = tk.Tk()
        search.geometry('448x378')
        search.title('MyWall')



        #Creates the backbutton 
        backbutton = tk.Button(search, text = "<--", command = home)
        backbutton.place(x =10, y =11)


        #creates search entry bar 
        self.search_bar = tk.Entry(search, width =40)
        self.search_bar.place(x =63, y = 10 )



        #Listbox to display results 
        search_listbox = tk.Listbox(search, height =16 , width = 46)
        search_listbox.place(x=14, y = 66)



        #Add Button 
        add_button = tk.Button(search, text = 'Add', height =1 , width = 10)
        add_button.place(x=171, y=343)

        

        search.mainloop()
  









if __name__ == "__main__":
    h = home() 
    h 