# 2-4. Name Cases Assignment

## Assignment Instructions
Store a person's name in a variable and display it in lowercase, uppercase, and title case using Python's string methods.

## Python Program Code

```python
# Variable representing a person's name in different cases
name = "arthur"

# Display the name in different cases
print("Original variable:", name)
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())
print("Title case:", name.title())
```

## Program Output
```
Original variable: arthur
Lowercase: arthur
Uppercase: ARTHUR
Title case: Arthur
```

## Code Screenshot
![Name_case](Name_case.png)

## Description

This Python program demonstrates string case manipulation methods in Python:

1. **Original variable**: Displays the name as stored in the variable ("arthur").
2. **Lowercase (.lower())**: Converts all characters to lowercase.
3. **Uppercase (.upper())**: Converts all characters to uppercase.
4. **Title case (.title())**: Capitalizes the first letter of each word for proper formatting of names.

These string methods are non-destructive, meaning they return a new string without modifying the original variable.

## GitHub Repository
File uploaded to: https://github.com/arthurcathey/CSC-121/blob/main/name_cases.py
