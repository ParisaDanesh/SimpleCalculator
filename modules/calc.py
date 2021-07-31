from tkinter import *
import math

class Calculator():

    def __init__(self, txtDisplay):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.operator = ""
        self.result = False
        self.txtDisplay = txtDisplay

    def display(self, value):
        self.txtDisplay.delete(0, END)
        self.txtDisplay.insert(0, value)

    def input_number(self, num):
        self.result = False
        first_num = self.txtDisplay.get()
        second_num = str(num)
        if self.input_value:
            self.current = second_num
            self.input_value = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(self.txtDisplay.get())

    def valid_function(self):
        if self.operator == "add":
            self.total += self.current
        if self.operator == "sub":
            self.total -= self.current
        if self.operator == "multi":
            self.total *= self.current
        if self.operator == "divide":
            self.total /= self.current

        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True

        self.check_sum = True
        self.operator = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def clear_all(self):
        self.clear_entry()
        self.total = 0

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(self.txtDisplay.get()))
        self.display(self.current)

    def math_pm(self):
        self.result = False
        self.current = -(float(self.txtDisplay.get()))
        self.display(self.current)