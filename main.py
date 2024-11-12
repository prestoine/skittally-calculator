import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("calc")
        self.root.geometry("400x500")
        
        self.current_theme = "light"
        
        # Create the menu bar
        self.create_menu()

        # Create widgets (buttons, display, etc.)
        self.create_widgets()
        
        # Set initial theme
        self.update_theme()

    def create_menu(self):
        # make da menu bar
        menubar = tk.Menu(self.root)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        settings_menu.add_separator()
        settings_menu.add_command(label="Credits", command=self.show_credits)
        settings_menu.add_separator()
        settings_menu.add_command(label="Exit", command=self.root.quit)
        
        # settings menu :3
        menubar.add_cascade(label="Settings", menu=settings_menu)
        
        self.root.config(menu=menubar)
        self.menubar = menubar

    def create_widgets(self):
        # widget for showing calculations
        self.display = tk.Entry(self.root, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        
        # b u t t o n s
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        # b u t t o n s
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 20), height=2, width=4, 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        # make da grid properly expand
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)
        
        #  backspace key to clear the display
        self.root.bind("<BackSpace>", self.on_backspace)

    def on_button_click(self, char):
        current_text = self.display.get()
        
        if char == "=":
            try:
                result = str(eval(current_text))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

    def on_backspace(self, event):
        # clear da display when backspace 
        self.display.delete(0, tk.END)

    def toggle_theme(self):
        # toggle light and dark
        if self.current_theme == "light":
            self.current_theme = "dark"
        else:
            self.current_theme = "light"
        self.update_theme()

    def update_theme(self): # obvious
        if self.current_theme == "light":
            bg_color = "#FFFFFF"
            fg_color = "#000000"
            btn_bg = "#DDDDDD"
            btn_fg = "#000000"
            menu_bg = "#DDDDDD"
            menu_fg = "#000000"
            self.root.config(bg=bg_color)
        else:
            bg_color = "#2E2E2E"
            fg_color = "#FFFFFF"
            btn_bg = "#444444"
            btn_fg = "#FFFFFF"
            menu_bg = "#444444"
            menu_fg = "#FFFFFF"
            self.root.config(bg=bg_color)
        
        # change the display theme
        self.display.config(bg=bg_color, fg=fg_color)
        
        # change button colors
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=btn_bg, fg=btn_fg)
        
        self.menubar.config(bg=menu_bg, fg=menu_fg)

    def show_credits(self):
        messagebox.showinfo("", "Calculator App\nhttps://github.com/skittally")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

