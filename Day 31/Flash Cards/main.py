from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
is_front = True

# ---------------------------- Check if there is a file ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- Next ------------------------------- #

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

# ---------------------------- Flip the card ------------------------------- #

def flip_card(event):
    global is_front
    if is_front:
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas.itemconfig(card_background, image=card_back_img)
        is_front = False
    else:
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        is_front = True


# ---------------------------- Remove ------------------------------- #

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas.bind("<Button-1>", flip_card)

# ---------------------------- Buttons ------------------------------- #

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
