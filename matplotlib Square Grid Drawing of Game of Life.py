# Author: Md. Tarek Hasan
import matplotlib.pyplot as plt
import numpy as np


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

        plt.scatter(blacks[:, 0], blacks[:, 1], color='black', marker='s', s=12)
        plt.scatter(whites[:, 0], whites[:, 1], color='white', marker='s', s=12)
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        plt.grid(color=self.grid_color)
        plt.show(block=False)
        return


if __name__ == "__main__":
    state = [
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 1],
    ]
    GameOfLife_GridDraw(state)
