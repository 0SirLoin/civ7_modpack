import os
from collections import defaultdict

def find_duplicate_files(start_path):
    file_dict = defaultdict(list)
    ignored_files = {"ModuleText.xml", "README.md", "ModInfoText.xml", "Changelog.txt"}

    for dirpath, dirnames, filenames in os.walk(start_path):
        # Ignore .git directory
        if ".git" in dirnames:
            dirnames.remove(".git")

        for filename in filenames:
            if filename not in ignored_files:
                file_dict[filename].append(dirpath)

    duplicates = {filename: paths for filename, paths in file_dict.items() if len(paths) > 1}

    return duplicates

if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))
    duplicates = find_duplicate_files(script_path)

    if duplicates:
        print("Duplicate files found:")
        for filename, paths in duplicates.items():
            print(f"File: {filename}")
            for path in paths:
                print(f" - {path}")
    else:
        print("No duplicate files found.")
