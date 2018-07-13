from defines import *
import pygame as pg
import snake as snk
import food as fd
import sys

# wall blocks
wallblock = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
wallblock.set_alpha(255)
wallblock.fill(BLUE)

# check if the snake's head is outside the limits
def inLimits(snake):
    headpos = snake.getHeadPos()
    return not (headpos[0] < OFFSET + 1 or headpos[1] < 1 or headpos[0] >= MAP_LENGTH + OFFSET + 1 or headpos[1] >= MAP_LENGTH + 1)

# draw walls
def drawWalls(surface):
    # left and right walls
    for x in range(MAP_LENGTH + 2):
        for y in range(MAP_LENGTH + 2):
            if x == 0 or y == 0 or x == MAP_LENGTH + 1 or y == MAP_LENGTH + 1:
                surface.blit(wallblock, (x * BLOCK_SIZE, y * BLOCK_SIZE + MAP_ORIGIN[1] ))

# initialize pygame, clock for game speed and screen to draw
pg.init()

# initializing clock and screen
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake Game")
font = pg.font.SysFont(pg.font.get_default_font(), BLOCK_SIZE)
gameOverText = font.render(sGameOverText, 1, WHITE)
startText = font.render(sStartText, 1, WHITE)
scoreText = font.render(sScore, 1, WHITE)
screen.fill(BLACK)

# snake and food
snake = snk.snake(screen, int(MAP_LENGTH / 2) + OFFSET, int(MAP_LENGTH / 2))
food = fd.food(screen, 6, MAP_LENGTH + 5, 1, MAP_LENGTH + 1)

# food should not appear where the snake is
while food.getPos() in snake.getPosList():
    food.__init__(screen, 6, MAP_LENGTH + 5, 1, MAP_LENGTH + 1)

# increase game speed every 10 times
eaten = 0

#score
score = 0
scorePointsText = font.render(str(score), 1, WHITE)

food.draw()
snake.draw()

# press any key to start
drawWalls(screen)
screen.blit(startText, ((MAP_LENGTH - len(sStartText) / 3) * BLOCK_SIZE / 2,
                        ((MAP_LENGTH * BLOCK_SIZE) / 2) + BLOCK_SIZE * (OFFSET - 1)))
screen.blit(scoreText, (BLOCK_SIZE * 2, BLOCK_SIZE))
screen.blit(scorePointsText, (BLOCK_SIZE * OFFSET + BLOCK_SIZE, BLOCK_SIZE))
pg.display.flip()

#waiting for any key to be pressed
waiting = True
while waiting:
    event = pg.event.wait()
    if event.type == pg.KEYDOWN:
        waiting = False
screen.fill(BLACK)

screen.blit(scoreText, (BLOCK_SIZE * 2, BLOCK_SIZE))
screen.blit(scorePointsText, (BLOCK_SIZE * OFFSET + BLOCK_SIZE, BLOCK_SIZE))

# main loop
running = True
while running:
    if not inLimits(snake) or snake.crashed:
        running = False
    else:
        food.draw()
        snake.draw()
        drawWalls(screen)
        pg.display.flip()

        # check if snake eates
        if food.getPos() == snake.getHeadPos():
            snake.grow()

            #update score
            score += 1

            #delete old score region
            oldRegion = pg.Surface((BLOCK_SIZE * OFFSET, BLOCK_SIZE))
            oldRegion.set_alpha(255)
            oldRegion.fill(BLACK)
            screen.blit(oldRegion, (BLOCK_SIZE * OFFSET, BLOCK_SIZE))

            #update the new region with score
            scorePointsText = font.render(str(score), 1, WHITE)
            screen.blit(scorePointsText, (BLOCK_SIZE * OFFSET + BLOCK_SIZE, BLOCK_SIZE))
            pg.display.flip()

            # food should not appear where the snake is
            food.__init__(screen, 6, MAP_LENGTH + 5, 1, MAP_LENGTH + 1)
            while food.getPos() in snake.getPosList():
                food.__init__(screen, 6, MAP_LENGTH + 5, 1, MAP_LENGTH + 1)

            eaten += 1

            # increase game speed
            if eaten % SPEED_INC == 0:
                SPEED += SPEED_TICK

        # game speed control
        clock.tick(SPEED)

        # get the next event on queue
        event = pg.event.poll()
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            direction = snake.getMotionDir()
            if event.key == pg.K_ESCAPE:
                sys.exit()
            elif event.key == pg.K_UP and direction != snk.DOWN:
                snake.setMotionDir(snk.UP)
            elif event.key == pg.K_DOWN and direction != snk.UP:
                snake.setMotionDir(snk.DOWN)
            elif event.key == pg.K_RIGHT and direction != snk.LEFT:
                snake.setMotionDir(snk.RIGHT)
            elif event.key == pg.K_LEFT and direction != snk.RIGHT:
                snake.setMotionDir(snk.LEFT)

        # remove the snake and make movement
        snake.remove()
        snake.move()


# if crashed print "game over"
snake.draw()
drawWalls(screen)
screen.blit(gameOverText, ((MAP_LENGTH - len(sGameOverText)/3) * BLOCK_SIZE / 2,
                           MAP_LENGTH * BLOCK_SIZE / 2 + BLOCK_SIZE * OFFSET))

# wait for "esc" key
while True:
    pg.display.flip()
    event = pg.event.wait()
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            sys.exit()