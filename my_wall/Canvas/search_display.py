import tkinter as tk 
import tmdbsimple as tmdb
from home import home_screen 




class Search_Display(home_screen):

    def __init__(self,*args,**kwargs):
        #inherit all the methoids and properties from the home screen class in home_screen.py 
        super().__init__(Search_Display,*args,**kwargs)
        self.root = tk.Tk()
        self.search_canvas() 
        


    
    def search_canvas(self):

        self.root = tk.Tk()
        #title of application 
        self.root.title('myWall')
        #controls canvas size 
        self.height = 667 
        self.width = 375

        #creates canvas 
        self.canvas = tk.Canvas(self.root, height = self.height, width = self.width)
        self.canvas.pack()
        
    
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

        self.root.mainloop()



if __name__ == "__main__":

    search_diplay = Search_Display()
    search_diplay
