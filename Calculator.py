import math
from tkinter import *
#save numbers to a string, then just convert it to an int.
class Calculator:
    def __init__(self):
        self.opcode = ""
        self.firstIn = ""
        self.secondIn = ""
        self.total = 0.0
        self.window = Tk()
        self.entry = Entry(self.window, width=66, bg="white")
        self.entry.grid(row=0, column=0, columnspan=5)
        self.buttonFrame = Frame(self.window)
        self.buttonFrame.grid(row=3, column=3, columnspan=5)
        Button(self.buttonFrame, text = "7", height = 5, width = 10, command=lambda: self.getter("7")).grid(row = 1, column = 0)
        Button(self.buttonFrame, text = "8", height = 5, width = 10, command=lambda: self.getter("8")).grid(row = 1, column = 1)
        Button(self.buttonFrame, text = "9", height = 5, width = 10, command=lambda: self.getter("9")).grid(row = 1, column = 2)
        Button(self.buttonFrame, text = "+", height = 5, width = 10, command=lambda: self.getter("+")).grid(row = 1, column = 3)
        Button(self.buttonFrame, text = "4", height = 5, width = 10, command=lambda: self.getter("4")).grid(row = 2, column = 0)
        Button(self.buttonFrame, text = "5", height = 5, width = 10, command=lambda: self.getter("5")).grid(row = 2, column = 1)
        Button(self.buttonFrame, text = "6", height = 5, width = 10, command=lambda: self.getter("6")).grid(row = 2, column = 2)
        Button(self.buttonFrame, text = "-", height = 5, width = 10, command=lambda: self.getter("-")).grid(row = 2, column = 3)
        Button(self.buttonFrame, text = "1", height = 5, width = 10, command=lambda: self.getter("1")).grid(row = 3, column = 0)
        Button(self.buttonFrame, text = "2", height = 5, width = 10, command=lambda: self.getter("2")).grid(row = 3, column = 1)
        Button(self.buttonFrame, text = "3", height = 5, width = 10, command=lambda: self.getter("3")).grid(row = 3, column = 2)
        Button(self.buttonFrame, text = "x", height = 5, width = 10, command=lambda: self.getter("x")).grid(row = 3, column = 3)
        Button(self.buttonFrame, text = ".", height = 5, width = 10, command=lambda: self.getter(".")).grid(row = 4, column = 0)
        Button(self.buttonFrame, text = "0", height = 5, width = 10, command=lambda: self.getter("0")).grid(row = 4, column = 1)
        Button(self.buttonFrame, text = "=", height = 5, width = 10, command=lambda: self.getter("=")).grid(row = 4, column = 2)
        Button(self.buttonFrame, text = "/", height = 5, width = 10, command=lambda: self.getter("/")).grid(row = 4, column = 3)
        Button(self.buttonFrame, text = "sin", height = 5, width = 10, command=lambda: self.getter("sin")).grid(row = 3, column = 4)
        Button(self.buttonFrame, text = "cos", height = 5, width = 10, command=lambda: self.getter("cos")).grid(row = 2, column = 4)
        Button(self.buttonFrame, text = "tan", height = 5, width = 10, command=lambda: self.getter("tan")).grid(row = 1, column = 4)
        Button(self.buttonFrame, text = "CE", height = 5, width = 10, command=lambda: self.getter("CE")).grid(row = 4, column = 4)
        self.window.mainloop()

    def getter(self, button_id):
        if button_id == "CE":
            self.firstIn = ""
            self.secondIn = ""
            self.opcode = ""
            self.total = 0.0
            self.entry.delete(0,END)
        if button_id != "+" and button_id != "-" and button_id != "x" and button_id != "=" and button_id != "/" and self.opcode == "" and button_id != "CE" and button_id != "sin" and button_id != "cos" and button_id != "tan":
            self.firstIn += button_id
            self.entry.insert(len(self.firstIn), button_id)
        if (button_id == "+" or button_id == "-" or button_id == "x" or button_id == "/" or button_id == "sin" or button_id == "cos" or button_id == "tan") and button_id != "CE" and self.total == 0.0:
            self.opcode = button_id
            self.entry.insert(len(self.firstIn), button_id)
        if button_id != "+" and button_id != "-" and button_id != "x" and button_id != "=" and button_id != "/" and self.opcode != "" and button_id != "CE" and button_id != "sin" and button_id != "cos" and button_id != "tan":
            self.secondIn += button_id
            self.entry.insert(len(self.firstIn + self.opcode + self.secondIn), button_id)
        if self.total != 0 and (button_id == "+" or button_id == "-" or button_id == "x" or button_id == "/"):
            self.firstIn = str(self.total)
            self.opcode = button_id
            self.entry.insert(len(self.firstIn), button_id)
            self.secondIn = ""
        if button_id == "=":
            self.entry.delete(0,END)
            if self.opcode == "+":
                self.total = float(self.firstIn) + float(self.secondIn)
            elif self.opcode == "-":
                self.total = float(self.firstIn) - float(self.secondIn)
            elif self.opcode == "x":
                self.total = float(self.firstIn) * float(self.secondIn)
            elif self.opcode == "/":
                self.total = float(self.firstIn) / float(self.secondIn)
            elif self.opcode == "sin":
                self.total = math.sin(float(self.secondIn))
            elif self.opcode == "cos":
                self.total = math.cos(float(self.secondIn))
            elif self.opcode == "tan":
                self.total = math.tan(float(self.secondIn))
            self.entry.insert(0, self.total)

calc = Calculator()