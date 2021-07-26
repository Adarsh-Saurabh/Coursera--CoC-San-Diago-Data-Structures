# Calculating fibanochi number
import numpy as np
import random

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fastfib(n):
    # a[i] = a[i-1] + a[i - 2]
    a = [0,1]
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
    return a[n]
if __name__ == '__main__':
    while True:
        n = int(random.randint(0,20))
        print(n)
        print(fib(n) , " " , fastfib(n))
        if fib(n) == fastfib(n):
            break