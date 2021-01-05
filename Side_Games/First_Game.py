import pygame
from random import randint
import math
from pygame import mixer

# Initialize PyGame
pygame.init()

# Create Player
character = randint(1, 3)

# Create The Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Bullet Icon

# <div>Icons made by <a href="https://www.flaticon.com/authors/good-ware"
# title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/"
# title="Flaticon">www.flaticon.com</a></div>


# Enemy, Player and Title Icon URL
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title=
# "Freepik">Freepik</a> from <a href="https://www.flaticon.com/"
# title="Flaticon">www.flaticon.com</a></div><div>Icons made by <a href=
# "https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons
# </a> from <a href="https://www.flaticon.com/" title="Flaticon">
# www.flaticon.com</a></div><div>Icons made by <a href="https://
# www.flaticon.com/authors/vitaly-gorbachev" title="Vitaly Gorbachev">
# Vitaly Gorbachev</a> from <a href="https://www.flaticon.com/" title="Flaticon"
# >www.flaticon.com</a></div>


# Background Image URL
# <a href='https://www.freepik.com/vectors/background'>Background vector
# created by rawpixel.com - www.freepik.com</a>

# Background
background = pygame.image.load("galaxy.jpg")


class Enemy:
    def __init__(self,
                 enemy_x_axis,
                 enemy_y_axis):
        self.enemy_x_axis = enemy_x_axis
        self.enemy_y_axis = enemy_y_axis


class BottomTier(Enemy):
    def __init__(self, enemy_x_axis, enemy_y_axis, exd=0, eyd=0):
        Enemy.__init__(self, enemy_x_axis, enemy_y_axis)
        self.exd = exd
        self.eyd = eyd
        self.enemy_image = pygame.image.load("001-space-invaders.png")

    def enemy_x_delta(self, movement):
        self.exd += movement

    def enemy_y_delta(self, movement):
        self.eyd += movement


class MidTier(Enemy):
    def __init__(self, enemy_x_axis, enemy_y_axis, exd=0, eyd=0):
        Enemy.__init__(self, enemy_x_axis, enemy_y_axis)
        self.exd = exd
        self.eyd = eyd
        self.enemy_image = pygame.image.load("002-space-invaders.png")

    def enemy_x_delta(self, movement):
        self.exd += movement + 1

    def enemy_y_delta(self, movement):
        self.eyd += movement + 1


class TopTier(Enemy):
    def __init__(self, enemy_x_axis, enemy_y_axis, exd=0, eyd=0):
        Enemy.__init__(self, enemy_x_axis, enemy_y_axis)
        self.exd = exd
        self.eyd = eyd
        self.enemy_image = pygame.image.load("003-space-invaders.png")

    def enemy_x_delta(self, movement):
        self.exd += movement + 2

    def enemy_y_delta(self, movement):
        self.eyd += movement + 2


class Player:
    """
    Player class that creates spaceship
    """
    def __init__(self,
                 player_image,
                 player_x_axis,
                 player_y_axis,
                 xd=0,
                 yd=0,
                 health=10):
        self.player_image = pygame.image.load(f"00{player_image}-spaceship.png")
        self.player_x_axis = player_x_axis
        self.player_y_axis = player_y_axis
        self.xd = xd
        self.yd = yd
        self.health = health

    def y_delta(self, movement):
        self.yd += movement

    def x_delta(self, movement):
        self.xd += movement


class Bullet:
    def __init__(
            self, image, bullet_x_axis, bullet_y_axis, state, bxd=0, byd=20
    ):
        self.image = image
        self.x_axis, self.y_axis = bullet_x_axis, bullet_y_axis
        self.bxd = bxd
        self.byd = byd
        self.state = state


acc_low = []
acc_mid = []
acc_high = []
ship = Player(character, 370, 480)
ENEMIES = 3
for i in range(ENEMIES):

    low = BottomTier(randint(0, 800 - 64), randint(50, 150))

    acc_low.append(low)

for i in range(ENEMIES):
    mid = MidTier(randint(0, 800 - 64), randint(50, 150))

    acc_mid.append(mid)

for i in range(ENEMIES):
    high = TopTier(randint(0, 800 - 64), randint(50, 150))

    acc_high.append(high)


bullet = Bullet(
    "001-bullet.png", 0, 0, "ready"
)
bullet_image = pygame.image.load(bullet.image)


def player():

    screen.blit(ship.player_image, (ship.player_x_axis, ship.player_y_axis))
    # screen.blit(10, (ship.player_x_axis + 32, ship.player_y_axis + 70))


def enemy():

    count = 0
    while count <= 10:
        num = randint(1, 3)
        if num == 1:
            for index in range(len(acc_low)):
                screen.blit(acc_low[index].enemy_image,
                            (acc_low[index].enemy_x_axis,
                            acc_low[index].enemy_y_axis))
        elif num == 2:
            for index in range(len(acc_mid)):
                screen.blit(acc_mid[index].enemy_image,
                            (acc_mid[index].enemy_x_axis,
                             acc_mid[index].enemy_y_axis))
        else:
            for index in range(len(acc_high)):
                screen.blit(acc_high[index].enemy_image,
                            (acc_high[index].enemy_x_axis,
                             acc_high[index].enemy_y_axis))
        count += 1


def fire():
    bullet.state = "fire"
    screen.blit(
        bullet_image, (bullet.x_axis + 16, bullet.y_axis - 32)
    )


def did_it_collide(ex, ey, bx, by):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < 27


# SCORE = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
font_game = pygame.font.Font('freesansbold.ttf', 64)
SCORE_X = 20
SCORE_Y = 20


def show_score():
    score = font.render("SCORE: " + str(score_value), True, (255, 128, 0))
    screen.blit(score, (SCORE_X, SCORE_Y))


HEALTH_X = SCORE_X
HEALTH_Y = SCORE_Y + 42


def show_health():
    health = font.render("HEALTH: " + str(ship.health), True, (128, 255, 0))
    screen.blit(health, (HEALTH_X, HEALTH_Y))


def did_ship_crash(ex, ey, sx, sy):
    distance = math.sqrt((ex - sx) ** 2 + (ey - sy) ** 2)
    return distance < 32


GAME_X = 50
GAME_Y = 250

GAME_OVER = False


def game_over():
    stuff = font_game.render("GAME OVER (Press R)", True, (255, 0, 0))
    screen.blit(stuff, (GAME_X, GAME_Y))
    for index in range(len(acc_low)):
        acc_low[index].enemy_x_axis = -4000
        acc_mid[index].enemy_x_axis = -4000
        acc_high[index].enemy_x_axis = -4000
        acc_low[index].enemy_y_axis = -4000
        acc_mid[index].enemy_y_axis = -4000
        acc_high[index].enemy_y_axis = -4000


# Game Window
running = True
flag_low = [True for i in range(len(acc_low))]
flag_mid = [False for i in range(len(acc_mid))]
flag_high = [randint(0, 1) for i in range(len(acc_high))]
while running:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ship.y_delta(2)
            if event.key == pygame.K_UP:
                ship.y_delta(-2)
            if event.key == pygame.K_RIGHT:
                ship.x_delta(2)
            if event.key == pygame.K_LEFT:
                ship.x_delta(-2)
            if event.key == pygame.K_SPACE and bullet.state == "ready":
                mixer.Sound("laser.wav").play()
                bullet.x_axis = ship.player_x_axis
                bullet.y_axis = ship.player_y_axis
                fire()
            if event.key == pygame.K_r:
                player()
                enemy()
                score_value = 0
                show_score()
                ship.health = 10
                show_health()
                GAME_OVER = False
                for i in range(ENEMIES):
                    acc_low[i] = BottomTier(randint(0, 800 - 64), randint(50, 150))

                for i in range(ENEMIES):
                    acc_mid[i] = MidTier(randint(0, 800 - 64), randint(50, 150))

                for i in range(ENEMIES):
                    acc_high[i] = TopTier(randint(0, 800 - 64), randint(50, 150))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.xd = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.yd = 0

    ship.player_y_axis += ship.yd

    for i in range(len(acc_low)):
        if flag_low[i]:
            acc_low[i].enemy_x_axis += 0.25
        if not flag_low[i]:
            acc_low[i].enemy_x_axis -= 0.25

        if acc_low[i].enemy_x_axis > 800 - 64:
            flag_low[i] = False
            acc_low[i].enemy_x_axis = 800 - 64
            acc_low[i].enemy_y_axis += 16

        if acc_low[i].enemy_x_axis < 0:
            flag_low[i] = True
            acc_low[i].enemy_x_axis = 0
            acc_low[i].enemy_y_axis += 16

    for i in range(len(acc_mid)):
        if flag_mid[i]:
            acc_mid[i].enemy_x_axis += 0.5
        if not flag_mid[i]:
            acc_mid[i].enemy_x_axis -= 0.5

        if acc_mid[i].enemy_x_axis > 800 - 64:
            flag_mid[i] = False
            acc_mid[i].enemy_x_axis = 800 - 64
            acc_mid[i].enemy_y_axis += 16

        if acc_mid[i].enemy_x_axis < 0:
            flag_mid[i] = True
            acc_mid[i].enemy_x_axis = 0
            acc_mid[i].enemy_y_axis += 16

    for i in range(len(acc_high)):
        if flag_high[i]:
            acc_high[i].enemy_x_axis += 1
        if not flag_high[i]:
            acc_high[i].enemy_x_axis -= 1

        if acc_high[i].enemy_x_axis > 800 - 64:
            flag_high[i] = False
            acc_high[i].enemy_x_axis = 800 - 64
            acc_high[i].enemy_y_axis += 16

        if acc_high[i].enemy_x_axis < 0:
            flag_high[i] = True
            acc_high[i].enemy_x_axis = 0
            acc_high[i].enemy_y_axis += 16

        if acc_high[i].enemy_y_axis > 600 - 64 or \
                acc_mid[i].enemy_y_axis > 600 - 64 or \
                acc_low[i].enemy_y_axis > 800 - 64:
            GAME_OVER = True

    if ship.player_y_axis > HEIGHT - 64:
        ship.player_y_axis = HEIGHT - 64
    if ship.player_y_axis < 0:
        ship.player_y_axis = 0
    ship.player_x_axis += ship.xd
    if ship.player_x_axis > WIDTH - 64:
        ship.player_x_axis = WIDTH - 64
    if ship.player_x_axis < 0:
        ship.player_x_axis = 0

    # Bullet Movement
    if bullet.y_axis <= -32:
        bullet.state = "ready"

    if bullet.state == "fire":
        fire()
        bullet.y_axis -= bullet.byd

    # Bullet Collision
    for i in range(len(acc_low)):
        collision_low = did_it_collide(
            acc_low[i].enemy_x_axis,
            acc_low[i].enemy_y_axis,
            bullet.x_axis,
            bullet.y_axis
        )
        if collision_low and bullet.state == "fire":
            mixer.Sound("explosion.wav").play()
            bullet.state = "ready"
            score_value += 10
            acc_low[i].enemy_x_axis = randint(0, 800 - 64)
            acc_low[i].enemy_y_axis = randint(50, 150)

    for i in range(len(acc_mid)):
        collision_mid = did_it_collide(
            acc_mid[i].enemy_x_axis,
            acc_mid[i].enemy_y_axis,
            bullet.x_axis,
            bullet.y_axis
        )

        if collision_mid and bullet.state == "fire":
            mixer.Sound("explosion.wav").play()
            bullet.state = "ready"
            score_value += 15
            acc_mid[i].enemy_x_axis = randint(0, 800 - 64)
            acc_mid[i].enemy_y_axis = randint(50, 150)

    for i in range(len(acc_high)):
        collision_high = did_it_collide(
            acc_high[i].enemy_x_axis,
            acc_high[i].enemy_y_axis,
            bullet.x_axis,
            bullet.y_axis
        )

        if collision_high and bullet.state == "fire":
            mixer.Sound("explosion.wav").play()
            bullet.state = "ready"
            score_value += 20
            acc_high[i].enemy_x_axis = randint(0, 800 - 64)
            acc_high[i].enemy_y_axis = randint(50, 150)

    # Ship Collision
    for i in range(len(acc_low)):
        crash_low = did_ship_crash(
            acc_low[i].enemy_x_axis,
            acc_low[i].enemy_y_axis,
            ship.player_x_axis,
            ship.player_y_axis
        )
        if crash_low:
            mixer.Sound("explosion.wav").play()
            ship.player_x_axis = 370
            ship.player_y_axis = 480
            ship.health -= 2

    for i in range(len(acc_mid)):
        crash_mid = did_ship_crash(
            acc_mid[i].enemy_x_axis,
            acc_mid[i].enemy_y_axis,
            ship.player_x_axis,
            ship.player_y_axis
        )
        if crash_mid:
            mixer.Sound("explosion.wav").play()
            ship.player_x_axis = 370
            ship.player_y_axis = 480
            ship.health -= 2

    for i in range(len(acc_high)):
        crash_high = did_ship_crash(
            acc_high[i].enemy_x_axis,
            acc_high[i].enemy_y_axis,
            ship.player_x_axis,
            ship.player_y_axis
        )
        if crash_high:
            mixer.Sound("explosion.wav").play()
            ship.player_x_axis = 370
            ship.player_y_axis = 480
            ship.health -= 2

    if ship.health <= 0:
        game_over()
        score_value = 0

    player()
    enemy()
    show_score()
    show_health()
    pygame.display.update()
