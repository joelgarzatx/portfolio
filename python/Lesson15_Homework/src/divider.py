""" Lesson 15 Project Homework -- Divider """

print("Dividing 10 by an integer")
while True:
    try:
        inp = int(input("Provide an integer: "))
        print(10/inp)
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")