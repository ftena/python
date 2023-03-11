import pygame
import random

# initialize pygame
pygame.init()

# set up the display
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue Ball Game")

# define colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Player:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.radius < WIDTH:
            self.x += self.speed

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

class Bar:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, speed):
        self.rect.y += speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

def generate_bars():
    bars = []
    for i in range(5):
        gap_start = random.randint(0, WIDTH - GAP_SIZE)
        bars.append(Bar(0, i * 150, gap_start, BAR_HEIGHT))
        bars.append(Bar(gap_start + GAP_SIZE, i * 150, WIDTH - gap_start - GAP_SIZE, BAR_HEIGHT))
    return bars

# set up the blue ball
BALL_RADIUS = 20
player = Player(WIDTH // 2, HEIGHT - BALL_RADIUS - 10, BALL_RADIUS, 5)

# set up the bars
BAR_WIDTH = 80
BAR_HEIGHT = 20
GAP_SIZE = 200
bars = generate_bars()

# set up the clock
clock = pygame.time.Clock()

# main game loop
game_running = True
next_bar_index = 0  # track the index of the next bar to be destroyed

# main game loop
game_running = True
next_bar_index = 0  # track the index of the next bar to be destroyed
while game_running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # destroy the next bar if it exists
                if next_bar_index < len(bars):
                    del bars[next_bar_index]
    
    # handle user input
    keys = pygame.key.get_pressed()
    player.move(keys)

    # update the bars
    for i, bar in enumerate(bars):
        bar.move(2)
        if bar.rect.y > HEIGHT:
            bars.remove(bar)
            gap_start = random.randint(0, WIDTH - GAP_SIZE)
            bars.append(Bar(0, -BAR_HEIGHT, gap_start, BAR_HEIGHT))
            bars.append(Bar(gap_start + GAP_SIZE, -BAR_HEIGHT, WIDTH - gap_start - GAP_SIZE, BAR_HEIGHT))
            
            # update the index of the next bar to be destroyed
            if i < next_bar_index:
                next_bar_index -= 1
            elif i == next_bar_index:
                next_bar_index = min(next_bar_index+1, len(bars)-1)

    # detect collision between the ball and the bars
    player_rect = pygame.Rect(player.x - player.radius, player.y - player.radius, player.radius * 2, player.radius * 2)
    for i, bar in enumerate(bars):
        if player_rect.colliderect(bar.rect):
            game_running = False
        elif i == next_bar_index:
            # mark the next bar to be destroyed
            pygame.draw.rect(screen, (255, 0, 0), bar.rect, 3)

    # clear the screen
    screen.fill(WHITE)

    # draw the blue ball
    player.draw()

    # draw the bars
    for bar in bars:
        bar.draw()

    # update the display
    pygame.display.update()

    # limit the frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
