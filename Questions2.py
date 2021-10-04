import tkinter as tk
import sys
import json
from tkinter import ttk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.filename = tk.PhotoImage(file="C:\\Users\\nikol\\Desktop\\SoftUni\\image.png")
        self.button = tk.PhotoImage(file="C:\\Users\\nikol\\Desktop\\SoftUni\\button.png")
        self.menu = tk.PhotoImage(file="C:\\Users\\nikol\\Desktop\\SoftUni\\menu_image.png")
        self.background_label = tk.Label(image=self.filename)
        self.background_label.place(relwidth=1, relheight=1)
        self.frame_one = None
        self.create_widgets()
        self.br = 0
        self.correct = ""
        with open('data.txt') as json_file:
            self.basequestions = json.load(json_file)
        #self.basequestions = [{"When WW 2 has began?": {"A 1939": True, "B 1941": False, "C 1942": False, "D 1937": False}},
        #{"Which is the measurement indicator for inflation?": {"A GDP": False, "B CPI": True, "C IPI": False, "D BOP": False}}]
        self.questions = list(self.basequestions)

    def create_widgets(self):
        self.label = tk.Label(text="Menu", image=self.menu, compound="center", width=150, height=50)
        self.testButton = tk.Button(text="Start Test", image=self.button, compound="center", command=self.test, width=150, height=50)
        self.addButton = tk.Button(text="Add Question", image=self.button, compound="center", command=self.add, width=150, height=50)
        self.deleteButton = tk.Button(text="Delete Question", image=self.button, compound="center", command=self.DeleteQuestion, width=150, height=50)
        self.exitButton = tk.Button(text="Exit", image=self.button, compound="center", command=self.exit, width=150, height=50)

        self.label.pack(side="top", pady=20)
        self.testButton.pack(side="top", pady=10)
        self.addButton.pack(side="top", pady=10)
        self.deleteButton.pack(side="top", pady=10)
        self.exitButton.pack(side="top", pady=10)

        self.destroy_frame_one()


    def exit (self):
        sys.exit()

    def forget_widgets(self):
        self.label.pack_forget()
        self.testButton.pack_forget()
        self.addButton.pack_forget()
        self.deleteButton.pack_forget()
        self.exitButton.pack_forget()

    def forget_result(self):
        self.destroy_frame_one()
        self.questions = list(self.basequestions)
        self.br = 0
        self.create_widgets()

    def checkAll(self):
        self.questions.pop(0)
        self.destroy_frame_one()
        if self.questions:
            self.test()
        else:
            self.frame_one = tk.Frame(self.master)
            self.frame_one.pack()
            self.outputResult = tk.Label(self.frame_one, text="You finished the Test. Your result is " + str(
                round(self.br / len(self.basequestions) * 100)) + " %")
            self.outputResult.pack(side="top")
            self.outputHome = tk.Button(self.frame_one, text="Back to the Menu", command=self.forget_result)
            self.outputHome.pack(side="top")

    def checkA(self):
        if self.correct == "A":
            self.br += 1
        self.checkAll()

    def checkB(self):
        if self.correct == "B":
            self.br += 1
        self.checkAll()

    def checkC(self):
        if self.correct == "C":
            self.br += 1
        self.checkAll()

    def checkD(self):
        if self.correct == "D":
            self.br += 1
        self.checkAll()

    def test(self):
        self.forget_widgets()
        self.frame_one = tk.Frame(self.master)
        self.frame_one.pack()
        c = self.questions[0]
        for t in c.keys():
            self.outputQ = tk.Label(self.frame_one, text=str(t))
            self.outputQ.pack(side="top")
            for j in c.values():
                b = 0
                for k, l in j.items():
                    if b == 0:
                        if l:
                            self.correct = "A"
                        self.outputA = tk.Button(self.frame_one, text=str(k), command=self.checkA)
                        self.outputA.pack(side="top")
                        b += 1
                        continue
                    elif b == 1:
                        if l:
                            self.correct = "B"
                        self.outputB = tk.Button(self.frame_one, text=str(k), command=self.checkB)
                        self.outputB.pack(side="top")
                        b += 1
                        continue
                    elif b == 2:
                        if l:
                            self.correct = "C"
                        self.outputC = tk.Button(self.frame_one, text=str(k), command=self.checkC)
                        self.outputC.pack(side="top")
                        b += 1
                        continue
                    elif b == 3:
                        if l:
                            self.correct = "D"
                        self.outputD = tk.Button(self.frame_one, text=str(k), command=self.checkD)
                        self.outputD.pack(side="top")
                        b += 1

    def add(self):
        self.forget_widgets()
        self.frame_one = tk.Frame(self.master)
        self.frame_one.pack()
        self.NewQuestion = tk.Label(self.frame_one, text="Type the new question")
        self.NewQuestion.pack(side="top")
        self.NewQuestionType = tk.Entry(self.frame_one)
        self.NewQuestionType.pack(side="top")
        self.NewAnswerA= tk.Label(self.frame_one, text="Type the A answer")
        self.NewAnswerA.pack(side="top")
        self.NewAnswerAType = tk.Entry(self.frame_one)
        self.NewAnswerAType.pack(side="top")
        self.NewAnswerB = tk.Label(self.frame_one, text="Type the B answer")
        self.NewAnswerB.pack(side="top")
        self.NewAnswerBType = tk.Entry(self.frame_one)
        self.NewAnswerBType.pack(side="top")
        self.NewAnswerC = tk.Label(self.frame_one, text="Type the C answer")
        self.NewAnswerC.pack(side="top")
        self.NewAnswerCType = tk.Entry(self.frame_one)
        self.NewAnswerCType.pack(side="top")
        self.NewAnswerD = tk.Label(self.frame_one, text="Type the D answer")
        self.NewAnswerD.pack(side="top")
        self.NewAnswerDType = tk.Entry(self.frame_one)
        self.NewAnswerDType.pack(side="top")
        self.vlist = ["Answer A", "Answer B", "Answer C", "Answer D"]
        self.Combo = ttk.Combobox(self.frame_one, values=self.vlist)
        self.Combo.set("Pick the correct answer")
        self.Combo.pack(side="top", padx=5, pady=5)
        self.saveButton = tk.Button(self.frame_one, text="Save", command=self.save)
        self.saveButton.pack()
        self.backButton = tk.Button(self.frame_one, text="Back to the Menu", command=self.create_widgets)
        self.backButton.pack()

    def save(self):
        new_question = str(self.NewQuestionType.get())
        new_a = str(self.NewAnswerAType.get())
        new_b = str(self.NewAnswerBType.get())
        new_c = str(self.NewAnswerCType.get())
        new_d = str(self.NewAnswerDType.get())
        correct_answer = str(self.Combo.get())
        if correct_answer == self.vlist[0]:
            self.basequestions.append(
                {new_question: {"A " + new_a: True, "B " + new_b: False, "C " + new_c: False, "D " + new_d: False}})
        elif correct_answer == self.vlist[1]:
            self.basequestions.append(
                {new_question: {"A " + new_a: False, "B " + new_b: True, "C " + new_c: False, "D " + new_d: False}})
        elif correct_answer == self.vlist[2]:
            self.basequestions.append(
                {new_question: {"A " + new_a: False, "B " + new_b: False, "C " + new_c: True, "D " + new_d: False}})
        elif correct_answer == self.vlist[3]:
            self.basequestions.append(
                {new_question: {"A " + new_a: False, "B " + new_b: False, "C " + new_c: False, "D " + new_d: True}})
        self.questions = list(self.basequestions)
        with open('data.txt', 'w') as outfile:
            json.dump(self.basequestions, outfile)
        self.create_widgets()

    def DeleteQuestion(self):
        self.forget_widgets()
        if self.frame_one == None:
            self.frame_one = tk.Frame(self.master)
            self.frame_one.pack()
        self.varlist = []
        for l in range(len(self.basequestions)):
            self.varlist.append(tk.IntVar())
        b = 0
        for i in self.basequestions:
            for j in i.keys():
                self.ChkBttn = tk.Checkbutton(self.frame_one, text=str(j), variable=self.varlist[b])
                self.ChkBttn.pack(padx=5, pady=5)
                b += 1

        Button = tk.Button(self.frame_one, text="Delete", command=self.DelRetrieve)
        Button.pack(padx=5, pady=5)

        ButtonBack = tk.Button(self.frame_one, text="Back to the Menu", command=self.create_widgets)
        ButtonBack.pack(padx=5, pady=5)

    def DelRetrieve(self):
        br = 0
        for i in self.varlist:
            if i.get() == 1:
                self.basequestions.pop(br)
            br += 1
        self.questions = list(self.basequestions)
        with open('data.txt', 'w') as outfile:
            json.dump(self.basequestions, outfile)
        self.create_widgets()

    def destroy_frame_one(self):
        if self.frame_one:
            self.frame_one.destroy()
            self.frame_one = None

app = Application()
app.master.title("Exam")
app.master.geometry("500x500")
app.mainloop()