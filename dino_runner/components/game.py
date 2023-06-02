import pygame

from dino_runner.utils.constants import *
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.button import Button

class Game:
    def __init__(self):
            pygame.init()
            pygame.display.set_caption(TITLE)
            pygame.display.set_icon(ICON)
            self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            self.clock = pygame.time.Clock()
            self.playing = False
            self.running = False
            #adc game pause e main
            self.game_paused = False
            self.menu_state = MAIN_STATE
            
            self.time_is_up = False
            
            self.score = 0
            self.death_count = 0
            self.game_speed = 10
            self.x_pos_bg = 0
            self.y_pos_bg = 0

            self.player = Dinosaur()
            self.obstacle_manager = ObstacleManager()
            self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def reset_score(self):
        self.game_speed = 10
        self.score = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.reset_score()

        while self.playing:
            self.events()
            self.update()
            self.draw()
 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                #elif para evento do pausa
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_paused = True
                    self.my_menu()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3


    def draw(self):
        self.clock.tick(FPS)
        #self.screen.fill((255, 255, 255)) # "#FFFFFF"
        self.screen.blit(MENU_JOGO,(0,0))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
           draw_message_component(
            f"score: {self.score}",
            self.screen, 
            font_color= BRANCO, 
            font_size= 31,
            pos_x_center=1000,
            pos_y_center=50
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} ativado por {time_to_show} segundos",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.run()
            elif event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def my_buttons(self):
            self.resume_button = Button(340, 125, BUTTONS[0], 1)
            self.quit_button = Button(400, 260, BUTTONS[1], 1)
    
    def my_menu(self):
        self.my_buttons()
        while self.game_paused:
            if self.menu_state == MAIN_STATE:
                if self.resume_button.draw(self.screen):
                    self.game_paused = False
                    
                elif self.quit_button.draw(self.screen):
                    self.playing = False
                    pygame.quit()
                self.handle_events_on_menu()
                pygame.display.update()
    
    def show_menu(self):
        self.screen.blit(MENU_JOGO,(0,0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            draw_message_component("Pressione qualquer tecla  para iniciar", self.screen,font_color= BRANCO,font_size=35 , pos_y_center=half_screen_height + 250)
            self.screen.blit(BUTTON_INICIAL, (half_screen_width -215,390  ))
        else:
            draw_message_component("Pressione qualquer tecla  para reiniciar", self.screen, pos_y_center=half_screen_height + 190)
            draw_message_component("OPS, TENTE NOVAMENTE", self.screen, pos_y_center=half_screen_height + 150)         
            draw_message_component(
                f"Sua pontuação: {self.score}", self.screen,
                pos_y_center=half_screen_height - 190
            )
            draw_message_component(
                f"contagem de mortes: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )
            
            self.screen.blit(GAME_OVER, (half_screen_width - 320, half_screen_height - 150))

        pygame.display.flip()

        self.handle_events_on_menu()