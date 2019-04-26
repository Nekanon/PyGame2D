import pygame
import generation2D

MAX_X = 800
MAX_Y = 800
game_over = True

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("HelloGame!")


tankHero = pygame.image.load("tankHero.png").convert()
tankHero = pygame.transform.scale(tankHero, (40, 40))

grass = pygame.image.load("grass.png").convert()
grass = pygame.transform.scale(grass, (40, 40))

brickWall = pygame.image.load("brickWall.png").convert()
brickWall = pygame.transform.scale(brickWall, (40, 40))

concreteWall = pygame.image.load("concreteWall.png").convert()
concreteWall = pygame.transform.scale(concreteWall, (40, 40))

water = pygame.image.load("water.png").convert()
water = pygame.transform.scale(water, (40, 40))



# =============new code================
# choice level
level = input("Сhoice your level complexity")
print("Your level is " + str(level))
# generate map
gen = generation2D.generator(level, 20)
map = gen.mapGenerate()
for i in map:
    print(i)


# generate questions(enemy, bonus, mount enemy)

# game
move_left = False
move_right = False
move_up = False
move_down = False

x = 0
y = 0

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_ESCAPE:
                game_over = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if move_left == True:
            x -= 1;
            if x < 0:
                x = 0
        if move_right == True:
            x += 1;
            if x > MAX_X:
                x = MAX_X
        if move_up == True:
            y -= 1;
            if x < 0:
                x = 0
        if move_down == True:
            y += 1;
            if x > MAX_Y:
                x = MAX_Y

    for i in range(0, 20):
        for j in range(0, 20):
            if map[i][j] == 1:
                screen.blit(grass, (i*40, j*40))
            if map[i][j] == 2:
                screen.blit(brickWall, (i*40, j*40))
            if map[i][j] == 3:
                screen.blit(concreteWall, (i*40, j*40))
            if map[i][j] == 4:
                screen.blit(water, (i*40, j*40))

    screen.blit(tankHero, (x*40, y*40))

    pygame.display.flip()
# output score