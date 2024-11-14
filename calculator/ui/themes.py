# calculator/ui/themes.py
from dataclasses import dataclass
from typing import Literal

ThemeType = Literal["light", "dark"]

@dataclass
class ThemeColors:
    background: str
    foreground: str
    button_bg: str
    button_fg: str
    menu_bg: str
    menu_fg: str

class ThemeManager:
    """Manages application themes and colors."""
    
    THEMES = {
        "light": ThemeColors(
            background="#FFFFFF",
            foreground="#000000",
            button_bg="#DDDDDD",
            button_fg="#000000",
            menu_bg="#DDDDDD",
            menu_fg="#000000"
        ),
        "dark": ThemeColors(
            background="#2E2E2E",
            foreground="#FFFFFF",
            button_bg="#444444",
            button_fg="#FFFFFF",
            menu_bg="#444444",
            menu_fg="#FFFFFF"
        )
    }
    
    @classmethod
    def get_theme_colors(cls, theme: ThemeType) -> ThemeColors:
        """Returns color configuration for the specified theme."""
        return cls.THEMES[theme]
