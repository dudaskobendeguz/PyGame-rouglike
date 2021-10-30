from model import data_manager, util


def create_player(color):
    """Creates a player dictionary with attributes:
    name, x, y, width, height, velocity

    Returns: dictionary"""
    return {
        "name": 'Nick',
        "color": color,
        "x": 10,
        "y": 10,
        "width": 64,
        "height": 64,
        "velocity": 10
    }
