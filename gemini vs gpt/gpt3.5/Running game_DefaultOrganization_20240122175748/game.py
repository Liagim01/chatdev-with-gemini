'''
This file contains the Game class responsible for managing the game state.
'''
import pygame
from player import Player
from obstacle import Obstacle
from constants import *
class Game:
    def __init__(self, window):
        self.window = window
        self.player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR)
        self.obstacles = []
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over_panel = None
        self.restart = False
    def update(self):
        self.player.update()
        self.spawn_obstacle()
        self.update_obstacles()
        self.check_collision()
        self.update_score()
        if self.restart:
            self.restart_game()
    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        self.player.draw(self.window)
        for obstacle in self.obstacles:
            obstacle.draw(self.window)
        self.draw_score()
        if self.game_over_panel:
            self.window.blit(self.game_over_panel, (window_width // 2 - self.game_over_panel.get_width() // 2, window_height // 2 - self.game_over_panel.get_height() // 2))
    def spawn_obstacle(self):
        if len(self.obstacles) == 0 or self.obstacles[-1].x < window_width - OBSTACLE_GAP - OBSTACLE_WIDTH:
            self.obstacles.append(Obstacle(OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_COLOR, window_width))
    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()
    def check_collision(self):
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.game_over()
    def update_score(self):
        self.score += 1
    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.window.blit(score_text, (10, 10))
    def game_over(self):
        self.obstacles.clear()
        self.score = 0
        self.game_over_panel = self.font.render("Game Over", True, SCORE_COLOR)
        self.restart = True
    def restart_game(self):
        self.game_over_panel = None
        self.restart = False
        self.player.reset()