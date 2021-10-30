from model.player import player
from view import terminal as view
import pygame


def get_colors():
    return [view.RED, view.BLUE, view.GREEN, view.YELLOW]


def get_player():
    return player.Player(view.RED)


def control_player(player):
    keys = view.get_input()

    if keys[pygame.K_LEFT] and player.x > 0:
        player.move_left()
    if keys[pygame.K_RIGHT] and player.x + player.width < view.SCREEN_WIDTH:
        player.move_right()
    if keys[pygame.K_UP] and player.y > 0:
        player.move_up()
    if keys[pygame.K_DOWN] and player.y + player.height < view.SCREEN_HEIGHT:
        player.move_down()
    if keys[pygame.K_LSHIFT]:
        player.sprint()
    else:
        player.walk()


def change_player_color(player, timer):
    keys = view.get_input()

    seconds = 0.2

    if timer > seconds * 60:
        timer = 0

    if timer == 0:
        if keys[pygame.K_SPACE]:
            player.change_color(get_colors())
            timer += 1
    else:
        timer += 1
    return timer
