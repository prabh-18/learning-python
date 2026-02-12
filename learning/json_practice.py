import json
import os

def manage_profile():
    # 1. Create a dictionary with your profile
    profile = {
        "name": "Prabh",
        "age": 19,
        "hobbies": ["shiting", "reading", "Helping Humans"],
        "skills": ["Python", "Machine Learning", "Natural Language Processing"],
        "projects": [
            {"title": "Weather App", "status": "Completed"},
            {"title": "JSON Practice", "status": "In Progress"}
        ]
    }

    file_name = "profile.json"

    try:
        # 2. Convert to JSON and save to file
        # 'json.dump()' (no 's') writes data directly to a file stream.
        # 'indent=4' makes the file human-readable rather than one long line.
        with open(file_name, "w") as file:
            json.dump(profile, file, indent=4)
        print(f"Successfully saved profile to {file_name}")

        # 3. Read the JSON file back
        # 'json.load()' (no 's') reads data directly from a file object.
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                loaded_data = json.load(file)
            
            print("\n--- Loaded Profile Data ---")
            # Using 'json.dumps' (with 's') to convert the dict back to a string 
            # just for a pretty print in the console.
            print(json.dumps(loaded_data, indent=4))
        
    # 4. Error Handling
    except IOError as e:
        print(f"File Error: Could not write/read file. {e}")
    except json.JSONDecodeError:
        print("Error: Failed to decode the JSON data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    manage_profile()