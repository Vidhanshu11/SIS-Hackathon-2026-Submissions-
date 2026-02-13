"""
Particle Effects System
Creates visual effects like exhaust smoke, sparks, and boost trails
"""

import pygame
import random
from config import *


class Particle:
    """Single particle for effects"""
    
    def __init__(self, x, y, color, speed, lifetime):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.size = random.randint(*PARTICLE_SIZE_RANGE)
        self.dx = random.uniform(-1, 1)
        
    def update(self):
        """Update particle position and lifetime"""
        self.y += self.speed
        self.x += self.dx
        self.lifetime -= 1
        
    def draw(self, screen):
        """Draw the particle with fade effect"""
        if self.lifetime > 0:
            # Fade effect based on remaining lifetime
            alpha_ratio = self.lifetime / self.max_lifetime
            current_size = int(self.size * alpha_ratio)
            
            if current_size > 0:
                # Create a surface with alpha for transparency
                particle_surface = pygame.Surface((current_size * 2, current_size * 2), pygame.SRCALPHA)
                
                # Adjust color alpha
                fade_color = (*self.color[:3], int(255 * alpha_ratio))
                pygame.draw.circle(particle_surface, fade_color, 
                                 (current_size, current_size), current_size)
                screen.blit(particle_surface, (int(self.x - current_size), int(self.y - current_size)))
    
    def is_dead(self):
        """Check if particle should be removed"""
        return self.lifetime <= 0


class ParticleSystem:
    """Manages all particle effects"""
    
    def __init__(self):
        self.particles = []
        
    def emit_exhaust(self, x, y, boost=False):
        """Create exhaust particles from car"""
        color = ORANGE if boost else LIGHT_GRAY
        speed_range = (4, 8) if boost else PARTICLE_SPEED_RANGE
        
        for _ in range(PARTICLE_COUNT if boost else 2):
            speed = random.uniform(*speed_range)
            lifetime = PARTICLE_LIFETIME if boost else PARTICLE_LIFETIME // 2
            particle = Particle(x, y, color, speed, lifetime)
            self.particles.append(particle)
    
    def emit_collision_sparks(self, x, y):
        """Create spark effect on collision"""
        for _ in range(15):
            speed = random.uniform(3, 7)
            lifetime = random.randint(15, 30)
            color = random.choice([YELLOW, ORANGE, RED, WHITE])
            particle = Particle(x, y, color, speed, lifetime)
            # More spread for sparks
            particle.dx = random.uniform(-3, 3)
            self.particles.append(particle)
    
    def emit_boost_trail(self, x, y):
        """Create continuous boost trail effect"""
        for _ in range(3):
            speed = random.uniform(2, 5)
            lifetime = random.randint(20, 35)
            color = random.choice([BLUE, (0, 150, 255), WHITE])
            particle = Particle(x, y, color, speed, lifetime)
            self.particles.append(particle)
            
    def update(self):
        """Update all particles"""
        for particle in self.particles[:]:
            particle.update()
            if particle.is_dead():
                self.particles.remove(particle)
                
    def draw(self, screen):
        """Draw all particles"""
        for particle in self.particles:
            particle.draw(screen)
            
    def clear(self):
        """Remove all particles"""
        self.particles.clear()
