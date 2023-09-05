import pygame
import pygame.gfxdraw
import random

class Target(pygame.sprite.Sprite):
    """defines the target object for the aim trainer"""
    def __init__(self, background:pygame.surface.Surface,id):
        super().__init__()
        self.id = id
        self.max_width = 50
        self.width = 25
        self.step = 1.5
        self.background = background
        self.max_coordinates = background.get_size() # returns a tuple of the width and height of the background
        self.max_x = self.max_coordinates[0]
        self.max_y = self.max_coordinates[1]
        self.original_image = pygame.image.load('Aim Trainer/data/target_2.png').convert_alpha()
        self.image = self.original_image.copy()
        self.x, self.y = random.randrange(self.width*2, self.max_x-self.width*2, self.width), random.randrange(60, self.max_y-self.width*2, self.width)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.growing = True
        self.shrinking = False


    def draw(self):
        # if not hasattr(self, "new_image"):
        #     self.background.blit(self.image, (self.x, self.y))
        # else:
        #     self.background.blit(self.new_image, (self.x, self.y))
        self.background.blit(self.image, (self.x, self.y))
        

    def update(self):
        if self.width < self.max_width and self.growing == True:
            self.width += self.step
            self.image = pygame.transform.scale(self.original_image, (self.width, self.width))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y
            #print(self.rect.center)
        
        elif self.width >= self.max_width:
            self.growing = False
            self.width -= self.step
        
        elif self.width < self.max_width and self.growing == False and self.width > 1:
            self.width -= self.step
            self.image = pygame.transform.scale(self.original_image, (self.width, self.width))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y

        else:
            self.kill()
            