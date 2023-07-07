#pip install pymongo[srv]
#pip install python-dotenv

#import tkinter module
import tkinter as tk

#create window
root = tk.Tk()

#provide size to window
root.geometry("500x500")
root.title('Database Management Application')
#add text label
tk.Label(text="Hello from Me !!!").pack()
label = tk.Label(root, text='Database', font=(''))

root.mainloop()