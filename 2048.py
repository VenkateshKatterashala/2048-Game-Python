# the user interface and the total game is implemented here.
# from Tkinter import Frame, Label, CENTER

from tkinter import Frame, Label,CENTER

import Logics_2048
import constants_2048 as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_fun)
        self.commands = {c.KEY_UP: Logics_2048.move_up, c.KEY_DOWN: Logics_2048.move_down,
                         c.KEY_LEFT: Logics_2048.move_left, c.KEY_RIGHT: Logics_2048.move_right }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self,bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY, width=c.SIZE//c.GRID_LEN, height=c.SIZE//c.GRID_LEN)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                t = Label(master= cell,text= "",bg= c.BACKGROUND_COLOR_CELL_EMPTY, justify= CENTER, font= c.FONT,
                          width= 5, height= 2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = Logics_2048.start_game()
        Logics_2048.adding_2_randomly(self.matrix)
        Logics_2048.adding_2_randomly(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg= c.BACKGROUND_COLOR_DICT[int(new_number)],
                                                    fg= c.CELL_COLOR_DICT[int(new_number)])
        self.update_idletasks()

    def key_fun(self,event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                Logics_2048.adding_2_randomly(self.matrix)
                self.update_grid_cells()
                changed = False
                if Logics_2048.current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text="You", bg= c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if Logics_2048.current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text="You", bg= c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg= c.BACKGROUND_COLOR_CELL_EMPTY)




gamegrid = Game2048()













