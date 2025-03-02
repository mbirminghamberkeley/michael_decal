one_through_20 = [i for i in range(21)]
print(one_through_20)

def square_list(list):
    for i in range(len(list)):
        list[i] = list[i]**2
    return list

squared_list = square_list(one_through_20)
print(squared_list)

def first_fifteen(list):
    return list[0:15]

fifteen = first_fifteen(squared_list) 
print(fifteen)

def every_fifth(list):
    return list[4::5]

fifteen_fifth = every_fifth(squared_list)
print(fifteen_fifth)

def slice_and_reverse(list): 
    return list[::-3]

sliced_and_reversed = slice_and_reverse(squared_list)
print(sliced_and_reversed)

def create_2d_list():
    big_list = []
    for i in range(5):
        small_list = []
        for j in range(1,6):
            number = i*5 + j
            small_list.append(number)
        big_list.append(small_list)
    return big_list

matrix = create_2d_list()
print(matrix)

def replace_2d_list(list):
    new_list = []
    for i in list:
        small_list = []
        for j in i:
            if j % 3 == 0:
                small_list.append('?')
            else:
                small_list.append(j)
        new_list.append(small_list)
    return new_list

with_question = replace_2d_list(matrix)
print(with_question)

def summing_list(list):
    sum_list = []
    for i in list:
        for j in i:
            if j != '?':
                sum_list.append(j)
    return sum(sum_list)

total = summing_list(with_question)
print(total)