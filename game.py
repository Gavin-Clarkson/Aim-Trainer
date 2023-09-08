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
        self.score_pos = (5,5)
        self.miss_pos = (205,5)
        self.misses = 0
        self.lives = 10
        self.lives_pos = (405,5)
        self.timer_pos = (605, 5)
        self.screen = pygame.display.set_mode(self.screen_dimensions)
        pygame.display.set_caption('Aim Trainer')
        self.background = pygame.surface.Surface(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.time_interval = 500
        self.current_time = 0
        self.time_seconds = 0
        self.fps = 15
        self.running = True
        self.score = 0
        self.scoreboard_rect = pygame.surface.Surface((self.WIDTH,50))
        self.font = pygame.font.SysFont('arial', 25)
        self.targets = pygame.sprite.Group()
        self.game_state = 'start_menu'
        self.targets.add(Target(self.background,1))
        

    def run(self):
        """Execute main game loop"""
        while self.running:
            self.time_millis = self.clock.tick(self.fps)
            self.handle_input()
            if self.game_state == 'game':
                self.draw()
                self.update_targets()
            pygame.display.update()
            if self.lives == 0:
                self.game_state = 'game_over'
        self.quit()
        return

    def handle_input(self):
        """Handles user inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.game_state == 'start_menu':
                self.draw_start_menu()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.game_state = 'game'
                    
            
            elif self.game_state == 'game_over':
                self.draw_game_over_screen()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.game_state = 'start_menu'
                    print(self.game_state)
                    self.score = 0
                    self.time_display = 0
                    self.misses = 0
                    self.targets.empty()
                    self.targets.add(Target(self.background,1))
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False
            
            elif self.game_state == 'game':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # get a list of all sprites that are under the mouse cursor
                    clicked_sprites = [s for s in self.targets if s.rect.collidepoint(pos)]
                    # do something with the clicked sprites...
                    if len(clicked_sprites) != 0:
                        self.targets.remove(clicked_sprites[0])
                        self.score += 1
                    else:
                        self.misses += 1

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
        self.time_seconds += self.time_millis / 1000
        self.time_display = str(int(self.time_seconds*10) / 10)
        self.scoreboard_rect.fill(self.colors['scoreboard'])
        self.background.blit(self.scoreboard_rect, self.top_left)
        self.score_font = self.font.render(f'Score: {self.score}', True, self.colors['text'])
        self.miss_font = self.font.render(f'Miss Counter: {self.misses}', True, self.colors['text'])
        self.lives_font = self.font.render(f'Lives: {self.lives}', True, self.colors['text'])
        self.timer_font = self.font.render(f'Timer: {self.time_display}', True, self.colors['text'])
        self.background.blit(self.score_font, self.score_pos)
        self.background.blit(self.miss_font, self.miss_pos)
        self.background.blit(self.lives_font, self.lives_pos)
        self.background.blit(self.timer_font, self.timer_pos)

    def update_targets(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.time_interval > 500:
            print(self.current_time)
            self.time_interval = self.current_time
            self.targets.add(Target(self.background,self.current_time))
        group_len = len(self.targets)
        for target in self.targets:
            target.update()
        current_len = len(self.targets)
        if current_len < group_len:
            self.lives -= 1

    def quit(self):
        """Quits the game"""
        pygame.quit()
        return

    def draw_start_menu(self):
        self.screen.fill((0, 0, 0))
        self.title = self.font.render('Aim Trainer', True, (255, 255, 255))
        self.start_button = self.font.render('Press Enter to start', True, (255, 255, 255))
        self.screen.blit(self.title, (self.WIDTH/2 - self.title.get_width()/2, self.HEIGHT/2 - self.title.get_height()/2))
        self.screen.blit(self.start_button, (self.WIDTH/2 - self.start_button.get_width()/2, self.HEIGHT/2 + self.start_button.get_height()/2))
        pygame.display.update()

    def draw_game_over_screen(self):
        self.screen.fill((0, 0, 0))
        
        title = self.font.render('Game Over', True, (255, 255, 255))
        restart_button = self.font.render('R - Restart', True, (255, 255, 255))
        quit_button = self.font.render('Q - Quit', True, (255, 255, 255))
        self.final_score = self.font.render(f'Score: {self.score}, Time Survived: {self.time_display}, Misses: {self.misses}', True, (255, 255, 255))
        self.screen.blit(title, (self.WIDTH/2 - title.get_width()/2, 300))
        self.screen.blit(restart_button, (self.WIDTH/2 - restart_button.get_width()/2, 350))
        self.screen.blit(quit_button, (self.WIDTH/2 - quit_button.get_width()/2, 400))
        self.screen.blit(self.final_score, (self.WIDTH/2 - self.final_score.get_width()/2, 450))
        pygame.display.update()