# calculator/__main__.py
import tkinter as tk
from calculator.ui.calculator_ui import CalculatorUI

def main():
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

