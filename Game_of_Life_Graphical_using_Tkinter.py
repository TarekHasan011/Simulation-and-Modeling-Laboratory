import os
import threading
import time
from tkinter import *


class Game_of_Life():
    def __init__(self, state):
        self.state = state
        self.n = len(state)

    def valid_index(self, i, j):
        return bool(i >= 0 and i < self.n and j >= 0 and j < self.n)

    def alive_neighbours(self, i, j):
        dx = [1, -1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, 1, -1, -1, -1, 1, 1]
        alive_count = 0
        for it in range(len(dx)):
            alive_count += int(self.valid_index(i + dx[it], j + dy[it]) and self.state[i + dx[it]][j + dy[it]] == 1)
        return alive_count

    def AliveOrDead(self, alive, no_of_alive_neighbours):
        if alive:
            if no_of_alive_neighbours in [2, 3]:
                return True
            else:
                return False
        else:
            if no_of_alive_neighbours == 3:
                return True
            else:
                return False

    def next_generation(self):
        next_state = []
        for i in range(self.n):
            next_state.append([])

        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                next_state[i].append(int(self.AliveOrDead(bool(self.state[i][j]), self.alive_neighbours(i, j))))
        self.state = next_state
        return

    def draw(self):
        generation = 1
        while True:
            os.system('cls')
            print(f'Generation {generation}')
            for i in range(len(self.state)):
                for j in range(len(self.state[i])):
                    print(self.state[i][j], end=' ')
                print()

            for i in range(len(self.state)):
                for j in range(len(self.state[i])):
                    if self.state[i][j] == 1:
                        buttons[i][j].configure(bg='black')
                    else:
                        buttons[i][j].configure(bg='white')
            self.next_generation()
            generation += 1
            time.sleep(0.4)



state = [
         [0,0,0,0,0],
         [0,0,1,1,1],
         [0,1,1,1,0],
         [0,0,0,0,0],
         [0,0,0,0,0]
]

root = Tk()
root.geometry(f"{len(state)*66}x{len(state)*71}")
root.title('Conway\'s Game of Life')
game_of_life = Game_of_Life(state)

buttons = []
for i in range(game_of_life.n):
    temp = []
    for j in range(game_of_life.n):
        temp_button = Button(text='', width=8, height=4)
        temp_button.grid(row=i, column=j)
        temp.append(temp_button)
    buttons.append(temp)

drawing = threading.Thread(target=game_of_life.draw)
drawing.daemon = True
drawing.start()
root.mainloop()
