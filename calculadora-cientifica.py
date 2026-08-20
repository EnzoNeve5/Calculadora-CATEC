import math
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora científica')
        self.root.geometry('620x680')
        self.root.resizable(0, 0)

        self.total_expression = ''
        self.current_expression = ''
        self.angle_mode = 'DEG'

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {'/': '\u00F7', '*': '\u00D7', '-': '-', '+': '+'}

        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 7):
            self.buttons_frame.rowconfigure(x, weight=1)
        for x in range(1, 7):
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_scientific_buttons()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg='white', fg='black', padx=24, font=('Arial', 18))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg='white', fg='black', padx=24, font=('Arial', 24))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg='white')
        frame.pack(expand=True, fill='both')
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg='black', fg='white', font=('Arial', 24), borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        if self.current_expression == 'Error':
            self.clear()
        self.total_expression += self.current_expression + operator
        self.current_expression = ''
        self.update_display()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg='orange', fg='white', font=('Arial', 20), borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=6, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg='grey', fg='white', font=('Arial', 20), borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def toggle_angle_mode(self):
        self.angle_mode = 'RAD' if self.angle_mode == 'DEG' else 'DEG'
        self.angle_button.config(text=self.angle_mode)

    def scientific_namespace(self):
        def sin(value):
            return math.sin(math.radians(value)) if self.angle_mode == 'DEG' else math.sin(value)

        def cos(value):
            return math.cos(math.radians(value)) if self.angle_mode == 'DEG' else math.cos(value)

        def tan(value):
            return math.tan(math.radians(value)) if self.angle_mode == 'DEG' else math.tan(value)

        return {
            '__builtins__': {}, 'sin': sin, 'cos': cos, 'tan': tan,
            'asin': lambda value: math.degrees(math.asin(value)) if self.angle_mode == 'DEG' else math.asin(value),
            'acos': lambda value: math.degrees(math.acos(value)) if self.angle_mode == 'DEG' else math.acos(value),
            'atan': lambda value: math.degrees(math.atan(value)) if self.angle_mode == 'DEG' else math.atan(value),
            'sqrt': math.sqrt, 'log': math.log10, 'ln': math.log,
            'factorial': math.factorial, 'abs': abs, 'pi': math.pi, 'e': math.e
        }

    def evaluate_expression(self, expression):
        return eval(expression, self.scientific_namespace())

    def format_result(self, value):
        if isinstance(value, (int, float)) and abs(value) >= 10 ** 12:
            mantissa, exponent = format(value, '.10e').split('e')
            mantissa = mantissa.rstrip('0').rstrip('.')
            return f'{mantissa}e{int(exponent):+d}'
        return str(value)

    def apply_function(self, function):
        if not self.current_expression:
            return
        try:
            value = self.evaluate_expression(self.current_expression)
            self.current_expression = self.format_result(function(value))
        except (ValueError, TypeError, ZeroDivisionError, SyntaxError):
            self.current_expression = 'Error'
        self.update_label()

    def add_scientific_function(self, function):
        self.current_expression += function
        self.update_label()

    def create_scientific_buttons(self):
        buttons = [
            ('DEL', self.backspace, 0, 2),
            ('(', lambda: self.add_scientific_function('('), 0, 3),
            (')', lambda: self.add_scientific_function(')'), 0, 4),
            ('²x', lambda: self.apply_function(lambda value: value ** value), 0, 5),
            ('sen', lambda: self.add_scientific_function('sin('), 1, 5),
            ('cos', lambda: self.add_scientific_function('cos('), 2, 5),
            ('tan', lambda: self.add_scientific_function('tan('), 3, 5),
            ('x²', lambda: self.apply_function(lambda value: value ** 2), 4, 5),
            ('(-)', lambda: self.append_operator('-'), 5, 1),
            ('x⁻¹', lambda: self.apply_function(lambda value: 1 / value), 5, 2),
            ('x³', lambda: self.apply_function(lambda value: value ** 3), 5, 3),
            ('e', lambda: self.add_scientific_function('e'), 5, 4),
            ('√', lambda: self.add_scientific_function('sqrt('), 5, 5),
            ('log', lambda: self.add_scientific_function('log('), 5, 6),
            ('ln', lambda: self.add_scientific_function('ln('), 1, 4),
            ('xʸ', lambda: self.append_operator('**'), 2, 4),
            ('!', lambda: self.apply_function(math.factorial), 3, 4),
            ('π', lambda: self.add_scientific_function('pi'), 4, 4),
            ('=', self.evaluate, 4, 3),
        ]
        for text, command, row, column in buttons:
            tk.Button(self.buttons_frame, text=text, bg='#444444', fg='white', font=('Arial', 15), borderwidth=0, command=command).grid(row=row, column=column, sticky=tk.NSEW)
        self.angle_button = tk.Button(self.buttons_frame, text=self.angle_mode, bg='#004499', fg='white', font=('Arial', 15), borderwidth=0, command=self.toggle_angle_mode)
        self.angle_button.grid(row=4, column=6, sticky=tk.NSEW)

    def evaluate(self):
        expression = self.total_expression + self.current_expression
        try:
            self.current_expression = self.format_result(self.evaluate_expression(expression))
            self.total_expression = ''
        except (ValueError, TypeError, ZeroDivisionError, SyntaxError, NameError):
            self.current_expression = 'Error'
        self.update_display()

    def create_equals_button(self):
        pass

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill='both')
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def update_display(self):
        self.update_total_label()
        self.update_label()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    calc.run()