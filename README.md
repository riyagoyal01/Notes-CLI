# 📝 Notes-CLI

> A lightweight, offline-first command-line notes manager built with Python — no external dependencies required.

---

## 📌 About

**Notes-CLI** is a terminal-based note-taking application that lets you create, read, search, update, and delete text notes — all stored locally as `.txt` files. No internet connection, no database, no third-party libraries needed. Just Python and your filesystem.

Built as a hands-on project to practice **file I/O**, **modular function design**, and **CLI application architecture** in Python.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 📄 **Create Note** | Write a new note with a custom title and multi-line content |
| 👁️ **Read Note** | View the full contents of any saved note |
| 🔍 **Search Notes** | Find notes containing a specific keyword across all files |
| ➕ **Append to Note** | Add more content to an existing note without overwriting it |
| 🗑️ **Delete Note** | Remove any note permanently from local storage |
| 🕒 **Auto Timestamp** | Each note is automatically timestamped on creation |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

No third-party packages required. The project uses only Python's standard library (`os`, `datetime`).

### Installation

```bash
# Clone the repository
git clone https://github.com/riyagoyal01/Notes-CLI.git

# Navigate into the project directory
cd Notes-CLI

# Run the application
python main.py
```

---

## 🖥️ Usage

Once launched, you'll be presented with an interactive menu:

```
-----------------NOTE MANAGER------------------
1. Create Note
2. Read Note
3. Search Notes
4. Remove Note
5. Add more details
6. Exit
```

### Example Workflow

**Creating a note:**
```
Choose an option: 1
Enter note title: meeting-recap
Enter the content of the note (type END on a new line to finish):
Discussed Q2 roadmap and assigned tasks.
END
```

**Searching notes:**
```
Choose an option: 3
Enter the keyword to search in notes: roadmap
Keyword is in meeting-recap.txt
```

Notes are saved locally inside a `Notes/` directory that is automatically created on first run.

---

## 📁 Project Structure

```
Notes-CLI/
│
├── main.py           # Core application logic with all CLI functions
├── requirements.txt  # No external dependencies (stdlib only)
├── LICENSE           # MIT License
└── README.md         # Project documentation
```

### Key Functions

| Function | Responsibility |
|----------|---------------|
| `creating_notes()` | Creates a new `.txt` note with timestamped content |
| `reading_notes()` | Lists and displays an existing note |
| `searching_notes()` | Keyword search across all note files |
| `adding_notes()` | Appends content to an existing note |
| `removing_notes()` | Deletes a note file permanently |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `os` (file system operations), `datetime` (auto-timestamping)
- **Storage:** Local filesystem (plain `.txt` files)

---