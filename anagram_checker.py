def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitivity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # If the sorted characters of both strings are the same, they're anagrams
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
