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
            #Empty square
            if grid.grid[i][j] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (j * square_width, i * square_height, square_width, square_height), 1)
            #Wall
            elif grid.grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (j * square_width, i * square_height, square_width, square_height))
            #Seen square
            elif grid.grid[i][j] == 2:
                pygame.draw.rect(screen, (0, 0, 255), (j * square_width, i * square_height, square_width, square_height))
            #Start square
            elif grid.grid[i][j] == 6:
                pygame.draw.rect(screen, (0, 255, 0), (j * square_width, i * square_height, square_width, square_height))
            #End Square
            elif grid.grid[i][j] == 9:
                pygame.draw.rect(screen, (255, 0, 0), (j * square_width, i * square_height, square_width, square_height))
            #Shortest path
            elif grid.grid[i][j] == 3:
                pygame.draw.rect(screen, (255, 0, 255), (j * square_width, i * square_height, square_width, square_height))


while running:
    
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
                        
        row = mouse_pos[1] // square_height
        col = mouse_pos[0] // square_width
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #Setting drag mode to either select or deselect depending on starting square
                mode = grid.grid[row][col]
                print(f"Row: {row}, Col: {col}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                grid.clear_grid()
            elif event.key == pygame.K_s:
                grid.place_start(row, col)
            elif event.key == pygame.K_f:
                grid.place_finish(row, col)
            elif event.key == pygame.K_b:
                grid.bfs()
                
    #Dragging to select or deselect squares
    mouse_buttons = pygame.mouse.get_pressed()            
                
    if mouse_buttons[0]:
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // square_height
        col = mouse_pos[0] // square_width

        if mode == 0:
            grid.select_cell(row, col)   
        elif mode == 1:
            grid.deselect_cell(row, col)          

    #DRAW
    screen.fill((255, 255, 255))
    draw_grid(grid)
    pygame.display.flip()

pygame.quit()
