import tkinter as tk
window = tk.Tk()
window.columnconfigure(0, weight=1)
window.title("Calculator")
window.geometry("640x550")
window.configure(background="#2c3e50")
main_label = tk.Label(text="Mini-Calculator", width=20, bg="#2c3e50", font=("Arial", 40), fg="#ffffff")
label1 = tk.Label(text="Enter the first number", font=("Arial", 13), bg='#2c3e50', fg='#ffffff')
first_number = tk.Entry(font=("Arial", 15), bd=0, bg="#ecf0f1", justify='center')
action_label = tk.Label(text="Enter the action: x, /, +, -", font=("Arial", 13), bg='#2c3e50', fg='#ffffff')
action = tk.Entry(font=("Arial", 15), bd = 0, justify='center')
label2 = tk.Label(text="Enter the second number", font=("Arial", 13), bg='#2c3e50', fg='#ffffff')
second_number = tk.Entry(font=("Arial", 15), bd=0, justify='center')
main_label.grid(row=0, column=0, sticky='ew', pady=(10,30))
label1.grid(row=1, column=0, sticky="ew", padx=(30,30))
first_number.grid(row=2, column=0, sticky="ew", pady=15, padx=75, ipady=2.5)
action_label.grid(row=3, column=0, sticky="ew", padx=(10,10))
action.grid(row=4, column=0, sticky="ew", pady=15, padx=75, ipady=2.5)
label2.grid(row=5, column=0, sticky="ew", padx=(10,10))
second_number.grid(row=6, column=0, sticky="ew", padx=75, ipady=2.5)
def calculator():
    if not first_number.get().isdigit():
        label = tk.Label(text="You didn't enter the correct first number", width=35, bg="white", font=("Arial", 15))
        label.grid(pady=7.5)
    if  action.get() not in ['x', '/', '+', '-']:
        label = tk.Label(text="You didn't enter the correct action", width=32, bg="white", font=("Arial", 15))
        label.grid(pady=7.5)
    if not second_number.get().isdigit():
        label = tk.Label(text="You didn't enter the correct second number", width=38, bg="white", font=("Arial", 15))
        label.grid(pady=7.5)
        return
    if action.get() == "+":
        result1 = int(first_number.get()) + int(second_number.get())
        label = tk.Label(text = str(result1), width=20, bg="white", font=("Arial", 14))
        label.grid(row=8, column=0, sticky="ew", pady=7.5, padx=50)
    if action.get() == "-":
        result2 = int(first_number.get()) - int(second_number.get())
        label = tk.Label(text=str(result2), width=20, bg="white", font=("Arial", 14))
        label.grid(row=8, column=0, sticky="ew", pady=7.5, padx=50)
    if action.get() == "x":
        result3 = int(first_number.get()) * int(second_number.get())
        label = tk.Label(text=str(result3), width=20, bg="white", font=("Arial", 14))
        label.grid(row=8, column=0, sticky="ew", pady=7.5, padx=50)
    if action.get() == "/" and int(second_number.get()) == 0:
        label = tk.Label(text="Impossible division by zero", width=20, bg="white", font=("Arial", 14))
        label.grid(row=8, column=0, sticky="ew", pady=7.5, padx=50)
    elif action.get() == "/":
        result4 = int(first_number.get()) / int(second_number.get())
        label = tk.Label(text=str(result4), width=20, bg="white", font=("Arial", 14))
        label.grid(row=8, column=0, sticky="ew", pady=7.5, padx=50)
c_button = tk.Button(text="C", font=("Arial", 14))
c_button.grid(row=7, column=0, padx=(0,100))
btn = tk.Button(text="Calculate", command=calculator, width=10, font=("Arial", 15), bg='#3498db', bd=2.5, fg='#ffffff')
btn.grid(row=7, column=0, sticky='ew', padx=(100,100), pady=20)
first_number.focus()
first_number.bind("<Return>", lambda event: action.focus())
second_number.bind("<Return>", lambda event: first_number.focus())
action.bind("<Return>", lambda event: second_number.focus())
window.mainloop()