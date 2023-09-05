import pygame

# Window size
WINDOW_WIDTH      = 800
WINDOW_HEIGHT     = 800

# Colours
SKY_BLUE = ( 161, 255, 254 )
BLUE     = (   5,   5, 180 )
WHITE    = ( 255, 255, 255 )


# DOts Sprite
class Dots( pygame.sprite.Sprite ):
    def __init__(self,color,x,y,radius,window,id,step):
        pygame.sprite.Sprite.__init__(self)
        self.maxspeed = 4
        self.window   = window
        self.id       = id
        self.color    = color
        self.x        = x
        self.y        = y
        self.pos      = pygame.math.Vector2 (self.x,self.y)
        self.radius   = radius
        # Create the circle image
        self.image = pygame.Surface((self.radius*2, self.radius*2),pygame.SRCALPHA)
        self.rect  = self.image.get_rect(center=self.pos)
        #self.image.fill(color)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        print(self.image)
        pygame.draw.circle(self.image, SKY_BLUE, (self.radius, self.radius),self.radius-5)
        self.vel   = pygame.math.Vector2(0, 0)
        self.accel = pygame.math.Vector2(0, 0)
        self.dead  = False



### MAIN
pygame.init()
window  = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("Circle Sprite")

# Add a circle
circle_sprite = Dots(BLUE,200,200, 30 ,window,1,0)
circle_sprite_2 = Dots(BLUE,300,300,30,window,2,0)
circle_sprite_group = pygame.sprite.Group()
circle_sprite_group.add( circle_sprite )
circle_sprite_group.add ( circle_sprite_2 )

clock = pygame.time.Clock()
done = False
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            done = True

    # Update the window, but not more than 60fps
    window.fill( SKY_BLUE )
    circle_sprite_group.draw( window )
    pygame.display.flip()

    # Clamp FPS
    clock.tick_busy_loop(60)

pygame.quit()