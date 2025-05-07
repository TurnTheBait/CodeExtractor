# Code Extractor from Folder

This is a simple desktop application built in Python using the Tkinter GUI library.  
It allows users to select a folder and automatically generate a `.txt` file that contains the code or text content from all files found in that folder and its subfolders.

---

## ✨ Features

- Select a folder via graphical interface
- Recursively scan all subfolders
- Read the content of all readable (text-based) files
- Generate a single `.txt` file containing all contents, organized and separated
- Show popup messages for user guidance

---

## 📦 Libraries Used

### Frontend (GUI)
- `tkinter` – Python’s standard GUI library
  - `Tk`, `Label`, `Button`, `Frame` – for layout and design
  - `filedialog` – to select folders and specify output file path
  - `messagebox` – to show information messages

### Backend (Logic)
- `os.walk` – to recursively browse directories
- `os.path` – to handle file and path operations
- `open()` – to read and write text files

---

## 🖥️ How to Use

1. Run the script (`python filename.py`)
2. Click **"Select Folder"**
3. Choose the target folder containing code or text files
4. Choose where to save the output `.txt` file
5. The program will generate a consolidated `.txt` with all content

---

## 📁 Output Format

The output file will include:
- A header showing each file's name
- The full content of each file
- Separation between files
