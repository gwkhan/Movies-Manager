# 🎬 Movie Manager CLI

A simple command-line based movie management tool built in Python.

## 💡 Features:
- 📥 Add new movies with title, genre, and rating
- 📃 View all saved movies
- 🔍 Search movies by genre
- 🌟 Show the top-rated movie
- 🕵️ Displays the last added movie at launch
- 📁 Automatically creates the CSV file if it doesn’t exist

## 🚀 Skills Used:
- File Handling (`open()`, read/write CSV)
- CSV Module
- Loops & Conditions
- Exception Handling (`try/except`)
- Basic String and List Operations
- User Input Handling

## 📂 Files:
- `movies.csv` – Stores all added movie data
- `Movies.py` – Contains the main CLI code

## 🛠️ How It Works:
1. On first run, it creates `movies.csv` with column headers.
2. On every run, it shows the last movie added (if any).
3. User is prompted with a menu:
   - `1` → Add a new movie (format: Title,Genre,Rating)
   - `2` → View all movies
   - `3` → Search movies by genre (case-insensitive match)
   - `4` → Find and display the highest-rated movie
   - `5` → Exit the program
