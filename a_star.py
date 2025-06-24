import numpy as np
import heapq
class node:
    def __init__(self, pos,walkable=True,h=0):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.walkable = walkable
        self.g = 0  # Cost from start to this node
        self.h = h # Heuristic cost to end node
        self.f = 0  # Total cost (g + h)
        self.parent = None
        self.neighbors = [(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1)]
    def __lt__(self, other):
        return self.f < other.f
def init_grid(grid,end):
    ex,ey=end
    def heuristic(x, y):
        return abs(x - ex) + abs(y - ey)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                grid[i][j] = node([j,i],True,heuristic(j,i))
            else:
                grid[i][j] = node([j,i],False,heuristic(j,i))

    return grid
def a_star(grid, start, end):
   
    grid =init_grid(grid,end)
    
    open_set = []
    closed_set=[]
    open_set.append(grid[start[1]][start[0]])
    heapq.heapify(open_set)
    while open_set:
        
        current=heapq.heappop(open_set)
        closed_set.append(current)
        if current.pos==end:
            path=[]
            while current.pos!=start:
                path.append(current.pos)
                current=current.parent
            
            return path,closed_set
        for neigh in current.neighbors:
            if neigh[0]<0 or neigh[0]>=len(grid[0]) or neigh[1]<0 or neigh[1]>=len(grid):
                continue
            neigh=grid[neigh[1]][neigh[0]]
            
            if not neigh.walkable or neigh in closed_set:
               
                continue
            
            
            if neigh in open_set:
                if current.g+1<neigh.g:
                    neigh.parent=current
                    neigh.g=current.g+1
                    neigh.f=neigh.g+neigh.h 
            else:
                neigh.parent=current
                neigh.g=current.g+1
                neigh.f=neigh.g+neigh.h  
                heapq.heappush(open_set,neigh)
            
        #open_set.sort(key=lambda x: (x.f,x.h)) 
        
    return None,None

# Example usage:
if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 1, 1]
    ]
   
   
    start = (0, 0)  # (x, y)
    end = (4, 3)    # (x, y)
    path = a_star(grid, start, end)
    print("Path:", path)