# Student Progression Outcome Predictor

This is a Python program developed as part of the **4COSC006C: Software Development I** coursework for the academic year 2023/24 at the University of Westminster.

The program determines a student's academic progression outcome based on credit input values for **Pass**, **Defer**, and **Fail** modules.

---

## 📚 Coursework Overview

Students input their achieved credits in three categories:
- **Pass Credits**
- **Defer Credits**
- **Fail Credits**

The system then calculates the progression outcome using specified rules and displays results in various formats.

---

## 🚀 Features by Part

### ✅ Part 1: Basic Version
- Validates user input.
- Determines outcome:
  - Progress
  - Progress (module trailer)
  - Module retriever
  - Excluded
- Accepts multiple sets of data in one session.
- Displays a **horizontal histogram** of outcomes.
- Shows total outcomes count.

### ✅ Part 2: List Version
- Stores each set of results and input data in a **list**.
- Displays stored data with outcomes.

### ✅ Part 3: Dictionary Version
- Uses a **dictionary** instead of a list to store each outcome.
- Displays stored results with associated credit values.

### ✅ Part 4 (Optional): File Handling
- Saves all student outcomes to a text file (`progression_data.txt`).
- Reads from the file and displays results to the user.

---

## 🧠 Progression Rules

- Total credits must equal **120**.
- Acceptable input values: `0, 20, 40, 60, 80, 100, 120`.

| Pass | Defer | Fail | Outcome                   |
|------|-------|------|----------------------------|
| 120  | 0     | 0    | Progress                   |
| 100  | any   | any  | Progress – module trailer |
| 0–80 | any   | ≥80  | Excluded                   |
| else |       |      | Module retriever           |

---

## ⚙️ How to Run

Make sure you have Python installed. Then:

```bash
python w2053782.py
