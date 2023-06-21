"""
This program has about 50 lines of sh!t. I can't even understand it anymore,
so I asked ChatGPT to re-write it.
It is uploaded only because a friend wants to have it quoted in his essay.
"""
from math import *
import matplotlib.pyplot as plt

def sequence(n, expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        print(f"Warning: Division by zero encountered at n={n}. Returning 0")
        return 0

def plot_sequence(a, delta_max, amount, start, stop, is_recursive, initial_value=None):
    if is_recursive and initial_value is not None:
        a[start] = float(initial_value)

    count = 0
    for n in range(start, stop+1):
        if n != start or not is_recursive:
            a[n] = float(sequence(n, exp))
            if n > start:
                delta = abs(a[n] - a[n-1])
                if delta < delta_max:
                    plt.plot(n, a[n], 'gs')
                    count += 1
                else:
                    plt.plot(n, a[n], 'rs')
                    count = 0
            plt.show()

            if count >= amount:
                print(f"a(n)={exp}")
                print(f"Done! a(n) is convergent in given range! a({n}) = {a[n]}")
                return True
    print("Done! a(n) is not convergent in given range")
    return False

if __name__ == "__main__":
    exp = str(input('Sequence a(n)= '))
    delta_max = float(eval(input('maximum Delta= ')))
    amount = int(eval(input('Amount= ')))
    start = int(eval(input('Start= ')))
    stop = int(eval(input('Stop= ')))
    is_recursive = bool(int(input('is a(n) recursive? (1 or 0): ')))

    a = [''] * (stop + 1)  # Initialize a

    if is_recursive:
        initial_value = eval(input(f'a[{start}]= '))
    else:
        initial_value = None

    plot_sequence(a, delta_max, amount, start, stop, is_recursive, initial_value)
