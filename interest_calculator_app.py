import tkinter as tk

def calculate():
    try:
        P = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())
        if P < 0 or t < 0 or r < 0:
            raise ValueError
    except ValueError:
        result_var.set("Enter valid positive numbers")
        return


    A = P * (1 + r / 100) ** t
    CI = A - P
    result_var.set(f"Amount: {A:.2f}    Compound Interest: {CI:.2f}")

root = tk.Tk()
root.title("Compound Interest (annual)")

tk.Label(root, text="Principal:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=6, pady=6)

tk.Label(root, text="Time (years):").grid(row=1, column=0, sticky="e", padx=6, pady=6)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=6, pady=6)

tk.Label(root, text="Rate (% per year):").grid(row=2, column=0, sticky="e", padx=6, pady=6)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=6, pady=6)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=8)
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").grid(row=4, column=0, columnspan=2, pady=6)

root.mainloop()

import tkinter as tk

def calculate():
    try:
        P = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())
        if P < 0 or t < 0 or r < 0:
            raise ValueError
    except ValueError:
        result_var.set("Enter valid positive numbers")
        return

    
    A = P * (1 + r / 100) ** t
    CI = A - P
    result_var.set(f"Amount: {A:.2f}    Compound Interest: {CI:.2f}")

root = tk.Tk()
root.title("Compound Interest (annual)")

tk.Label(root, text="Principal:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=6, pady=6)

tk.Label(root, text="Time (years):").grid(row=1, column=0, sticky="e", padx=6, pady=6)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=6, pady=6)

tk.Label(root, text="Rate (% per year):").grid(row=2, column=0, sticky="e", padx=6, pady=6)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=6, pady=6)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=8)
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").grid(row=4, column=0, columnspan=2, pady=6)

root.mainloop()                                                                                                                                                                        