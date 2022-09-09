import pygame 
import os


#const
WIDTH ,HEIGHT = 900 , 500 
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 ,40
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
DARK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PURPLE = (147, 51, 234)
BORDER = pygame.Rect(WIDTH//2 - 5 , 0 , 10 , HEIGHT)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
pygame.display.set_caption('First Game !')
YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets' , 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)) , 90)
RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets' , 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG , (55,40)) , 270)
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


#draw itams to the window
def draw_win(red,yellow,red_bullets,yellow_bullets):
    WIN.fill(DARK)
    pygame.draw.rect(WIN , PURPLE , BORDER)
    WIN.blit(YELLOW_SPACESHIP , (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP , (red.x,red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    
    
    pygame.display.update()

#move spaceships

def yellow_handle_movement(keys_pressed , yellow):
    
        if keys_pressed[pygame.K_q] and yellow.x - VEL > 0: #move left
            yellow.x -= VEL
        
        if keys_pressed[pygame.K_d] and yellow.x + VEL + SPACESHIP_WIDTH < BORDER.x : #move right
            yellow.x += VEL
        
        if keys_pressed[pygame.K_z] and yellow.y - VEL >0: #move up
            yellow.y -= VEL
        
        if keys_pressed[pygame.K_s] and yellow.y + yellow.height + VEL < HEIGHT - 17: #move down
            yellow.y += VEL

def red_handle_movement(keys_pressed , red):
       
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  #move left
            red.x -= VEL
        
        if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < WIDTH : #move right
            red.x += VEL
        
        if keys_pressed[pygame.K_UP] and red.y - VEL >0: #move up
            red.y -= VEL
        
        if keys_pressed[pygame.K_DOWN] and red.y + red.height + VEL < HEIGHT - 17: #move down
            red.y += VEL

#fire
def handle_bullets(yellow_bullets , red_bullets , yellow , red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
 
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        





#main function
def main():
    yellow_bullets = []
    red_bullets = []
    red = pygame.Rect(750,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True 
    while run :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 run = False

            if event.type == pygame.KEYDOWN:
                # if event.mod & pygame.KMOD_LCRL & len(yellow_bullets) < MAX_BULLETS:
                if event.key == pygame.K_p and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height/2 -2 , 10 ,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width , red.y + red.height/2 -2 , 10 ,5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        draw_win(red,yellow,red_bullets,yellow_bullets)
         

    
    pygame.quit()





if __name__ == '__main__':
    main()
