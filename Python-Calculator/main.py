from tkinter import *

op = ""
first_digit = ""
second_digit = ""

def clicked(digit):
    if digit == "←":
        # 끝에 있는 숫자 하나 삭제
        input_entry.delete(len(input_entry.get())-1)
    elif digit == "+" or digit == "-" or digit == "*" or digit == "/":
        global first_digit, op
        op = digit
        input_entry.delete(0, END)
        input_entry.insert(0, str(digit))
        if len(op) > 1:
            op = op[-1]
    else:
        if op :
            input_entry.delete(0, END)
            current = input_entry.get()
            input_entry.insert(0, current + str(digit))
        else:
            current = input_entry.get()
            input_entry.delete(0, END)
            input_entry.insert(0, current + str(digit))
            first_digit = input_entry.get()

# 클리어 버튼
def clear_digit():
    global first_digit, op, second_digit
    first_digit = ""
    op = ""
    second_digit = ""
    input_entry.delete(0, END)

# 계산 함수
def calculate():
    global first_digit, op, second_digit
    second_digit = input_entry.get()
    input_entry.delete(0, END)

    cal_result = first_digit + op + second_digit
    result = eval(cal_result)
    first_digit = str(result)
    input_entry.insert(0, result)

window = Tk()
window.title("파이썬 계산기")
window.geometry("350x500")
# window.resizable(False, False)
window.config(padx=10, pady=10)


# 입력 프레임
upper_frame = Frame(window, width=400, height=70)
upper_frame.pack(pady=40)

# 입력창
input_entry = Entry(upper_frame, width=20, font=("나눔바른펜", 18),justify=RIGHT, borderwidth=5)
# input_entry.grid(column=0, row=0, columnspan=4)
input_entry.pack()
input_entry.insert(0, "")
input_entry.focus()

# 버튼 프레임
down_frame = Frame(window, width=400, height=100)
down_frame.pack(padx=10, pady=10)

digits = [
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '←', '/']
]

# 버튼
for row in range(4):
    for col in range(4):
        digit = digits[row][col]
        button = Button(down_frame, text=digit, padx=15, pady=10, width=2, font=("나눔바른펜", 15),
                        command=lambda x=digit: clicked(x))
        button.grid(column=col, row=row, padx=5, pady=5)

# Clear 버튼
clear_button = Button(down_frame, text="C", width=10, font=("나눔바른펜", 15, "bold"), command=clear_digit, bg='orange')
clear_button.grid(column=0, row=4, columnspan=2)
#
# 계산 버튼
cal_button = Button(down_frame, text="=", width=10, font=("나눔바른펜", 15, "bold"), command=calculate, bg='orange')
cal_button.grid(column=2, row=4, columnspan=2)

# def return_key(event):
#     calculate()
# window.bind("<Return>", return_key)

window.mainloop()