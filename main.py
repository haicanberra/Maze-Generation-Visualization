import pygame, random
from config import *
from cell import *
from grid import *
from maze import *
from pathfind import *


if __name__ == "__main__":
    pygame.init()

    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Generator")
    clock = pygame.time.Clock()

    grid = Grid()
    grid.create()
    grid = Maze(grid).generate()

    start_btn = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    end_btn = pygame.Rect(BUTTON_X+BUTTON_WIDTH, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    choose_start, choose_end = False, False
    
    find_btn = pygame.Rect(BUTTON_X+2*BUTTON_WIDTH,BUTTON_Y,BUTTON_WIDTH, BUTTON_HEIGHT)
    gen_btn = pygame.Rect(BUTTON_X+3*BUTTON_WIDTH,BUTTON_Y,BUTTON_WIDTH, BUTTON_HEIGHT)
    clear_btn = pygame.Rect(BUTTON_X+4*BUTTON_WIDTH,BUTTON_Y,BUTTON_WIDTH, BUTTON_HEIGHT)

    dij_btn = pygame.Rect(ALGO_X, ALGO_Y, ALGO_WIDTH, ALGO_HEIGHT)
    astar_btn = pygame.Rect(ALGO_X-ALGO_WIDTH, ALGO_Y, ALGO_WIDTH, ALGO_HEIGHT)
    bfs_btn = pygame.Rect(ALGO_X-2*ALGO_WIDTH, ALGO_Y, ALGO_WIDTH, ALGO_HEIGHT)
    dfs_btn = pygame.Rect(ALGO_X-3*ALGO_WIDTH, ALGO_Y, ALGO_WIDTH, ALGO_HEIGHT)

    font = pygame.font.Font("freesansbold.ttf", 15)
    start_text = font.render("Start", True, TEXT)
    start_text_rect = start_text.get_rect(center=start_btn.center)
    end_text = font.render("End", True, TEXT)
    end_text_rect = end_text.get_rect(center=end_btn.center)
    gen_text = font.render("Regen", True, TEXT)
    gen_text_rect = gen_text.get_rect(center=gen_btn.center)
    find_text = font.render("Find", True, TEXT)
    find_text_rect = find_text.get_rect(center=find_btn.center)
    clear_text = font.render("Clear", True, TEXT)
    clear_text_rect = clear_text.get_rect(center=clear_btn.center)

    dij_text = font.render("DIJK", True, TEXT)
    dij_text_rect = dij_text.get_rect(center=dij_btn.center)
    astar_text = font.render("A*", True, TEXT)
    astar_text_rect = astar_text.get_rect(center=astar_btn.center)
    bfs_text = font.render("BFS", True, TEXT)
    bfs_text_rect = bfs_text.get_rect(center=bfs_btn.center)
    dfs_text = font.render("DFS", True, TEXT)
    dfs_text_rect = dfs_text.get_rect(center=dfs_btn.center)

    running = True
    one_start = False
    one_end = False
    algorithm = ALGORITHMS[0]
    algo_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2,BUTTON_Y-BUTTON_HEIGHT,BUTTON_WIDTH, BUTTON_HEIGHT)
    algo_text = font.render("Dijk", True, TEXT)
    algo_text_rect = algo_text.get_rect(center=algo_rect.center)

    start_pos, end_pos = None, None
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_btn.collidepoint(event.pos) and not one_start:
                    choose_start = True
                    one_start = True
                elif end_btn.collidepoint(event.pos) and not one_end:
                    choose_end = True
                    one_end = True
                elif gen_btn.collidepoint(event.pos):
                    grid = Grid()
                    grid.create()
                    grid = Maze(grid).generate()
                    one_start = False
                    one_end = False
                elif clear_btn.collidepoint(event.pos):
                    grid.clear()
                    one_start = False
                    one_end = False  
                elif find_btn.collidepoint(event.pos):
                    if one_start and one_end:
                        if not pathfind(algorithm, grid, start_pos, end_pos):
                            print("No path found!")
                            running = False
                elif dij_btn.collidepoint(event.pos):
                    algorithm = ALGORITHMS[0]
                elif astar_btn.collidepoint(event.pos):
                    algorithm = ALGORITHMS[1]
                elif bfs_btn.collidepoint(event.pos):
                    algorithm = ALGORITHMS[2]
                elif dfs_btn.collidepoint(event.pos):
                    algorithm = ALGORITHMS[3]
                else:
                    choose_start, choose_end = grid.cell_clicked(event, choose_start, choose_end)
                    start_pos = grid.get_start()
                    end_pos = grid.get_end()
                    
        clock.tick(FPS)
        canvas.fill(BACKGROUND)

        grid.draw(canvas)
        algo_string = get_algo_string(algorithm)
        algo_text = font.render(algo_string, True, TEXT)
        
        pygame.draw.rect(canvas, START, start_btn)
        pygame.draw.rect(canvas, END, end_btn)
        pygame.draw.rect(canvas, GENERATE, gen_btn)
        pygame.draw.rect(canvas, FIND, find_btn)
        pygame.draw.rect(canvas, CLEAR, clear_btn)

        pygame.draw.rect(canvas, DIJ, dij_btn)
        pygame.draw.rect(canvas, ASTAR, astar_btn)
        pygame.draw.rect(canvas, BFS, bfs_btn)
        pygame.draw.rect(canvas, DFS, dfs_btn)

        pygame.draw.rect(canvas, ALGO, algo_rect)

        canvas.blit(start_text, start_text_rect)
        canvas.blit(end_text, end_text_rect)
        canvas.blit(gen_text, gen_text_rect)
        canvas.blit(find_text, find_text_rect)
        canvas.blit(clear_text, clear_text_rect)
        
        canvas.blit(dij_text, dij_text_rect)
        canvas.blit(astar_text, astar_text_rect)
        canvas.blit(bfs_text, bfs_text_rect)
        canvas.blit(dfs_text, dfs_text_rect)

        canvas.blit(algo_text, algo_text_rect)

        pygame.display.update()
    
    pygame.quit()
    quit()

