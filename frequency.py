# Test dictionary
test_dict = {'codingal': 3, 'is': 2, 'best': 2, 'coding': 1}

# Print the dictionary
print("Test dictionary:", test_dict)

# Ask user for the key to check frequency
key = input("Enter the word you want to check the frequency of: ")

# Print the frequency (number of occurrences)
if key in test_dict:
    print(f"The frequency of '{key}' is {test_dict[key]}")
else:
    print(f"'{key}' is not found")