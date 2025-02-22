def second_largest(numbers):
    # Check if the list has enough elements to have a second largest
    if len(numbers) < 2:
        return None  # Return None if there is no second largest element

    # Initialize two variables to track the largest and second largest
    first, second = float('-inf'), float('-inf')

    for num in numbers:
        if num > first:
            second = first  # Update second largest
            first = num      # Update largest
        elif num > second and num != first:
            second = num     # Update second largest

    return second if second != float('-inf') else None


# Taking input from the user
input_str = input("Enter numbers separated by space: ")
numbers = list(map(int, input_str.split()))

result = second_largest(numbers)
if result is None:
    print("There is no second largest number.")
else:
    print("The second largest number is:", result)
