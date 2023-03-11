import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

class Room(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((255, 255, 255))
        self.font = pygame.font.SysFont(None, 40)
        self.number = number
        self.text = self.font.render(str(self.number), True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=self.image.get_rect().center)
        self.image.blit(self.text, self.text_rect)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))

room_list = [Room(random.randint(1, 5)) for i in range(10)]
room_group = pygame.sprite.Group(room_list)

player = Player()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    # Check for collisions between player and rooms
    collided_rooms = pygame.sprite.spritecollide(player, room_group, True)
    for room in collided_rooms:
        print("You entered room", room.number)

    # Draw everything on the screen
    WINDOW.fill((0, 0, 0))
    room_group.draw(WINDOW)
    WINDOW.blit(player.image, player.rect)

    pygame.display.update()

pygame.quit()
