import tkinter as tk

expression = ""

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

root = tk.Tk()
root.title("Calculator")

input_text = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_field = tk.Entry(input_frame, textvar=input_text, font=('arial', 16, 'bold'), bd=3, relief='ridge', justify='right')
input_field.pack(ipady=5, ipadx=5)

btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['C','exit']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn_text = buttons[i][j]
        if btn_text == "=":
            btn = tk.Button(btns_frame, text=btn_text, font=('arial', 14), height=2, width=4, command=calculate)
        elif btn_text == "C":
            btn = tk.Button(btns_frame, text=btn_text, font=('arial', 14), height=2, width=4, command=clear)
        elif btn_text == "exit":
            btn = tk.Button(btns_frame, text=btn_text, font=('arial', 14), height=2, width=4, command=root.destroy)
        else:
            btn = tk.Button(btns_frame, text=btn_text, font=('arial', 14), height=2, width=4, command=lambda x=btn_text: press(x))
        btn.grid(row=i, column=j, padx=1, pady=1)

root.mainloop()