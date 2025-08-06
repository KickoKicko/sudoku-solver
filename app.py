import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
ROWS, COLS = 9, 9
CELL_SIZE = WIDTH // COLS
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
NUM_COLOR = (50, 50, 50)
BIG_FONT = pygame.font.SysFont("arial", 40)
SMALL_FONT = pygame.font.SysFont("arial", 18)
PUZZLE_1 = [0,0,0,2,6,0,7,0,1,6,8,0,0,7,0,0,9,0,1,9,0,0,0,4,5,0,0,8,2,0,1,0,0,0,4,0,0,0,4,6,0,2,9,0,0,0,5,0,0,0,3,0,2,8,0,0,9,3,0,0,0,7,4,0,4,0,0,5,0,0,3,6,7,0,3,0,1,8,0,0,0]


# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


class Cell:
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.value = 0
        self.selected = False
        self.potential_values=[True,True,True,True,True,True,True,True,True]
        self.board=board

    def draw(self, screen):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        # Draw value
        if self.value != 0:
            text = BIG_FONT.render(str(self.value), True, NUM_COLOR)
            screen.blit(text, (x + CELL_SIZE // 3, y + CELL_SIZE // 6))
        else:
            if(self.potential_values[0]):
                text = SMALL_FONT.render("1", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)-15, (y + CELL_SIZE // 6)-8))
            if(self.potential_values[1]):
                text = SMALL_FONT.render("2", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+5, (y + CELL_SIZE // 6)-8))
            if(self.potential_values[2]):
                text = SMALL_FONT.render("3", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+25, (y + CELL_SIZE // 6)-8))
            if(self.potential_values[3]):
                text = SMALL_FONT.render("4", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)-15, (y + CELL_SIZE // 6)+10))
            if(self.potential_values[4]):
                text = SMALL_FONT.render("5", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+5, (y + CELL_SIZE // 6)+10))
            if(self.potential_values[5]):
                text = SMALL_FONT.render("6", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+25, (y + CELL_SIZE // 6)+10))
            if(self.potential_values[6]):
                text = SMALL_FONT.render("7", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)-15, (y + CELL_SIZE // 6)+30))
            if(self.potential_values[7]):
                text = SMALL_FONT.render("8", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+5, (y + CELL_SIZE // 6)+30))
            if(self.potential_values[8]):
                text = SMALL_FONT.render("9", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+25, (y + CELL_SIZE // 6)+30))

        # Draw selection
        if self.selected:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, CELL_SIZE, CELL_SIZE), 3)
    
    def potential_numbers_count(self):
        count = 0
        for pn in self.potential_values:
            if pn:
                count+=1
        return count
    
class Board:
    def __init__(self):
        self.grid = [[Cell(row, col, self) for col in range(COLS)] for row in range(ROWS)] 

    def row(self, number):
        row=[self.grid[number][0],self.grid[number][1],self.grid[number][2],self.grid[number][3],self.grid[number][4],self.grid[number][5],self.grid[number][6],self.grid[number][7],self.grid[number][8]]
        return row
    
    def column(self, number):
        row=[self.grid[0][number],self.grid[1][number],self.grid[2][number],self.grid[3][number],self.grid[4][number],self.grid[5][number],self.grid[6][number],self.grid[7][number],self.grid[8][number]]
        return row
    
    def setup(self, list):
        for i in range(9):
            for j in range(9):
                self.grid[i][j].value = list[i*9+j]


def draw_grid():
    screen.fill(BG_COLOR)

    # Draw thin and thick lines
    for i in range(ROWS + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)

def solve(board):
    for i in range(9):
        for j in range(9):
            onePotential(board.grid[i][j])
    for i in range(9):
        for j in range(9):
            remove_from_row(board.row(i),board.grid[i][j])
    for i in range(9):
        for j in range(9):
            remove_from_column(board.column(j),board.grid[i][j])


def onePotential(cell):
    if cell.potential_numbers_count() == 1:
        for i in range(9):
            if(cell.potential_values[i]):
                cell.value = i+1
                #cell.potential_values=[False,False,False,False,False,False,False,False,False]
                #print("yippie")

def remove_from_row(row,cell):
    for c in row:
        if c is not cell:
            if c.value != 0:
                cell.potential_values[c.value-1] = False
def remove_from_column(col,cell):
    for c in col:
        if c is not cell:
            if c.value != 0:
                cell.potential_values[c.value-1] = False



# Create 9x9 grid of Cell objects
board = Board()
#print(board.grid[0][0].value)
board.setup(PUZZLE_1)
#print(board.grid[0][0].value)
chosen_cell=board.grid[0][0]

for i in range(9):
    for j in range(9):
        board.grid[i][j].value = 0

board.setup(PUZZLE_1)

#board.grid[2][4].potential_values=[False,False,False,True,False,False,False,False,False]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_value = mouse_x//60
            y_value = mouse_y//60
            chosen_cell.selected = False
            chosen_cell = board.grid[y_value][x_value]
            chosen_cell.selected = True
            #print(chosen_cell.value)
            #print(chosen_cell.potential_values)

        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_1):
                chosen_cell.value = 1
            if(event.key == pygame.K_2):
                chosen_cell.value = 2
            if(event.key == pygame.K_3):
                chosen_cell.value = 3
            if(event.key == pygame.K_4):
                chosen_cell.value = 4
            if(event.key == pygame.K_5):
                chosen_cell.value = 5
            if(event.key == pygame.K_6):
                chosen_cell.value = 6
            if(event.key == pygame.K_7):
                chosen_cell.value = 7
            if(event.key == pygame.K_8):
                chosen_cell.value = 8
            if(event.key == pygame.K_9):
                chosen_cell.value = 9
            if(event.key==pygame.K_SPACE):
                solve(board)

                
            

    draw_grid()

    # Draw all cells
    for row in board.grid:
        for cell in row:
            cell.draw(screen)

    pygame.display.flip()
