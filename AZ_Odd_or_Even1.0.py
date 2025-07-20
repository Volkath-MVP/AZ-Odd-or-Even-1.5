#All libraries
import tkinter as tk
import random as ra
root=tk.Tk() #Initialize window
root.title("AZ Odd or Even")#Window title
root.minsize(800, 600)#Minimum window size
#Random Number Generator
number=ra.randint(1, 99)
#Question with random number
Question=tk.Label(root, text=f"O numero {number} é Impar ou par?", font=("Arial", 14))
Question.pack(pady=40) #This already works, so I’m not switching to .place :/
#Result
result=tk.Label(root, text="Where is your Motivation?", font=("Arial", 20))
result.pack(pady=20) #This already works too, soooooo I’m not switching to .place :)
#Buttons
#button Odd
Button_Odd = tk.Button(root, text="Impar", font=("Arial", 12))
Button_Odd.place(relx=0.25, rely=0.60, anchor="center")
#Button Even
Button_Even = tk.Button(root, text="Par", font=("Arial", 12))
Button_Even.place(relx=0.75, rely=0.60, anchor="center")
root.mainloop()#Keep window open