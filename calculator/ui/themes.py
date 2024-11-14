# calculator/ui/themes.py
from dataclasses import dataclass
from typing import Literal

ThemeType = Literal["dark"]

@dataclass
class ThemeColors:
    background: str
    display_bg: str
    display_fg: str
    button_number_bg: str
    button_number_fg: str
    button_operator_bg: str
    button_operator_fg: str
    button_clear_bg: str
    button_clear_fg: str
    button_equals_bg: str
    button_equals_fg: str
    button_outline: str

class ThemeManager:
    """Manages calculator theme."""
    
    THEMES = {
        "dark": ThemeColors(
            background="#1A1A1A",  # Dark background
            display_bg="#1A1A1A",  # Same as background
            display_fg="#FFFFFF",  # White text
            button_number_bg="#333333",  # Dark gray for numbers
            button_number_fg="#FFFFFF",  # White text
            button_operator_bg="#FF9F0A",  # Orange
            button_operator_fg="#FFFFFF",  # White text
            button_clear_bg="#666666",  # Gray for clear
            button_clear_fg="#FFFFFF",  # White text
            button_equals_bg="#FF9F0A",  # Orange for equals
            button_equals_fg="#FFFFFF",  # White text
            button_outline="#FFFFFF"  # White outline
        )
    }
    
    @classmethod
    def get_theme_colors(cls, theme: ThemeType) -> ThemeColors:
        """Returns color configuration for the specified theme."""
        return cls.THEMES[theme]
