import random
import time

"""
-------BATTLESHIPS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 8 ships of variable length randomly placed about
    2. You will have 50 bullets to take down the ships that are placed down
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are unearthed before using up all bullets, you win
        else, you lose

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship
"""

# Global variable for grid
grid = [[]]

# Global variable for grid size
grid_size = 10

# Global variable for number of ships to place
num_of_ships = 8

# Global variable for bullets left
bullets_left = 50

# Global variable for game over
game_over = False

# Global variable for ships sunk
num_of_ships_sunk = 0

# Global variable for ship positions
ship_positions = [[]]

# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Will check the row or column to see if it is safe to place a ship there.
    """
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid



def try_to_place_ship_on_grid(row, col, direction, length):
    """
    Based on direction will call helper method to try and place a ship on the grid.
    Returns validate_grid_and_place_ship which will be True or False.
    """
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
         if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    if direction == "up":
         if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(0, 0, 0, 0)



def create_grid():
    """
    Will create a 10x10 grid and randomly place down ships
    of different sizes in different directions.
    Has no return but will use try_to_place_ship_on_grid.
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    pass

    try_to_place_ship_on_grid(0, 0, 0, 0)

def print_grid():
    """
    Will print the grid with rows A-J and columns 0-9.
    has no return
    """
    global grid
    global alphabet

    pass

def accept_valid_bullet_placement():
    """
    Will get valid row and column to place bullet shot.
    Has return row, col, both are integers.
    """
    global alphabet
    global grid

    pass

    return 0, 0

def check_for_ship_sunk():
    """
    If all parts of a ship have been shot it is sunk and will increment ships sunk.
    Has return True or False.
    """
    global ship_positions
    global grid

    pass

def shoot_bullet():
    """
    Updates grid and ships based on where the bullet was shot.
    Has no return but will use accept_valid_bullet_placement.
    """
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()

    pass

def check_for_game_over():
    """
    If all ships have been sunk or we run out of bullets it's game over.
    Has no return
    """
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    pass

def main():
    """
    Main entry point of application that runs the game loop.
    Has no return, but will use create_grid, print_grid, shoot_bullet and check_for_game_over.
    """
    global game_over

    pass

if __name__ == "__main__":
    """
    Will only be called when program is run from terminal or an IDE like "Codeanywhere"
    """
    main()