#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Dictionary to map numbers to words
number_words = {
    0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
    6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN",
    11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN", 14: "FOURTEEN", 15: "FIFTEEN",
    16: "SIXTEEN", 17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN",
    20: "TWENTY", 30: "THIRTY", 40: "FORTY", 50: "FIFTY",
    60: "SIXTY", 70: "SEVENTY", 80: "EIGHTY", 90: "NINETY"
}

# Function to convert a number less than 1000 into words
def number_to_words(n):
    if n == 0:
        return "ZERO"
    words = ""
    if n >= 100:
        hundreds = n // 100
        words += number_words[hundreds] + " HUNDRED"
        n = n % 100
        if n != 0:
            words += " "
    if n >= 20:
        tens = n // 10 * 10
        ones = n % 10
        words += number_words[tens]
        if ones != 0:
            words += " " + number_words[ones]
    elif n > 0:
        words += number_words[n]
    return words

# Ask the user to input a number
amount = input("Enter a cheque amount less than 1000 (e.g. 112.43): ")
# Split into dollar and cents
dollars, cents = amount.split(".")

# Convert to int
dollars = int(dollars)
cents = int(cents)

# Get the word version of the dollar amount
dollar_words = number_to_words(dollars)

# Format the output
final_output = f"{dollar_words} AND {cents:0>2}/100"
print(final_output)


# In[ ]:




