import os
import pygame
import random

WINDOW_SIZE = 500
GRID_SIZE = 8
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
BACKGROUND_COLOR = (30, 30, 30)
GRID_COLOR = (50, 50, 50)

BLOCK_COLORS = [
    (230, 182, 28),  # Orange
    (46, 204, 113),  # Green
    (141, 245, 66),  # Blue
    (155, 89, 182),  # Purple
    (241, 196, 15),  # Yellow
    (231, 76, 60),  # Red
    (26, 188, 156)  # Turquoise
]

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 250))
pygame.display.set_caption("1010! Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

BEST_SCORE_FILE = "best_score.txt"

def load_best_score():
    if os.path.exists(BEST_SCORE_FILE):
        with open(BEST_SCORE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

def save_best_score(best_score):
    with open(BEST_SCORE_FILE, "w") as file:
        file.write(str(best_score))

best_score = load_best_score()

board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

SHAPES = [
    #[[1]],  # Single block
    # [[1, 1]],  # Horizontal small
    # [[1], [1]],  # Vertical small
    [[1, 1], [1, 1]],  # Square
    [[1, 1, 1]],  # Horizontal line
    [[1], [1], [1]],  # Vertical line
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # Reversed L
    [[1, 0], [1, 0], [1, 1]],  # Vertical L
    [[0, 1], [0, 1], [1, 1]]  # Vertical reversed L
]

score = 0

def generate_block():
    shape = random.choice(SHAPES)
    color = random.choice(BLOCK_COLORS)
    return {"shape": shape, "color": color, "x": 0, "y": 0, "dragged": False}

def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE + 200, CELL_SIZE, CELL_SIZE)
            if board[row][col] == 0:
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)
            else:
                pygame.draw.rect(screen, board[row][col], rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)

def draw_block(block, offset=(0, 0), small=False):
    shape = block["shape"]
    color = block["color"]
    scale_factor = 0.6 if small else 1.0
    offset_x, offset_y = offset

    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                rect = pygame.Rect(
                    block["x"] + col * CELL_SIZE * scale_factor + offset_x,
                    block["y"] + row * CELL_SIZE * scale_factor + offset_y,
                    CELL_SIZE * scale_factor,
                    CELL_SIZE * scale_factor
                )
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)

def draw_preview_blocks(blocks):
    start_x = 50
    for i, block in enumerate(blocks):
        if not block["dragged"]:
            block["x"] = start_x + i * (CELL_SIZE * 5)
            block["y"] = 50
            draw_block(block, small=True)

def draw_restart_button():
    button_rect = pygame.Rect(WINDOW_SIZE //2 -50, 0, 100, 40)
    pygame.draw.rect(screen, (70, 70, 70), button_rect)
    pygame.draw.rect(screen, (255, 255, 255), button_rect, 2)
    text = font.render("Restart", True, (255, 255, 255))
    screen.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, 5))
    return button_rect

def can_place_block(block, grid_x, grid_y):
    shape = block["shape"]
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                if not (0 <= grid_x + col < GRID_SIZE and 0 <= grid_y + row < GRID_SIZE):
                    return False
                if board[grid_y + row][grid_x + col] != 0:
                    return False
    return True

def place_block(block, grid_x, grid_y):
    global score
    shape = block["shape"]
    block_cells = 0
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                board[grid_y + row][grid_x + col] = block["color"]
                block_cells += 1
    score += block_cells

def check_full_lines_and_columns():
    global score
    full_rows, full_cols = 0, 0

    for row in range(GRID_SIZE):
        if all(board[row][col] != 0 for col in range(GRID_SIZE)):
            for col in range(GRID_SIZE):
                board[row][col] = 0
            full_rows += 1

    for col in range(GRID_SIZE):
        if all(board[row][col] != 0 for row in range(GRID_SIZE)):
            for row in range(GRID_SIZE):
                board[row][col] = 0
            full_cols += 1

    score += (full_rows + full_cols) * 10

def draw_score():
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    best_score_text = font.render(f'Best Score: {best_score}', True, (255, 255, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(best_score_text, (WINDOW_SIZE- WINDOW_SIZE/3 -20, 10))

def restart_game():
    global board, score, blocks, best_score
    if score > best_score:
        best_score = score
        save_best_score(best_score)

    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    score = 0
    blocks = [generate_block() for _ in range(3)]

running = True
dragging_block = None
blocks = [generate_block() for _ in range(3)]

while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > best_score:
                save_best_score(score)
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if restart_button.collidepoint(mouse_x, mouse_y):
                restart_game()
            for block in blocks:
                if block["x"] <= mouse_x <= block["x"] + len(block["shape"][0]) * CELL_SIZE * 0.6 and \
                        block["y"] <= mouse_y <= block["y"] + len(block["shape"]) * CELL_SIZE * 0.6:
                    dragging_block = block
                    dragging_block["dragged"] = True
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_block:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = (mouse_x // CELL_SIZE)
                grid_y = ((mouse_y - 200) // CELL_SIZE)
                if can_place_block(dragging_block, grid_x, grid_y):
                    place_block(dragging_block, grid_x, grid_y)
                    blocks.remove(dragging_block)
                    blocks.append(generate_block())
                    check_full_lines_and_columns()
                dragging_block["dragged"] = False
                dragging_block = None

        elif event.type == pygame.MOUSEMOTION:
            if dragging_block:
                dragging_block["x"], dragging_block["y"] = pygame.mouse.get_pos()

    draw_board()
    draw_preview_blocks(blocks)
    draw_score()
    restart_button = draw_restart_button()

    if dragging_block:
        draw_block(dragging_block, offset=(-CELL_SIZE // 2, -CELL_SIZE // 2))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
