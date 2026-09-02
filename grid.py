from collections import deque

class Grid:
    
    def __init__(self, rows, columns):
        
        self.rows = rows
        self.columns = columns

        self.grid = []

        self.start_square = ()
    
    def make_grid(self):
        
        for row in range(self.rows):
            self.grid.append([])
            for col in range(self.columns):
                self.grid[row].append(0)
        
    def print_cell(self, row, col):
        print(f"Row: {row}, Col: {col}")
    
    def select_cell(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = 1
    
    def deselect_cell(self, row, col):
        if self.grid[row][col] == 1:
            self.grid[row][col] = 0
    
    def clear_grid(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                self.grid[i][j] = 0


        print("Grid cleared")
    
    def place_start(self, row, col):

        if self.grid[row][col] == 6:
            self.grid[row][col] = 0

        elif not self.start_placed() and self.grid[row][col] == 0:
            self.grid[row][col] = 6
            self.start_square = (row, col)
    
    
    def place_finish(self, row, col):
        
        if self.grid[row][col] == 9:
            self.grid[row][col] = 0
  
        elif not self.finish_placed() and self.grid[row][col] == 0:
            self.grid[row][col] = 9

    
    def start_placed(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j] == 6:
                    return True
        
        return False

    def finish_placed(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j] == 9:
                    return True
        
        return False

    def get_neighbour_cells(self, row, col):
        
        neighbours = []
        
        #Up
        if 0 <= (row - 1) < self.rows:
            if self.grid[row - 1][col] != 1:
                neighbours.append((row - 1, col))
        #Down
        if 0 <= (row + 1) < self.rows:
            if self.grid[row + 1][col] != 1:
                neighbours.append((row + 1, col))
        #Left
        if 0 <= (col - 1) < self.columns:
            if self.grid[row][col - 1] != 1:
                neighbours.append((row, col - 1))
        #Right
        if 0 <= (col + 1) < self.columns:
            if self.grid[row][col + 1] != 1:
                neighbours.append((row, col + 1))      
        return neighbours
    
    def bfs(self):
        
        #Create a queue, current square, and seen squares
        queue = deque([])
        current_square = ()
        seen_squares = []
        
        #Store parent of every discovered square
        parents = {}
        
        #Add start square to queue and seen squares
        queue.append(self.start_square)
        seen_squares.append(self.start_square)
        
        #Continue loop while the queue is not empty yet
        while queue:
            #New current square is the first square in queue
            current_square = queue.popleft()
            
            #Check if square is finished square
            if self.grid[current_square[0]][current_square[1]] == 9:
                #print(f"{current_square} IS THE FINISH SQUARE")
                break
            else:
                #print(f"{current_square} is not the finish square")
                pass
            
            #If not finished square, add valid/unseen neighbours to queue 
            for square in self.get_neighbour_cells(current_square[0], current_square[1]):
                
                if square not in seen_squares:
                    parent_square = current_square
                    parents[square] = parent_square
                    queue.append(square)
                    seen_squares.append(square)
                    #Turn into seen square (test)
                    if self.grid[current_square[0]][current_square[1]] != 6:
                        self.grid[current_square[0]][current_square[1]] = 2
        
        #Create array of shortest path
        shortest_path = []
        s = current_square
        parents[self.start_square] = 0
        
        #Retrace steps from finish and add to shortest path
        while not parents[s] == 0:
            shortest_path.append(s)
            s = parents[s]
        shortest_path.append(self.start_square)
        print(shortest_path)
          
                
            
            
            
            
            