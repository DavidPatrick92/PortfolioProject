#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Phone keypad mapping (excluding 0 and 1)
digit_to_letters = [
    [],      # 0 - not used
    [],      # 1 - not used
    ['A', 'B', 'C'],      # 2
    ['D', 'E', 'F'],      # 3
    ['G', 'H', 'I'],      # 4
    ['J', 'K', 'L'],      # 5
    ['M', 'N', 'O'],      # 6
    ['P', 'Q', 'R', 'S'], # 7
    ['T', 'U', 'V'],      # 8
    ['W', 'X', 'Y', 'Z']  # 9
]

# Ask the user for a valid 7-digit number
phone_number = input("Enter a 7-digit phone number (digits 2-9 only): ")

# Check for valid input
if len(phone_number) != 7 or not phone_number.isdigit():
    print("Invalid input. Please enter exactly 7 digits.")
elif '0' in phone_number or '1' in phone_number:
    print("Phone number should not contain 0 or 1.")
else:
    # Initialize list with an empty string to start combinations
    combinations = [""]

    # Loop through each digit in the phone number
    for digit_char in phone_number:
        digit = int(digit_char)
        letters = digit_to_letters[digit]

        # Build new combinations with the current digit's letters
        new_combinations = []

        for prefix in combinations:
            for letter in letters:
                new_word = prefix + letter
                new_combinations.append(new_word)

        # Update the combinations list
        combinations = new_combinations

    # Print all possible combinations
    print("Possible combinations:")
    for word in combinations:
        print(word)

    print("\nTotal combinations:", len(combinations))


# In[ ]:




