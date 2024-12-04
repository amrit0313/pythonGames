from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("monospace", 10, "bold")
class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg= THEME_COLOR)

        self.text_label = Label(text=f"score: {self.score}", fg="white", bg=THEME_COLOR)
        self.text_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, font=FONT, text="some question text", fill=THEME_COLOR)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.true_command)
        self.true_button.grid(row = 2, column = 0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.false_command)
        self.false_button.grid(row = 2, column = 1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.text_label.config(text=f"score: {self.score}/10")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text )
        else:
            self.canvas.itemconfig(self.question_text, text = f"Hey, have reached the end, your final score is {self.score}/10")
            self.canvas.config(bg="white")



    def true_command(self) ->None:
        self.give_feedback(self.quiz.check_answer("true"))


    def false_command(self):
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score+=1
            self.window.after(1000, self.next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.next_question)

