'''
This file contains the Tetris class which represents the game itself.
'''
import pygame
import random
from piece import Piece
class Tetris:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.grid = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.score = 0
        self.font = pygame.font.Font(None, 36)
    def run(self):
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_piece(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_piece(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move_piece(0, 1)
                    elif event.key == pygame.K_SPACE:
                        self.rotate_piece()
            self.update()
            self.draw()
        pygame.quit()
    def move_piece(self, dx, dy):
        if self.current_piece:
            new_x = self.current_piece.x + dx
            new_y = self.current_piece.y + dy
            if self.is_valid_move(new_x, new_y, self.current_piece.shape):
                self.current_piece.x = new_x
                self.current_piece.y = new_y
                return True
        return False
    def rotate_piece(self):
        if self.current_piece:
            new_shape = self.current_piece.rotate()
            if self.is_valid_move(self.current_piece.x, self.current_piece.y, new_shape):
                self.current_piece.shape = new_shape
    def is_valid_move(self, x, y, shape):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    new_x = x + col
                    new_y = y + row
                    if not (0 <= new_x < 10 and 0 <= new_y < 20) or self.grid[new_y][new_x] != 0:
                        return False
        return True
    def update(self):
        if not self.current_piece:
            self.current_piece = self.create_piece()
        else:
            if not self.move_piece(0, 1):
                self.lock_piece()
                self.clear_lines()
                self.current_piece = self.create_piece()
    def create_piece(self):
        shapes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        shape = random.choice(shapes)
        x = 4
        y = 0
        return Piece(shape, x, y)
    def lock_piece(self):
        for row in range(len(self.current_piece.shape)):
            for col in range(len(self.current_piece.shape[row])):
                if self.current_piece.shape[row][col] != 0:
                    x = self.current_piece.x + col
                    y = self.current_piece.y + row
                    self.grid[y][x] = 1
    def clear_lines(self):
        lines_cleared = 0
        for row in range(len(self.grid)):
            if all(cell != 0 for cell in self.grid[row]):
                del self.grid[row]
                self.grid.insert(0, [0] * 10)
                lines_cleared += 1
        self.score += lines_cleared * 100
    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, 300, 500), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (400, 50, 300, 500), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (700, 50, 50, 500), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (400, 550, 300, 50), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (400, 50, 50, 500), 5)
        if self.current_piece:
            for row in range(len(self.current_piece.shape)):
                for col in range(len(self.current_piece.shape[row])):
                    if self.current_piece.shape[row][col] != 0:
                        x = self.current_piece.x + col
                        y = self.current_piece.y + row
                        pygame.draw.rect(self.screen, (255, 255, 255), (x * 30 + 50, y * 30 + 50, 30, 30))
        pygame.display.flip()