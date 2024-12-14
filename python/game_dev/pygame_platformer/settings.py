# game options
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = "arial"

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = -20
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# game property
BOOST_POWER = 60
POW_SPAWN_PCT = 7 

# PLATFORM
PLATFORM_LIST = [
    (0, HEIGHT - 50),
    (WIDTH / 2 - 50, HEIGHT * 3 / 4),
    (100, HEIGHT / 2),
    (350, 200),
    (175, 100),
]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
