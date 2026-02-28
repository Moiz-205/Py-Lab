import tkinter as tk
from main import calculate


def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


def on_calculate():
    expression = entry.get()
    result = calculate(expression)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))


def on_clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
]

for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        btn = tk.Button(root, text=val, font="Arial 15", width=5, height=2,
                        command=lambda v=val: on_button_click(v))
        btn.grid(row=r + 1, column=c)

clear_btn = tk.Button(root, text="C", font="Arial 15", width=5, height=2, command=on_clear)
clear_btn.grid(row=5, column=0, columnspan=2, sticky="nsew")

eq_btn = tk.Button(root, text="=", font="Arial 15", width=5, height=2, command=on_calculate)
eq_btn.grid(row=5, column=2, columnspan=2, sticky="nsew")

root.mainloop()
