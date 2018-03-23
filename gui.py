
import tkinter as tk                    # imports
from tkinter import ttk

win = tk.Tk()                           # Create instance      
win.title("Python GUI")                 # Add a title 
tabControl = tk.ttk.Notebook(win)          # Create Tab Control
tab1 = tk.ttk.Frame(tabControl)            # Create a tab
tab2 = tk.ttk.Frame(tabControl)          
tab3 = tk.ttk.Frame(tabControl)          
tab4 = tk.ttk.Frame(tabControl)         
tab5 = tk.ttk.Frame(tabControl)           
tab6 = tk.ttk.Frame(tabControl)             
 
tabControl.add(tab1, text='Create a Player')      # Add the tab
#label_1 = Label(win, text ="Player Name")

tabControl.add(tab2, text='Tab 2')      


tabControl.add(tab3, text='Tab 3')     


tabControl.add(tab4, text='Tab 4')      


tabControl.add(tab5, text='Tab 5')      


tabControl.add(tab6, text='Tab 6')      


tabControl.pack(expand=1, fill="both")  # Pack to make visible


#frame = Frame(win, width=100, height=50)
#frame.place(x=700, y=0)
#label = Label(frame, text="test").pack()

#frame_2 = Frame(win, width=100, height=50)
#frame_2.place(x=700, y=0)
#label_2 = Label(frame_2, text="test").pack()
win.mainloop()                          # Start GUI