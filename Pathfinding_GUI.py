import pygame
import numpy as np
import enum
import a_star
import time
import copy
import test
from stable_baselines3 import PPO

class pathfinding_mode(enum.Enum):
    A_STAR=0
    RL=1
class make(enum.Enum):
    obstace=1
    start=2
    end=3
class state(enum.Enum):
    selection=0
    instructions=1
    editing=2
    running=3
def make_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, WHITE, rect)
    pygame.display.flip()

def change_block(pos,color):
    global grid
    x, y = pos
    x = x - (x % GRID_SIZE)
    y = y - (y % GRID_SIZE)
    pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
    x //= GRID_SIZE
    y //= GRID_SIZE
    
    if color == BLACK:
        grid[y][x] = 0
    elif color == WHITE:
        grid[y][x] = 1
        
    
    pygame.display.flip()
    
def make_instruction():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)  
    instructions = [
        "Instructions:",
        "press 1 to make obstace",
        "press 2 to make starting point",
        "press 3 to make ending point",
        "press enter to start pathfinding",
        "press any key to continue",
    ]
    for i, line in enumerate(instructions):
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, 10 + i * 30))
    pygame.display.flip()
    
def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Checks if a key was pressed
                print(event.key)
                return event.key
            elif event.type == pygame.QUIT:  # Checks if the window is closed
                pygame.quit()
                exit()

def change_start(pos):
    global start_pos
    if start_pos is not None:
        x,y=start_pos
        x*= GRID_SIZE
        y*= GRID_SIZE
        change_block((x,y), WHITE)
    x, y = pos
    x = x - (x % GRID_SIZE)
    y = y - (y % GRID_SIZE)
    pygame.draw.rect(screen, GREEN, (x, y, GRID_SIZE, GRID_SIZE))
    x //= GRID_SIZE
    y //= GRID_SIZE
    grid[y][x] = 1
    start_pos = (x, y)
    pygame.display.flip()

def change_end(pos):
    global end_pos
    if end_pos is not None:
        x,y=end_pos
        x*= GRID_SIZE
        y*= GRID_SIZE
        change_block((x,y), WHITE)
    x, y = pos
    x = x - (x % GRID_SIZE)
    y = y - (y % GRID_SIZE)
    pygame.draw.rect(screen, RED, (x, y, GRID_SIZE, GRID_SIZE))
    x //= GRID_SIZE
    y //= GRID_SIZE
    grid[y][x] = 1
    end_pos = (x, y)
    pygame.display.flip()
def find_path():
    global current_path,pathfinding_started,grid,start_pos,end_pos,has_path,current_pos_inpath
    
    
    if play_mode==pathfinding_mode.A_STAR:
        if has_path:
            for i in current_path:
                
                if(grid[i[1]][i[0]]==1):
                    change_block(np.array(i)*GRID_SIZE,WHITE)
        print("start_pos",start_pos)
        print("end_pos",end_pos)
        pathfinding_started=True
        current_pos_inpath=0
        find_path_a_star()
    elif play_mode==pathfinding_mode.RL:
        pass

def RL_next_pos():
    global grid,start_pos,end_pos,model
    grid_copy=copy.deepcopy(grid)
    grid_copy[start_pos[1]][start_pos[0]]=2
    grid_copy[end_pos[1]][end_pos[0]]=3
    print(grid_copy)
    action=int(model.predict(grid_copy)[0])
    print(action)
    pos=[0,0]
    if action == 0:
        pos[0] = 1           
    elif action == 1: 
        pos[1] = 1
                
    elif action == 2: 
        pos[0] = -1

    elif action == 3:
        pos[1] = -1   
    print(start_pos,pos)        
    start_pos=[start_pos[0]+pos[0],start_pos[1]+pos[1]]
    print("new start pos",start_pos)    
    
   
def find_path_a_star():
    global current_path,pathfinding_started,grid,start_pos,end_pos,has_path,current_pos_inpath
    current_path,_=a_star.a_star(copy.deepcopy(grid) , list(start_pos), list(end_pos))
    current_path.reverse()
    has_path=current_path!=[]
    for i in current_path:
        change_block(np.array(i)*GRID_SIZE,GREEN)
    pathfinding_started=False
    
    
start_button_rect = None
rl_button_rect = None
def make_selection_panel():
    global start_button_rect, rl_button_rect, WIDTH, HEIGHT
    panel_width, panel_height = WIDTH, HEIGHT
    panel_surface = pygame.Surface((panel_width, panel_height))
    panel_surface.fill(GRAY)
    button_width, button_height = 150, 40
    start_button_rect = pygame.Rect(150, 150, button_width, button_height)
    rl_button_rect = pygame.Rect(150,250, button_width, button_height)
    pygame.draw.rect(panel_surface, WHITE, start_button_rect)
    pygame.draw.rect(panel_surface, WHITE, rl_button_rect)

    font = pygame.font.Font(None, 30)
    start_text = font.render("A_STAR", True, BLACK)
    rl_text = font.render("RL", True, BLACK)

    panel_surface.blit(start_text, (start_button_rect.x + 30, start_button_rect.y + 10))
    panel_surface.blit(rl_text, (rl_button_rect.x + 60, rl_button_rect.y + 10))
    return panel_surface

def select_a_star():
    global play_mode,grid,GRID_SIZE,GRID_HEIGHT,GRID_WIDTH
    play_mode=pathfinding_mode.A_STAR
    GRID_WIDTH = WIDTH // GRID_SIZE
    GRID_HEIGHT = HEIGHT // GRID_SIZE
    grid =np.ones((GRID_HEIGHT, GRID_WIDTH), dtype=np.uint8,).tolist()
    
    init_instruction_state()
    
def select_rl():
    global play_mode,GRID_SIZE,grid,GRID_HEIGHT,GRID_WIDTH
    GRID_SIZE=100
    play_mode=pathfinding_mode.RL
    GRID_WIDTH = WIDTH // GRID_SIZE
    GRID_HEIGHT = HEIGHT // GRID_SIZE
    grid =np.ones((GRID_HEIGHT, GRID_WIDTH), dtype=np.uint8,).tolist()
    init_instruction_state()
    
def init_instruction_state():
    global current_state
    current_state=state.instructions
    make_instruction()
    event = wait_for_key()
    make_grid()    
    current_state=state.editing

    
pygame.init()
grid=None
WIDTH = 500
HEIGHT = 500
GRID_SIZE = 25

GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

print("loading rl Model ...")
model=PPO.load("model/PPO-v0_final")
print("-----done-------")
# Define grid size

start_pos = None
end_pos = None
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualizer")
screen.fill(WHITE) 






pygame.display.flip()
running=True
pathfinding_started=False
makeMode=make.obstace
current_path=[]
clock=pygame.time.Clock()
current_pos_inpath=0
has_path=False
speed=1000000
frames=0
play_mode=None
play_mode_panel=make_selection_panel()
editing_grid=False
current_state=state.selection
screen.blit(play_mode_panel, (0, 0))
pygame.display.update()
while running:
    
    frames+=1
    for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(current_state==state.selection):
                    
                    if start_button_rect.collidepoint(event.pos[0] , event.pos[1] ):
                        select_a_star()
                    elif rl_button_rect.collidepoint(event.pos[0] , event.pos[1] ):
                        select_rl()
                elif current_state==state.instructions:
                    pass
                elif current_state==state.editing:
                    pass
                elif current_state==state.running:
                    pass
            elif event.type == pygame.KEYDOWN:
                if(current_state==state.editing):
                    if event.key == pygame.K_1:
                        makeMode=make.obstace
                    elif event.key == pygame.K_2:
                        makeMode=make.start
                    elif event.key == pygame.K_3:
                        makeMode=make.end
                    elif event.key == pygame.K_RETURN:
                        print("start pathfinding")
                        find_path()
                        current_state=state.running
                elif current_state==state.running:
                    if event.key == pygame.K_RETURN:
                        print("stop pathfinding")
                        current_state=state.editing

    if current_state==state.editing:
        buttons = pygame.mouse.get_pressed()

        # Check if the left mouse button is being held down
        if buttons[0]:
            if makeMode==make.obstace:
                change_block(pygame.mouse.get_pos(), BLACK)
            elif makeMode==make.start:
                change_start(pygame.mouse.get_pos())

            elif makeMode==make.end:
                change_end(pygame.mouse.get_pos())
        if buttons[2]:
            change_block(pygame.mouse.get_pos(), WHITE)
    elif current_state==state.running:
        if list(start_pos)== list(end_pos):
                running=False
        if play_mode==pathfinding_mode.A_STAR:
            if list(start_pos)== list(end_pos):
                running=False
            if(frames%speed==0 and current_pos_inpath<len(current_path) and has_path):
                change_block(np.array(current_path[current_pos_inpath])*GRID_SIZE,BLUE)
                current_pos_inpath+=1
                start_pos=current_path[current_pos_inpath-1]
        elif frames%speed==0:
            change_block(np.array(start_pos)*GRID_SIZE,WHITE)
            RL_next_pos()
            change_block(np.array(start_pos)*GRID_SIZE,BLUE)
            
            
            
    if False:
        
            
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    makeMode=make.obstace
                elif event.key == pygame.K_2:
                    makeMode=make.start
                elif event.key == pygame.K_3:
                    makeMode=make.end
                elif event.key == pygame.K_RETURN:
                    print("start pathfinding")
                    find_path_a_star()
            elif event.type == pygame.MOUSEBUTTONUP:
                if start_pos!=None and end_pos!=None:
                    find_path_a_star()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in current_path:
                    change_block(np.array(i)*GRID_SIZE,WHITE)
                    
        buttons = pygame.mouse.get_pressed()

        # Check if the left mouse button is being held down
        if buttons[0]:
            if makeMode==make.obstace:
                change_block(pygame.mouse.get_pos(), BLACK)
            elif makeMode==make.start:
                change_start(pygame.mouse.get_pos())

            elif makeMode==make.end:
                change_end(pygame.mouse.get_pos())
        if buttons[2]:
            change_block(pygame.mouse.get_pos(), WHITE)
    
        