import os
from pathlib import Path

home_dir = Path.home()
current_working_dir = home_dir / "programming"

print("-" * 10)
print("Printing any files over 1MB")


def check_files(current):
    # current is a path
    for foldername, subfolders, filenames in os.walk(current):
        if current == None:
            print("No more")
            break
        print(f"Currently exploring {foldername}")
        os.chdir(current / foldername)
        path = Path.cwd()

        for filename in filenames:
            curr_path = path / filename
            size = os.path.getsize(curr_path)
            if size > 1000000:
                print(f"{os.path.abspath(filename)}, size: {size}")

        for subfolder in subfolders:
            print(f"subfolder: {subfolder}")
            if subfolder == "node_modules":
                continue  # ignore node modules
            check_files(path / subfolder)


check_files(current_working_dir)
print()
print("Done.")
