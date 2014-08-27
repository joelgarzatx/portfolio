# Homework Lab 3
# Joel Garza
# check_string.py
"""This program asks the user to input a string and verifies with tests whether the string is all upper case and ends with a period. Appropriate messages are returned based on input."""

uin = input ("Please enter an upper-case string ending with a period: ")
if not uin.isupper():
    print("Input is not all upper case.")
if not uin.endswith("."):
    print("Input does not end with a period.")
if uin.isupper() and uin.endswith("."):
    print("Input meets both requirements.")
