import random
import time

# Global variables for player and computer grids
player_grid = []
computer_grid = []

# Global variable for grid size
grid_size = 10

# Global variable for number of ships to place
num_of_ships = 8

# Global variables for bullets left
player_bullets_left = 50
computer_bullets_left = 50

# Global variable for game over
game_over = False

# Global variables for ships sunk
player_ships_sunk = 0
computer_ships_sunk = 0

# Global variable for ship positions
player_ship_positions = []
computer_ship_positions = []

# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(grid, ship_positions, start_row, end_row, start_col, end_col):
    """
    Will check the row or column to see if it is safe to place a ship there.
    """
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


def try_to_place_ship_on_grid(grid, ship_positions, row, col, direction, length):
    """
    Based on direction, will call helper method to try and place a ship on the grid.
    Returns validate_grid_and_place_ship.
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

    return validate_grid_and_place_ship(grid, ship_positions, start_row, end_row, start_col, end_col)


def create_grid():
    """
    Will create two 10x10 grids and randomly place down ships
    of different sizes in different directions.
    """
    global player_grid
    global computer_grid
    global grid_size
    global num_of_ships
    global player_ship_positions
    global computer_ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    player_grid = []
    computer_grid = []
    for r in range(rows):
        player_row = []
        computer_row = []
        for c in range(cols):
            player_row.append(".")
            computer_row.append(".")
        player_grid.append(player_row)
        computer_grid.append(computer_row)

    player_ship_positions = []
    computer_ship_positions = []

    print("Please place your ships on the grid.")
    for i in range(num_of_ships):
        placed = False
        while not placed:
            print_grid(player_grid, show_ships=True)
            print(f"Place ship {i + 1} (size 3-5):")
            row = input("Enter start row (A-J): ").upper()
            col = input("Enter start column (0-9): ")
            direction = input("Enter direction (left, right, up, down): ").lower()
            size = int(input("Enter ship size (3-5): "))
            row = alphabet.find(row)
            col = int(col)
            if try_to_place_ship_on_grid(player_grid, player_ship_positions, row, col, direction, size):
                placed = True
            else:
                print("Invalid placement. Try again.")

    num_of_ships_placed = 0
    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(computer_grid, computer_ship_positions, random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def print_grid(grid, show_ships=False):
    """
    Will print the grid with rows A-J and columns 0-9.
    If show_ships is True, it will display the positions of the ships.
    """
    global alphabet

    print(". = water or empty space")
    print("O = part of ship")
    print("X = part of ship that was hit with bullet")
    print("# = water that was shot with bullet, a miss, because it hit no ship")

    alphabet = alphabet[:len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O" and not show_ships:
                print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def accept_valid_bullet_placement():
    """
    Will get valid row and column to place bullet shot.
    Has return row, col.
    """
    global alphabet
    global computer_grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A1:\n")
        placement = placement.upper()
        if len(placement) < 2 or len(placement) > 3:
            print("Error: Please enter only one row and column such as A1:\n")
            continue
        row = placement[0]
        col = placement[1:]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column\n")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if computer_grid[row][col] == "#" or computer_grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if computer_grid[row][col] == "." or computer_grid[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_ship_sunk(grid, ship_positions, row, col):
    """
    If all parts of a ship have been shot it is sunk and will later increment ships sunk.
    Has return True or False.
    """
    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row < end_row and start_col <= col < end_col:
            # Ship found, now check if it's all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    """
    Updates grid and ships based on where the bullet was shot.
    Has no return but will use accept_valid_bullet_placement.
    """
    global computer_grid
    global computer_ships_sunk
    global player_bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if computer_grid[row][col] == ".":
        print("You missed, no ship was shot")
        computer_grid[row][col] = "#"
    elif computer_grid[row][col] == "O":
        print("You hit!", end=" ")
        computer_grid[row][col] = "X"
        if check_for_ship_sunk(computer_grid, computer_ship_positions, row, col):
            print("A ship was completely sunk!")
            computer_ships_sunk += 1
        else:
            print("A ship was shot")

    player_bullets_left -= 1


def computer_shoot():
    """
    Computer shoots at random positions.
    """
    global player_grid
    global player_ships_sunk
    global computer_bullets_left

    valid_shot = False
    while not valid_shot:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if player_grid[row][col] == "." or player_grid[row][col] == "O":
            valid_shot = True

    print(f"Computer shoots at {alphabet[row]}{col}")

    if player_grid[row][col] == ".":
        print("Computer missed, no ship was shot")
        player_grid[row][col] = "#"
    elif player_grid[row][col] == "O":
        print("Computer hit!", end=" ")
        player_grid[row][col] = "X"
        if check_for_ship_sunk(player_grid, player_ship_positions, row, col):
            print("Your ship was completely sunk!")
            player_ships_sunk += 1
        else:
            print("Your ship was shot")

    computer_bullets_left -= 1


def check_for_game_over():
    """
    If all ships have been sunk or we run out of bullets it's game over.
    Has no return
    """
    global player_ships_sunk
    global computer_ships_sunk
    global num_of_ships
    global player_bullets_left
    global computer_bullets_left
    global game_over

    if computer_ships_sunk == num_of_ships:
        print("Congrats you won!")
        game_over = True
    elif player_ships_sunk == num_of_ships:
        print("Sorry, you lost! The computer sunk all your ships!")
        game_over = True
    elif player_bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True
    elif computer_bullets_left <= 0:
        print("Congrats you won! The computer ran out of bullets!")
        game_over = True


def main():
    """
    Main entry point of application that runs the game loop.
    Has no return, but will use create_grid, print_grid, shoot_bullet, computer_shoot, and check_for_game_over.
    """
    global game_over

    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()

    while not game_over:
        print("Your grid:")
        print_grid(player_grid, show_ships=True)
        print("\nComputer's grid:")
        print_grid(computer_grid, show_ships=False)
        print("Number of ships remaining (computer): " + str(num_of_ships - computer_ships_sunk))
        print("Number of bullets left: " + str(player_bullets_left))
        shoot_bullet()
        computer_shoot()
        print("----------------------------")
        print("")
        check_for_game_over()


if __name__ == "__main__":
    main()
