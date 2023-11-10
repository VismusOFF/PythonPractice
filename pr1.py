import tkinter as tk
from math import cos, pow
from cmath import sqrt

def calculate():
    x = float(x_entry.get())
    y = float(y_entry.get())
    z = float(z_entry.get())
    
    u = abs(x ** (y / x) - pow(y / x, 1/3)) + (y - x) * ((cos(y) - (z / (y - x))) / (1 + ((y - x) ** 3)))
    
    result_label.configure(text=f"Результат: {u.real:.4f}")

root = tk.Tk()
root.title("Вычисления")
root.geometry("400x250")

group_label = tk.Label(root, text="Группа ИСП21.1А")
group_label.pack()

student_label = tk.Label(root, text="Выполнил студент Жигач Д.Н.")
student_label.pack()

variant_label = tk.Label(root, text="Вариант №9")
variant_label.pack()

x_label = tk.Label(root, text="Введите x =")
x_label.pack()

x_entry = tk.Entry(root)
x_entry.pack()

y_label = tk.Label(root, text="Введите y =")
y_label.pack()

y_entry = tk.Entry(root)
y_entry.pack()

z_label = tk.Label(root, text="Введите z =")
z_label.pack()

z_entry = tk.Entry(root)
z_entry.pack()

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()