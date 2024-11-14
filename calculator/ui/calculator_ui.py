# calculator/ui/calculator_ui.py
import tkinter as tk
from tkinter import font
from typing import List, Tuple

from ..core.calculator import Calculator
from .themes import ThemeManager

class CalculatorUI:
    """Calculator UI with outlined buttons."""
    
    BUTTON_LAYOUT: List[Tuple[str, int, int, str]] = [
        ('7', 1, 0, 'number'), ('8', 1, 1, 'number'), ('9', 1, 2, 'number'), ('/', 1, 3, 'operator'),
        ('4', 2, 0, 'number'), ('5', 2, 1, 'number'), ('6', 2, 2, 'number'), ('×', 2, 3, 'operator'),
        ('1', 3, 0, 'number'), ('2', 3, 1, 'number'), ('3', 3, 2, 'number'), ('-', 3, 3, 'operator'),
        ('0', 4, 0, 'number'), ('C', 4, 1, 'clear'), ('=', 4, 2, 'equals'), ('+', 4, 3, 'operator')
    ]

    def __init__(self, root: tk.Tk):
        self.root = root
        self.calculator = Calculator()
        
        # Create custom font
        self.digit_font = font.Font(family="Arial", size=16, weight="bold")
        self.display_font = font.Font(family="Arial", size=36, weight="normal")
        
        self._setup_window()
        self._create_display()
        self._create_buttons()
        self._configure_grid()
        self._setup_bindings()

    def _setup_window(self) -> None:
        """Configure the main window."""
        self.root.title("Calculator")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        
        colors = ThemeManager.get_theme_colors("dark")
        self.root.configure(bg=colors.background)
        
        # Main frame
        self.main_frame = tk.Frame(
            self.root,
            bg=colors.background,
            padx=5,
            pady=5
        )
        self.main_frame.pack(expand=True, fill='both')

    def _create_display(self) -> None:
        """Create the calculator display."""
        colors = ThemeManager.get_theme_colors("dark")
        
        self.display = tk.Label(
            self.main_frame,
            text="0",
            font=self.display_font,
            bg=colors.display_bg,
            fg=colors.display_fg,
            anchor="e",
            padx=20,
            pady=40
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

    def _create_buttons(self) -> None:
        """Create calculator buttons with outlines."""
        colors = ThemeManager.get_theme_colors("dark")
        
        for text, row, col, btn_type in self.BUTTON_LAYOUT:
            # Create frame for button with white border
            btn_frame = tk.Frame(
                self.main_frame,
                bg=colors.button_outline,  # White frame for border
                padx=1,  # Border thickness
                pady=1
            )
            btn_frame.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            
            # Button styling based on type
            if btn_type == 'number':
                bg_color = colors.button_number_bg
                fg_color = colors.button_number_fg
            elif btn_type == 'operator':
                bg_color = colors.button_operator_bg
                fg_color = colors.button_operator_fg
            elif btn_type == 'equals':
                bg_color = colors.button_equals_bg
                fg_color = colors.button_equals_fg
            else:  # clear
                bg_color = colors.button_clear_bg
                fg_color = colors.button_clear_fg
            
            button = tk.Button(
                btn_frame,
                text=text,
                font=self.digit_font,
                bg=bg_color,
                fg=fg_color,
                activebackground=bg_color,
                activeforeground=fg_color,
                relief="flat",
                borderwidth=0,
                command=lambda t=text: self._handle_button_click(t)
            )
            button.pack(expand=True, fill='both')

    def _configure_grid(self) -> None:
        """Configure grid weights."""
        # Display takes more space
        self.main_frame.grid_rowconfigure(0, weight=2)
        
        # Equal button rows
        for i in range(1, 5):
            self.main_frame.grid_rowconfigure(i, weight=1)
            
        # Equal columns
        for j in range(4):
            self.main_frame.grid_columnconfigure(j, weight=1)

    def _handle_button_click(self, char: str) -> None:
        """Handle calculator button clicks."""
        current_text = self.display.cget("text")
        
        if char == "=":
            result = self.calculator.evaluate(current_text)
            self.display.configure(text=result)
        elif char == "C":
            self.display.configure(text="0")
        elif char == "×":
            if current_text == "0":
                self.display.configure(text="*")
            else:
                self.display.configure(text=current_text + "*")
        else:
            if current_text == "0" and char not in "/*-+":
                self.display.configure(text=char)
            else:
                self.display.configure(text=current_text + char)

    def _setup_bindings(self) -> None:
        """Set up keyboard bindings."""
        self.root.bind("<BackSpace>", lambda e: self.display.configure(text="0"))
