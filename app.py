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
PUZZLE_1 = [0,0,0,2,6,0,7,0,1,6,8,0,0,7,0,0,9,0,1,9,0,0,0,4,5,0,0,8,2,0,1,0,0,0,4,0,0,0,4,6,0,2,9,0,0,0,5,0,0,0,3,0,2,8,0,0,9,3,0,0,0,7,4,0,4,0,0,5,0,0,3,6,7,0,3,0,1,8,0,0,0]#EASY
PUZZLE_2 = [8,0,1,2,9,6,0,0,0,3,0,0,0,8,1,7,0,6,2,0,0,0,0,0,0,9,0,1,0,2,0,6,5,4,7,9,0,0,0,1,0,9,0,3,0,5,9,0,3,0,0,0,6,2,4,0,0,0,0,0,0,1,3,9,1,0,0,0,0,6,8,7,0,8,0,0,0,7,0,5,0]#EASY
PUZZLE_3 = [0,0,0,8,1,0,0,0,2,3,1,2,4,6,0,7,8,0,7,0,4,9,3,0,6,5,1,1,9,0,0,0,4,0,6,0,0,0,0,0,7,0,0,0,5,8,0,7,0,2,6,0,0,0,0,0,9,0,0,1,0,0,0,0,0,0,0,4,0,9,7,0,2,7,0,0,0,0,5,0,4]#MEDIUM
PUZZLE_4 = [2,0,0,0,0,0,3,0,0,0,7,4,6,8,0,0,0,0,0,0,0,2,0,7,0,0,8,0,0,0,0,6,0,0,0,7,0,2,3,0,0,9,8,0,0,7,0,1,0,0,0,9,0,4,8,0,7,9,3,6,0,2,5,0,0,0,0,4,0,0,1,3,4,3,5,7,0,1,0,8,9]#MEDIUM
PUZZLE_5 = [5,0,9,0,0,0,0,8,0,0,0,0,0,0,0,0,0,4,6,7,0,9,0,0,0,0,3,1,5,0,0,3,0,0,4,9,0,9,0,7,4,0,0,0,0,0,0,0,0,0,0,3,0,0,4,0,5,3,7,0,2,0,0,7,6,0,0,0,9,0,1,8,0,0,8,5,0,1,0,0,0]#HARD
PUZZLE_6 = [0,0,3,9,0,6,7,0,1,1,6,0,5,0,0,0,0,0,0,5,0,1,0,0,0,9,0,0,4,0,3,0,1,0,0,6,2,0,0,0,0,9,0,3,0,0,0,0,0,0,7,0,0,5,0,8,7,0,0,0,0,0,4,0,0,2,0,0,0,3,6,0,5,0,6,0,0,0,8,0,9]#HARD
PUZZLE_7 = [7,5,0,2,0,0,0,0,0,0,1,0,0,9,6,0,0,4,4,0,0,0,5,0,0,0,3,0,0,0,0,3,0,0,0,5,0,0,7,0,4,0,0,3,0,5,0,1,0,0,2,9,0,0,9,0,0,0,0,0,3,8,7,0,0,0,0,6,0,0,0,0,0,0,4,0,0,8,5,1,0]#EXPERT
PUZZLE_8 = [6,1,3,0,4,0,0,0,0,0,5,0,8,0,1,0,0,0,9,0,0,0,7,0,5,0,0,0,2,0,0,0,3,0,0,0,5,6,1,0,2,0,0,0,4,3,0,8,0,0,0,0,0,0,8,3,2,0,5,0,4,9,0,0,4,5,3,0,0,0,1,0,0,0,0,0,0,4,0,0,0]#EXPERT
PUZZLE_9 = [4,0,3,0,0,0,8,0,0,0,0,0,0,9,0,7,0,0,0,0,6,8,0,7,0,0,0,5,0,0,0,7,0,9,0,0,0,0,2,9,0,1,0,0,0,0,0,0,0,0,8,0,5,0,0,0,0,1,2,0,4,7,9,0,3,4,0,0,0,1,0,2,2,0,0,0,0,6,0,0,8]#MASTER







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
    
    def set_value(self, value):
        self.value = value
        for i in range(9):
            self.potential_values[i]=False

    
class Board:
    def __init__(self):
        self.grid = [[Cell(row, col, self) for col in range(COLS)] for row in range(ROWS)] 

    def row(self, number):
        row=[self.grid[number][0],self.grid[number][1],self.grid[number][2],self.grid[number][3],self.grid[number][4],self.grid[number][5],self.grid[number][6],self.grid[number][7],self.grid[number][8]]
        return row
    
    def column(self, number):
        row=[self.grid[0][number],self.grid[1][number],self.grid[2][number],self.grid[3][number],self.grid[4][number],self.grid[5][number],self.grid[6][number],self.grid[7][number],self.grid[8][number]]
        return row
    
    def box(self, number):
        box=[]
        a = number//3
        b = number%3
        for i in range(a*3,3+(a*3)):
            for j in range(b*3,3+(b*3)):
                box.append(self.grid[i][j])
        return box
    
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
            remove_from_group(board.row(i),board.grid[i][j])
    for i in range(9):
        for j in range(9):
            remove_from_group(board.column(j),board.grid[i][j])
    for y in range(9):
        for x in range(9):
            if(x<=2 and y<=2):
                remove_from_group(board.box(0),board.grid[y][x])
            if(x>=3 and x<=5 and y<=2):
                remove_from_group(board.box(1),board.grid[y][x])
            if(x>=6 and y<=2):
                remove_from_group(board.box(2),board.grid[y][x])
            if(x<=2 and y>=3 and y<=5):
                remove_from_group(board.box(3),board.grid[y][x])
            if(x>=3 and x<=5 and y>=3 and y<=5):
                remove_from_group(board.box(4),board.grid[y][x])
            if(x>=6 and y>=3 and y<=5):
                remove_from_group(board.box(5),board.grid[y][x])
            if(x<=2 and y>=6):
                remove_from_group(board.box(6),board.grid[y][x])
            if(x>=3 and x<=5 and y>=6 and y<=8):
                remove_from_group(board.box(7),board.grid[y][x])
            if(x>=6 and y>=6):
                remove_from_group(board.box(8),board.grid[y][x])
    for i in range(9):
        for j in range(9):
            if(onePotential(board.grid[i][j])):
                return
    for i in range(9):
        if(only_potential_in_group(board.box(i))):
            return
        if(only_potential_in_group(board.row(i))):
            return
        if(only_potential_in_group(board.column(i))):
            return
        if(only_pair_in_group(board.box(i))):
            return
        if(only_pair_in_group(board.row(i))):
            return
        if(only_pair_in_group(board.column(i))):
            return
        if(only_cells_cointaining_pair(board.column(i))):
            return
        if(only_cells_cointaining_pair(board.row(i))):
            return
        if(only_cells_cointaining_pair(board.box(i))):
            return
    print("end")


def onePotential(cell):
    if cell.potential_numbers_count() == 1:
        for i in range(9):
            if(cell.potential_values[i]):
                cell.set_value(i+1)
                return True
    return False

def remove_from_group(group,cell):
    for c in group:
        if c is not cell:
            if c.value != 0:
                cell.potential_values[c.value-1] = False

def only_potential_in_group(group):
    for i in range(9):
        list=[]
        for c in group:
            if(c.potential_values[i]):
                list.append(c)
        if(len(list)==1):
            list[0].set_value(i+1)
            return True
    return False

def only_pair_in_group(group):# When two cells in a group have a pair of two values like(2,6) then remove those potentials from the rest of the cells
    for c in group:
        if(c.potential_numbers_count()==2):
            list = []
            for c2 in group:
                if compare_list(c.potential_values, c2.potential_values):
                    list.append(c2)
            if len(list)==2:
                for c3 in group:
                    if c3 is not list[0] and c3 is not list[1]:
                        for i in range(9):
                            if(list[0].potential_values[i] and c3.potential_values[i]):
                                c3.potential_values[i] = False
                                return True
    return False

def only_cells_cointaining_pair(group):
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            list = []
            for c in group:
                if c.potential_values[i] or c.potential_values[j]:
                    list.append(c)
            if(len(list)==2):
                if list[0].potential_values[i] and list[0].potential_values[j] and list[1].potential_values[i] and list[1].potential_values[j]:
                    if(list[0].potential_numbers_count() != 2 or list[1].potential_numbers_count() != 2):
                        for x in range(9):
                            list[0].potential_values[x] = False
                            list[1].potential_values[x] = False
                        list[0].potential_values[i] = True
                        list[0].potential_values[j] = True
                        list[1].potential_values[i] = True
                        list[1].potential_values[j] = True
                        return True
                
    return False


def compare_list(l1,l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if(l1[i]!=l2[i]):
            return False
    return True





board = Board()
chosen_cell=board.grid[0][0]

for i in range(9):
    for j in range(9):
        board.grid[i][j].value = 0

board.setup(PUZZLE_8)

for i in range(9):
    for j in range(9):
        if(board.grid[i][j].value != 0):
            board.grid[i][j].potential_values = [False,False,False,False,False,False,False,False,False]

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
            print(chosen_cell.potential_values)

        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_1):
                chosen_cell.value = 1
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_2):
                chosen_cell.value = 2
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_3):
                chosen_cell.value = 3
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_4):
                chosen_cell.value = 4
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_5):
                chosen_cell.value = 5
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_6):
                chosen_cell.value = 6
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_7):
                chosen_cell.value = 7
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_8):
                chosen_cell.value = 8
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key == pygame.K_9):
                chosen_cell.value = 9
                chosen_cell.potential_values = [False,False,False,False,False,False,False,False,False]
            if(event.key==pygame.K_SPACE):
                solve(board)

                
            

    draw_grid()

    # Draw all cells
    for row in board.grid:
        for cell in row:
            cell.draw(screen)

    pygame.display.flip()
