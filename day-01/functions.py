
# Write a function with one `number` argument that returns double the argument
def double(number: int):
    return 2 * number

# Write a function with two `number` arguments that returns double the first argument
def double_first(number1: int, number2: int):
    return 2 * number1

# Write a function with two `number` arguments that returns double the largest argument
def big_double(number1: int, number2: int):
    if number1 > number2:
        return 2 * number1
    elif number2 > number1:
        return 2 * number2

# Write a function with a `string` argument and a `number` argument that repeates the string from the first argument but repeated the amount of times equal to the second argument. If the second number is negative, return an empty string
def repeat(text: str, number: int):
    return text *number 

# Write a function without any arguments. Have it return the string `'na'` repeated 10 times followed by the string `' batman!'`. Use the `repeat` function you used before to accomplish this
def batman():
    na = 'na'
    batman = ' batman!'
    return repeat(na, 10) + batman

# Write a function with two `number` arguments. Have it return the largest number of the two
def max(number1: int, number2: int):
    if number1 < number2:
        return number2
    elif number2 < number1:
        return number1

# Write a function with two `number` arguments. Have it return the smallest number of the two divided by the largest number
def max_divide(number1: int, number2: int):
    return min(number1, number2) / max(number1, number2)
            
# Write a function with two `string` arguments. Have it return the longest string
def max_string(string1: str, string2: str):
    if len(string1) >= len(string2):
        return string1
    elif len(string1) <= len(string2):
        return string2

# Write a function with a single `number` argument. Return a boolean that indicated wether this number is even
def even(number: int):
    return number % 2 == 0

# Write a function with a single `number` argument. Return a list of all the positive numbers lower than this argument that are even
def even_below(number: int):
    return [x for x in range(number) if x % 2 == 0]

# Write a function with a single `list of numbers` argument. Return a list of all the numbers in this list that are even
def even_in(numbers: list[int]):
    return [x for x in numbers if x % 2 == 0]

# Write a function with a single `list of numbers` argument. Return the result of multiplying all the numbers. If the input contains just 1 number, return that number
def multiply_list(numbers: list[int]):
    m = 1
    for x in numbers: 
        m = m * x
    return m
    
# Write a function with a single `list of numbers` argument. Return the result of dividing the number from left to right. So the first number gets divided by the second and the result of that gets divided by the third (and so on..). If the list contains a zero, return zero. If the list contains just one number, return that number
def divide_array(numbers: list[int]):
    if len(numbers) == 1:
        return numbers[0]
    elif 0 in numbers:
        return 0
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result /= numbers[i]
        return result 

# Write a functions that takes a list of numbers and an argument. Return the average of those numbers
def average(numbers: list[int]):
    return sum(numbers)/len(numbers)

# Write a function that takes a 'list of numbers' argument. Return the sum of that list multiplied by the length of the array.
def sum_product(numbers: list[int]):
    sum_numbers = sum(numbers)
    return sum_numbers * len(numbers)

# Write a function that capitalizes every other word in a string starting with the first one.
def uppercase_string(string1: str):
    words = string1.split()
    for i in range(0, len(words), 2):
        words[i] = words[i].upper()
    return ' '.join(words)

# Write a function that takes a single letter (may be upper or lower case). Return the number of this letter in the English Alphabet.
def alphabet(letter: str):
  letter = letter.lower()
  return ord(letter) - 96
    
# Write a function that takes 2 arguments a text and number of letter in the alphabet. Return the number of times the letter appears in the string (no matter upper or lower case).
def letter_count(text: str, letter_number: int):
    count = 0
    target_letter = chr(ord('a') + letter_number - 1)  # Convert the letter number to a character
    for char in text.lower():  # Convert all characters to lowercase for case-insensitive search
        if char == target_letter:
            count += 1
    return count
