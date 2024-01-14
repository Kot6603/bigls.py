## bigls.py

A small project to get comfortable with using os and pathlib libraries in python.

#### Usage
- fork and clone this repository
- if there are any folders you want to ignore, put it on a new line inside `ignore.txt`
  - anything inside `ignore.txt` will be ignored (useful for things like node_modules, .git, .next)
- in the command line, cd into the repo and run `python bigls.py`
- all files that are greater than the filesize threshold (currently set to 1000000B or 1MB) will be outputted onto the terminal

#### Future Improvements:
- a way for the user to input a specific filesize they want to look for (vary the filesize threshold)
- a way for the user to specify which directory they want to search
- a way to filter out or only search for certain filetypes
- a way to incorporate ignoring files and folders in .gitignore
