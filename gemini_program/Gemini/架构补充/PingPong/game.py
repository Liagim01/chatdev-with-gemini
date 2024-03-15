import pygame
from paddle import Paddle
from ball import Ball
class Game:
    def __init__(self):
        self.width = 800
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PingPong Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paddle1 = Paddle(20, self.height // 2)
        self.paddle2 = Paddle(self.width - 20, self.height // 2)
        self.ball = Ball(self.width // 2, self.height // 2)
        self.score1 = 0
        self.score2 = 0
        self.font = pygame.font.Font(None, 36)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.paddle1.move_up()
                if event.key == pygame.K_s:
                    self.paddle1.move_down()
                if event.key == pygame.K_UP:
                    self.paddle2.move_up()
                if event.key == pygame.K_DOWN:
                    self.paddle2.move_down()
    def update(self):
        self.ball.update(self.paddle1, self.paddle2)
        self.paddle1.update()
        self.paddle2.update()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.ball.draw(self.screen)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        score1_text = self.font.render(str(self.score1), True, (255, 255, 255))
        score2_text = self.font.render(str(self.score2), True, (255, 255, 255))
        self.screen.blit(score1_text, (self.width // 4, 20))
        self.screen.blit(score2_text, (self.width * 3 // 4, 20))
        pygame.display.update()
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        self.game_over()
    def game_over(self):
        if self.ball.x < 0:
            self.score2 += 1
            self.ball.reset()
        if self.ball.x > self.width:
            self.score1 += 1
            self.ball.reset()
        if self.score1 == 10 or self.score2 == 10:
            self.running = False
