import tkinter as tk
from turtle import color

calc = ""

def add_to_calc(item):
    global calc
    calc += str(item)
    results.delete(1.0, "end")
    results.insert(1.0, calc)

def evaluate_calc():
    global calc
    try:
        calc = str(eval(calc))
        results.delete(1.0, "end")
        results.insert(1.0, calc)
    except:
        clear_calc()
        results.insert(1.0, "Error")

def clear_calc():
    global calc
    calc = ""
    results.delete(1.0, "end")


root = tk.Tk()
root.geometry("265x290")
root.title("Calculator")
results = tk.Text(root, height=2, width=16, font=("Calibri", 24))
results.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), width=5, font=("Calibri 14"))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), width=5, font=("Calibri 14"))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), width=5, font=("Calibri 14"))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), width=5, font=("Cambria 14"))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), width=5, font=("Calibri 14"))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), width=5, font=("Calibri 14"))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), width=5, font=("Calibri 14"))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), width=5, font=("Calibri 14"))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), width=5, font=("Calibri 14"))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), width=5, font=("Calibri 14"))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=5, font=("Calibri 14"))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=5, font=("Calibri 14"))
btn_minus.grid(row=3, column=4)

btn_mult = tk.Button(root, text="*", command=lambda: add_to_calc("*"), width=5, font=("Calibri 14"))
btn_mult.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calc("/"), width=5, font=("Calibri 14"))
btn_div.grid(row=5, column=4)

btn_open_par = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=5, font=("Calibri 14"))
btn_open_par.grid(row=5, column=1)

btn_close_par = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=5, font=("Calibri 14"))
btn_close_par.grid(row=5, column=3)

btn_period = tk.Button(root, text=".", command=lambda: add_to_calc("."), width=5, font=("Calibri 14"))
btn_period.grid(row=6, column=3)

btn_perc = tk.Button(root, text="%", command=lambda: add_to_calc("%"), width=5, font=("Calibri 14"))
btn_perc.grid(row=6, column=2)

btn_clear = tk.Button(root, text="C", command=clear_calc, width=5, font=("Calibri 14"))
btn_clear.grid(row=6, column=1, columnspan=1)

btn_equal = tk.Button(root, text="=", bg="#766fad", command=evaluate_calc, width=5, font=("Calibri 14"))
btn_equal.grid(row=6, column=4, columnspan=1)

root.mainloop()
