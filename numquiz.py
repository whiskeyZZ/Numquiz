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
        self.welcome_txt = "Willkommen zum Zahlenquiz! Mach dich bereit, einige Rätsel zu lösen! Die gesuchte Antwort ist immer eine Dezimalzahl. Für manche Fragen wirst du das Internet brauchen und ab und zu musst du aus anderen Zahlensystemen umrechnen. Hast du das Zeug zum Meister der Zahlen?"
                 
        window = tk.Tk()     
        window.geometry("700x500")
        window.configure(background="black")

        self.start_lbl = tk.Label(window, text=self.welcome_txt ,wraplength=400, font=("Arial", 18), fg="white", bg="black")
        self.start_btn = tk.Button(window, text="Start", bg="cornflower blue", fg="white",font=("Arial", 20) ,command=lambda: self.start())
        self.start_lbl.pack(pady=20)
        self.start_btn.pack()

        self.question_lbl = tk.Label(window, wraplength=400, font=("Arial", 18), fg="white", bg="black", height=5, anchor="center")
        self.entry = tk.Entry(window, font=("Helvetica", 36, "italic"))
        self.button = tk.Button(window, text="Antwort", bg="cornflower blue", fg="white",font=("Arial", 20) ,command=lambda: self.set_question(False))
        self.info_lbl = tk.Label(window, font=("Arial", 22), fg="white", bg="black")

        window.mainloop()

    def set_question(self, first):
        if self.entry.get() == self.answer or first:
            if self.i < len(self.quest):
                self.question = self.quest[self.i]["question"]
                self.answer =  self.quest[self.i]["answer"]
                self.question_lbl.config(text=self.question)
                self.info_lbl.config(text="")
                self.entry.delete(0, tk.END)
                self.i += 1
            else:
                self.question_lbl.config(text="Alles Richtig! Du bist ein Zahlenmagier!")
                self.entry.delete(0, tk.END)
        elif self.i < len(self.quest):
            self.info_lbl.config(text="Falsche Antwort")

    def start(self):
        self.start_lbl.destroy()
        self.start_btn.destroy()
        self.question_lbl.pack(fill=tk.BOTH, expand=True)
        self.entry.pack(pady=20)
        self.button.pack()
        self.info_lbl.pack(pady=20)
        self.set_question(True)


if __name__ == "__main__":
    Numquiz()