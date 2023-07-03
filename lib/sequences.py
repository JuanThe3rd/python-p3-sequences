#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []

    for num in range(length):
        if (num <= 1):
            fib_seq.append(num)
        else:
            fib_seq.append(fib_seq[num-2] + fib_seq[num-1])
    
    print(fib_seq)