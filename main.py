import pygame
from grid import Grid

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.init()
running = True

grid = Grid(20, 20)
grid.make_grid()

square_width = screen_width // len(grid.grid[0])
square_height = screen_height // len(grid.grid)
mode = 0

def draw_grid(grid):
    
    for i, row in enumerate(grid.grid):
        for j, col in enumerate(row):
            if grid.grid[i][j] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (j * square_width, i * square_height, square_width, square_height), 1)
            elif grid.grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (j * square_width, i * square_height, square_width, square_height))
            


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                
                row = mouse_pos[1] // square_height + 1
                col = mouse_pos[0] // square_width + 1
                
                mode = grid.grid[row][col]
                

    mouse_buttons = pygame.mouse.get_pressed()            
                
    if mouse_buttons[0]:
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // square_height + 1
        col = mouse_pos[0] // square_width + 1

        if mode == 0:
            grid.select_cell(row - 1, col - 1)   
        elif mode == 1:
            grid.deselect_cell(row - 1, col - 1)          

    #DRAW
    screen.fill((255, 255, 255))
    draw_grid(grid)
    pygame.display.flip()

pygame.quit()
