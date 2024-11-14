# Calculator App

A simple calculator application built with Python and Tkinter, featuring both light and dark themes. This project demonstrates Python best practices including modular design, proper package structure, and clean code principles.

## Project Structure

The project follows a modular architecture:
```
calculator/
├── calculator/          # Main package directory
│   ├── core/           # Core business logic
│   │   └── calculator.py
│   ├── ui/            # User interface components
│   │   ├── calculator_ui.py
│   │   └── themes.py
│   └── __main__.py    # Entry point
└── tests/             # Test directory
```

## Features

- Modular, maintainable codebase
- Clear separation of concerns (UI, logic, themes)
- Basic arithmetic operations (+, -, *, /)
- Light and dark theme toggle
- Error handling for invalid calculations
- Keyboard support (Backspace to clear)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/skittally/calculator.git
cd calculator
```

2. Run the installation script:
```bash
python3 install.py
```

The script will automatically:
- Create a virtual environment
- Install required dependencies
- Set up the package in development mode
- Install tkinter if needed (on Linux systems)

3. Activate the virtual environment:
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Run the calculator:
```bash
python -m calculator
```

## Code Organization

- **core/calculator.py**: Contains the core calculation logic
- **ui/calculator_ui.py**: Manages the user interface components
- **ui/themes.py**: Handles theme management and styling
- **__main__.py**: Application entry point

## Best Practices Implemented

- **Modular Design**: Code is organized into logical modules with clear responsibilities
- **Separation of Concerns**: UI logic is separated from business logic
- **Clean Code**: Following PEP 8 style guide and proper documentation
- **Type Hints**: Using Python type hints for better code clarity
- **Error Handling**: Proper exception handling throughout the application
- **Configuration Management**: Centralized theme and style management
- **Package Structure**: Proper Python package structure with setuptools

## Development

To work on the calculator:

1. Follow the installation steps above
2. Make changes in the relevant modules:
   - UI changes: `calculator/ui/`
   - Core logic: `calculator/core/`
   - Theme modifications: `calculator/ui/themes.py`
3. Run the application to test changes: `python -m calculator`

## Why This Structure?

This project structure provides several benefits:
- **Maintainability**: Easy to locate and modify specific functionality
- **Testability**: Components can be tested in isolation
- **Extensibility**: New features can be added without modifying existing code
- **Reusability**: Components can be reused in other projects
- **Clarity**: Clear separation of concerns makes the code easier to understand

## Credits

Original project by [skittally](https://github.com/skittally)
Modular restructuring by [project contributor]
