from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            120,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,command=lambda: self.check("True"))
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.check("False"))
        self.false_button.grid(column=1, row=2)

        self.get_question_text()

        self.window.mainloop()

    def get_question_text(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check(self, answer: str):
        self.give_feedback(self.quiz.check_answer(answer))


    def give_feedback(self, is_right: bool):
        if is_right:
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question_text)

