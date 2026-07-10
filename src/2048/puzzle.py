"""Tkinter GUI for the 2048 game.

Students implement the game logic in logic.py; this module provides the
graphical interface. Run with: python3 puzzle.py
Controls: WASD or the arrow keys.
"""

import tkinter as tk

from logic import add_two, down, game_state, left, new_game, right, up

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {
    2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
    32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
    512: "#edc850", 1024: "#edc53f", 2048: "#edc22e",
}
CELL_COLOR_DICT = {
    2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
    32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
    512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2",
}
FONT = ("Verdana", 40, "bold")

# Maps a key symbol (event.keysym) to the logic function it triggers.
COMMANDS = {
    "w": up, "s": down, "a": left, "d": right,
    "Up": up, "Down": down, "Left": left, "Right": right,
}


class GameGrid(tk.Frame):
    def __init__(self):
        super().__init__()

        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>", self.key_down)

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

    def init_grid(self):
        background = tk.Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = tk.Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY,
                                width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = tk.Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY,
                             justify=tk.CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = new_game(GRID_LEN)
        self.matrix = add_two(self.matrix)
        self.matrix = add_two(self.matrix)

    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),
                                                    bg=BACKGROUND_COLOR_DICT[new_number],
                                                    fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        command = COMMANDS.get(event.keysym)
        if command is None:
            return
        self.matrix, moved = command(self.matrix)
        if moved:
            self.matrix = add_two(self.matrix)
            self.update_grid_cells()
            state = game_state(self.matrix)
            if state == "win":
                self.show_message("You", "Win!")
            elif state == "lose":
                self.show_message("You", "Lose!")

    def show_message(self, first, second):
        self.grid_cells[1][1].configure(text=first, bg=BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[1][2].configure(text=second, bg=BACKGROUND_COLOR_CELL_EMPTY)


if __name__ == "__main__":
    GameGrid().mainloop()
