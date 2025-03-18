import os
import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

if os.path.exists("data/words_to_learn.csv") == False or os.path.getsize("data/words_to_learn.csv") == 0:
    french_words = pd.read_csv("data/french_words.csv")
else:
    french_words = pd.read_csv("data/words_to_learn.csv")

french_words_dict = french_words.to_dict(orient="records")
french_title = "French"
english_title = "English"
random_word = {

}


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(french_words_dict)
    random_word_fr = random_word.get(french_title)
    canvas.itemconfig(image_back, image=front_img)
    canvas.itemconfig(title_text, text=french_title, fill="black")
    canvas.itemconfig(word_text, text=random_word_fr, fill="black")
    flip_timer = window.after(3000, func=flash_card)


def remove_card():
    global random_word
    if len(random_word) > 0:
        french_words_dict.remove(random_word)
        df = pd.DataFrame(french_words_dict)
        df.to_csv("data/words_to_learn.csv", index=False)
        next_card()


def flash_card():
    global random_word
    random_word_en = random_word.get(english_title)
    canvas.itemconfig(image_back, image=back_img)
    canvas.itemconfig(title_text, text=english_title, fill="white")
    canvas.itemconfig(word_text, text=random_word_en, fill="white")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526)
image_back = canvas.create_image(400, 263)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 253, text="", font=("Ariel", 60, "bold"))

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, borderwidth=0, command=remove_card)
button_right.grid(column=1, row=1)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, borderwidth=0, command=next_card)
button_wrong.grid(column=0, row=1)

flip_timer = window.after(3000, func=flash_card)
next_card()

window.mainloop()
