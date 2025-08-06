import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
ROWS, COLS = 9, 9
CELL_SIZE = WIDTH // COLS
LINE_COLOR = (0, 0, 0)
CHOSEN_LINE_COLOR = (1,1,1)
BG_COLOR = (255, 255, 255)
NUM_COLOR = (50, 50, 50)
BIG_FONT = pygame.font.SysFont("arial", 40)
SMALL_FONT = pygame.font.SysFont("arial", 18)


# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = 0
        self.selected = False
        self.potential_values=[True,True,True,True,True,True,True,True,True]

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
                text = SMALL_FONT.render("3", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)-15, (y + CELL_SIZE // 6)+10))
            if(self.potential_values[4]):
                text = SMALL_FONT.render("4", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+5, (y + CELL_SIZE // 6)+10))
            if(self.potential_values[5]):
                text = SMALL_FONT.render("5", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+25, (y + CELL_SIZE // 6)+10))
            if(self.potential_values[6]):
                text = SMALL_FONT.render("6", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)-15, (y + CELL_SIZE // 6)+30))
            if(self.potential_values[7]):
                text = SMALL_FONT.render("7", True, NUM_COLOR)
                screen.blit(text, ((x + CELL_SIZE// 3)+5, (y + CELL_SIZE // 6)+30))
            if(self.potential_values[8]):
                text = SMALL_FONT.render("8", True, NUM_COLOR)
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


def draw_grid():
    screen.fill(BG_COLOR)

    # Draw thin and thick lines
    for i in range(ROWS + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)

def solve(grid):
    for i in range(9):
        for j in range(9):
            onePotential(grid[i][j])


def onePotential(cell):
    if cell.potential_numbers_count() == 1:
        for i in range(9):
            if(cell.potential_values[i]):
                cell.value = i
                #cell.potential_values=[False,False,False,False,False,False,False,False,False]
                print("yippie")


# Create 9x9 grid of Cell objects
grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
chosen_cell=grid[0][0]
# Example: fill a few cells with dummy values
grid[0][0].value = 5
grid[1][3].value = 7
grid[4][4].value = 9

for i in range(9):
    for j in range(9):
        grid[i][j].value = 0

grid[2][4].potential_values=[False,False,False,True,False,False,False,False,False]

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
            chosen_cell = grid[y_value][x_value]
            chosen_cell.selected = True

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
                solve(grid)

                
            

    draw_grid()

    # Draw all cells
    for row in grid:
        for cell in row:
            cell.draw(screen)

    pygame.display.flip()
