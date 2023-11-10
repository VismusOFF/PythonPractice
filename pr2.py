import tkinter as tk
from tkinter import messagebox
from math import sin, cos, exp, fabs

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("pr2")

        self.x_entry = self.create_entry("Введите значение X", (0, 0))
        self.y_entry = self.create_entry("Введите значение Y", (1, 0))
        self.z_entry = self.create_entry("Введите значение Z", (2, 0))

        self.function_var = tk.StringVar(value="sin")
        self.create_radio_button("Sin(x)", "sin", (0, 1))
        self.create_radio_button("Cos(x)", "cos", (1, 1))
        self.create_radio_button("Exp(x)", "exp", (2, 1))

        self.result_box = tk.Listbox()
        self.result_box.grid(row=3, column=0, columnspan=2)

        self.create_button("Выполнить", self.calculate, (4, 0))
        self.create_button("Очистить", self.clear, (4, 1))

        self.window.mainloop()

    def create_entry(self, text, position):
        label = tk.Label(text=text)
        label.grid(row=position[0], column=position[1])
        entry = tk.Entry()
        entry.grid(row=position[0], column=position[1]+1)
        return entry

    def create_radio_button(self, text, value, position):
        radio_button = tk.Radiobutton(text=text, variable=self.function_var, value=value)
        radio_button.grid(row=position[0], column=position[1]+2)

    def create_button(self, text, command, position):
        button = tk.Button(text=text, command=command)
        button.grid(row=position[0], column=position[1])

    def calculate(self):
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            z = float(self.z_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Введены некорректные значения")
            return

        self.result_box.delete(0, 'end')
        self.result_box.insert('end', f"X={x}")
        self.result_box.insert('end', f"Y={y}")
        self.result_box.insert('end', f"Z={z}")

        try:
            u = self.calculate_u(x, y, z)
            self.result_box.insert('end', f"Результат U={round(u, 3)}")
        except Exception as e:
            self.result_box.insert('end', "Решение не найдено")

    def calculate_u(self, x, y, z):
        if self.function_var.get() == "sin":
            func = sin
        elif self.function_var.get() == "cos":
            func = cos
        elif self.function_var.get() == "exp":
            func = exp
        else:
            raise ValueError("Неверная функция")

        if x > fabs(z):
            return 2 * func(x)**3 + (3 * z**2)
        elif x == fabs(z):
            return (func(x) - z)**2
        else:
            return fabs(func(x) - z)

    def clear(self):
        self.x_entry.delete(0, 'end')
        self.y_entry.delete(0, 'end')
        self.z_entry.delete(0, 'end')
        self.result_box.delete(0, 'end')

if __name__ == "__main__":
    App()