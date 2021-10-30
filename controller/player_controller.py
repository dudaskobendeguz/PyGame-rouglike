from model.player import player
from view import terminal as view
import pygame


def get_player():
    return player.Player(view.RED)


def control_player(player):
    keys = view.get_input()

    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()
    if keys[pygame.K_LSHIFT]:
        player.sprint()
    else:
        player.walk()

    return player
