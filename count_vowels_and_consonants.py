def count_vowels_and_consonants(input_string):
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Initialize counters
    vowels_count = 0
    consonants_count = 0
    
    # Loop through each character in the string
    for char in input_string:
        # Check if the character is alphabetic
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    
    return vowels_count, consonants_count

# Example usage
input_string = "Hello World"
vowels, consonants = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")
