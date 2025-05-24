# Python Coffee Machine Simulator ☕

A fun, interactive terminal-based coffee machine simulation written in Python. This project simulates a basic coffee vending machine that accepts virtual coins, tracks resources (like milk, water, coffee, sugar), and processes orders for espresso, latte, and cappuccino.

---

## 🎮 How It Works

- Users choose a drink: `espresso`, `latte`, or `cappuccino`.
- The machine asks for coin input (₹5, ₹10, ₹20).
- If enough coins are inserted, the machine:
  - Deducts ingredients from its resources.
  - Returns change if needed.
  - Serves the drink and updates stats.
- Users can continue ordering or exit the simulation.
- At the end, a full order summary and ingredient balance is displayed.

---

## ⚙️ Features

- Menu stored using a dictionary for clean resource and cost mapping.
- Dynamic resource management for milk, water, coffee, and sugar.
- Order tracking for each drink type.
- Simple payment system with ₹5, ₹10, ₹20 coins.
- Graceful handling of insufficient resources or funds.
- Terminal-friendly and easy to run anywhere.

---

## 🧠 What I Was Exploring

This project was built with a focus on **data structures and flow control**. I deliberately used a nested dictionary (`coffee_menu`) to represent drink data. This could have been modeled differently (e.g., list of tuples, classes), but I used this approach for learning and experimentation.

---

## 💡 Future Enhancements

- Add `report` or `refill` commands for operators.
- Handle incorrect input more robustly.
- Use classes to encapsulate machine logic.
- Add logging or file-based order history.

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Copy the code into a file called `coffee_machine.py`.
3. Run it using:

```bash
python coffee_machine.py
