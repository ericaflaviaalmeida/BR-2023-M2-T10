import random
import pygame

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.life import HeartLife


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.power_ups_type = [Shield(), Hammer(), HeartLife()]
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(random.choice(self.power_ups_type))

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.shield = True
                game.player.hammer = True
                game.player.life = True
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)