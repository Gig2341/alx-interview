#!usr/bin/python3

'''In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n: int) -> int:
    '''returns the minimum no of operations'''
    if n <= 1:  # If 'n' is 1, it's impossible to achieve more 'H'
        return 0

    count = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            count += divisor
            n //= divisor
        divisor += 1

    return count
