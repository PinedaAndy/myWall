import tkinter as tk
import tkinter.font as tkFont
import tkinter.frame as tkFrame



class Loading_Screen(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        container = tk.Frame(self)
        container.pack()


        self.parent = parent 
        self.loading_screen()


        ### Source code used from source https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
        ### used for packing frames into layers

        

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = page_name
        frame.tkraise()     
     

    def loading_screen(self):
        ls = Loading_Screen(tk.Frame)


        self.parent.geometry("600x600")
        self.parent.title("Login")
        
        ## Creates the Login Caption 
        self.label = tk.Label(self.parent, text = "My Wall", font = ("Marker Felt", 80), fg = 'white' , height = 5, )
        self.label.pack()

        self.button =tk.Button(self.parent, text = "Enter" ,height = 5 ,width = 10, command = ls.show_frame('Home_Screen'))
        self.button.pack()

    

class Home_Screen(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent 
        self.main()

    def main(self):
        self.parent.geometry("600x600")
        self.parent.title("Home")
        

    
      


if __name__ == '__main__':


   # Run app 
  
   root = tk.Tk()
   run = Loading_Screen(root)
   root.mainloop()

   