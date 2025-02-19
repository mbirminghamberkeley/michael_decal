def computePower(x,y):
    '''returns x raised to the y power'''
    principal = x
    for i in range(y-1):
        principal = principal*x
    return principal

computePower(2,5)

def temperatureRange(readings):
    '''returns the min and max temperature from a list'''
    return(min(readings), max(readings))

temperatureRange([15,14,17,20,23,28])

def isWeekend(day):
    '''checks if the day (integer 1-7) is a weekend'''
    if day == 6 or 7:
        return True
    else:
        return False

isWeekend(6)

def fuel_efficiency(distance, fuel):
    '''returns fuel efficiency'''
    return distance/fuel

fuel_efficiency(70,21.5)

def decodeNumbers(n):
    '''move the last digit of a number to the front.'''
    non_leading, first_digit = n//10, n%10
    digits = 0
    while n > 0: # continuously floor divide to find the number of digits
        digits += 1
        n//=10
    return non_leading + first_digit*10**(digits-1)

decodeNumbers(123123798)

def find_max_with_for_loops(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum

find_max_with_for_loops([98, 2024, 131, 2, 3, 72])

def find_min_with_for_loops(nums):
    minimum = nums[0]
    for i in nums:
        if i < minimum:
            minimum = i
    return minimum

find_min_with_for_loops([98, 2024, 131, 2, 3, 72])
 
def find_max_with_while_loops(nums):
    maximum = nums[0]
    i = 0
    while i < len(nums):
        num = nums[i]
        if num > maximum:
            maximum = num
        i += 1
    return maximum

find_max_with_while_loops([98, 2024, 131, 2, 3, 72])

def find_min_with_while_loops(nums):
    minimum = nums[0]
    i = 0
    while i < len(nums):
        num = nums[i]
        if num < minimum:
            minimum = num
        i += 1
    return minimum

find_min_with_while_loops([98, 2024, 131, 2, 3, 72])

def vowel_and_consonant_count(text):
    vowels, consonants = 0, 0
    lowercase = text.lower()
    vowel_list = ["a","e","i","o","u"]
    for i in lowercase:
        if i.isalpha():
            if i in vowel_list:
                vowels += 1
            else:
                consonants += 1
    return(vowels,consonants)

vowel_and_consonant_count("UC Berkeley, founded in 1868!")

def digital_root(integer):
    sum = 0
    string = str(integer)
    for i in string:
        sum += int(i)
    return sum

digital_root(2468)

