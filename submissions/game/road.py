"""
Road Class
Handles the racing track rendering and animation
"""

import pygame
from config import *


class Road:
    """Animated racing road/track"""
    
    def __init__(self):
        self.width = ROAD_WIDTH
        self.speed = ROAD_SPEED
        self.line_offset = 0
