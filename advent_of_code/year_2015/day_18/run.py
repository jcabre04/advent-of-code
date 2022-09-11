import numpy as np
import numpy.typing as npt


def _create_grid(instructions: list[str], grid_dims: int) -> npt.NDArray[np.ubyte]:
    "Return a 2D grid (numpy array) representing lights turned on (1) or off (0)"
    grid = np.zeros((grid_dims, grid_dims), dtype=np.ubyte)
    for row, line in enumerate(instructions):
        for col, char in enumerate(line):
            if char == "#":
                grid[row][col] = 1
    return grid


def _count_neighbors(grid: npt.NDArray[np.ubyte], row: int, col: int) -> int:
    "Returns the number of neighbors turned on"
    neighbors_on = 0

    for neigh_row in range(max(row - 1, 0), min(row + 2, grid.shape[0])):
        for neigh_col in range(max(col - 1, 0), min(col + 2, grid.shape[0])):

            if grid[neigh_row][neigh_col] and (neigh_row, neigh_col) != (row, col):
                neighbors_on += 1

    return neighbors_on


def _simulate_step_part1(grid: npt.NDArray[np.ubyte]) -> npt.NDArray[np.ubyte]:
    "Create a new grid and fill each position according to the neighbors of its predecessor"
    new_grid = np.zeros(grid.shape, dtype=np.ubyte)

    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            neighbors_on = _count_neighbors(grid, row_idx, col_idx)
            if val == 1 and neighbors_on in (2, 3):
                new_grid[row_idx][col_idx] = 1

            elif val == 0 and neighbors_on == 3:
                new_grid[row_idx][col_idx] = 1

    return new_grid


def _simulate_step_part2(grid: npt.NDArray[np.ubyte]) -> npt.NDArray[np.ubyte]:
    "Same as _simlate_step_part1 except that the corners are always on"
    new_grid = np.zeros(grid.shape, dtype=np.ubyte)
    corners = (
        (0, 0),
        (0, grid.shape[0] - 1),
        (grid.shape[0] - 1, 0),
        (grid.shape[0] - 1, grid.shape[0] - 1),
    )

    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            if (row_idx, col_idx) not in corners:
                neighbors_on = _count_neighbors(grid, row_idx, col_idx)
                if val == 1 and neighbors_on in (2, 3):
                    new_grid[row_idx][col_idx] = 1

                elif val == 0 and neighbors_on == 3:
                    new_grid[row_idx][col_idx] = 1
            else:
                new_grid[row_idx][col_idx] = 1

    return new_grid


def part1(instructions: list[str], grid_dims: int, sim_length: int) -> int:
    "Return the number of lights turned on after simulating the grid for the given simulation legnth"
    grid = _create_grid(instructions, grid_dims)

    for _ in range(sim_length):
        grid = _simulate_step_part1(grid)

    return grid.sum()


def part2(instructions: list[str], grid_dims: int, sim_length: int) -> int:
    "Same as part 1 except that the four corners must always stay on"
    grid = _create_grid(instructions, grid_dims)
    grid[0][0] = 1
    grid[0][grid_dims - 1] = 1
    grid[grid_dims - 1][0] = 1
    grid[grid_dims - 1][grid_dims - 1] = 1

    for _ in range(sim_length):
        grid = _simulate_step_part2(grid)

    return grid.sum()


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_18/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions, 100, 100)}")
    print(f"Part 2: {part2(instructions, 100, 100)}")
