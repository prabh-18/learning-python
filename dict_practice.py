"""
Dictionary Practice - Demonstrating how to create, modify, and use dictionaries
"""

# -----------------------------------------------------------------------------
# 1. Create a dictionary for a student
#    Keys can be strings; values can be any type (str, int, list, etc.)
# -----------------------------------------------------------------------------
student = {
    "name": "Alice",
    "age": 16,
    "grade": 10,
    "subjects": ["Math", "Science", "English"]
}

# -----------------------------------------------------------------------------
# 2. Print the student's name
#    Access a value using the key in square brackets
# -----------------------------------------------------------------------------
print("Student's name:", student["name"])

# -----------------------------------------------------------------------------
# 3. Add a new key "school" with a value
#    Use assignment: dict[key] = value (creates the key if it doesn't exist)
# -----------------------------------------------------------------------------
student["school"] = "Central High"
print("Added school:", student["school"])

# -----------------------------------------------------------------------------
# 4. Update the grade
#    Same syntax as adding - if key exists, the value is overwritten
# -----------------------------------------------------------------------------
student["grade"] = 11
print("Updated grade:", student["grade"])

# -----------------------------------------------------------------------------
# 5. Loop through and print all key-value pairs
#    .items() gives us (key, value) pairs for each entry
# -----------------------------------------------------------------------------
print("\n--- All student info ---")
for key, value in student.items():
    print(f"  {key}: {value}")

# -----------------------------------------------------------------------------
# 6. Create a dictionary of 3 students (nested dictionaries)
#    Each value is another dictionary - dictionaries inside a dictionary
# -----------------------------------------------------------------------------
students = {
    "student_1": {
        "name": "Alice",
        "age": 16,
        "grade": 10,
        "subjects": ["Math", "Science"]
    },
    "student_2": {
        "name": "Bob",
        "age": 17,
        "grade": 11,
        "subjects": ["History", "Art"]
    },
    "student_3": {
        "name": "Charlie",
        "age": 15,
        "grade": 9,
        "subjects": ["Physics", "Music"]
    }
}

print("\n--- All 3 students ---")
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()
