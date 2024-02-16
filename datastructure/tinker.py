import tkinter as tk

memo = [0 if 1 ==0 else 1 if i == 1 else None for i in range(100)]

def fibo_memoization(number: int) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number-1) + fibo_memoization(number-2)
        memo[number] = result
    return result   
    
w = tk.Tk()
w.geometry("200x100")

lbl_display_fibonacci_result = tk.Label(w, text='Fibonacci by memoization')
en_input_number = tk.Entry(w)
btm_click = tk.Button(w, text = "Click")

lbl_display_fibonacci_result.pack()
en_input_number.pack(fill='x')
btm_click.pack(fill='x')

w.mainloop()