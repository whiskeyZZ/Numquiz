from random import shuffle
import tkinter as tk
import json


class Numquiz:

    def __init__(self):
        with open("quest.json") as f:
            self.quest = json.load(f)

        shuffle(self.quest)

        self.i = 0
        self.question = ""
        self.answer = ""

        window = tk.Tk()
        window.geometry("700x500")
        window.configure(background="black")
        self.question_lbl = tk.Label(window, wraplength=400, font=("Arial", 22), fg="white", bg="black")
        self.question_lbl.pack(pady=20)

        self.entry = tk.Entry(window, font=("Helvetica", 36))
        self.entry.pack(pady=20)

        self.button = tk.Button(window, text="Antwort", bg="cornflower blue", fg="white",font=("Arial", 20) ,command=lambda: self.set_question(False))
        self.button.pack()

        self.set_question(True)

        window.mainloop()

    def set_question(self, first):
        if self.entry.get() == self.answer or first:
            if self.i < len(self.quest):
                self.question = self.quest[self.i]["question"]
                self.answer =  self.quest[self.i]["answer"]
                self.question_lbl.config(text=self.question)
                self.entry.delete(0, tk.END)
                self.i += 1
            else:
                self.question_lbl.config(text="Alles Richtig!")
                self.entry.delete(0, tk.END)


if __name__ == "__main__":
    Numquiz()