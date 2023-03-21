import numpy as np
import tkinter as tk
import re

allowed_expression = re.compile(r"^\|[01]+\>\<[01]+\|$")


label_to_array = {
    '|0><0|': np.array([[1, 0], [0, 0]]),
    '|0><1|': np.array([[0, 1], [0, 0]]),
    '|1><0|': np.array([[0, 0], [1, 0]]),
    '|1><1|': np.array([[0, 0], [0, 1]])
}

q_arr = None
p_arr = None

def check_input_expression():
    q = qinput.get()
    p = pinput.get()
    if allowed_expression.match(q) or allowed_expression.match(p):
        q_arr = label_to_array.get(q, None)
        p_arr = label_to_array.get(p, None)
            
        if q_arr is not None and p_arr is not None:
            calculate_trace_distance(q_arr, p_arr)
        else:
            output.configure(text="Invalid input")
    else:
        output.configure(text="Invalid input")

        
def calculate_trace_distance(q_arr,p_arr):
    trace_distance = np.trace(np.matmul((q_arr-p_arr).conj().T,(q_arr-p_arr)))/2
    output.configure(text="Trace distance: {}".format(trace_distance))

    
    
root=tk.Tk()

qlabel = tk.Label(root,text="Please enter the density matrix for Q:")
qlabel.pack()
qinput=tk.Entry(root)
qinput.pack()

qsubmit=tk.Button(root, text="Enter",command=check_input_expression)
qsubmit.pack()

plabel = tk.Label(root,text="Please enter the density matrix for P:")
plabel.pack()
pinput=tk.Entry(root)
pinput.pack()

psubmit=tk.Button(root, text="Enter",command=check_input_expression)
psubmit.pack()

output=tk.Label(root,text="")
output.pack()
root.mainloop()
