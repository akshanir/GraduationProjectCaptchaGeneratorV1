import numpy as np
import pygame
import sys
import tensorflow as tf
import time
from generator import get_captcha_image
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Start pygame
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

# Fonts
OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
largeFont = pygame.font.Font(OPEN_SANS, 40)

ROWS, COLS = 28, 28

OFFSET = 20
CELL_SIZE = 10


while True:

    # Check if game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    resetButton = pygame.Rect(
        30, OFFSET + ROWS * CELL_SIZE + 30,
        100, 30
    )
    resetText = smallFont.render("Reset", True, BLACK)
    resetTextRect = resetText.get_rect()
    resetTextRect.center = resetButton.center
    pygame.draw.rect(screen, WHITE, resetButton)
    screen.blit(resetText, resetTextRect)

    if event.type == pygame.QUIT:
        done = True
        # This block is executed once for each MOUSEBUTTONDOWN event.
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse = pygame.mouse.get_pos()
      if resetButton.collidepoint(mouse):
        screen.fill(BLACK)
        solution = get_captcha_image(4)
        imp = pygame.image.load("out.png").convert()
        # Using blit to copy content from one surface to other
        screen.blit(imp, (0, 0))
        pygame.draw.rect(screen, WHITE, resetButton)
        screen.blit(resetText, resetTextRect)
        pygame.time.wait(100)

    # # Classify button
    # classifyButton = pygame.Rect(
    #     150, OFFSET + ROWS * CELL_SIZE + 30,
    #     100, 30
    # )
    # classifyText = smallFont.render("Classify", True, BLACK)
    # classifyTextRect = classifyText.get_rect()
    # classifyTextRect.center = classifyButton.center
    # pygame.draw.rect(screen, WHITE, classifyButton)
    # screen.blit(classifyText, classifyTextRect)

    # screen.fill(BLACK)
    # solution = get_captcha_image(4)
    # imp = pygame.image.load("out.png").convert()
    # # Using blit to copy content from one surface to other
    # screen.blit(imp, (0, 0))

    # Check for mouse press
    # click, _, _ = pygame.mouse.get_pressed()
    # if click == 1:
    #     mouse = pygame.mouse.get_pos()
    # else:
    #     mouse = None

    
    # Reset button


    # Reset drawing
    # if mouse and resetButton.collidepoint(mouse):
    #     screen.fill(BLACK)
    #     solution = get_captcha_image(4)
    #     imp = pygame.image.load("out.png").convert()
    #     # Using blit to copy content from one surface to other
    #     screen.blit(imp, (0, 0))


    # # Generate classification
    # if mouse and classifyButton.collidepoint(mouse):
    #     classification = model.predict(
    #         [np.array(handwriting).reshape(1, 28, 28, 1)]
    #     ).argmax()

    # # Show classification if one exists
    # if classification is not None:
    #     classificationText = largeFont.render(str(classification), True, WHITE)
    #     classificationRect = classificationText.get_rect()
    #     grid_size = OFFSET * 2 + CELL_SIZE * COLS
    #     classificationRect.center = (
    #         grid_size + ((width - grid_size) / 2),
    #         100
    #     )
    #     screen.blit(classificationText, classificationRect)

    pygame.display.flip()
