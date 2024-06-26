import pygame        

class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    def __init__(self, x, y, filename):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

    def prevdirection(self):

        self.prev_x = self.change_x
        self.prev_y = self.change_y

    def changespeed(self, x, y):

        self.change_x += x
        self.change_y += y

    def update(self, walls, gate):

        old_x = self.rect.left
        new_x = old_x + self.change_x
        prev_x = old_x + self.prev_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        prev_y = old_y + self.prev_y

        x_collide = pygame.sprite.spritecollide(self, walls, False)

        if x_collide:

            self.rect.left = old_x

        else :

            self.rect.top = new_y

            y_collide = pygame.sprite.spritecollide(self, walls, False)

            if y_collide:
                self.rect.top = old_y

        if gate != False:

            gate_hit = pygame.sprite.spritecollide(self, gate, False)
            
            if gate_hit:
                self.rect.left = old_x
                self.rect.top = old_y