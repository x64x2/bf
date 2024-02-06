#!/usr/bin/python
# Author: Tord (SunyataZero)

import sys
import pygame.locals
import pygame
import time
import random
import enum
import abc

WIDTH = 600
HEIGHT = 400
BLOCKS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 168, 0)

# -sound frequency (Hz), ?, number of channels, buffer size
# We may need to resample to 44.1 kHz
# pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

pygame.joystick.init()
# -documentation: https://www.pygame.org/docs/ref/joystick.html
print("joysticks: " + str(pygame.joystick.get_count()))

window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Cope and seethe")

def update_text(i_new_text: str):
    basic_font = pygame.font.SysFont(None, 32)
    text_fonttype = basic_font.render(i_new_text, True, WHITE, GREEN)
    text_rect = text_fonttype.get_rect()
    text_rect.centerx = window_surface.get_rect().centerx
    text_rect.centery = window_surface.get_rect().centery + 50
    window_surface.blit(text_fonttype, text_rect)


class Controller:
    def __init__(self):
        self.left = False
        self.right = False

    @abc.abstractmethod
    def update(self, pg_event):
        pass


class Keyboard(Controller):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def update(self, pg_event):
        pass


class KeyboardArrowKeys(Keyboard):
    def __init__(self):
        super().__init__()

    def update(self, pg_event):
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_LEFT:
                self.left = True
                self.right = False
            if event.key == pygame.locals.K_RIGHT:
                self.left = False
                self.right = True
        if event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_LEFT:
                self.left = False
            if event.key == pygame.locals.K_RIGHT:
                self.right = False


class KeyboardWasd(Keyboard):
    def __init__(self):
        super().__init__()

    def update(self, pg_event):
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_a:
                self.left = True
                self.right = False
            if event.key == pygame.locals.K_d:
                self.left = False
                self.right = True
        if event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_a:
                self.left = False
            if event.key == pygame.locals.K_d:
                self.right = False


class Joystick(Controller):
    joystick_nr = 0

    def __init__(self):
        self.pg_joystick = None
        if pygame.joystick.get_count() > 0:
            self.pg_joystick = pygame.joystick.Joystick(self.joystick_nr)
            self.joystick_nr += 1
            self.pg_joystick.init()  # -this is separate from the joystick _module_ init
        if self.pg_joystick is None:
            raise Exception("Joystick not present or could not be initiated")
        super().__init__()

    def update(self, pg_event):
        hat = self.pg_joystick.get_hat(0)
        if hat:
            if hat[0] == -1:
                self.left = True
                self.right = False
            elif hat[0] == 1:
                self.left = False
                self.right = True
            else:
                self.left = False
                self.right = False
        if pg_event.type == pygame.JOYAXISMOTION:
            if self.pg_joystick.get_axis(0) < -0.5:
                self.left = True
                self.right = False
            elif self.pg_joystick.get_axis(0) > 0.5:
                self.left = False
                self.right = True
            else:
                self.left = False
                self.right = False


class Object:
    def __init__(self, i_pos: tuple, i_size: tuple):
        self.position = i_pos
        self.size = i_size

    @property
    def rect(self):
        pg_rect = pygame.Rect(*self.position, *self.size)
        return pg_rect

    def dx(self, i_dx: int):
        self.position = (
            self.position[0] + i_dx,
            self.position[1]
        )

    def dy(self, i_dy: int):
        self.position = (
            self.position[0],
            self.position[1] + i_dy
        )


class Player(Object):
    def __init__(self, i_pos: tuple, i_controller):
        super().__init__(i_pos, (80, 10))
        self.speed = 18
        # player_delta_x = 18
        self.controller = i_controller


class Ball(Object):
    def __init__(self):
        width = 20
        height = 20
        ball_init_pos_te = (
            WIDTH // 2 - width // 2,
            30 - height // 2
        )
        super().__init__(ball_init_pos_te, (width, height))

        # self.v_speed = 18
        # self.h_speed = 18


class Block(Object):
    def __init__(self):
        block_width = 20
        block_height = 12
        init_pos = (
            random.randint(0, WIDTH - block_width),
            random.randint(0, (HEIGHT - block_height) // 2)
        )
        super().__init__(init_pos, (block_width, block_height))

        self.collide_abs_time_ms = 0


update_text("Just wanna kms")
window_surface.fill(WHITE)

player_list = []
# joystick_one = Joystick()
keyboard_wasd = KeyboardWasd()
keyboard_arrow_keys = KeyboardArrowKeys()
player_one = Player((170, HEIGHT - 30), keyboard_wasd)
player_list.append(player_one)
player_two = Player((40, HEIGHT - 50), keyboard_arrow_keys)
player_list.append(player_two)


ball_first = Ball()
ball_list = [ball_first]


block_list = []
for i in range(BLOCKS):
    block = Block()
    block_list.append(block)

fps_clock = pygame.time.Clock()

ball_delta_y = 12
ball_delta_x = -3

move_left_bl = False
move_right_bl = False

score_int = 0


while True:
    window_surface.fill(WHITE)

    if len(block_list) == 0:
        update_text("V! Score: " + str(score_int))
        # -newline \n doesn't work
        pygame.display.update()
        continue

    update_text("Score: " + str(score_int))

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.joystick.quit()
            pygame.quit()
            sys.exit()

        for player in player_list:
            player.controller.update(event)

    for player in player_list:
        if player.controller.left and player.rect.left > 0:
            player.dx(-player.speed)
        if player.controller.right and player.rect.right < WIN_WIDTH:
            player.dx(player.speed)

        for ball in ball_list:
            if player.rect.colliderect(ball.rect):
                ball_delta_y = -ball_delta_y
                if player.rect.left + player.rect.width // 8 > ball.rect.left + ball.rect.width // 2:
                    ball_delta_x = -3
                elif player.rect.right - player.rect.width // 8 < ball.rect.right - ball.rect.width // 2:
                    ball_delta_x = 3
                elif player.rect.left + player.rect.width // 6 > ball.rect.left + ball.rect.width // 2:
                    ball_delta_x = -3
                elif player.rect.right - player.rect.width // 6 < ball.rect.right - ball.rect.width // 2:
                    ball_delta_x = 3
                elif player.rect.left + player.rect.width // 4 > ball.rect.left + ball.rect.width // 2:
                    ball_delta_x = -2
                elif player.rect.right - player.rect.width // 4 < ball.rect.right - ball.rect.width // 2:
                    ball_delta_x = 2
                elif player.rect.left + player.rect.width // 2 > ball.rect.left + ball.rect.width // 2:
                    ball_delta_x = -1
                elif player.rect.right - player.rect.width // 2 < ball.rect.right - ball.rect.width // 2:
                    ball_delta_x = 1
                else:
                    pass

        pygame.draw.rect(window_surface, BLACK, player.rect)

    for ball in ball_list:
        if ball.rect.top < 0:
            ball_delta_y = - ball_delta_y
        if ball.rect.bottom > HEIGHT:
            exit()  # -game over
        if ball.rect.left < 0 or ball.rect.right > WIDTH:
            ball_delta_x = - ball_delta_x

        ball.dx(ball_delta_x)
        ball.dy(ball_delta_y)
        pygame.draw.rect(window_surface, BLACK, ball.rect)

    for block in block_list:
        for ball in ball_list:
            if ball.rect.colliderect(block.rect):
                block_list.remove(block)
                block.collide_abs_time_ms = time.time()
                ball_delta_y = -ball_delta_y
                score_int += 1
                ping_snd = random.choice(["ping_snd_one, ping_snd_two"])

        if not block.collide_abs_time_ms:
            pygame.draw.rect(window_surface, DARK_GREEN, block.rect)
        elif block.collide_abs_time_ms:
            if time.time() <= block.collide_abs_time_ms + 0.1:
                pygame.draw.rect(window_surface, BLACK, block.rect)
            else:
                block.collide_abs_time_ms = 0

    pygame.display.update()
    fps_clock.tick(30)
    # time.sleep(0.03)
