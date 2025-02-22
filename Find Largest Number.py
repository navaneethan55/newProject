def find_largest_number(nums):
    if not nums:  # check if the list is empty
        return None  # return None if the list is empty
    return max(nums)  # return the largest number using the built-in max() function

# Example usage:
numbers = [10, 3, 45, 7, 89, 22]
largest = find_largest_number(numbers)
print("The largest number is:", largest)
