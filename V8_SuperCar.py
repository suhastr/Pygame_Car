import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Keyboard Event listener")
car = pygame.image.load("media/car1.png").convert()
car = pygame.transform.scale(car, (car.get_width() // 4, car.get_height() // 4))
car_sound = pygame.mixer.Sound('media/v8_supercar_acceleration.wav')

# Set up the sound timer
sound_timer = None
sound_volume = 0.0
max_sound_volume = 1.0
sound_step = 0.01
angle = 0
x=y=0
move_x=move_y=0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x=-1
                angle = 180
                
                
            elif event.key == K_RIGHT:
                move_x=1
                angle = 0

            elif event.key == K_UP:
                move_y=-1
                angle = 90
            elif event.key == K_DOWN:
                move_y=1
                angle = -90
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0

    rotated_image = pygame.transform.rotate(car, angle)
    
    x+=move_x
    y+=move_y
    screen.fill((0,0,0))
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
        if not sound_timer:
            sound_timer = pygame.time.get_ticks()
            sound_volume = 0.0
        else:
            time_diff = pygame.time.get_ticks() - sound_timer
            sound_volume = min(max_sound_volume, sound_volume + (sound_step * time_diff))
            sound_timer = pygame.time.get_ticks()
        car_sound.set_volume(sound_volume)
        car_sound.play(-1)
    else:
        car_sound.stop()
        sound_timer = None
        sound_volume = 0.0
    screen.blit(rotated_image,(x,y))
    pygame.display.update()
