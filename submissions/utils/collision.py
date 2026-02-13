"""
Collision Detection Utilities
Advanced collision detection and handling
"""

import pygame


class CollisionDetector:
    """Handles collision detection between game objects"""
    
    @staticmethod
    def check_collision(rect1, rect2):
        """Basic rectangle collision detection"""
        return rect1.colliderect(rect2)
    
    @staticmethod
    def check_precise_collision(car1_rect, car2_rect, tolerance=5):
        """
        More precise collision detection with tolerance
        Reduces the hitbox slightly to make gameplay more forgiving
        """
        # Shrink rectangles slightly for more forgiving collision
        adjusted_rect1 = car1_rect.inflate(-tolerance, -tolerance)
        adjusted_rect2 = car2_rect.inflate(-tolerance, -tolerance)
        
        return adjusted_rect1.colliderect(adjusted_rect2)
    
    @staticmethod
    def get_collision_point(rect1, rect2):
        """Get the approximate collision point between two rectangles"""
        if not rect1.colliderect(rect2):
            return None
            
        # Calculate center points
        center1 = rect1.center
        center2 = rect2.center
        
        # Return midpoint between centers
        collision_x = (center1[0] + center2[0]) // 2
        collision_y = (center1[1] + center2[1]) // 2
        
        return (collision_x, collision_y)
    
    @staticmethod
    def check_multiple_collisions(player_rect, obstacle_rects):
        """
        Check collision between player and multiple obstacles
        Returns list of colliding obstacle indices
        """
        collisions = []
        for i, obstacle_rect in enumerate(obstacle_rects):
            if CollisionDetector.check_precise_collision(player_rect, obstacle_rect):
                collisions.append(i)
        return collisions
      
