"""
This file contains simple examples of functions in Python.
Each function has comments to explain:
- parameters
- return values
- the difference between print() and return
"""


def greet(name):
    """
    Greet a person by name.

    Parameters:
        name: the person's name (a string).

    This function does NOT return a value. It only prints a message.
    """
    # Inside the function, we can use the parameter `name`
    # just like a normal variable.
    print(f"Hello, {name}! Welcome to the program.")


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length: the length of the rectangle (a number, e.g. int or float).
        width: the width of the rectangle (a number).

    Returns:
        The area, which is length * width.

    Note:
        We use `return` here instead of print(), because we want to send
        the result back to the caller so it can be used later.
    """
    area = length * width
    return area  # send the value back to the place where the function was called


def is_adult(age):
    """
    Check if a person is an adult.

    Parameters:
        age: the person's age (a number).

    Returns:
        True if age is 18 or older, otherwise False.
    """
    if age >= 18:
        return True
    else:
        return False


# ---------------------------------------------------------------------------
# Example usage of the functions above.
# You can run this file directly (python functions.py) to see what happens.
# ---------------------------------------------------------------------------

def main():
    """
    Demonstrate how to call the functions and use their results.
    """

    # 1. Calling greet() with different names
    # Here, "Alice" and "Bob" are *arguments* (actual values)
    # that get passed into the parameter `name` inside greet().
    greet("Alice")
    greet("Bob")

    print()  # print a blank line to separate the outputs

    # 2. Calling calculate_area() and printing the result
    # length and width are arguments; inside the function, they are
    # received as parameters with the same names.
    room_length = 5
    room_width = 3
    # calculate_area() returns a value, so we store it in a variable.
    area_of_room = calculate_area(room_length, room_width)
    print(f"The area of the room is: {area_of_room}")

    print()  # another blank line

    # 3. Using is_adult() in an if statement
    age_1 = 16
    age_2 = 21

    # is_adult() returns True or False. We can use that in an if.
    if is_adult(age_1):
        print(f"Age {age_1}: You are an adult.")
    else:
        print(f"Age {age_1}: You are NOT an adult.")

    if is_adult(age_2):
        print(f"Age {age_2}: You are an adult.")
    else:
        print(f"Age {age_2}: You are NOT an adult.")

    # -------------------------------------------------------------------
    # Extra explanation: print() vs return
    #
    # - print() shows something on the screen right now.
    #   After printing, the value is gone unless you stored it somewhere.
    #
    # - return sends a value back to the place where the function was called.
    #   You can:
    #       - store it in a variable (like area_of_room above)
    #       - use it in calculations
    #       - pass it to other functions
    #
    # A function can:
    #   - only print
    #   - only return
    #   - do both (print something and return a value)
    #
    # In this file:
    #   - greet() uses print() (no return)
    #   - calculate_area() uses return (no print inside the function)
    #   - is_adult() uses return (no print inside the function)
    # -------------------------------------------------------------------


if __name__ == "__main__":
    main()

