import pygame
from math import sin, cos

pygame.init()
pygame.display.set_caption("Donut")

# initializing the screen
RES = WIDTH, HEIGHT = 800, 700
FPS = 60
WIN = pygame.display.set_mode(RES)

# variables handling the projection and rotation
A , B = 0 , 0
theta_spacing = 30
phi_spacing = 15
radius_1 = 10
radius_2 = 18
k2 = 180
k1 = (WIDTH*k2*3)/(8*(radius_1+radius_2))


# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127,127,127)

# function that takes in coordinates and displays a dot
def draw_dot(pos, color = WHITE):
    pygame.draw.circle(WIN, color, pos, 2)

# all the things to be displayed
def draw_window():
    WIN.fill(BLACK)
    display_torus()
    pygame.display.update()

# mathematics for torus and luminance    
def display_torus():
    xp, yp = 0, 0
    global A
    global B
    
    cosA = cos(A)
    cosB = cos(B)
    sinA = sin(A)
    sinB = sin(B)
    
    for theta in range(0, 628, theta_spacing):
        cos_theta = cos(theta/100)
        sin_theta = sin(theta/100)
        
        for phi in range(0, 628, phi_spacing):
            cos_phi = cos(phi/100)
            sin_phi = sin(phi/100)
            
            circlex = (radius_2 + radius_1*cos_theta)
            circley = (radius_1 * sin_theta)
            
            x = circlex * (cosB * cos_phi + sinA * sinB * sin_phi) - circley * cosA * sinB
            y = circlex * (sinB * cos_phi - sinA * cosB * sin_phi) + circley * cosA * cosB
            z = k2 + cosA * circlex * sin_phi + circley * sinA
            ooz = 1 / z
            
            # final position of dots
            xp = (WIDTH / 2 + k1*ooz*x)
            yp = (HEIGHT/2 - k1*ooz*y)
            
            # luminance calculation and change in colors
            L = cos_phi * cos_theta * sinB - cosA * cos_theta * sin_phi - sinA * sin_theta + cosB * (cosA * sin_theta - cos_theta * sinA * sin_phi)
            
            if L>0:
                # L = ((L/1.4142)+1)/2
                L = L/1.4142
                # shade = (int(255*L),int(255*L),int(255*L))
                shade = (int(255*L*ooz*150),int(255*L*ooz*150),int(255*L*ooz*150))
                draw_dot((xp,yp), shade)            
    
    A += 0.008
    B += 0.006
            

# main function
def main():
    clock = pygame.time.Clock()
    run = True
    paused = False
    while run:
        #maintains FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    
        if paused:
            continue
        
        draw_window()    
                
    pygame.quit()
    
    
if __name__ == "__main__":
    main()