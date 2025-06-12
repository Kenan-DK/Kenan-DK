import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5
ENEMY_VEL = 4

window = pygame.display.set_mode((WIDTH, HEIGHT))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("Assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        print(join(path, image))
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_left"] = sprites
            all_sprites[image.replace(".png", "") + "_right"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size): #Cavern tile 1
    path = join("Assets", "Terrain", "TerrainV2.2.6.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def get_block2(size): #Desert tile 1
    path = join("Assets", "Terrain", "TerrainV2.2.6.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def get_block3(size): #Dark Ruins tile 1
    path = join("Assets", "Terrain", "TerrainV2.2.6.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("Character", "Toadsprites", 16, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.dash_cooldown = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def dash(self, vel):
        if self.dash_cooldown == 0:
            self.dash_cooldown = 200
            if self.direction == "right":
                for z in range(5, 120):
                    self.x_vel = z
                

            if self.direction == "left":
                for z in range(5, 120):
                    self.x_vel = -vel
                    self.x_vel = -z
                


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1
  

    def update_sprite(self):
        sprite_sheet = "Blue Toad Idle"
        if self.hit:
            sprite_sheet = "Blue Toad Hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "Blue Toad Jump"
            elif self.jump_count == 2:
                sprite_sheet = "Blue Toad Double Jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "Blue Toad Fall"
        elif self.x_vel != 0:
            sprite_sheet = "Blue Toad Run"
            if self.x_vel > 10:
                sprite_sheet = "Blue Toad Dash"



        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

        if self.dash_cooldown > 0:
            self.dash_cooldown -= 1

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))








class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object): #Cave tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Block2(Object): #Desert tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Block3(Object): # Dark Ruins tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "FirePlantSprites", width, height)
        self.image = self.fire["Fire Piranha Plant off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "Fire Piranha Plant on"

    def off(self):
        self.animation_name = "Fire Piranha Plant off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0



class Psyeye(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "psy")
        self.psy = load_sprite_sheets("Traps", "Psy-eye Sprites", width, height)
        self.image = self.psy["Psy-eye"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Psy-eye"

    def on(self):
        self.animation_name = "Psy-eye"


    def loop(self):
        sprites = self.psy[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class PsyeyeCapt(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "psy")
        self.psy = load_sprite_sheets("Traps", "Psy-eye Captain Sprites", width, height)
        self.image = self.psy["Psy-eye captain"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Psy-eye captain"

    def on(self):
        self.animation_name = "Psy-eye captain"


    def loop(self):
        sprites = self.psy[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0




class Enemy():
    ANIMATION_DELAY = 3
    GRAVITY = 0.01

    def __init__(self, dx, dy, vel, width, height):
        self.rect = pygame.Rect(dx, dy, width, height)
        self.shyguy = load_sprite_sheets("Enemies", "GreenGuy", width, height)
        self.image = self.shyguy["Green Shy Guy Run"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "guy"
        self.animation_count = 0
        self.animation_name = "Green Shy Guy Run"


    def update(self, objects):
        for obj in objects:
            ex_rect = (self.rect.x + self.x_vel, self.rect.y, self.rect.width, self.rect.height)
            if obj.rect.colliderect(ex_rect):
                self.x_vel *= -1

            if obj and obj.name == "fire":
                self.x_vel = 1

            bottom_right_rect = (self.rect.right, self.rect.bottom, 16, 16)
            bottom_left_rect = (self.rect.left, self.rect.bottom, 16, 16)
            if (not obj.rect.colliderect(bottom_right_rect)) or (not obj.rect.colliderect(bottom_left_rect)):
                self.x_vel = -1

            elif(obj.rect.colliderect(bottom_right_rect)) or (obj.rect.colliderect(bottom_left_rect)):
                self.x_vel = 1

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

    def move(self, dx, vel):
        self.rect.x += dx
        self.rect.y += 0
        self.direction = "left"
        self.step_count = 0

        if self.direction == "left":
            self.x_vel = -vel
            for x in range (10):
                self.step_count += 1
                if self.step_count >= 10:
                    self.x_vel = ENEMY_VEL
                    self.direction = "right"
                    self.step_count = 0
                    
        if self.direction == "right":
            self.x_vel = vel
            for x in range (10):
                self.step_count += 1
                if self.step_count >= 10:
                    self.x_vel = -vel
                    self.direction = "left"
                    self.step_count = 0

        
            
            




            
    def loop(self, fps, vel):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, ENEMY_VEL)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        sprites = self.shyguy[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


    
           


def get_background(name):
    image = pygame.image.load(join("Assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    cooldown = False
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_a] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d] and not collide_right:
        player.move_right(PLAYER_VEL)

    if keys[pygame.K_w] and not collide_left:
        player.dash(PLAYER_VEL)


        
            
        

    

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()





def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Rocks_bg.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    
    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)
    shyguy2 = Enemy(920, 672, ENEMY_VEL, 16, 16)
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 4, block_size),
               Block(block_size * 4, HEIGHT - block_size * 4, block_size),
               Block(block_size * 5, HEIGHT - block_size * 4, block_size),
               Block(block_size * 6, HEIGHT - block_size * 3, block_size),
               Block(block_size * 5, HEIGHT - block_size * 3, block_size),
               Block(block_size * 8, HEIGHT - block_size * 2, block_size),
               Block(block_size * 9, HEIGHT - block_size * 2, block_size),
               Block(block_size * 6, HEIGHT - block_size * 4, block_size), fire, fire2, shyguy, shyguy2]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()


        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        handle_move(player, objects)
        shyguy.update(objects)
        shyguy.loop(FPS, ENEMY_VEL)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()


def main2(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("sky.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    
    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()
    floor = [Block2(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block2(0, HEIGHT - block_size * 2, block_size),
               Block2(block_size * 3, HEIGHT - block_size * 4, block_size),
               Block2(block_size * 4, HEIGHT - block_size * 4, block_size),
               Block2(block_size * 5, HEIGHT - block_size * 4, block_size),
               Block2(block_size * 6, HEIGHT - block_size * 5, block_size),
               Block2(block_size * 9, HEIGHT - block_size * 5, block_size),
               Block2(block_size * 10, HEIGHT - block_size * 5, block_size),
               Block2(block_size * 14, HEIGHT - block_size * 3, block_size),
               Block2(block_size * 15, HEIGHT - block_size * 3, block_size),fire, fire2, shyguy]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()


        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        handle_move(player, objects)
        shyguy.update(objects)
        shyguy.loop(FPS, ENEMY_VEL)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()

def main3(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Ruins V1.2.3.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    
    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)
    psye = Psyeye(185, HEIGHT - block_size - 123, 64, 32) #64 was first value
    psye.on()
    psye2 = Psyeye(405, HEIGHT - block_size - 390, 64, 32) #64 was first value
    psye.on()
    psyc = PsyeyeCapt(700, HEIGHT - block_size - 450, 64, 64)
    psyc.on()
    psyc2 = PsyeyeCapt(700, HEIGHT - block_size - 150, 64, 64)
    psyc2.on()
    floor = [Block3(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block3(1, HEIGHT - block_size * 3, block_size),
               Block3(block_size * 3, HEIGHT - block_size * 4, block_size),
               Block3(block_size * 4, HEIGHT - block_size * 4, block_size),
               Block3(block_size * 5, HEIGHT - block_size * 4, block_size),
               Block3(block_size * 5, HEIGHT - block_size * 4, block_size),
               Block3(block_size * 6, HEIGHT - block_size * 5, block_size),
               Block3(block_size * 3, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 4, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 5, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 6, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 7, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 8, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 9, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 10, HEIGHT - block_size * 8, block_size),
               Block3(block_size * 3, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 4, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 5, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 6, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 7, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 8, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 9, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 10, HEIGHT - block_size * 9, block_size),
               Block3(block_size * 9, HEIGHT - block_size * 5, block_size),
               Block3(block_size * 10, HEIGHT - block_size * 5, block_size),
               Block3(block_size * 14, HEIGHT - block_size * 3, block_size),
               Block3(block_size * 15, HEIGHT - block_size * 3, block_size),
               Block3(block_size * 16, HEIGHT - block_size * 4, block_size),
               Block3(block_size * 17, HEIGHT - block_size * 4, block_size),
               Block3(block_size * 18, HEIGHT - block_size * 4, block_size),psye, psye2, shyguy, psyc, psyc2]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()


        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        psye.loop()
        psye2.loop()
        psyc.loop()
        psyc2.loop()
        handle_move(player, objects)
        shyguy.update(objects)
        shyguy.loop(FPS, ENEMY_VEL)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main3(window)
