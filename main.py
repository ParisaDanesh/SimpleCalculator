from tkinter import *
from modules.calc import Calculator

root = Tk()
root.title("modules")
root.configure(background="gray22")
root.resizable(width=False, height=False)
root.geometry("480x520+0+0")

calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="gray55", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

new_value = Calculator(txtDisplay)

numberpad = "789456123"
i = 0
btn = []

for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=5, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: new_value.input_number(x)
        i += 1

clsBtn = Button(calc, text="C", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                command=lambda: new_value.clear_entry()).grid(row=1, column=0, pady=1)

clsAllBtn = Button(calc, text="CE", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                   command=lambda: new_value.clear_all()).grid(row=1, column=1, pady=1)

sqBtn = Button(calc, text="√", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
               command=lambda: new_value.squared()).grid(row=1, column=2, pady=1)

addBtn = Button(calc, text="+", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                command=lambda: new_value.operation("add")).grid(row=1, column=3, pady=1)

subBtn = Button(calc, text="-", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                command=lambda: new_value.operation("sub")).grid(row=2, column=3, pady=1)

multBtn = Button(calc, text="*", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                 command=lambda: new_value.operation("multi")).grid(row=3, column=3, pady=1)

divBtn = Button(calc, text="/", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                command=lambda: new_value.operation("divide")).grid(row=4, column=3, pady=1)

pmBtn = Button(calc, text=chr(177), width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
               command=lambda: new_value.math_pm()).grid(row=5, column=0, pady=1)

zeroBtn = Button(calc, text="0", width=5, height=2, font=('arial', 20, 'bold'), bd=4,
                 command=lambda: new_value.input_number(0)).grid(row=5, column=1, pady=1)

dotBtn = Button(calc, text=".", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                command=lambda: new_value.input_number(".")).grid(row=5, column=2, pady=1)

equalBtn = Button(calc, text="=", width=5, height=2, font=('arial', 20, 'bold'), bd=4, bg='gray55',
                  command=lambda: new_value.sum_of_total()).grid(row=5, column=3, pady=1)

root.mainloop()
