"""
================================================================================
PYTHON ERROR HANDLING TUTORIAL FOR BEGINNERS
================================================================================
Learn about try/except, exceptions, and how to write code that doesn't crash!
"""

import os
import tempfile

# =============================================================================
# 1. WHAT ARE EXCEPTIONS AND WHY PROGRAMS CRASH
# =============================================================================
#
# An EXCEPTION is Python's way of saying "something went wrong."
# When your code does something invalid (e.g., divide by zero, open a missing
# file), Python "raises" an exception. If you don't handle it, the program
# STOPS (crashes) and prints a traceback (the red error message).
#
# Why this matters: In real programs, you don't want one bad input or missing
# file to shut down the whole app. Error handling lets you catch problems and
# respond (e.g., show a friendly message, use a default value, log and retry).
#

# =============================================================================
# 2. HOW TRY/EXCEPT WORKS
# =============================================================================
#
#   try:
#       # Code that might cause an error
#       result = risky_operation()
#   except SomeError:
#       # What to do if that error happens
#       print("Something went wrong!")
#
# Python runs the try block. If an exception occurs, it jumps to the except
# block. If no exception occurs, the except block is skipped.
#

# =============================================================================
# 3. COMMON EXCEPTIONS
# =============================================================================
#
#   ValueError        - Wrong type or invalid value (e.g. int("hello"))
#   FileNotFoundError - File doesn't exist when you try to open it
#   ZeroDivisionError - Division by zero (e.g. 5 / 0)
#   KeyError          - Dictionary key doesn't exist (e.g. d["missing"])
#   TypeError         - Wrong type for an operation (e.g. "hi" + 3)
#   IndexError        - List index out of range (e.g. [1,2][10])
#

# =============================================================================
# 4. CATCH SPECIFIC vs CATCH ALL
# =============================================================================
#
# SPECIFIC (recommended when you know what can go wrong):
#   except ValueError:
#       ...
#   except FileNotFoundError:
#       ...
#
# CATCH ALL (use sparingly - can hide bugs):
#   except Exception:
#       ...
#
# You can catch multiple specific types in one except:
#   except (ValueError, TypeError):
#       ...
#

# =============================================================================
# 5. ELSE AND FINALLY
# =============================================================================
#
#   try:
#       do_something()
#   except SomeError:
#       handle_error()
#   else:
#       # Runs ONLY if no exception was raised (optional)
#       print("Success!")
#   finally:
#       # Runs ALWAYS - whether there was an error or not (cleanup, close files)
#       cleanup()
#

# =============================================================================
# 6. WHEN TO USE ERROR HANDLING vs PREVENT ERRORS
# =============================================================================
#
# USE TRY/EXCEPT when:
#   - You can't control the input (user input, files, network, external data)
#   - The "error" is an expected possibility (e.g. file might not exist)
#   - You want to recover and continue instead of crashing
#
# PREFER PREVENTING ERRORS when:
#   - You can check before acting: if key in dict, if len(list) > 0
#   - You can validate input and reject bad data early
#   - The situation is under your control (e.g. your own function's arguments)
#
# Rule of thumb: Validate what you control; catch what you don't.
#

print("\n" + "="*60)
print("EXAMPLE 1: ValueError (invalid conversion)")
print("="*60)

# --- BAD: Crashes if user enters non-numeric string ---
def get_age_bad():
    age = input("Enter your age: ")
    return int(age)  # CRASHES if user types "twenty" or ""

# --- GOOD: Catches ValueError and asks again or uses default ---
def get_age_good():
    try:
        age = input("Enter your age: ")
        return int(age)
    except ValueError:
        print("That's not a valid number. Using 0 as default.")
        return 0

# Uncomment to try (comment out after testing):
# print("Bad version would crash on invalid input.")
# print("Good version:", get_age_good())


print("\n" + "="*60)
print("EXAMPLE 2: ZeroDivisionError (divide by zero)")
print("="*60)

# --- BAD: Crashes when divisor is 0 ---
def average_bad(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count  # CRASHES if numbers is empty (0/0)

# --- GOOD: Handle empty list and avoid division by zero ---
def average_good(numbers):
    try:
        total = sum(numbers)
        count = len(numbers)
        return total / count
    except ZeroDivisionError:
        print("Cannot average an empty list.")
        return 0.0

print("Bad: average_bad([]) would crash.")
print("Good: average_good([]) =", average_good([]))
print("Good: average_good([10, 20, 30]) =", average_good([10, 20, 30]))


print("\n" + "="*60)
print("EXAMPLE 3: FileNotFoundError (missing file)")
print("="*60)

# --- BAD: Crashes if file doesn't exist ---
def read_config_bad(filename):
    with open(filename) as f:
        return f.read()

# --- GOOD: Catch FileNotFoundError and return default or inform user ---
def read_config_good(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Using default config.")
        return "default_value"

# Test with a file that doesn't exist
result = read_config_good("nonexistent_file_12345.txt")
print("Result when file missing:", result)


print("\n" + "="*60)
print("EXAMPLE 4: KeyError (missing dictionary key)")
print("="*60)

# --- BAD: Crashes if key doesn't exist ---
def get_capital_bad(countries, country):
    return countries[country]  # CRASHES if country not in dict

# --- GOOD: Catch KeyError or use .get() to avoid the exception ---
def get_capital_good(countries, country):
    try:
        return countries[country]
    except KeyError:
        print(f"Unknown country: {country}")
        return None

countries = {"USA": "Washington", "France": "Paris", "Japan": "Tokyo"}
print("Bad: get_capital_bad(countries, 'Mars') would crash.")
print("Good: get_capital_good(countries, 'USA') =", get_capital_good(countries, "USA"))
print("Good: get_capital_good(countries, 'Mars') =", get_capital_good(countries, "Mars"))


print("\n" + "="*60)
print("EXAMPLE 5: else and finally (success path + cleanup)")
print("="*60)

# --- BAD: No cleanup if something fails in the middle ---
def process_file_bad(path):
    f = open(path)
    data = f.read()
    result = int(data.strip())
    f.close()
    return result

# --- GOOD: finally ensures file is always closed; else runs on success ---
def process_file_good(path):
    f = None
    try:
        f = open(path)
        data = f.read()
        result = int(data.strip())
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("File content is not a valid number.")
        return None
    else:
        print("Successfully read and parsed the file.")
        return result
    finally:
        if f is not None:
            f.close()
            print("File closed.")

# Simulate: we don't have the file, so we'll just show the structure
print("Calling process_file_good('missing.txt'):")
process_file_good("missing.txt")

# Demo with a real temp file to show else + finally
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
    tmp.write("42")
    tmp_path = tmp.name
print("\nCalling process_file_good on a real file with '42':")
process_file_good(tmp_path)
os.remove(tmp_path)


print("\n" + "="*60)
print("QUICK REFERENCE: Catching multiple specific exceptions")
print("="*60)

def safe_divide(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, TypeError):
        print("Invalid input: need two numbers.")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

print("safe_divide(10, 2) =", safe_divide(10, 2))
print("safe_divide(10, 0) =", safe_divide(10, 0))
print("safe_divide('ten', 2) =", safe_divide("ten", 2))

print("\n--- End of tutorial ---\n")
