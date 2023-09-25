# A Python program to calculate the sum of numbers in a list

def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

result = sum_of_numbers(numbers)
print(f"The sum of numbers is: {result}")
