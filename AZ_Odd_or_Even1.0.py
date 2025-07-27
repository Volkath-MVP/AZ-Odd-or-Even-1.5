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
#Function to update the question AFTER the answer
def update_number():
    global number, message, result #Global calls the variables needed for the function, in this case "number", "message", and "result"
    number = ra.randint(1, 99)
    Question.config(text=f"O número {number} é Ímpar ou Par?")
    result.config(text="" )  #Reset message
    message=""
#Message reset
def reset_message():
    global message
    message=""
#Function that adds and subtracts the score.
score = 0
#Odd or Even Function
def check(AZ):#Yes, I added AZ in the code. I’m AZheaven, I need to leave my mark.
    global number, response
    response = (number % 2 == 0 and AZ=="Even") or (number % 2 != 0 and AZ == "Odd")#Calculates the number that was randomly generated and assigns "Even" or "Odd"
    message = "YOU HAVE POWER!" if response else "You need more Energy..."#initial message
    result.config(text = message, fg="Green" if response else "Red") #Message settings
    V(response)
    atualizar_rank()
    root.after(800, lambda: result.config(text=""))
    root.after(800, lambda: reset_message())
    root.after(800, update_number)
def V(response): #Yeah, I put "V" because I didn’t know what to name it :/
    global score
    if response:
        score += 500 #score addition
    else:
        score -=800 #score subtraction
        if score <=0: #prevents it from going below zero
            score =0
    Score.config(text=f"{score}")  #Updates the score in the text. I hadn’t thought of that... Ah... It was the f-string... I had forgotten :/
Score=tk.Label(root, text=f"{score}", font=("Arial", 12))
Score.place(relx=0.90, rely=0.30, anchor="center") # ".place" refers to the general positioning of things
#Function to update the rank
rank_text= ""
def atualizar_rank():
    global score, rank_text
    if score >= 7000:
        rank_text = "SSS"
    elif score >= 6000:
        rank_text = "SS"
    elif score >= 5000:
        rank_text = "S"
    elif score >= 4000:
        rank_text = "A"
    elif score>= 3000:
        rank_text = "B"
    elif score>= 2000:
        rank_text = "C"
    elif score>=1000:
        rank_text = "D"
    else:
        rank_text = ""
    rank_label.config(text=f"{rank_text}")
rank_label=tk.Label(root, text=f"{rank_text}", font=("Arial", 12))
rank_label.place(relx=0.90, rely=0.20, anchor="center")
#Buttons
#button Odd
Button_Odd = tk.Button(root, text="Impar", font=("Arial", 12), command=lambda: check("Odd"))
Button_Odd.place(relx=0.25, rely=0.60, anchor="center")
#Button Even
Button_Even = tk.Button(root, text="Par", font=("Arial", 12), command=lambda: check("Even"))
Button_Even.place(relx=0.75, rely=0.60, anchor="center")
root.mainloop()#Keep window open