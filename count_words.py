def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create an empty dictionary to store word counts
    word_count = {}
    
    # Iterate through each word in the list of words
    for word in words:
        # Convert word to lowercase to make the count case-insensitive
        word = word.lower()
        
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        else:
            # Otherwise, add the word to the dictionary with count 1
            word_count[word] = 1
    
    # Return the dictionary with word counts
    return word_count

# Input sentence
sentence12 = input("Enter a sentence: ")

# Get word counts
word_counts = count_words(sentence12)

# Print the word counts
print("Word occurrences:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
