"""
Игра "Жизнь"
https://neerc.ifmo.ru/wiki/index.php?title=%D0%98%D0%B3%D1%80%D0%B0_%C2%AB%D0%96%D0%B8%D0%B7%D0%BD%D1%8C%C2%BB
Двухмерный клеточный автомат
Правила игры:
- в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки,
  зарождается жизнь;
- если у живой клетки есть две или три живые соседки,
  то эта клетка продолжает жить;
- если соседей меньше двух или больше трёх, клетка умирает
"""
from kubiki.mc import mc, block
import time
class Game(object):

    def __init__(self, state, infinite_board = True):

        self.state = state
        self.width = state.width
        self.height = state.height
        self.infinite_board = infinite_board

    def step(self, count = 1):

        #for generation in range(count):

            new_board = [[False] * self.width for row in range(self.height)]

            for y, row in enumerate(self.state.board):
                for x, cell in enumerate(row):
                    neighbours = self.neighbours(x, y)
                    previous_state = self.state.board[y][x]
                    should_live = neighbours == 3 or (neighbours == 2 and previous_state == True)
                    new_board[y][x] = should_live

            self.state.board = new_board

    def neighbours(self, x, y):

        count = 0

        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if not hor == ver == 0 and (self.infinite_board == True or (0 <= x + hor < self.width and 0 <= y + ver < self.height)):
                    count += self.state.board[(y + ver) % self.height][(x + hor) % self.width]

        return count

    def display(self):
        return self.state.display()

class State(object):

    def __init__(self, positions, x, y, width, height):

        active_cells = []

        for y, row in enumerate(positions.splitlines()):
            for x, cell in enumerate(row.strip()):
                if cell == 'o':
                    active_cells.append((x,y))

        board = [[False] * width for row in range(height)]

        for cell in active_cells:
            board[cell[1] + y][cell[0] + x] = True

        self.board = board
        self.width = width
        self.height = height

    def display(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]:
                    mc.setBlock(x, y, 0, block.SAND)
                else:
                    mc.setBlock(x, y, 0, block.GRASS)


glider = """ oo.
             o.o
             o.. """

my_game = Game(State(glider, x = 2, y = 3, width = 20, height = 20))
my_game.display()
for i in range(50):
    my_game.step()
    my_game.display()
    time.sleep(0.05)
