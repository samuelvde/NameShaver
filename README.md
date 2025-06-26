# NameShaver

NameShaver is a desktop utility built with Python and tkinter that allows users to remove specified words from all filenames in a chosen folder.

## Features

- Select a folder via a GUI.
- Enter space-separated words to remove from filenames.
- Processes all files in the selected folder.
- Displays messages on success or errors.
- Easily extend logic to skip files based on custom rules.

## Installation

1. Clone the repository.
2. (Optional) Create a virtual environment.
3. Install dependencies (only needed for packaging):

    ```
    pip install -r requirements.txt
    ```

## Usage

Run the app:

```
python main.py
```

### Packaging as an executable

Install PyInstaller if not already installed:

```
pip install pyinstaller
```

Build the executable:

```
pyinstaller --onefile --windowed main.py
```

The executable will be in the `dist` folder.

## Notes

- The app only renames files, not folders.
- You can add custom skip logic in `renamer.py` as needed.
- Tested with Python 3.8+ (tkinter is included in standard Python distributions).
