import tkinter as tk
import math

root = tk.Tk()
#keyboard bindings
root.bind("<Return>", lambda event: calculate_result())
root.bind("<KP_Enter>", lambda event: calculate_result())
root.title("Calculator")
root.geometry("500x500")

label = tk.Label(root, text="Calculator", font=("Open Sans", 24))
label.pack(pady=10)

display = tk.Entry(
    root,
    font=("Open Sans", 28),   # bigger font
    justify="right",
    bd=4,
    relief="sunken"
)
display.pack(fill="x", padx=10, pady=10)

# button container
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# configure grid so spacing exists
for r in range(6):
    button_frame.grid_rowconfigure(r, weight=1)
for c in range(4):
    button_frame.grid_columnconfigure(c, weight=1)

# common button style
btn_style = {
    "font": ("Open Sans", 18),  # slightly bigger font
    "width": 6,                 # wider buttons
    "height": 3,                # taller buttons
    "relief": "raised",
    "bd": 3
}

#insert value
def insert_value(value):
    display.insert(tk.END, value)

#clear values
def clear_display():
    display.delete(0, tk.END)

#backspace values
def backspace():
    current_text = display.get()
    if current_text:
        display.delete(len(current_text)-1, tk.END)

#calculate values
def calculate_result():
    try:
        expression = display.get()
        expression = expression.replace("×", "*").replace("÷", "/")
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

#square values
def square():
    try:
        value = float(display.get())
        result = value**2
        display.delete(0,tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0,tk.END)
        display.insert(tk.END, "Error")

#inverse values
def inverse():
    try:
        value = float(display.get())
        if value == 0:
            raise ZeroDivisionError
        result = 1 / value
        display.delete(0,tk.END)
        display.insert(tk.END,str(result))
    except:
        display.delete(0,tk.END)
        display.insert(tk.END, "Error")

#square root values
def square_root():
    try:
        value = float(display.get())
        if value < 0:
            raise ValueError
        result = math.sqrt(value)
        display.delete(0,tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0,tk.END)
        display.insert(tk.END, "Error")

#percent values
def percents():
    try:
        value = float(display.get())
        result = value / 100
        display.delete(0,tk.END)
        display.insert(tk.END,str(result))
    except:
        display.delete(0,tk.END)
        display.insert(tk.END, "Error")

#nth root values
nth_root_first = None
def nth_root():
    global nth_root_first
    try:
        if nth_root_first is None:
            nth_root_first = float(display.get())
            display.delete(0,tk.END)
        else:
            x = float(display.get())
            result = x **(1/nth_root_first)
            display.delete(0,tk.END)
            display.insert(tk.END,str(result))
            nth_root_first = None
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        nth_root_first = None

#toggle pos/neg sign
def toggle_sign():
    try:
        value = display.get().strip()
        if not value:
            return
        if any(op in value for op in "+-×÷"):
            return
        num = float(value)
        num = -num
        display.delete(0, tk.END)
        display.insert(tk.END, str(num))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error") 

def make_button(text, row, column, command=None):
    tk.Button(button_frame, text=text,command=command, **btn_style)\
        .grid(row=row, column=column, padx=6, pady=6, sticky="nsew")  # sticky makes button fill the grid cell

#numbers
numbers = [
    ("0", 5, 1),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2)
]
for num, row, col in numbers:
    make_button(num, row, col, lambda n=num: insert_value(n))

#operators
operators = [
    ("+", 4, 3),
    ("-", 3, 3),
    ("×", 2, 3),
    ("÷", 1, 3)
]
for op, row, col in operators:
    make_button(op, row, col, lambda o=op: insert_value(o))

# row 5
make_button("+/-", 5, 0, toggle_sign)
make_button(".",   5, 2, lambda: insert_value("."))
make_button("=",   5, 3, calculate_result)

# row 1
make_button("1/x", 1, 0, inverse)
make_button("x²",  1, 1, square)
make_button("√x",  1, 2, square_root)

# row 0
make_button("%",  0, 0, percents)
make_button("ⁿ√", 0, 1, nth_root)
make_button("C",  0, 2, lambda: clear_display())
make_button("⌫",  0, 3, backspace)

root.mainloop()
