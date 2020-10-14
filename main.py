#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    path = ''
    # print all the moves here
    bot_row = 0
    bot_column = 0
    princess_row = 0
    princess_column = 0

    # know the coordinates of the bot and the princess
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'p':
                princess_row = i
                princess_column = j

            elif grid[i][j] == 'm':
                bot_row = i
                bot_column = j

    vertical_difference = princess_row - bot_row
    horizontal_difference = princess_column - bot_column

    if vertical_difference != 0:
        vertical_direction = 'UP'

        if vertical_difference > 0:
            vertical_direction = 'DOWN'

        path += '{}\n'.format(vertical_direction) * abs(vertical_difference)

    if horizontal_difference != 0:
        horizontal_direction = 'LEFT'

        if horizontal_difference > 0:
            horizontal_direction = 'RIGHT'

        path += '{}\n'.format(horizontal_direction) * abs(horizontal_difference)

    print(path)


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
