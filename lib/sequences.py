#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        init = [0, 1]
        for num in range(1, length-1):
            new_number = init[num-1] + init[num]
            init.append(new_number)
        print(init)