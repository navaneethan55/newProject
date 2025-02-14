def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    # Loop through the list and separate even and odd numbers
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = separate_even_odd(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)
