#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    if length == 0:
        print(fib_sequence)
        return
    fib_sequence.append(0)
    if length == 1:
        print(fib_sequence)
        return
    fib_sequence.append(1)
    if length == 2:
        print(fib_sequence)
        return
    for i in range(2, length):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    print(fib_sequence)