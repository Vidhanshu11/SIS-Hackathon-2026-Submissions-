"""
Toggle Button
On/Off button for controlling music and sound effects
"""

import pygame
from config import *


class ToggleButton:
    """Toggle button that switches between ON and OFF states"""
    
    def __init__(self, x, y, width, height, label="Sound"):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.is_on = False  # Default to OFF
        
        # Colors
        self.on_color = GREEN
        self.off_color = RED
        self.border_color = WHITE
        self.text_color = WHITE
        
        # Fonts
        self.label_font = pygame.font.Font(None, FONT_SIZE_SMALL)
        self.state_font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        
        # Toggle switch dimensions
        self.switch_width = width - 20
        self.switch_height = height - 20
        self.switch_rect = pygame.Rect(
            x + 10,
            y + 10,
            self.switch_width,
            self.switch_height
        )
        
        # Slider circle
        self.slider_radius = (self.switch_height - 4) // 2
        
    def draw(self, screen):
        """Draw the toggle button"""
        # Label above the button
        label_text = self.label_font.render(self.label, True, self.text_color)
        label_rect = label_text.get_rect(midtop=(self.rect.centerx, self.rect.top - 25))
        screen.blit(label_text, label_rect)
        
        # Switch background
        switch_color = self.on_color if self.is_on else self.off_color
        pygame.draw.rect(screen, switch_color, self.switch_rect, border_radius=self.switch_height // 2)
        pygame.draw.rect(screen, self.border_color, self.switch_rect, 3, border_radius=self.switch_height // 2)
        
        # Slider circle
        if self.is_on:
            slider_x = self.switch_rect.right - self.slider_radius - 5
        else:
            slider_x = self.switch_rect.left + self.slider_radius + 5
            
        slider_y = self.switch_rect.centery
        pygame.draw.circle(screen, WHITE, (slider_x, slider_y), self.slider_radius)
        pygame.draw.circle(screen, DARK_GRAY, (slider_x, slider_y), self.slider_radius - 2)
        
        # State text (ON/OFF)
        state_text = "ON" if self.is_on else "OFF"
        state_surface = self.state_font.render(state_text, True, WHITE)
        
        # Position text on the opposite side of the slider
        if self.is_on:
            text_x = self.switch_rect.left + 15
        else:
            text_x = self.switch_rect.right - 35
            
        text_rect = state_surface.get_rect(center=(text_x, slider_y))
        screen.blit(state_surface, text_rect)
        
    def is_hovered(self, mouse_pos):
        """Check if mouse is hovering over the button"""
        return self.rect.collidepoint(mouse_pos)
    
    def handle_click(self, mouse_pos, mouse_pressed):
        """Handle click and toggle state"""
        if self.is_hovered(mouse_pos) and mouse_pressed[0]:
            self.toggle()
            return True
        return False
    
    def toggle(self):
        """Toggle the button state"""
        self.is_on = not self.is_on
        return self.is_on
    
    def set_state(self, state):
        """Manually set the button state"""
        self.is_on = state
        
    def get_state(self):
        """Get current state"""
        return self.is_on


class MusicToggleButton(ToggleButton):
    """Specialized toggle button for music control"""
    
    def __init__(self, x, y, width=120, height=50):
        super().__init__(x, y, width, height, label="Music")
        self.icon_font = pygame.font.Font(None, 40)
        
    def draw(self, screen):
        """Draw music toggle with icon"""
        # Draw the base toggle
        super().draw(screen)
        
        # Add music icon (♪)
        icon = "♪" if self.is_on else "♪"
        icon_surface = self.icon_font.render(icon, True, WHITE if self.is_on else LIGHT_GRAY)
        icon_rect = icon_surface.get_rect(midbottom=(self.rect.centerx, self.rect.top - 5))
        screen.blit(icon_surface, icon_rect)


class SoundToggleButton(ToggleButton):
    """Specialized toggle button for sound effects control"""
    
    def __init__(self, x, y, width=120, height=50):
        super().__init__(x, y, width, height, label="Sound FX")
        self.icon_font = pygame.font.Font(None, 40)
        
    def draw(self, screen):
        """Draw sound toggle with icon"""
        # Draw the base toggle
        super().draw(screen)
        
        # Add speaker icon (🔊/🔇)
        icon = "🔊" if self.is_on else "🔇"
        try:
            icon_surface = self.icon_font.render(icon, True, WHITE if self.is_on else LIGHT_GRAY)
            icon_rect = icon_surface.get_rect(midbottom=(self.rect.centerx, self.rect.top - 5))
            screen.blit(icon_surface, icon_rect)
        except:
            # Fallback if emoji not supported
            pass
