import pygame as p
import random


p.init()

# setup the game window
window_width = 500
window_height = 500
window = p.display.set_mode((window_width, window_height))
p.display.set_caption("Snake Game")


# Set up the fonts
font_style1 = p.font.SysFont("helvetica", 30, 0, 1)
font_style2 = p.font.SysFont("helvetica", 50, 1, 1)

# function to display score


def display_score(score):
    score_text = font_style1.render("Score: "+str(score), 1, "black")
    window.blit(score_text, [0, 0])

# function to display game over


def display_game_over():
    game_over_text = font_style2.render("GAME OVER", 1, "black")
    window.blit(game_over_text, (150, 225))
    p.display.flip()


# set up the snake
snake_block_size = 20
snake_speed = 10
snake_list = []
snake_length = 1
snake_x = round((window_width/2)/snake_block_size)*snake_block_size
snake_y = round((window_height/2)/snake_block_size)*snake_block_size
snake_x_change = 0
snake_y_change = 0

# Set up the food
food_block_size = 20
food_x = round(random.randrange(0, window_width-food_block_size) /
               snake_block_size)*snake_block_size
food_y = round(random.randrange(0, window_height -
               food_block_size)/snake_block_size)*snake_block_size

# Define function to draw the snake


def draw_snake(snake_block_size, snake_list):
    for block in snake_list:
        p.draw.rect(window, "blue", [
            block[0], block[1], snake_block_size, snake_block_size])


run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    # Move the Snake
    snake_x += snake_x_change
    snake_y += snake_y_change

    # check for the collision of the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width -
                       food_block_size)/snake_block_size)*snake_block_size
        food_y = round(random.randrange(0, window_height -
                       food_block_size)/snake_block_size)*snake_block_size
        snake_length += 1

    # Update the snake list
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with the walls
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        display_game_over()
        p.time.delay(1000)
        run = False

    # Set the game speed
    clock = p.time.Clock()
    clock.tick(snake_speed)

    # draw the game objects
    window.fill("white")
    p.draw.rect(window, "green", [food_x, food_y,
                food_block_size, food_block_size])
    draw_snake(snake_block_size, snake_list)
    display_score(snake_length-1)
    p.display.flip()

    # Get the user input
    keys = p.key.get_pressed()
    if keys[p.K_LEFT]:
        snake_x_change = -snake_block_size
        snake_y_change = 0
    if keys[p.K_RIGHT]:
        snake_x_change = snake_block_size
        snake_y_change = 0
    if keys[p.K_UP]:
        snake_y_change = -snake_block_size
        snake_x_change = 0
    if keys[p.K_DOWN]:
        snake_y_change = snake_block_size
        snake_x_change = 0

p.quit()
