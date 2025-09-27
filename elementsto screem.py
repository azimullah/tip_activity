import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))

# Load images (update the paths as needed)
background_image = pygame.Surface((400, 300))
background_image.fill((211, 211, 211))  # Light gray background

penguin_image = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.ellipse(penguin_image, (0, 0, 0), [0, 0, 100, 100])  # Simple black ellipse as penguin
penguin_rect = penguin_image.get_rect(center=(200, 180))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, (0, 0))
    screen.blit(penguin_image, penguin_rect)

    # Draw a red rectangle at (50, 50) with width 100 and height 60
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 60))

    pygame.display.flip()

pygame.quit()