import matplotlib.pyplot as plt
import numpy as np
import os


class GameOfLife_GridDraw():
    def __init__(self, state, grid_color='dimgrey'):
        self.current_state = state
        self.grid_color = grid_color
        self.DrawSquareGrid()

    def DrawSquareGrid(self):
        state = self.current_state.copy()
        state.reverse()

        plt.clf()

        plt.xticks(np.arange(0, len(state) + 1, 1))
        plt.yticks(np.arange(0, len(state) + 1, 1))
        plt.xlim(0, len(state))
        plt.ylim(0, len(state))

        blacks = []
        whites = []

        for i in range(len(state)):
            for j in range(len(state[i])):
                x = np.arange(j, j + 1, 0.02)
                y = np.arange(i, i + 1, 0.02)
                for tx in x:
                    for ty in y:
                        if state[i][j] == 1:
                            blacks.append([tx, ty])
                        else:
                            whites.append([tx, ty])
        blacks = np.array(blacks)
        whites = np.array(whites)
        plt.get_current_fig_manager().canvas.set_window_title('Game of Life')
        if len(blacks) > 0:
            plt.scatter(blacks[:, 0], blacks[:, 1], color='black', marker='s', s=12)
        if len(whites) > 0:
            plt.scatter(whites[:, 0], whites[:, 1], color='white', marker='s', s=12)
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        plt.grid(color=self.grid_color)
        plt.show(block=False)
        plt.pause(1)
        return


def valid_index(i, j, n):
    return bool(i>=0 and i<n and j>=0 and j<n)
def alive_neighbours(state, i, j, n):
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1]
    alive_count = 0
    for it in range(len(dx)):
        alive_count += int(valid_index(i + dx[it], j + dy[it], n) and state[i + dx[it]][j + dy[it]]==1)
    return alive_count

def AliveOrDead(alive,no_of_alive_neighbours):
    if alive:
        if no_of_alive_neighbours in [2,3]:
            return True
        else:
            return False
    else:
        if no_of_alive_neighbours == 3:
            return True
        else:
            return False

def next_generation(state, n):
    next_state = []
    for i in range(n):
        next_state.append([])
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            next_state[i].append(int(AliveOrDead(bool(state[i][j]),alive_neighbours(state,i,j,n))))
    return next_state

def print_generation(state,generation_count):
    os.system('cls')
    print(f'Generation {generation_count}: ')
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end=' ')
        print()
    GameOfLife_GridDraw(state)
    return

def Conway_s_Game_of_Life(state, no_of_generation):
    for i in range(no_of_generation):
        print_generation(state,i+1)
        state = next_generation(state,len(state))
    return

state = [
         [0,0,0,0,0],
         [0,0,1,1,1],
         [0,1,1,1,0],
         [0,0,0,0,0],
         [0,0,0,0,0]
]

Conway_s_Game_of_Life(state, no_of_generation=10)