import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
class My_GUI:
    def __init__(self):
        self.App = tk.Tk()
        
        self.App.resizable("False",'False')
        
        self.App.geometry("600x400")
        
        self.App.title("App")
        
        self.App.configure(background="wheat")
        
        self.img = PhotoImage(file="C:\\Users\\MRCOM\\Downloads\\rubik.png")
        
        self.label = Label(self.App , text = "Password-Generator",font=("Arial",18))
        
        self.label.pack(padx=10,pady=10)
        
        
        
        self.label1=Label(self.App,text = "Enter Length-Max(75)")
        self.label1.pack(padx = 10 , pady = 10)
        
        self.textbox = Text(self.App , bg="white" ,height = 1 , width = 15,font = ("Arial"),borderwidth=2,relief="solid")
        self.textbox.pack(padx = 10 , pady = 10)
        
        self.btn = Button(self.App,text="Convert" , bg="red",borderwidth=1,relief="solid" ,fg="white",font=("Arial"),command = self.Convert )
        self.btn.pack(padx = 10  , pady = 10)
        
        self.result_textbox = tk.Text(self.App, bg="white", height=1, width= 15, font=("Arial",18),relief="solid",borderwidth=2)
        self.result_textbox.pack(padx = 10, pady = 10)
        
        self.App.iconphoto(False,self.img)
        
        self.App.mainloop()
        
    def Convert(self):
     lower = "abcdefghijklmnopqrstuvwxyz"
    
     upper = lower.upper()
    
     Numbers = "123456789"
    
     symbols = "!@#$%^&*()}{';"
    
     string = lower + upper + Numbers + symbols
    
     str_Val = self.textbox.get("1.0","end-1c")
     
     length = int(str_Val)
     
     password = ''.join(random.sample(string,length))
     
     try:
           
            if length > 0:
                self.result_textbox.delete("1.0", tk.END)  # Clear previous content
                self.result_textbox.insert(tk.END, password)
            else:
                raise ValueError("Please enter a positive integer for the length.")
            
     except ValueError as e:
            messagebox.showerror("Error", str(e))
         
    
         
    

    
    
    
My_GUI()