import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Space Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

#Cores
BRANCO = (255,255,255)

#musicas
#pulo
JUMP_SOUND =  pygame.mixer.Sound(os.path.join(IMG_DIR, 'Other/score_sound.wav'))
JUMP_SOUND.set_volume(1)
#morte
DEATH_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Other/death_sound.wav'))
DEATH_SOUND.set_volume(1)
#musica q fica rodando no jogo
SCORE_SOUND = pygame.mixer.music.load(os.path.join(IMG_DIR, 'Other/musica.wav'))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun3.png"))
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
     pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun3Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckrunHammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckrun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckrun2Hammer.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
#BOTOES PARA O MENU
BUTTONS = [
    pygame.image.load(os.path.join(IMG_DIR,"Other/startt.png")),
    pygame.image.load(os.path.join(IMG_DIR,"Other/exitt.png"))
    
]

#BOTÇAO_PARA INICIO
BUTTON_INICIAL = pygame.image.load(os.path.join(IMG_DIR,"Other/StartButton.png"))

#PODERES
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

#CHÃO 
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/teste.png'))
BG = pygame.transform.scale(BG,(SCREEN_WIDTH, SCREEN_HEIGHT ))
#MENU
MENU_JOGO =  pygame.image.load(os.path.join(IMG_DIR, 'Other/menu.png'))
MENU_JOGO = pygame.transform.scale(MENU_JOGO,(SCREEN_WIDTH, SCREEN_HEIGHT ))
#BOTÃO RESET 
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/i.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))


MAIN_STATE = 'main'#menu
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HEART_TYPE = "heart"