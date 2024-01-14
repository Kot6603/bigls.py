import os
from pathlib import Path

home_dir = Path.home()
current_working_dir = home_dir / "programming"

print("-" * 10)
print("Printing any files over 1MB")


def read_ignore_patterns(file_path):
    with open(file_path, "r") as ignore_file:
        return [line.strip() for line in ignore_file]


def check_files(current, ignore_path=None):
    # current is a path

    ignore_patterns = []
    if ignore_path:
        ignore_patterns = read_ignore_patterns(ignore_path)

    for foldername, subfolders, filenames in os.walk(current):
        if any(pattern in foldername for pattern in ignore_patterns):
            return  # ignore any patterns in the ignore file if specified

        if current == None:
            print("No more")
            return
        # print(f"Currently exploring {foldername}")

        for filename in filenames:
            size = os.path.getsize(Path(foldername) / filename)
            if size > 1000000:
                print(f"{foldername + filename}, size: {size}")

        for subfolder in subfolders:
            # print(f"subfolder: {subfolder}")
            check_files(Path(foldername) / subfolder, ignore_path)


ignore_check_path = Path.cwd() / "ignore.txt"
if os.path.exists(ignore_check_path):
    print("exists")
    check_files(current_working_dir, ignore_check_path)
else:
    # check_files(current_working_dir)
    print("no")
print()
print("Done.")
