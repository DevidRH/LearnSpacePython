import os
import re

# Replace with your folder path
folder_path = r"D:\Learn Space\Repository\LearnSpacePython\Udemy"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Match pattern like "CodingExercise4"
    match = re.match(r"^(CodingExercise)(\d+)(.*\.py)$", filename)
    if match:
        prefix, number, suffix = match.groups()
        new_filename = f"{prefix} {number}{suffix}"
        
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} ➡️ {new_filename}")