import tkinter as tk

# Main window
root = tk.Tk()
root.title("Aesthetic GUI Calculator with History")
root.geometry("380x580")
root.configure(bg="#f0f0f0")  # Light background

# Entry display
entry = tk.Entry(root, width=20, font=("Helvetica", 24), bd=5, relief="flat", justify="right", bg="#d0efff", fg="#000")
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=(20, 10), ipady=10)

# Global variables
current_input = ""
history_list = []
last_was_equal = False  # Flag to detect if last action was '='

def update_entry(char):
    global current_input, last_was_equal
    if last_was_equal:
        current_input = ""
        entry.delete(0, tk.END)
        last_was_equal = False
    current_input += str(char)
    entry.delete(0, tk.END)
    entry.insert(0, current_input)

def clear_entry():
    global current_input
    current_input = ""
    entry.delete(0, tk.END)

def calculate():
    global current_input, history_list, last_was_equal
    try:
        result = str(eval(current_input))
        expression = current_input + " = " + result
        history_list.append(expression)
        if len(history_list) > 5:
            history_list.pop(0)
        update_history()
        entry.delete(0, tk.END)
        entry.insert(0, result)
        current_input = result
        last_was_equal = True
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot divide by 0")
        current_input = ""
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        current_input = ""

def update_history():
    history_box.delete(0, tk.END)
    for item in history_list:
        history_box.insert(tk.END, item)

# Create styled button
def create_button(text, row, col, colspan=1):
    def hover_in(e): e.widget.config(bg="#a0a0a0")
    def hover_out(e): e.widget.config(bg="#c0c0c0")
    action = (
        calculate if text == '=' else
        clear_entry if text == 'C' else
        lambda char=text: update_entry(char)
    )
    btn = tk.Button(root, text=text, width=8, height=2, font=("Helvetica", 14, "bold"),
                    bg="#c0c0c0", fg="#000", bd=0, command=action, activebackground="#a0a0a0")
    btn.grid(row=row, column=col, columnspan=colspan, padx=8, pady=8, sticky="nsew")
    btn.bind("<Enter>", hover_in)
    btn.bind("<Leave>", hover_out)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for b in buttons:
    if len(b) == 3:
        create_button(b[0], b[1], b[2])
    else:
        create_button(b[0], b[1], b[2], b[3])

# History Label
tk.Label(root, text="History (Last 5)", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333").grid(row=6, column=0, columnspan=4, pady=(10, 0))

# History display
history_box = tk.Listbox(root, height=5, width=40, font=("Courier", 12), bg="#ffffff", fg="#222", bd=2, relief="groove")
history_box.grid(row=7, column=0, columnspan=4, padx=15, pady=10)

# Expand buttons to fill grid space
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
