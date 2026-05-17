# 💰 Tip Calculator

A simple Python project that calculates the total tip amount and divides the bill equally among a group of people.

The user enters the total bill amount, selects the tip percentage, and enters the number of people to split the bill. The program then calculates how much each person should pay.

---

## 🚀 Features

- Calculates tip based on percentage
- Splits the total bill equally among people
- Simple and beginner-friendly
- Fast and accurate calculations

---

## 🛠️ Technologies Used

- Python

---

## 📂 Project Structure

```bash
Tipcalculator/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ▶️ How It Works

The program asks the user for:

1. Total bill amount
2. Tip percentage
3. Number of people sharing the bill

It then calculates the final amount each person needs to pay.

---

## 💻 Example Output

```bash
Welcome to the Tip Calculator!

What was the total bill? ₹1000
How much tip would you like to give? 10, 12, or 15? 10
How many people to split the bill? 5

Each person should pay: ₹220.0
```

---

## 📜 Python Code

```python
print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount
each_person = total_bill / people

print(f"Each person should pay: ₹{round(each_person, 2)}")
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venkatasai-world/Tipcalculator.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Tipcalculator
```

### 3️⃣ Run the Program

```bash
python main.py
```

---

## 📌 Requirements

No external libraries are required.

Example `requirements.txt`

```txt
# No external dependencies
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

- Variables
- User Input
- Mathematical Operations
- Type Conversion
- String Formatting
- Python Basics

---

## 🌟 Future Improvements

- Create a web-based version
- Add a graphical user interface
- Support custom tip percentages
- Add currency conversion

---

## 🔗 GitHub Repository

:contentReference[oaicite:0]{index=0}

---

## 👨‍💻 Author

Created by Venkata Sai
