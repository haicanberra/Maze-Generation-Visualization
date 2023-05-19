import pygame, random
from config import *
from cell import *

if __name__ == "__main__":
    pygame.init()

    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Generator")
    clock = pygame.time.Clock()

    grids = []
    x, y = X_DEFAULT, Y_DEFAULT
    for j in range(TOP_MARGIN+BOTTOM_MARGIN, HEIGHT//CELL_WIDTH):
        x = X_DEFAULT
        row = []
        for i in range(SIDE_MARGIN*2, WIDTH//CELL_WIDTH):
            row.append(Cell(x, y, CELL_WIDTH))
            x = x + CELL_WIDTH
        grids.append(row)
        y = y + CELL_WIDTH

    start_btn = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    end_btn = pygame.Rect(WIDTH-BUTTON_X-BUTTON_WIDTH+WALL_WIDTH, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    choose_start, choose_end = False, False

    font = pygame.font.Font("freesansbold.ttf", 15)
    start_text = font.render("Set Start", True, TEXT)
    start_text_rect = start_text.get_rect(center=start_btn.center)
    end_text = font.render("Set End", True, TEXT)
    end_text_rect = end_text.get_rect(center=end_btn.center)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_btn.collidepoint(event.pos):
                    print("start clicked!")
                    choose_start = True
                elif end_btn.collidepoint(event.pos):
                    print("endclicked!")
                    choose_end = True
                else:
                    for row in grids:
                        for cell in row:
                            if cell.is_clicked(event.pos):
                                if choose_start:
                                    cell.set_start()
                                    choose_start = False
                                elif choose_end:
                                    cell.set_end()
                                    choose_end = False

        clock.tick(FPS)
        canvas.fill(BACKGROUND)

        for row in grids:
            for cell in row:
                cell.draw(canvas)
        
        pygame.draw.rect(canvas, START, start_btn)
        pygame.draw.rect(canvas, END, end_btn)

        canvas.blit(start_text, start_text_rect)
        canvas.blit(end_text, end_text_rect)

        pygame.display.update()
    
    pygame.quit()
    quit()

