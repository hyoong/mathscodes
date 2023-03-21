import numpy as np
import tkinter as tk
import re

class InputForm:
    def __init__(self, master):
        self.master = master
        self.var1_label = tk.Label(master, text="Enter the value for Q:")
        self.var1_entry = tk.Entry(master)
        self.var1_button = tk.Button(master, text="Next", command=self.show_var2_input)
        self.var2_label = tk.Label(master, text="Enter the value for P:")
        self.var2_entry = None
        self.result_label = tk.Label(master, text="")
        self.result_button = tk.Button(master, text="Calculate", command=self.check_input_expression)
        
        self.var1_label.pack()
        self.var1_entry.pack()
        self.var1_button.pack()
        
        self.result_label.pack() # add this line
    
    def show_var2_input(self):
        self.var1 = self.var1_entry.get()
        self.var1_label.pack_forget()
        self.var1_entry.pack_forget()
        self.var1_button.pack_forget()
        self.var2_label.pack()
        self.var2_entry = tk.Entry(self.master)
        self.var2_entry.pack()
        self.result_button.pack()
    
    def check_input_expression(self):
        allowed_expression = re.compile(r"(?P<coeff>\d*\.?\d+)?\|(?P<bra>[01])\>\<(?P<ket>[01])\|")

        label_to_array = {
            '|0><0|': np.array([[1, 0], [0, 0]]),
            '|0><1|': np.array([[0, 1], [0, 0]]),
            '|1><0|': np.array([[0, 0], [1, 0]]),
            '|1><1|': np.array([[0, 0], [0, 1]])
        }

        q = self.var1_entry.get()
        p = self.var2_entry.get()

        q_terms = re.findall(allowed_expression, q)
        p_terms = re.findall(allowed_expression, p)
        print(q_terms,p_terms)
        q_mat = np.zeros((2, 2), dtype=np.complex128)
        p_mat = np.zeros((2, 2), dtype=np.complex128)

        for term in q_terms:
            coeff = term[0] or 1
            bra = term[1]
            ket = term[2]

            label = f"|{bra}><{ket}|"
            if label not in label_to_array:
                label = f"|{ket}><{bra}|"

            q_mat += float(coeff) * label_to_array[label]

        for term in p_terms:
            coeff = term[0] or 1
            bra = term[1]
            ket = term[2]

            label = f"|{bra}><{ket}|"
            if label not in label_to_array:
                label = f"|{ket}><{bra}|"

            p_mat += float(coeff) * label_to_array[label]

        if q_mat is not None and p_mat is not None:
            trace_distance = np.trace(np.abs(q_mat - p_mat)) / 2
            self.result_label.config(text=f"Trace distance: {trace_distance}")
        else:
            self.result_label.config(text="Invalid input")

                        
root = tk.Tk()
my_form = InputForm(root)
root.mainloop()
