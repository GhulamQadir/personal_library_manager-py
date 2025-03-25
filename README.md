# Personal Library Manager (CLI)

This is a simple command-line interface (CLI) application written in Python for managing a personal library. It allows you to add, view, and potentially modify or delete book entries.

## Features

- **Add Books:** Store book information (title, author, etc.) in a JSON file.
- **View Books:** Display the list of books in the library.
- **Error Handling:** Robust error handling for file operations and JSON parsing.
- **Empty File Handling:** Gracefully handles cases where the library file is empty.

## Prerequisites

- Python 3.x installed on your system.
- No external libraries are required (uses the built-in `json` module).

## Installation

1.  **Clone the repository (if applicable):**

    ```bash
    git clone https://github.com/GhulamQadir/personal_library_manager-py
    cd personal_library_manager-py
    ```

2.  **Or, simply create the python file:**

    Create a python file, and copy the python code into the file.

3.  **Create library file:**

    Create a file called `library.txt` in the same directory as the python file. This file will store the library data in JSON format. If you run the python code for the first time, and this file does not exist, the program will create it.

## Usage

- **Run the script:**

  ```bash
  python library_manager.py
  ```

## File Structure

- `library.txt`: Stores the library data in JSON format.
- `library_manager.py`: The Python script containing the library manager code.
- `README.md`: Documentation for the project.
