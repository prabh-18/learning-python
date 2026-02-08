
# --- 1. Create "notes.txt" and write 3 lines ---
with open("notes.txt", "w") as f:
    f.write("First line of notes.\n")
    f.write("Second line of notes.\n")
    f.write("Third line of notes.\n")

# --- 2 & 3. Read and print the content ---
print("Content after writing 3 lines:")
print("-" * 30)
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
print("-" * 30)

# --- 4. Append 2 more lines ---
with open("notes.txt", "a") as f:
    f.write("Fourth line (appended).\n")
    f.write("Fifth line (appended).\n")

# --- 5. Read and print the updated content ---
print("Content after appending 2 more lines:")
print("-" * 30)
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
print("-" * 30)
print("Done. File 'notes.txt' is saved on disk.")
