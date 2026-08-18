# Python GUI Calculator

A fully functional calculator built from scratch in Python using the Tkinter library, featuring a custom graphical interface, keyboard support, and advanced mathematical operations.

---

## Description

Built as an independent Python project in December 2024 to develop practical skills in GUI programming, event-driven architecture, and modular code design. The calculator goes beyond basic arithmetic, implementing advanced functions like square root, inverse, percentage, nth root, and sign toggling — all while handling edge cases like division by zero and negative square roots gracefully.

---

## Features

- Custom GUI built with Tkinter — no external libraries required
- Full keyboard support (Enter key triggers calculation)
- Standard arithmetic operations — addition, subtraction, multiplication, division
- Advanced mathematical functions:
  - **x²** — squares the current value
  - **√x** — square root with negative number protection
  - **1/x** — inverse with division by zero protection
  - **%** — converts value to percentage
  - **ⁿ√** — nth root (two-step input)
  - **+/-** — toggles positive/negative sign
- Backspace button for correcting input
- Clear button to reset the display
- Division by zero and invalid input error handling
- Clean modular code structure with dedicated functions per operation

---

## How to Run

**Requirements:**
- Python 3.x
- Tkinter (included with most Python installations)

**Steps:**
1. Clone or download this repository
2. Open a terminal or command prompt
3. Navigate to the folder containing `calculator.py`
4. Run the script:

```bash
python calculator.py
```

---

## How to Use the nth Root Function (ⁿ√)

The nth root function is a two-step operation:
1. Enter the **root value** (e.g. `3` for a cube root)
2. Press **ⁿ√** — the display clears
3. Enter the **number** you want to find the root of
4. Press **ⁿ√** again to calculate

**Example:** To calculate the cube root of 27 — enter `3`, press `ⁿ√`, enter `27`, press `ⁿ√` → result is `3.0`

---

## Project Structure

```
python-calculator/
│
├── calculator.py    # Main script containing all logic and GUI
└── README.md        # Project documentation
```

---

## What I Learned

- Built a complete GUI application using Python's Tkinter library from scratch
- Applied event-driven programming concepts — binding keyboard inputs and button clicks to functions
- Debugged unexpected behavior when multiple buttons were pressed in sequence
- Implemented error handling for edge cases including division by zero, negative square roots, and invalid expressions
- Organized code into modular, reusable functions following clean code principles
- Developed persistence and independent problem-solving skills through designing, testing, and refining the project without external guidance
- Gained practical experience with Python's `math` module and `eval()` for expression parsing

---

## Example Output

```
┌─────────────────────────┐
│ Calculator              │
│ ┌─────────────────────┐ │
│ │            144.0    │ │
│ └─────────────────────┘ │
│  1/x   x²   √x   ÷     │
│   7     8    9   ×      │
│   4     5    6   -      │
│   1     2    3   +      │
│  +/-    0    .   =      │
└─────────────────────────┘
```

---

## Future Improvements

- Add memory functions (M+, M-, MR, MC)
- Implement calculation history so users can scroll through previous results
- Add a scientific mode with trigonometric functions (sin, cos, tan)
- Build a dark mode / light mode toggle
- Add parentheses support for more complex expressions

---

## Author

**Adedimeji Adebanjo**  
Computer Science — Texas A&M University  
[LinkedIn](https://linkedin.com/in/adedimeji-adebanjo) | [GitHub](https://github.com/Dimeji-A)
