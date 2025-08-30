#Pygame
import pygame 


#init
pygame.init()

#variable running game
isrun = True


#membuat display surface object
window = pygame.display.set_mode((500, 500))

#object game 
#posisi
x = 250
y = 250

#ukuran
panjang = 20
lebar = 20

#kecepatan
speed = 10

while isrun:
    pygame.time.delay(10)

    #user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrun = False
    
    # keyboard press
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= speed
    
    if keys[pygame.K_d] and x < 500 - lebar:
        x += speed
    
    if keys[pygame.K_s] and y < 500 - panjang:
        y += speed

    if keys[pygame.K_w] and y > 0 :
        y -= speed



    #update asset
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (x, y, lebar, panjang))

    #render display
    pygame.display.update()

pygame.quit()




