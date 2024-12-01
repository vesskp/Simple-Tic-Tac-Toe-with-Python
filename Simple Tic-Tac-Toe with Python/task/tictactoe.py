def display_grid(grid):
    # Print the grid with boundaries
    print("---------")
    for row in grid:
        print("|", " ".join(row), "|")
    print("---------")


def is_valid_move(grid, row, col):
    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        return False
    if grid[row - 1][col - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def get_user_move():
    while True:
        try:
            row, col = map(int, input("Enter the coordinates: ").split())
            return row, col
        except ValueError:
            print("You should enter numbers!")


def update_grid(grid, row, col, player):
    grid[row - 1][col - 1] = player


def check_winner(grid):
    lines = grid + [list(col) for col in zip(*grid)] + [[grid[i][i] for i in range(3)],
                                                        [grid[i][2 - i] for i in range(3)]]

    if ['X'] * 3 in lines:
        return 'X wins'
    if ['O'] * 3 in lines:
        return 'O wins'

    return None


def is_draw(grid):
    return all(cell != ' ' for row in grid for cell in row)


def main():
    grid = [[' ' for _ in range(3)] for _ in range(3)]
    display_grid(grid)
    current_player = 'X'
    while True:
        row, col = get_user_move()
        if is_valid_move(grid, row, col):
            update_grid(grid, row, col, current_player)
            display_grid(grid)
            winner = check_winner(grid)
            if winner:
                print(winner)
                break
            if is_draw(grid):
                print("Draw")
                break
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
