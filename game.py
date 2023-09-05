import pygame
from target import Target

class Game:
    """Main class that runs the game"""
    def __init__(self):
        """Initialize pygame and the starting variables"""
        pygame.init()
        self.colors = {
            'background': (119,136,153),
            'scoreboard': (169,169,169),
            'text': (0,0,0)
        }
        self.WIDTH, self.HEIGHT = 800, 800
        self.screen_dimensions = (self.WIDTH, self.HEIGHT)
        self.top_left = (0,0)
        self.text_pos = (5,5)
        self.screen = pygame.display.set_mode(self.screen_dimensions)
        pygame.display.set_caption('Aim Trainer')
        self.background = pygame.surface.Surface(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.fps = 10
        self.running = True
        self.score = 0
        self.scoreboard_rect = pygame.surface.Surface((self.WIDTH,50))
        self.font = pygame.font.SysFont('arial', 25)
        self.targets = pygame.sprite.Group()
        for i in range(10):
            self.targets.add(Target(self.background,i))
        

    def run(self):
        """Execute main game loop"""
        while self.running:
            self.clock.tick(self.fps)
            self.draw()
            self.handle_input()
            self.update_targets()
            print(self.targets)
            pygame.display.update()

    def handle_input(self):
        """Handles user inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f'mouse pos: {pos}')
                print([(s.rect.x,s.rect.y) for s in self.targets])
                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in self.targets if s.rect.collidepoint(pos)]
                # do something with the clicked sprites...
                if len(clicked_sprites) != 0:
                    self.targets.remove(clicked_sprites[0])
                    self.score += 1

    def draw(self):
        """draws the sceen and background to the screen"""
        self.background.fill(self.colors['background'])
        for target in self.targets:
            target.draw()
        #self.targets.draw(self.background)      
        self.show_scoreboard()
        self.screen.blit(self.background, self.top_left)

    def show_scoreboard(self):
        """draws the scoreboard to the background surface"""
        self.scoreboard_rect.fill(self.colors['scoreboard'])
        self.background.blit(self.scoreboard_rect, self.top_left)
        self.score_font = self.font.render(f'Score: {self.score}', True, self.colors['text'])
        self.background.blit(self.score_font, self.text_pos)

    def update_targets(self):
        for target in self.targets:
            target.update()

    def quit(self):
        """Quits the game"""
        pygame.quit()
        return
