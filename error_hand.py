"""
Error Handling Demonstration Program
This program demonstrates proper exception handling for common error scenarios.
Each function shows both what would happen without error handling and the proper way to handle it.
"""


def safe_divide(a, b):
    """
    Safely divides two numbers with error handling for division by zero.
    
    WITHOUT TRY/EXCEPT: Would raise ZeroDivisionError when b is 0
    Example: 10 / 0 → ZeroDivisionError: division by zero
    
    Args:
        a: numerator (any numeric type)
        b: denominator (any numeric type)
    
    Returns:
        float: result of division if successful
        str: error message if division by zero occurs
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        # ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero
        return f"Error: Cannot divide {a} by zero"
    except TypeError as e:
        # TypeError: Raised when operation is applied to inappropriate type
        return f"Error: Invalid types for division - {e}"


def safe_int_input():
    """
    Safely gets integer input from user with error handling for non-numeric input.
    
    WITHOUT TRY/EXCEPT: Would raise ValueError when user enters non-numeric string
    Example: int("abc") → ValueError: invalid literal for int() with base 10: 'abc'
    
    Returns:
        int: the integer entered by user if valid
        None: if input is invalid (with error message printed)
    """
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        return number
    except ValueError:
        # ValueError: Raised when a function receives an argument of correct type but inappropriate value
        # In this case, int() can't convert non-numeric strings
        print(f"Error: '{user_input}' is not a valid integer")
        return None
    except KeyboardInterrupt:
        # KeyboardInterrupt: Raised when user interrupts program (Ctrl+C)
        print("\nInput cancelled by user")
        return None


def safe_file_read(filename):
    """
    Safely reads content from a file with error handling for missing files.
    
    WITHOUT TRY/EXCEPT: Would raise FileNotFoundError when file doesn't exist
    Example: open("missing.txt") → FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
    
    Args:
        filename: path to the file to read
    
    Returns:
        str: file contents if successful
        str: error message if file not found or other I/O error
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        # FileNotFoundError: Raised when a file or directory is requested but doesn't exist
        return f"Error: File '{filename}' not found"
    except PermissionError:
        # PermissionError: Raised when trying to access a file without adequate permissions
        return f"Error: Permission denied to read '{filename}'"
    except IOError as e:
        # IOError: Raised when an I/O operation fails (now usually OSError in Python 3)
        return f"Error: Could not read file '{filename}' - {e}"


def safe_dict_access(dictionary, key):
    """
    Safely accesses a dictionary key with error handling for missing keys.
    
    WITHOUT TRY/EXCEPT: Would raise KeyError when key doesn't exist
    Example: my_dict["missing_key"] → KeyError: 'missing_key'
    
    Args:
        dictionary: the dictionary to access
        key: the key to look up
    
    Returns:
        any: the value associated with the key if found
        str: error message if key not found
    """
    try:
        value = dictionary[key]
        return value
    except KeyError:
        # KeyError: Raised when a dictionary key is not found
        return f"Error: Key '{key}' not found in dictionary"
    except TypeError:
        # TypeError: Raised when trying to use unhashable type as key (like a list)
        return f"Error: Invalid key type - keys must be hashable"


def safe_list_access(lst, index):
    """
    Safely accesses a list element with error handling for invalid indices.
    
    WITHOUT TRY/EXCEPT: Would raise IndexError when index is out of range
    Example: my_list[100] → IndexError: list index out of range
    
    Args:
        lst: the list to access
        index: the index to access (integer)
    
    Returns:
        any: the value at the specified index if valid
        str: error message if index out of range
    """
    try:
        value = lst[index]
        return value
    except IndexError:
        # IndexError: Raised when trying to access a sequence with an index that's out of range
        return f"Error: Index {index} is out of range (list has {len(lst)} elements)"
    except TypeError:
        # TypeError: Raised when index is not an integer (or slice)
        return f"Error: List indices must be integers, not {type(index).__name__}"


def main():
    """
    Main function to test all error handling functions with both valid and invalid inputs.
    """
    print("=" * 70)
    print("ERROR HANDLING DEMONSTRATION PROGRAM")
    print("=" * 70)
    
    # Test 1: safe_divide()
    print("\n1. TESTING safe_divide()")
    print("-" * 70)
    print("Valid case: 10 / 2 =", safe_divide(10, 2))
    print("Error case: 10 / 0 =", safe_divide(10, 0))
    print("Error case: 'text' / 2 =", safe_divide("text", 2))
    
    # Test 2: safe_int_input() - simulated instead of actual input for automated testing
    print("\n2. TESTING safe_int_input()")
    print("-" * 70)
    print("Note: This function requires interactive input.")
    print("To test manually, uncomment the lines below:")
    print("# result = safe_int_input()  # Try entering: 42 (valid)")
    print("# print(f'You entered: {result}')")
    print("# result = safe_int_input()  # Try entering: abc (invalid)")
    print("# print(f'You entered: {result}')")
    
    # Simulating the behavior for demo purposes
    print("\nSimulated test:")
    try:
        valid_num = int("42")
        print(f"Valid input '42' → {valid_num}")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        invalid_num = int("abc")
        print(f"Invalid input 'abc' → {invalid_num}")
    except ValueError:
        print("Invalid input 'abc' → Error: 'abc' is not a valid integer")
    
    # Test 3: safe_file_read()
    print("\n3. TESTING safe_file_read()")
    print("-" * 70)
    
    # Create a test file first
    test_filename = "test_file.txt"
    try:
        with open(test_filename, 'w') as f:
            f.write("Hello! This is a test file.\nIt has multiple lines.\n")
        print(f"Created test file: {test_filename}")
    except:
        print("Could not create test file")
    
    print(f"\nValid case - reading '{test_filename}':")
    content = safe_file_read(test_filename)
    print(content)
    
    print("\nError case - reading 'nonexistent.txt':")
    print(safe_file_read("nonexistent.txt"))
    
    # Test 4: safe_dict_access()
    print("\n4. TESTING safe_dict_access()")
    print("-" * 70)
    test_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print(f"Test dictionary: {test_dict}")
    print(f"\nValid case - accessing 'name': {safe_dict_access(test_dict, 'name')}")
    print(f"Error case - accessing 'country': {safe_dict_access(test_dict, 'country')}")
    print(f"Error case - accessing with list key: {safe_dict_access(test_dict, ['invalid'])}")
    
    # Test 5: safe_list_access()
    print("\n5. TESTING safe_list_access()")
    print("-" * 70)
    test_list = [10, 20, 30, 40, 50]
    print(f"Test list: {test_list}")
    print(f"\nValid case - accessing index 2: {safe_list_access(test_list, 2)}")
    print(f"Error case - accessing index 10: {safe_list_access(test_list, 10)}")
    print(f"Error case - accessing index -10: {safe_list_access(test_list, -10)}")
    print(f"Error case - accessing with string index: {safe_list_access(test_list, 'invalid')}")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY OF ERROR TYPES DEMONSTRATED:")
    print("=" * 70)
    print("1. ZeroDivisionError - Division by zero")
    print("2. ValueError - Invalid value for type conversion")
    print("3. FileNotFoundError - File doesn't exist")
    print("4. KeyError - Dictionary key not found")
    print("5. IndexError - List index out of range")
    print("6. TypeError - Operation on incompatible types")
    print("7. PermissionError - Insufficient file permissions")
    print("=" * 70)


if __name__ == "__main__":
    main()