from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
try:

    datao = pandas.read_csv('data/words_to_learn.csv')

    french_words = datao.to_dict(orient='records')

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

    french_words = data.to_dict(orient="records")
random_position ={}



# ------------------------------ Button Functionality----------------------------------------#

def random_word():
    global random_position,flip_timer
    window.after_cancel(flip_timer)
    random_position=random.choice(french_words)
    french_word=random_position["French"]
    canvas.itemconfig(canvas_title,text='French',fill='black')
    canvas.itemconfig(text_id,text=french_word,fill='black')
    canvas.itemconfig(canvas_image,image=fren_trans)
    flip_timer=window.after(3000,flip_card)

#------------------------------------- Flip Card --------------------------------------------#
def flip_card():

    canvas.itemconfig(canvas_title,text='English',fill='white')
    canvas.itemconfig(text_id,text=random_position['English'],fill='white')
    canvas.itemconfig(canvas_image,image=eng_trans)

def remove_card():
    global random_position
    french_words.remove(random_position)
    print(len(french_words))
    random_word()
    french_dict=pandas.DataFrame(french_words)
    french_dict.to_csv('data/words_to_learn.csv',index=False)




window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,highlightthickness=0)

flip_timer=window.after(3000,flip_card)

fren_trans=PhotoImage(file="images/card_front.png")
eng_trans = PhotoImage(file="images/card_back.png")

canvas =Canvas(width=800,height=526,highlightthickness=0,background=BACKGROUND_COLOR)
picture_imag= PhotoImage(file="images/card_front.png")
canvas_image=canvas.create_image(400,263,image=fren_trans)
canvas.grid(column=0,row=0,columnspan=2)

# Buttons
button_image= PhotoImage(file="images/wrong.png")
wrong_button = Button(image=button_image,highlightthickness=0,command=random_word)
wrong_button.grid(column=0,row=1)

button_image1= PhotoImage(file="images/right.png")
correct_button =Button(image=button_image1,highlightthickness=0,command=remove_card)
correct_button.grid(column=1,row=1)

# Text

canvas_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))

text_id=canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))



random_word()






















window.mainloop()