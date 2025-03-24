import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contains_primes(arr):
    rows_with_primes = []
    for row in arr:
        if any(is_prime(num) for num in row):
            rows_with_primes.append(row)
    return np.array(rows_with_primes)

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 131]])
print(contains_primes(arr))

def checkerboard():
    return np.zeros((8, 8), dtype=int)

print(checkerboard())       

def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    for i in np.arange(0,7,2):
            board[i, ::2] = 1  
    return board

print(checkerboard())

def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    for i in np.arange(0,8):
        if i % 2 == 0:
            board[i, ::2] = 1  
        else:
            board[i, 1::2] = 1
    return board

print(checkerboard())

def reverse_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    for i in np.arange(0,8):
        if i % 2 == 0:
            board[i, 1::2] = 1  
        else:
            board[i, ::2] = 1
    return board

print(reverse_checkerboard())

def expansion(strings, num_spaces):
    expanded_strings = []  
    for s in strings:
        expanded_string = (' ' * num_spaces).join(list(s))
        expanded_strings.append(expanded_string)
    return np.array(expanded_strings)

universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))
print(expansion(universe, 2))

import numpy as np

def second_dimmest_stars(arr):
    sorted_arr = np.sort(arr, axis=0)
    second_dimmest = sorted_arr[1, :]
    return second_dimmest

arr = np.array([[1123, 1456, 1789, 1324, 1876],
                [1567, 1987, 1678, 1405, 1589],
                [1345, 1654, 1523, 1109, 1923],
                [1298, 1890, 1367, 1784, 1432],
                [1823, 1756, 1489, 1672, 1550]])

print(second_dimmest_stars(arr))