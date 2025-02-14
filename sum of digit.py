# Function to calculate the sum of digits
def sum_of_digits(number):
    # Convert the number to a string to loop through its digits
    number_str = str(number)
    total = 0
    
    # Loop through each character in the string and add its integer value to total
    for digit in number_str:
        total += int(digit)
    
    return total

# Input from user
number = input("Enter a number: ")

# Call the function and display the result
print("The sum of the digits is:", sum_of_digits(number))
