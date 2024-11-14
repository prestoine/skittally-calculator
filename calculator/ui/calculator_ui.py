# calculator/ui/calculator_ui.py
import tkinter as tk
from tkinter import messagebox
from typing import Callable, List, Tuple

from ..core.calculator import Calculator
from .themes import ThemeManager, ThemeType

class CalculatorUI:
    """Main calculator UI class handling the graphical interface."""
    
    BUTTON_LAYOUT: List[Tuple[str, int, int]] = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]

    def __init__(self, root: tk.Tk):
        self.root = root
        self.calculator = Calculator()
        self.current_theme: ThemeType = "light"
        
        self._setup_window()
        self._create_menu()
        self._create_widgets()
        self._setup_bindings()
        self.update_theme()

    def _setup_window(self) -> None:
        """Configure the main window settings."""
        self.root.title("Calculator")
        self.root.geometry("400x500")

    def _create_menu(self) -> None:
        """Create and configure the application menu."""
        self.menubar = tk.Menu(self.root)
        
        settings_menu = tk.Menu(self.menubar, tearoff=0)
        settings_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        settings_menu.add_separator()
        settings_menu.add_command(label="Credits", command=self._show_credits)
        settings_menu.add_separator()
        settings_menu.add_command(label="Exit", command=self.root.quit)
        
        self.menubar.add_cascade(label="Settings", menu=settings_menu)
        self.root.config(menu=self.menubar)

    def _create_widgets(self) -> None:
        """Create and configure all UI widgets."""
        self._create_display()
        self._create_buttons()
        self._configure_grid()

    def _create_display(self) -> None:
        """Create the calculator display."""
        self.display = tk.Entry(
            self.root,
            font=("Arial", 24),
            bd=10,
            relief="sunken",
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4)

    def _create_buttons(self) -> None:
        """Create calculator buttons."""
        for text, row, col in self.BUTTON_LAYOUT:
            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 20),
                height=2,
                width=4,
                command=lambda t=text: self._handle_button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def _configure_grid(self) -> None:
        """Configure grid weights for proper widget scaling."""
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def _setup_bindings(self) -> None:
        """Set up keyboard bindings."""
        self.root.bind("<BackSpace>", self._handle_backspace)

    def _handle_button_click(self, char: str) -> None:
        """Handle calculator button clicks."""
        current_text = self.display.get()
        
        if char == "=":
            result = self.calculator.evaluate(current_text)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        elif char == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

    def _handle_backspace(self, event: tk.Event) -> None:
        """Handle backspace key press."""
        self.display.delete(0, tk.END)

    def toggle_theme(self) -> None:
        """Toggle between light and dark themes."""
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.update_theme()

    def update_theme(self) -> None:
        """Update UI elements with current theme colors."""
        colors = ThemeManager.get_theme_colors(self.current_theme)
        
        self.root.config(bg=colors.background)
        self.display.config(bg=colors.background, fg=colors.foreground)
        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=colors.button_bg, fg=colors.button_fg)
        
        self.menubar.config(bg=colors.menu_bg, fg=colors.menu_fg)

    def _show_credits(self) -> None:
        """Display credits information."""
        messagebox.showinfo("Credits", "Calculator App\nhttps://github.com/skittally")
