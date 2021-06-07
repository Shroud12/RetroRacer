import pygame, sys
import random


pygame.init()
def make_road():
    screen.blit(road_surface,(150,road_pos_y))
    screen.blit(road_surface,(150,road_pos_y-600))

def move_car():
    screen.blit(player_car,player_rect)

def create_ai_cars():
    random_car_positionx = random.randrange(200,400)
    new_car = ai_car1.get_rect(center =(random_car_positionx,-100))
    return new_car

def move_ai_cars(cars):
    for car in cars:
        car.centery += 4
    return cars

def display_enemy_car(cars):
    for car in cars:
        screen.blit(ai_car1,car)

def check_collisions(cars):
    for car in cars:
        if player_rect.colliderect(car):  
            return False
    return True

def level_up1(roadpos):
    roadpos +=5
    return roadpos

def level_up2(roadpos):
    roadpos +=10
    return roadpos

def level_up1_car_speed(cars):
    for car in cars:
        car.centery += 10
    return cars

def level_up2_car_speed(cars):
    for car in cars:
        car.centery += 15
    return cars
# Screen Variables
Screen_width = 600 
Screen_height = 600
screen = pygame.display.set_mode((Screen_width,Screen_height))
clock = pygame.time.Clock()

# Game Variables
player_score = 0
game_active = True

game_over_screen = pygame.image.load('/assets/gameover.png').convert_alpha()
game_over_rect = game_over_screen.get_rect(center=(300,300))

# Background Surface image load
bg_surface = pygame.image.load('/assets/Background.png').convert()

# Road Surface  assets load
road_surface = pygame.image.load('/assets/Road.png').convert()
road_surface = pygame.transform.scale(road_surface,(300,600))
road_pos_y = 0

# Player car asset load
player_car = pygame.image.load('/assets/red_car_bg.png').convert_alpha()
player_car = pygame.transform.scale2x(player_car)
player_car_position_x = 0
player_rect = player_car.get_rect(center=(300,490))

# Enemy car asset load
ai_car1 = pygame.transform.scale2x(pygame.image.load('/assets/yellow_car_ai.png').convert_alpha()) # combining the above 2 lines of code to shorten it
ai_car2 = pygame.transform.scale2x(pygame.image.load('/assets/blue_car_ai.png').convert_alpha())
ai_car = []
SPAWNCARS = pygame.USEREVENT
pygame.time.set_timer(SPAWNCARS,1600)

# game font asset 
game_font = pygame.font.Font('freesansbold.ttf',40)
light_grey = (200,200,200)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_car_position_x = -50
                player_rect.centerx += player_car_position_x

            if event.key == pygame.K_RIGHT:
                player_car_position_x = +50
                player_rect.centerx += player_car_position_x
                
            if  event.key == pygame.K_r and game_active == False:
                game_active = True
                ai_car.clear()
                player_rect.center = (300,490)
                player_score = 0

        if event.type == SPAWNCARS:
            ai_car.append(create_ai_cars())
           
    screen.blit(bg_surface,(0,0))
    if game_active == True:
        
        # background movement and player car function init.
        road_pos_y +=2
        make_road()
        move_car()
        # Ai cars init.
        ai_car = move_ai_cars(ai_car)
        display_enemy_car(ai_car)
        game_active = check_collisions(ai_car)
        
        #Score
        player_score +=10
        player_text = game_font.render(f"{player_score}",False,light_grey)
        screen.blit(player_text,(400,50))
        if player_score > 10000:
            x = level_up1(road_pos_y) # calling the level up function
            road_pos_y = 0 # resetting the speed to zero rather than adding to it
            road_pos_y += x # adding the new speed
            level_up1_car_speed(ai_car)
        if player_score > 12000:
            y = level_up2(road_pos_y)
            road_pos_y = 0
            road_pos_y += y
            level_up2_car_speed(ai_car)
    else:
        screen.blit(game_over_screen,game_over_rect)
    
    # codes for the car to not leave the road:
    if player_rect.centerx <=200:
        player_rect.centerx = 200
    if player_rect.centerx >=400:
        player_rect.centerx = 400
    if road_pos_y >= 600:
        road_pos_y = 0
    pygame.display.update()
    clock.tick(60)
   
