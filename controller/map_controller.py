from model.map import map
from view import view


def get_map():
    screen_size = (view.WINDOW_WIDTH, view.WINDOW_HEIGHT)
    return map.create_board(screen_size)
