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
ENEMY_VEL = 2
VEL = 1
bullets = pygame.sprite.Group()
LEVEL = 1
LEVEL_CLEAR = False

lives = 3 #may have to move somewhere later

window = pygame.display.set_mode((WIDTH, HEIGHT))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("Assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]


    all_sprites = {}

    for image in images:
        #print(join(path, image)) #output all sprites in level except terrain
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
    path = join("Assets", "Terrain", "TerrainV2.2.6.png") #terrain spritesheet
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






#============================================================================
#                               TERRAIN
#============================================================================

def grass_block(size): #grass tile 1
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def grass_block2(size): #grass tile 2
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def grass_block3(size): #grass tile 3
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)





def cave_block(size): #cave tile 1
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def cave_block2(size): #cave tile 2
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def cave_block3(size): #cave tile 3
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)





def factory_block(size): #factory tile 1
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def factory_block2(size): #factory tile 2
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def factory_block3(size): #factory tile 3
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(192, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)





def ruins_block(size): #ruin tile 1
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def ruins_block2(size): #ruin tile 2
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 64, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def ruins_block3(size): #ruin tile 3
    path = join("Assets", "Terrain", "TerrainV7 2.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 128, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)







#============================================================================
#                               SOUNDS
#============================================================================

def Player_Sounds(sound_type):
    sfx_type = sound_type
    filename = "" #sound file name goes here
    sfx_path = os.path.join("Assets", "Sounds", "Player_SFX", filename) #file path for player SFX files
    
    jump_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_jump.wav")
    hit_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_hit.wav")
    death_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_death.wav")
    start_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_start.wav")
    win_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_win.wav")
    shoot_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_shoot.wav")
    dash_sfx = pygame.mixer.Sound(sfx_path + "NSMBW_Toad_dash.wav")

    if sfx_type == "p_jump":
        pygame.mixer.Sound.play(jump_sfx)

    elif sfx_type == "p_hit":
        pygame.mixer.Sound.play(hit_sfx)

    elif sfx_type == "p_death":
        pygame.mixer.Sound.play(death_sfx)

    elif sfx_type == "p_start":
        pygame.mixer.Sound.play(start_sfx)

    elif sfx_type == "p_win":
        pygame.mixer.Sound.play(win_sfx)

    elif sfx_type == "p_shoot":
        pygame.mixer.Sound.play(shoot_sfx)

    elif sfx_type == "p_dash":
        pygame.mixer.Sound.play(dash_sfx)






def Menu_sounds(action_type):
    sfx_type = action_type
    filename = ""
    sfx_path = os.path.join("Assets", "Sounds", "Menu_SFX", filename)
    
    confirm_sfx = pygame.mixer.Sound(sfx_path + "MKWii_Pause.wav")
    back_sfx = pygame.mixer.Sound(sfx_path + "MKWii_UnPause.wav")
    exit_sfx = pygame.mixer.Sound(sfx_path + "MKWii_Exit.wav")

    if sfx_type == "m_confirm":
        pygame.mixer.Sound.play(confirm_sfx)

    elif sfx_type == "m_back":
        pygame.mixer.Sound.play(back_sfx)

    elif sfx_type == "m_exit":
        pygame.mixer.Sound.play(exit_sfx)







def Background_music(BG_music): #may not work
    level_theme = BG_music
    filename = ""
    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    Title_bgm = pygame.mixer.music.load(song_path + "NSMBWii Title Theme.mp3")
    Menu_bgm = pygame.mixer.music.load(song_path + "MKWii Main Menu.mp3")
    Grass_bgm = pygame.mixer.music.load(song_path + "NSMBWii Main Theme.mp3")
    Cave_bgm = pygame.mixer.music.load(song_path + "P4 I'll Face Myself Battle.mp3")
    Castle_bgm = pygame.mixer.music.load(song_path + "Yakuza funny song.mp3")

    Continue_bgm = pygame.mixer.music.load(song_path + "P4 I'll Face Myself.mp3")
    Game_over_bgm = pygame.mixer.music.load(song_path + "NSMBWii Game Over.mp3") #Might be a SFX
    Course_Clear_bgm = pygame.mixer.music.load(song_path + "NSMBWii OG Course Clear.mp3") #Might be a SFX
    MOBIL1_bgm = pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    


    if level_theme == "title":
        pygame.mixer.music.play(Titile_bgm)

    elif level_theme == "menu":
        pygame.mixer.music.play(Menu_bgm)

    elif level_theme == "grass":
        pygame.mixer.music.play(Grass_bgm)

    elif level_theme == "cave":
        pygame.mixer.music.play(Cave_bgm)

    elif level_theme == "castle":
        pygame.mixer.music.play(Castle_bgm)

    elif level_theme == "continue":
        pygame.mixer.music.play(Continue_bgm)

    elif level_theme == "MOBIL":
        pygame.mixer.music.play(MOBIL1_bgm)

    elif level_theme == "kiryu":
        pygame.mixer.music.play(Castle_bgm)





#============================================================================
#                               Menu
#============================================================================

class Button():
    def __init__(self, button_type, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.type = button_type
        self.image = ""
        self.image_select = ""
        button_path = os.path.join("Assets", "Menus", self.type + "_Button.png")
        button_select_path = os.path.join("Assets", "Menus", self.type + "_Button_selected.png")
        self.hovered = False
        self.clicked = False
        self.action = ""

        if self.type == "Test": #determines the button-instance's image
            self.image = pygame.image.load(button_path)
            if self.hovered == True:
                self.image = pygame.image.load(button_select_path)

            self.action = "main" #determines what it does
            

        elif self.type == "Start": 
            self.image = pygame.image.load(button_path)
            if self.hovered == True:
                self.image = pygame.image.load(button_select_path)

            self.action = "start"
            

        elif self.type == "Title": 
            self.image = pygame.image.load(button_path)
            if self.hovered == True:
                self.image = pygame.image.load(button_select_path)

            self.action = "return_to_title"
            


            

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            self.hovered = True

        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.clicked = True
            print("IT WORKS, THE BUTTON ACTUALLY WORKS!")
            
            if self.action == "main": #to the main menu
                MAIN_MENU()
                

            if self.action == "start": #starts the game
                main2(window, LEVEL_CLEAR, LEVEL, lives)
                #main3(window, LEVEL_CLEAR, LEVEL, lives) #added for testing
                

            if self.action == "return_to_title": #back to title screen
                TITLE_SCREEN()

                

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
        



    
class main_menu():
    def __init__(self):
        self.poopyman = True
        window.fill("green")
        mouse = pygame.mouse.get_pos()
        test_button = Button("Test", 500, 400, 150, 100)



    def update():
        test_button.draw(win)




    
#============================================================================
#                               PLAYER
#============================================================================

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("Character", "Toadsprites", 16, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, lives):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.alive = True
        self.HP = 5
        self.maxHP = 5 #Health based on difficulty
        #self.lives = 3 #lives based on difficulty
        self.lives = lives
        self.maxLives = 99
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.dash_cooldown = 0
        self.shoot_cooldown = 0
        self.hit_cooldown = 0
        self.shooting = False
        self.bullet_anchor_x = (self.rect.x)
        self.bullet_anchor_y = (self.rect.y)


    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def dash(self, vel):
        if self.dash_cooldown == 0:
            self.dash_cooldown = 200
            Player_Sounds("p_dash")
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
        if self.hit_cooldown == 0:
            self.hit_cooldown = 150
            Player_Sounds("p_hit")
            self.HP -= 1
            print("officer down")

            if self.HP <= 0:
                self.die()
        
        


    def die(self):
        print("dead")
        self.lives -=1

        self.kill()
        #Player_Sounds("p_die")
        

        

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


    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shooting = True
            #pellet = Bullet(self.rect.centerx, self.rect.centery, 11, 11, self.direction)
            pellet = Bullet(self.rect.x, self.rect.y, 11, 11, self)
            print("Player Coordinates:", self.rect.x, self.rect.y)
            Player_Sounds("p_shoot")
            self.shoot_cooldown = 250
            bullets.add(pellet)
            #print("Bullets group contents:", bullets)

        


        
        #if self.direction == "left":
            #bullet = Bullet(self.rect.center + (0.5 * self.rect.size[0] * self.direction), self.rect.centrey, 11, 11, self.direction)

        #if self.direction == "right":
            #bullet = Bullet(self.rect.center, self.rect.centrey, 11, 11, self.direction)
  

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
            elif self.x_vel < -10:
                sprite_sheet = "Blue Toad Dash"
        elif self.shooting == True:
            sprite_sheet = "Blue Toad Attack"
        #print(self.rect.x, self.rect.y) - these coordinates needed for bullets' spawn point.



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

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            self.shooting = False

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


#============================================================================
#                        BULLETS + PROJECTILES
#============================================================================

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, player): #x+y = player's x+y, width+height are 11
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20 #move speed
        self.range = 300 #dist. travelled
        self.image = pygame.image.load("projectile.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        self.origin = player.rect.x #start point
        
        self.rect.centery = player.rect.centery
        self.direction = player.direction

        if self.direction == "left":
            self.rect.centerx = player.rect.centerx - 30

        if self.direction == "right":
            self.rect.centerx = player.rect.centerx + 30

    def update(self, bullet, enemies):
        
        print("Bullet coordinates:", self.rect.x, self.rect.y)
        
        #movement check
        if self.direction == "left":
            self.rect.centerx -= (self.speed)
    
            if self.rect.left <= (self.origin - self.range):
                self.kill()
                print("offscreen - left")

        elif self.direction == "right":
            self.rect.centerx += (self.speed)
            
            if self.rect.right > (self.origin + self.range):
                self.kill()
                print("offscreen - right")


        for enemy in enemies: #enemies = enemy list
            if pygame.sprite.spritecollide(enemy, bullet, False): #enemy collision
                if enemy.alive:
                    enemy.HP -= 1
                    print("enemy hit")
                    self.kill()
                
                

    def draw(self, win, offset_x): 
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

        



#============================================================================
#                               OBJECT SETUP
#============================================================================


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

#======================================================= test stuff
class Block(Object): #Cave tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size) #gets terrain image
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
#=======================================================



class Grass_S(Object): #grass tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = grass_block(size) #gets terrain image
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Grass_D(Object): #grass tile 2
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = grass_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        

class Grass_D2(Object): # grass tile 3
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = grass_block3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)




class Cave_S(Object): #cave tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = cave_block(size) #gets terrain image
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Cave_D(Object): #cave tile 2
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = cave_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        

class Cave_D2(Object): # cave tile 3
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = cave_block3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)




class Factory_S(Object): #factory tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = factory_block(size) #gets terrain image
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Factory_D(Object): #factory tile 2
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = factory_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        

class Factory_D2(Object): #factory tile 3
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = factory_block3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)




class Ruins_S(Object): #ruins tile 1
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = ruins_block(size) #gets terrain image
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Ruins_D(Object): #ruins tile 2
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = ruins_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        


class Ruins_D2(Object): #ruins tile 3
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = ruins_block3(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

#============================================================================
#                               TRAPS
#============================================================================

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


class FireLily(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "FirePlantSprites", width, height)
        self.image = self.fire["fire lily"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "fire lily"

    def on(self):
        self.animation_name = "fire lily"

    def off(self):
        self.animation_name = "fire lily"

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





#============================================================================
#                               Level Assets
#============================================================================

class Goal(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Goal")
        self.Goal = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.Goal["Goal Sign"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Goal Sign"
        self.name = "GOOALASOOO"

    def on(self):
        self.animation_name = "Goal Sign"


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





class Bridge(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Bridge")
        self.Bridge = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.Bridge["bridge2"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "bridge things"
        self.name = "bridge"

    def on(self):
        self.animation_name = "bridge things"


    def loop(self):
        sprites = self.Bridge[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0




class Short_Vine(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Vine_S")
        self.Vine_S = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.Vine_S["short vine"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "viner"
        self.name = "vine"

    def on(self):
        self.animation_name = "viner"


    def loop(self):
        sprites = self.Vine_S[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0




class Long_Vine(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "Vine_L")
        self.Vine_L = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.Vine_L["long vine"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "viner2"
        self.name = "vine"

    def on(self):
        self.animation_name = "viner2"


    def loop(self):
        sprites = self.Vine_L[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0



class Top_Vine(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "vine_P")
        self.vine_P = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.vine_P["vine leaf"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "viner3"
        self.name = "vine"

    def on(self):
        self.animation_name = "viner3"


    def loop(self):
        sprites = self.vine_P[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0



class Lily_Vine(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "lily")
        self.lily = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.lily["lily stalk"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "lily stalk"
        self.name = "lily stalk"

    def on(self):
        self.animation_name = "lily stalk"


    def loop(self):
        sprites = self.lily[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0



class Stalactite(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spike")
        self.spike = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.spike["stalactite"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "stalactite"
        self.name = "NME"

    def on(self):
        self.animation_name = "stalactite"


    def loop(self):
        sprites = self.spike[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0



class Stalagmite(Object): #w = 48, h = 58
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spike")
        self.spike = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.spike["stalagmite"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "stalagmite"
        self.name = "NME"

    def on(self):
        self.animation_name = "stalagmite"


    def loop(self):
        sprites = self.spike[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0






class float_plat(Object): #w = 48, h = 58
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "float")
        self.float = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.float["floating platform idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "floating platform idle"
        self.name = "floating platform"
        self.direction = 1
        self.rect.x = x
        self.rect.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.steps = 0

    def on(self):
        self.animation_name = "floating platform move"


    def move_side(self, vel):
        self.animation_name = "floating platform move"
        

        if self.direction == 1:
            self.steps += 1
            self.rect.x += -vel

            if self.steps > 100:
                self.direction = 2
                self.steps = 0

        if self.direction == 2:
            self.steps += 1
            self.rect.x += vel

            if self.steps > 100:
                self.direction = 1
                self.steps = 0


    def move_sideR(self, vel):
        self.animation_name = "floating platform move"
        

        if self.direction == 1:
            self.steps += 1
            self.rect.x += vel

            if self.steps > 100:
                self.direction = 2
                self.steps = 0

        if self.direction == 2:
            self.steps += 1
            self.rect.x += -vel

            if self.steps > 100:
                self.direction = 1
                self.steps = 0



    def move_up(self, vel):
        self.animation_name = "sticky floating platform move"
        

        if self.direction == 1:
            self.steps += 1
            self.rect.y += vel

            if self.steps > 100:
                self.direction = 2
                self.steps = 0

        if self.direction == 2:
            self.steps += 1
            self.rect.y += -vel

            if self.steps > 100:
                self.direction = 1
                self.steps = 0



    def move_down(self, vel):
        self.animation_name = "sticky floating platform move"
        

        if self.direction == 1:
            self.steps += 1
            self.rect.y += -vel

            if self.steps > 100:
                self.direction = 2
                self.steps = 0

        if self.direction == 2:
            self.steps += 1
            self.rect.y += vel

            if self.steps > 100:
                self.direction = 1
                self.steps = 0


    def loop(self, vel, instruction):
        if instruction == "left":
            self.move_side(vel)

        if instruction == "right":
            self.move_sideR(vel)

        if instruction == "up":
            self.move_up(vel)

        if instruction == "down":
            self.move_down(vel)

        if instruction == "idle":
            pass
            
            
        
        
        sprites = self.float[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0








class plasmorb(Object): #w = 103, h = 30
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "plasma")
        self.plasma = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.plasma["plasmorb"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "plasmorb"
        self.name = "plasmorb"

    def on(self):
        self.animation_name = "plasmorb"


    def loop(self):
        sprites = self.plasma[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0




class LeftConveyor(Object): #w = 64, h = 30
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "belt")
        self.belt = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.belt["Conveyor belt L"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Conveyor belt L"
        self.name = "Conveyor belt L"

    def on(self):
        self.animation_name = "Conveyor belt L"


    def loop(self):
        sprites = self.belt[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0





class RightConveyor(Object): #w = 64, h = 30
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "belt")
        self.belt = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.belt["Conveyor belt R"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Conveyor belt R"
        self.name = "Conveyor belt R"

    def on(self):
        self.animation_name = "Conveyor belt R"


    def loop(self):
        sprites = self.belt[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0





class door_portal(Object): #w = 35, h = 37
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "gate")
        self.gate = load_sprite_sheets("Terrain", "Level_assets", width, height)
        self.image = self.gate["door"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "portal" #door
        self.name = "door"

        self.open = False


    def on(self):
        self.animation_name = "portal"


    def loop(self):
        if self.open == True:
            self.on()
            
        sprites = self.gate[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0





#============================================================================
#                               ENEMIES
#============================================================================


class Enemy(pygame.sprite.Sprite):
    ANIMATION_DELAY = 3
    GRAVITY = 1

    def __init__(self, dx, dy, vel, width, height):
        super().__init__()
        self.rect = pygame.Rect(dx, dy, width, height)
        self.shyguy = load_sprite_sheets("Enemies", "GreenGuy", width, height)
        self.image = self.shyguy["Green Shy Guy Run"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "NME"
        self.animation_count = 0
        self.animation_name = "Green Shy Guy Run"
        #self.direction = "left"
        self.steps = 0
        self.direction = 1
        self.HP = 2
        


    def move(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.x_vel = -vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.x_vel = vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 1
                self.steps = 0

        #print("steps:", self.steps, "  direction:", self.direction)



    def die(self, objects):

        for obj in objects:
            if self in objects:
                if self.HP <= 0:
                    self.kill()
                    self.alive = False
                    objects.remove(self)

            else:
                #print(objects) checks the list
                break
            
            
                

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


            
    def loop(self, fps, vel, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel, ENEMY_VEL)
        self.die(objects)
        
        

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








class Air_Enemy(pygame.sprite.Sprite):
    ANIMATION_DELAY = 3
    GRAVITY = 1

    def __init__(self, dx, dy, vel, width, height):
        super().__init__()
        self.rect = pygame.Rect(dx, dy, width, height)
        self.flying = load_sprite_sheets("Enemies", "Twiggy", width, height)
        self.image = self.flying["leaf bird"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "NME"
        self.animation_count = 0
        self.animation_name = "leaf bird"
        #self.direction = "left"
        self.steps = 0
        self.direction = 1
        self.HP = 2
        


    def moveX(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.x_vel = -vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.x_vel = vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 1
                self.steps = 0


    def moveY(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.y_vel = -vel
            self.rect.y += self.y_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.y_vel = vel
            self.rect.y += self.y_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 1
                self.steps = 0

        #print("steps:", self.steps, "  direction:", self.direction)

    def die(self, objects):
        for obj in objects:
            if self in objects:
                if self.HP <= 0:
                    self.kill()
                    self.alive = False
                    objects.remove(self)

                else:
                    #print(objects) checks the list
                    break
                
                

            
                    
                    
                    
                
            

        
            
            
                

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


            
    def loop(self, fps, vel, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.moveY(self.x_vel, self.y_vel, ENEMY_VEL)
        self.die(objects)
        
        

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        sprites = self.flying[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0




class Parashroom(pygame.sprite.Sprite):
    ANIMATION_DELAY = 3
    GRAVITY = 1

    def __init__(self, dx, dy, vel, width, height):
        super().__init__()
        self.rect = pygame.Rect(dx, dy, width, height)
        self.shroom = load_sprite_sheets("Enemies", "Parashroom", width, height)
        self.image = self.shroom["shroom stalker"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "NME"
        self.animation_count = 0
        self.animation_name = "shroom stalker"
        #self.direction = "left"
        self.steps = 0
        self.direction = 1
        self.HP = 2
        


    def move(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.x_vel = -vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.x_vel = vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 50:
                self.direction = 1
                self.steps = 0

        #print("steps:", self.steps, "  direction:", self.direction)



    def die(self, objects):

        for obj in objects:
            if self in objects:
                if self.HP <= 0:
                    self.kill()
                    self.alive = False
                    objects.remove(self)

            else:
                #print(objects) checks the list
                break



    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


            
    def loop(self, fps, vel, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel, ENEMY_VEL)
        self.die(objects)
        
        

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        sprites = self.shroom[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class mineghost(pygame.sprite.Sprite):
    ANIMATION_DELAY = 3
    GRAVITY = 1

    def __init__(self, dx, dy, vel, width, height):
        super().__init__()
        self.rect = pygame.Rect(dx, dy, width, height)
        self.miner = load_sprite_sheets("Enemies", "Ghosts", width, height)
        self.image = self.miner["Mining ghost 2"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "NME"
        self.animation_count = 0
        self.animation_name = "Mining ghost 2"
        #self.direction = "left"
        self.steps = 0
        self.direction = 1
        self.HP = 3
        


    def move(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.x_vel = -vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 60:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.x_vel = vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 60:
                self.direction = 1
                self.steps = 0

        #print("steps:", self.steps, "  direction:", self.direction)



    def die(self, objects):

        for obj in objects:
            if self in objects:
                if self.HP <= 0:
                    self.kill()
                    self.alive = False
                    objects.remove(self)

            else:
                #print(objects) checks the list
                break



    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


            
    def loop(self, fps, vel, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel, ENEMY_VEL)
        self.die(objects)
        
        

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        sprites = self.miner[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Robobear(pygame.sprite.Sprite): #w36, h72
    ANIMATION_DELAY = 5
    GRAVITY = 1

    def __init__(self, dx, dy, vel, width, height):
        super().__init__()
        self.rect = pygame.Rect(dx, dy, width, height)
        self.robo = load_sprite_sheets("Enemies", "Robots", width, height)
        self.image = self.robo["freddo bear5 2"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "NME"
        self.animation_count = 0
        self.animation_name = "freddo bear5 2"
        #self.direction = "left"
        self.steps = 0
        self.direction = 1
        self.HP = 3
        


    def move(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.x_vel = -vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 90:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.x_vel = vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 90:
                self.direction = 1
                self.steps = 0

        #print("steps:", self.steps, "  direction:", self.direction)



    def die(self, objects):

        for obj in objects:
            if self in objects:
                if self.HP <= 0:
                    self.kill()
                    self.alive = False
                    objects.remove(self)

            else:
                #print(objects) checks the list
                break



    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


            
    def loop(self, fps, vel, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel, ENEMY_VEL)
        self.die(objects)
        
        

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        sprites = self.robo[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0



class NyaFO(pygame.sprite.Sprite): #w40, h37
    ANIMATION_DELAY = 5
    GRAVITY = 1

    def __init__(self, dx, dy, vel, width, height):
        super().__init__()
        self.rect = pygame.Rect(dx, dy, width, height)
        self.robo = load_sprite_sheets("Enemies", "Robots", width, height)
        self.image = self.robo["NyaFO2.1"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "NME"
        self.animation_count = 0
        self.animation_name = "NyaFO2.1"
        #self.direction = "left"
        self.steps = 0
        self.direction = 1
        self.HP = 3
        


    def move(self, dx, dy, vel):
        self.rect.x += 0 #dx
        self.rect.y += 0 #dy
        #self.x_vel += dx
        #self.y_vel += dy
        
        
        

        if self.direction == 1: #left
            self.x_vel = -vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 110:
                self.direction = 2
                self.steps = 0
            
            
                    
        if self.direction == 2: #right
            self.x_vel = vel
            self.rect.x += self.x_vel
            self.steps += 1
            if self.steps > 110:
                self.direction = 1
                self.steps = 0

        #print("steps:", self.steps, "  direction:", self.direction)



    def die(self, objects):

        for obj in objects:
            if self in objects:
                if self.HP <= 0:
                    self.kill()
                    self.alive = False
                    objects.remove(self)

            else:
                #print(objects) checks the list
                break



    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


            
    def loop(self, fps, vel, objects):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel, ENEMY_VEL)
        self.die(objects)
        
        

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        sprites = self.robo[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


            

#============================================================================
#                               ENEMIES UPDATED
#============================================================================

class Enemy2(): #not necessary
    ANIMATION_DELAY = 3
    GRAVITY = 1


    def __init__(self, dx, dy, vel, width, height):
        self.rect = pygame.Rect(dx, dy, width, height)
        self.sniffet = load_sprite_sheets("Enemies", "Sniffet", width, height)
        self.image = self.sniffet["Yellow Sniffet"][0]
        self.rect.x = dx
        self.rect.y = dy
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.alive = True
        self.hit_count = 0
        self.fall_count = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.name = "guy"
        self.animation_count = 0
        self.animation_name = "Yellow Sniffet"


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
        
        sprites = self.sniffet[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

    



#============================================================================
#                               HUD
#============================================================================

class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Hud_black.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.x_vel = 0
        self.y_vel = 0


    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))





class HP_bar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("Heart.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect_centre = (self.rect.x, self.rect.y)
        self.name = "hp"


    def update(self):
        self.rect.x += 2


    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        
        




    
#============================================================================
#                               BACKGROUNDS
#============================================================================
    
def get_background(name):
    image = pygame.image.load(join("Assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image





#============================================================================
#                           DRAWING ON SCREEN
#============================================================================

def draw(window, background, bg_image, player, objects, offset_x, bullets):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)
    #bullets.draw(window, offset_x)
    for bullet in bullets:
        bullet.draw(window, offset_x)


    full_heart = pygame.image.load("Heart.png").convert_alpha() #width = 27, height = 24
    
    empty_heart = pygame.image.load("Heart_empty.png").convert_alpha()

    life_clover = pygame.image.load("Lives_icon2.png").convert_alpha()
    font = pygame.font.Font('freesansbold.ttf', 40)

    #pygame.draw.rect(window, "red", (25, 25, 35 * player.maxHP, 15))
    #pygame.draw.rect(window, "green", (25, 25, 35 * player.HP, 15))
    for i in range(player.maxHP): 
        window.blit(empty_heart, (20 + i * 52, 25, 27, 24)) #empty HP bar
        
    for i in range(player.maxHP - player.HP, player.maxHP): 
        window.blit(full_heart, (20 + i * 52, 25, 27, 24)) #full HP bar

    window.blit(life_clover, (500 + i * 52, 25, 27, 24))
    life_count = font.render("x" + str(player.lives), True, (255, 255, 255)) #rgb values
    window.blit(life_count, (785, i * 10))
    #window.blit(player.lives, (520 + i * 52, 25, 27, 24))
        

    pygame.display.update()





#============================================================================
#                           DRAWING MENUS EDITION
#============================================================================

def draw_menu(window, background, bg_image, button_list):
    for tile in background:
        window.blit(bg_image, tile)

    for btn in button_list:
        btn.draw(window)


    pygame.display.update()






#============================================================================
#                        COLLISION AND MOVEMENT
#============================================================================

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

    if keys[pygame.K_j]:
        player.shoot()


        
            
        
    

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()

        if obj and obj.name == "NME":
            player.make_hit()

        if obj and obj.name == "plasmorb":
            player.make_hit()

        if obj and obj.name == "door": #Conveyor belt R
            obj.open = True

        if obj and obj.name == "Conveyor belt L": 
            player.rect.x -= 2

        if obj and obj.name == "Conveyor belt R": 
            player.rect.x += 2





#============================================================================
#                               LEVELS
#============================================================================


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





def main2(window, LEVEL_CLEAR, LEVEL, lives):
    clock = pygame.time.Clock()
    background, bg_image = get_background("sky.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "NSMBWii Main Theme.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)

    shyguy2 = Enemy(820, 672, ENEMY_VEL, 16, 16)

    enemies = [shyguy, shyguy2]

    
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()

    goalpost = Goal(1550, HEIGHT - block_size - 128, 64, 64) #64 was first value
    fire.on()
    
    
    
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
               Block2(block_size * 15, HEIGHT - block_size * 3, block_size),fire, fire2, shyguy, shyguy2, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        handle_move(player, objects)
        shyguy.loop(FPS, ENEMY_VEL, objects)
        shyguy2.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()






def main3(window, LEVEL_CLEAR, LEVEL, lives):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Ruins V1.2.3.png")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "P4 I'll Face Myself Battle.mp3")
    pygame.mixer.music.play(1)
    

    block_size = 96

    player = Player(100, 100, 50, 50, lives)
    
    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)
    enemies = [shyguy]
    
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
        shyguy.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()



def main4(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Factory bg5 2.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)

    shyguy2 = Enemy(820, 672, ENEMY_VEL, 16, 16)

    enemies = [shyguy, shyguy2]

    
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()

    goalpost = Goal(1550, HEIGHT - block_size - 128, 64, 64) #64 was first value
    fire.on()
    
    
    
    floor = [Grass_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Grass_S(0, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 3, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 4, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 5, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 6, HEIGHT - block_size * 5, block_size),
               Factory_D2(block_size * 9, HEIGHT - block_size * 5, block_size),
               Factory_D(block_size * 10, HEIGHT - block_size * 5, block_size),
               Factory_S(block_size * 14, HEIGHT - block_size * 3, block_size),
               Ruins_D2(block_size * 15, HEIGHT - block_size * 3, block_size),
               Ruins_D(block_size * 15, HEIGHT - block_size * 3, block_size),
               Ruins_S(block_size * 15, HEIGHT - block_size * 3, block_size),fire, fire2, shyguy, shyguy2, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        handle_move(player, objects)
        shyguy.loop(FPS, ENEMY_VEL, objects)
        shyguy2.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()










#=================================================================================================
#                                   The Main Campaign
#=================================================================================================

#====================================WORLD 1================================================
def Grass_level1(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("grass bg6 2.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)

    shyguy2 = Enemy(820, 672, ENEMY_VEL, 16, 16)

    parashroom = Parashroom(1520, 415, ENEMY_VEL, 32, 50)

    parashroom2 = Parashroom(3550, 604, ENEMY_VEL, 32, 50)

    parashroom3 = Parashroom(4550, 356, ENEMY_VEL, 32, 50)

    parashroom4 = Parashroom(5625, 510, ENEMY_VEL, 32, 50)

    parashroom5 = Parashroom(6640, 604, ENEMY_VEL, 32, 50)

    

    twiggy = Air_Enemy(1990, 520, ENEMY_VEL, 40, 36)
    twiggy2 = Air_Enemy(2650, 572, ENEMY_VEL, 40, 36)
    twiggy3 = Air_Enemy(5235, 510, ENEMY_VEL, 40, 36)
    twiggy4 = Air_Enemy(7480, 590, ENEMY_VEL, 40, 36)
    twiggy5 = Air_Enemy(8160, 600, ENEMY_VEL, 40, 36)
    twiggy6 = Air_Enemy(8760, 530, ENEMY_VEL, 40, 36)

    enemies = [shyguy, shyguy2, parashroom, parashroom2, parashroom3, parashroom4, parashroom5, twiggy, twiggy2, twiggy3, twiggy4, twiggy5, twiggy6]

    
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()
    
    fire_lily = FireLily(815, HEIGHT - block_size - 222, 32, 64) #64 was first value
    fire_lily.on()
    lily_vine = Lily_Vine(815, HEIGHT - block_size - 55, 32, 31) # x positiom to be directly above vine is X is same, y +23

    fire_lily2 = FireLily(3125, HEIGHT - block_size - 188, 32, 64) #64 was first value
    fire_lily2.on()
    lily_vine2 = Lily_Vine(3125, HEIGHT - block_size - 60, 32, 31) # x positiom to be directly above vine is X is same, y +23

    fire_lily3 = FireLily(3850, HEIGHT - block_size - 222, 32, 64) #190 here first
    fire_lily3.on()
    lily_vine3 = Lily_Vine(3850, HEIGHT - block_size - 62, 32, 31) # x positiom to be directly above vine is X is same, y +23

    fire_lily4 = FireLily(6115, HEIGHT - block_size - 198, 32, 64) #64 was first value
    fire_lily4.on()
    lily_vine4 = Lily_Vine(6115, HEIGHT - block_size - 70, 32, 31) # x positiom to be directly above vine is X is same, y +23
    lily_vine4b = Lily_Vine(6115, HEIGHT - block_size - 10, 32, 31)
    lily_vine4c = Lily_Vine(6115, HEIGHT - block_size - -35, 32, 31)

    fire_lily5 = FireLily(7755, HEIGHT - block_size - 188, 32, 64) #64 was first value
    fire_lily5.on()
    lily_vine5 = Lily_Vine(7755, HEIGHT - block_size - 60, 32, 31) # x positiom to be directly above vine is X is same, y +23
    lily_vine5b = Lily_Vine(7755, HEIGHT - block_size - 3, 32, 31)
    lily_vine5c = Lily_Vine(7755, HEIGHT - block_size - -35, 32, 31)

    fire_lily6 = FireLily(8450, HEIGHT - block_size - 183, 32, 64) #64 was first value
    fire_lily6.on()
    lily_vine6 = Lily_Vine(8450, HEIGHT - block_size - 55, 32, 31) # x positiom to be directly above vine is X is same, y +23
    lily_vine6b = Lily_Vine(8450, HEIGHT - block_size - 22, 32, 31) # x positiom to be directly above vine is X is same, y +23
    lily_vine6c = Lily_Vine(8450, HEIGHT - block_size - -3, 32, 31) # x positiom to be directly above vine is X is same, y +23
    lily_vine6d = Lily_Vine(8450, HEIGHT - block_size - -35, 32, 31) # x positiom to be directly above vine is X is same, y +23


    goalpost = Goal(9600, HEIGHT - block_size - 128, 64, 64) #64 was first value
    bridge_seg = Bridge(4640, HEIGHT - block_size - 250, 32, 24) #64 was first value
    bridge_seg2 = Bridge(4576, HEIGHT - block_size - 250, 32, 24)
    bridge_seg3 = Bridge(4512, HEIGHT - block_size - 250, 32, 24) #each bride tile is 64
    bridge_seg4 = Bridge(4448, HEIGHT - block_size - 250, 32, 24)
    bridge_seg5 = Bridge(4384, HEIGHT - block_size - 250, 32, 24)
    bridge_seg6 = Bridge(4320, HEIGHT - block_size - 250, 32, 24)

    Pvine = Top_Vine(7014, HEIGHT - block_size - 14, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine = Long_Vine(7040, HEIGHT - block_size - -12, 18, 44) #-40 is the absolute minimum, -12 is for whole thing on screen
    
    Pvine2 = Top_Vine(7324, HEIGHT - block_size - 14, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine2 = Long_Vine(7350, HEIGHT - block_size - -12, 18, 44) #-40 is the absolute minimum, -12 is for whole thing on screen

    Pvine3 = Top_Vine(7624, HEIGHT - block_size - 55, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine3 = Long_Vine(7650, HEIGHT - block_size - 29, 18, 44) 
    Lvine3b = Long_Vine(7650, HEIGHT - block_size - -59, 18, 44) # difference in long vine length is 88

    Pvine4 = Top_Vine(7944, HEIGHT - block_size - 65, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine4 = Long_Vine(7970, HEIGHT - block_size - 39, 18, 44) 
    Lvine4b = Long_Vine(7970, HEIGHT - block_size - -49, 18, 44) # difference in long vine length is 88

    Pvine5 = Top_Vine(8304, HEIGHT - block_size - 65, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine5 = Long_Vine(8330, HEIGHT - block_size - 39, 18, 44) 
    Lvine5b = Long_Vine(8330, HEIGHT - block_size - -49, 18, 44) # difference in long vine length is 88

    Pvine6 = Top_Vine(8614, HEIGHT - block_size - 85, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine6 = Long_Vine(8640, HEIGHT - block_size - 59, 18, 44) 
    Lvine6b = Long_Vine(8640, HEIGHT - block_size - -29, 18, 44) # difference in long vine length is 88

    Pvine7 = Top_Vine(8910, HEIGHT - block_size - 20, 46, 13) # x positiom to be directly above vine is X-26, y +26
    Lvine7 = Long_Vine(8936, HEIGHT - block_size - -6, 18, 44) 
    Lvine7b = Long_Vine(8936, HEIGHT - block_size - -89, 18, 44) # difference in long vine length is 88
    
    
    
    
    
    floor = [Grass_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #Num1 = Xaxis, Num2 = Yaxis placement
    objects = [*floor, Grass_S(0, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 1, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 2, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 3, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 4, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 5, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 6, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 8, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 7, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 9, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 10, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 11, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 12, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 13, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 13, HEIGHT - block_size * 3, block_size),
               Grass_D(block_size * 14, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 14, HEIGHT - block_size * 3, block_size),
               Grass_D2(block_size * 15, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 15, HEIGHT - block_size * 3, block_size),
               Grass_D(block_size * 16, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 16, HEIGHT - block_size * 3, block_size),
               Grass_D2(block_size * 17, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 17, HEIGHT - block_size * 3, block_size),
               Grass_D2(block_size * 18, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 18, HEIGHT - block_size * 3, block_size),
               Grass_D(block_size * 19, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 19, HEIGHT - block_size * 3, block_size),
               Grass_D2(block_size * 22, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 22, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 23, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 23, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 24, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 24, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 25, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 25, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 26, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 26, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 29, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 29, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 30, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 30, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 31, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 31, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 32, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 33, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 34, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 35, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 36, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 37, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 38, HEIGHT - block_size * 1, block_size),
               Grass_D(block_size * 39, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 39, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 40, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 40, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 41, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 41, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 42, HEIGHT - block_size * 1, block_size),
               Grass_D(block_size * 42, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 42, HEIGHT - block_size * 3, block_size),
               Grass_S(block_size * 42, HEIGHT - block_size * 4, block_size),
               Grass_D(block_size * 43, HEIGHT - block_size * 1, block_size),
               Grass_D2(block_size * 43, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 43, HEIGHT - block_size * 3, block_size),
               Grass_S(block_size * 43, HEIGHT - block_size * 4, block_size),
               Grass_D(block_size * 44, HEIGHT - block_size * 1, block_size),
               Grass_D(block_size * 44, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 44, HEIGHT - block_size * 3, block_size),
               Grass_S(block_size * 44, HEIGHT - block_size * 4, block_size),
               Grass_D2(block_size * 49, HEIGHT - block_size * 1, block_size),
               Grass_D(block_size * 49, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 49, HEIGHT - block_size * 3, block_size),
               Grass_S(block_size * 49, HEIGHT - block_size * 4, block_size),
               Grass_D(block_size * 50, HEIGHT - block_size * 1, block_size),
               Grass_D2(block_size * 50, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 50, HEIGHT - block_size * 3, block_size),
               Grass_S(block_size * 50, HEIGHT - block_size * 4, block_size),
               Grass_D(block_size * 51, HEIGHT - block_size * 1, block_size),
               Grass_D(block_size * 51, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 51, HEIGHT - block_size * 3, block_size),
               Grass_S(block_size * 51, HEIGHT - block_size * 4, block_size),
               Grass_D(block_size * 52, HEIGHT - block_size * 1, block_size),
               Grass_D2(block_size * 52, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 52, HEIGHT - block_size * 3, block_size),
               Grass_D2(block_size * 53, HEIGHT - block_size * 1, block_size),
               Grass_D(block_size * 53, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 53, HEIGHT - block_size * 3, block_size),
               Grass_D(block_size * 56, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 56, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 57, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 57, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 58, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 58, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 59, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 59, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 60, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 60, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 61, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 61, HEIGHT - block_size * 2, block_size),
               Grass_D(block_size * 62, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 62, HEIGHT - block_size * 2, block_size),
               Grass_S(block_size * 66, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 67, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 68, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 69, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 70, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 95, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 96, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 97, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 98, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 99, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 100, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 101, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 102, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 103, HEIGHT - block_size * 1, block_size),
               Grass_S(block_size * 104, HEIGHT - block_size * 1, block_size),
               fire, fire2, fire_lily, fire_lily2, lily_vine2, fire_lily3, fire_lily4, lily_vine4, lily_vine4b, lily_vine4c, fire_lily5, lily_vine5,
               lily_vine5b, lily_vine5c, fire_lily6, lily_vine6, lily_vine6b, lily_vine6c, lily_vine6d, shyguy, shyguy2, twiggy, twiggy2, twiggy3, twiggy4, twiggy5, twiggy6,
               bridge_seg, bridge_seg2, bridge_seg3, bridge_seg4, bridge_seg5, bridge_seg6, Lvine, Pvine, Lvine2, Pvine2, Lvine3, parashroom, parashroom2, parashroom3,
               Lvine3b, Pvine3, Lvine4, Lvine4b, Pvine4, Lvine5, Lvine5b, Pvine5, Lvine6, Lvine6b, Pvine6, Lvine7, Lvine7, Pvine7, parashroom4, parashroom5, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        fire_lily.loop()
        fire_lily2.loop()
        fire_lily3.loop()
        fire_lily4.loop()
        fire_lily5.loop()
        fire_lily6.loop()
        handle_move(player, objects)
        shyguy.loop(FPS, ENEMY_VEL, objects)
        shyguy2.loop(FPS, ENEMY_VEL, objects)
        parashroom.loop(FPS, ENEMY_VEL, objects)
        parashroom2.loop(FPS, ENEMY_VEL, objects)
        parashroom3.loop(FPS, ENEMY_VEL, objects)
        parashroom4.loop(FPS, ENEMY_VEL, objects)
        parashroom5.loop(FPS, ENEMY_VEL, objects)
        twiggy.loop(FPS, ENEMY_VEL, objects)
        twiggy2.loop(FPS, ENEMY_VEL, objects)
        twiggy3.loop(FPS, ENEMY_VEL, objects)
        twiggy4.loop(FPS, ENEMY_VEL, objects)
        twiggy5.loop(FPS, ENEMY_VEL, objects)
        twiggy6.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)


        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()





#====================================WORLD 2================================================
def Cave_level1(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Rocks_bg5 2.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    ghost = mineghost(2600, 350, ENEMY_VEL, 32, 32)

    ghost2 = mineghost(3225, 450, ENEMY_VEL, 32, 32)

    ghost3 = mineghost(4300, 450, ENEMY_VEL, 32, 32)

    ghost4 = mineghost(5020, 350, ENEMY_VEL, 32, 32)

    ghost5 = mineghost(6520, 350, ENEMY_VEL, 32, 32)

    ghost6 = mineghost(7520, 450, ENEMY_VEL, 32, 32)

    enemies = [ghost, ghost2, ghost3, ghost4, ghost5, ghost6]


    spike = Stalagmite(1365, HEIGHT - block_size - 115, 48, 58) #64 was first value

    spike2 = Stalagmite(1680, HEIGHT - block_size - 115, 48, 58) 

    spike3 = Stalactite(1525, HEIGHT - block_size - 290, 48, 58)
    

    fplatform = float_plat(2080, HEIGHT - block_size - 115, 46, 52)#w=46, h=52

    fplatform2 = float_plat(5350, HEIGHT - block_size - 150, 46, 52)#w=46, h=52

    fplatform3 = float_plat(5690, HEIGHT - block_size - 130, 46, 52)#w=46, h=52

    fplatform4 = float_plat(6910, HEIGHT - block_size - 140, 46, 52)#w=46, h=52

    fplatform5 = float_plat(7150, HEIGHT - block_size - 130, 46, 52)#w=46, h=52

    fplatform6 = float_plat(8800, HEIGHT - block_size - 125, 46, 52)#w=46, h=52, 8450

    fplatform7 = float_plat(9120, HEIGHT - block_size - 135, 46, 52)#w=46, h=52

    fplatform8 = float_plat(9620, HEIGHT - block_size - 472, 46, 52)#w=46, h=52
    
    

    goalpost = Goal(9600, HEIGHT - block_size - 600, 64, 64) #64 was first value
    
    
    
    
    floor = [Cave_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Cave_D(0, HEIGHT - block_size * 2, block_size),
               Cave_D2(0, HEIGHT - block_size * 3, block_size),
               Cave_D(0, HEIGHT - block_size * 4, block_size),
               Cave_S(0, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 1, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 1, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 1, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 1, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 2, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 2, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 2, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 2, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 3, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 3, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 3, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 3, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 4, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 4, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 4, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 4, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 5, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 5, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 5, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 5, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 6, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 6, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 9, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 9, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 9, HEIGHT - block_size * 6, block_size),
               Cave_D2(block_size * 9, HEIGHT - block_size * 7, block_size),
               Cave_D(block_size * 9, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 9, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 10, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 10, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 10, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 10, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 10, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 10, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 11, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 11, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 11, HEIGHT - block_size * 6, block_size),
               Cave_D2(block_size * 11, HEIGHT - block_size * 7, block_size),
               Cave_D(block_size * 11, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 11, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 12, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 12, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 12, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 12, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 12, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 12, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 13, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 13, HEIGHT - block_size * 6, block_size),
               Cave_D2(block_size * 13, HEIGHT - block_size * 7, block_size),
               Cave_D(block_size * 13, HEIGHT - block_size * 8, block_size),
               Cave_D2(block_size * 13, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 14, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 14, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 14, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 14, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 14, HEIGHT - block_size * 9, block_size),
               Cave_D2(block_size * 15, HEIGHT - block_size * 5, block_size),
               Cave_D(block_size * 15, HEIGHT - block_size * 6, block_size),
               Cave_D2(block_size * 15, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 15, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 15, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 16, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 16, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 16, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 16, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 16, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 17, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 17, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 17, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 17, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 17, HEIGHT - block_size * 9, block_size),
               Cave_D2(block_size * 18, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 18, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 18, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 18, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 18, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 19, HEIGHT - block_size * 5, block_size),
               Cave_D2(block_size * 19, HEIGHT - block_size * 6, block_size),
               Cave_D(block_size * 19, HEIGHT - block_size * 7, block_size),
               Cave_D2(block_size * 19, HEIGHT - block_size * 8, block_size),
               Cave_D(block_size * 19, HEIGHT - block_size * 9, block_size),
               Cave_D(block_size * 24, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 24, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 24, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 24, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 25, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 25, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 25, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 25, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 26, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 26, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 26, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 26, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 27, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 27, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 27, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 27, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 28, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 28, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 28, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 28, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 29, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 29, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 29, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 29, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 30, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 30, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 30, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 30, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 31, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 31, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 31, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 32, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 32, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 32, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 33, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 33, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 33, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 34, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 34, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 34, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 35, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 35, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 35, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 39, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 39, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 40, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 40, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 41, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 41, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 42, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 42, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 43, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 43, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 43, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 44, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 44, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 44, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 45, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 45, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 45, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 46, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 46, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 46, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 49, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 49, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 49, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 49, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 50, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 50, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 50, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 50, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 51, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 51, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 51, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 51, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 52, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 52, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 52, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 52, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 53, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 53, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 53, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 53, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 62, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 62, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 62, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 63, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 63, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 63, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 64, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 64, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 64, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 65, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 65, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 65, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 66, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 66, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 66, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 67, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 67, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 67, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 67, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 68, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 68, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 68, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 68, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 69, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 69, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 69, HEIGHT - block_size * 3, block_size),
               Cave_S(block_size * 69, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 77, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 77, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 77, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 78, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 78, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 78, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 79, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 79, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 79, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 80, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 80, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 80, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 81, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 81, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 82, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 82, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 83, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 83, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 86, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 86, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 87, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 87, HEIGHT - block_size * 2, block_size),
               Cave_D(block_size * 89, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 89, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 89, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 90, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 90, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 90, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 97, HEIGHT - block_size * 1, block_size),
               Cave_D2(block_size * 97, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 97, HEIGHT - block_size * 3, block_size),
               Cave_D(block_size * 98, HEIGHT - block_size * 1, block_size),
               Cave_D(block_size * 98, HEIGHT - block_size * 2, block_size),
               Cave_S(block_size * 98, HEIGHT - block_size * 3, block_size),
               Cave_D2(block_size * 99, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 99, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 100, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 100, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 101, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 101, HEIGHT - block_size * 2, block_size),
               Cave_D2(block_size * 102, HEIGHT - block_size * 1, block_size),
               Cave_S(block_size * 102, HEIGHT - block_size * 2, block_size), ghost, ghost2, ghost3, ghost4,
               ghost5, ghost6, fplatform, fplatform2, fplatform3, fplatform4, fplatform5, fplatform6,
               fplatform7, fplatform8, goalpost, spike, spike2, spike3]


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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fplatform.loop(VEL, "down")
        fplatform2.loop(VEL, "idle")
        fplatform3.loop(VEL, "left")
        fplatform4.loop(VEL, "right")
        fplatform5.loop(VEL, "up")
        fplatform6.loop(VEL, "idle")
        fplatform7.loop(VEL, "right")
        fplatform8.loop(VEL, "idle")
        handle_move(player, objects)
        ghost.loop(FPS, ENEMY_VEL, objects)
        ghost2.loop(FPS, ENEMY_VEL, objects)
        ghost3.loop(FPS, ENEMY_VEL, objects)
        ghost4.loop(FPS, ENEMY_VEL, objects)
        ghost5.loop(FPS, ENEMY_VEL, objects)
        ghost6.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()




#====================================WORLD 3================================================
def Factory_level1A(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Factory bg5 2.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)
    
    

    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)

    shyguy2 = Enemy(820, 672, ENEMY_VEL, 16, 16)
    
    Robear = Robobear(820, 672, ENEMY_VEL, 36, 72)

    UFO = NyaFO(820, 672, ENEMY_VEL, 40, 37)

    enemies = [shyguy, shyguy2, Robear, UFO]

    fplatform = float_plat(2325, HEIGHT - block_size - 150, 46, 52)#w=46, h=52

    fplatform2 = float_plat(3450, HEIGHT - block_size - 150, 46, 52)#w=46, h=52

    fplatform3 = float_plat(3650, HEIGHT - block_size - 150, 46, 52)#w=46, h=52

    fplatform4 = float_plat(4450, HEIGHT - block_size - 185, 46, 52)#w=46, h=52


    orb = plasmorb(1620, HEIGHT - block_size - 250, 103, 30) #64 was first value

    orb2 = plasmorb(3290, HEIGHT - block_size - 60, 103, 30) #64 was first value

    orb3 = plasmorb(3500, HEIGHT - block_size - 60, 103, 30) #64 was first value

    orb4 = plasmorb(3710, HEIGHT - block_size - 60, 103, 30) #64 was first value
    

    
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()

    goalpost = Goal(5550, HEIGHT - block_size - 128, 64, 64) #64 was first value

    door = door_portal(5400, HEIGHT - block_size - 170, 35, 37)
    
    
    
    
    floor = [Factory_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Factory_S(0, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 1, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 2, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 3, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 4, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 5, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 6, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 7, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 8, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 9, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 10, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 11, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 11, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 12, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 12, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 13, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 13, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 14, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 14, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 15, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 15, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 16, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 16, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 17, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 17, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 18, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 18, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 19, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 19, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 20, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 20, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 20, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 21, HEIGHT - block_size * 1, block_size),
               Factory_D2(block_size * 21, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 21, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 27, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 27, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 27, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 28, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 28, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 28, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 29, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 29, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 29, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 30, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 30, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 31, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 31, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 32, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 32, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 33, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 33, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 34, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 35, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 36, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 37, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 38, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 39, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 40, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 41, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 41, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 42, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 42, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 43, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 43, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 44, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 44, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 49, HEIGHT - block_size * 1, block_size),
               Factory_D2(block_size * 49, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 49, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 49, HEIGHT - block_size * 4, block_size),
               Factory_D2(block_size * 50, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 50, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 50, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 50, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 51, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 51, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 51, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 51, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 52, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 52, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 52, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 52, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 53, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 53, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 54, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 54, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 55, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 55, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 56, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 56, HEIGHT - block_size * 2, block_size),fire, fire2, orb, orb2, orb3, orb4,
               fplatform, fplatform2, fplatform3, fplatform4, shyguy, shyguy2, Robear, UFO, goalpost, door]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        orb.loop()
        orb2.loop()
        orb3.loop()
        orb4.loop()
        fplatform.loop(VEL, "right")
        fplatform2.loop(VEL, "left")
        fplatform3.loop(VEL, "right")
        fplatform4.loop(VEL, "up")
        door.loop()
        handle_move(player, objects)
        shyguy.loop(FPS, ENEMY_VEL, objects)
        shyguy2.loop(FPS, ENEMY_VEL, objects)
        Robear.loop(FPS, ENEMY_VEL, objects)
        UFO.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR


        

        if door.open == True:
            cooldowner = 5
            while cooldowner != 0:
                print("pee pee")
                cooldowner -= 1

                if cooldowner == 0:
                    Factory_level1B(window, LEVEL_CLEAR, LEVEL, lives)
            





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()




def Factory_level1B(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Factory bg5 2.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    

    Robear = Robobear(1100, 365, ENEMY_VEL, 36, 72)

    Robear2 = Robobear(4280, 365, ENEMY_VEL, 36, 72)

    UFO = NyaFO(2500, 350, ENEMY_VEL, 40, 37)
    
    enemies = [Robear, Robear2, UFO]
    

    fplatform = float_plat(4550, HEIGHT - block_size - 150, 46, 52)#w=46, h=52

    fplatform2 = float_plat(5550, HEIGHT - block_size - 472, 46, 52)


    conveyoR = RightConveyor(2690, HEIGHT - block_size - 40, 64, 30)# w64, h30

    conveyoR2 = RightConveyor(2814, HEIGHT - block_size - 40, 64, 30)

    conveyoR3 = RightConveyor(2938, HEIGHT - block_size - 40, 64, 30)

    conveyoR4 = RightConveyor(3062, HEIGHT - block_size - 40, 64, 30)

    conveyoR5 = RightConveyor(3188, HEIGHT - block_size - 40, 64, 30)

    conveyoL = LeftConveyor(1185, HEIGHT - block_size - 234, 64, 30) # w64, h30

    conveyoL2 = LeftConveyor(1310, HEIGHT - block_size - 234, 64, 30)

    conveyoL3 = LeftConveyor(3805, HEIGHT - block_size - 138, 64, 30)


    
    

    goalpost = Goal(5532, HEIGHT - block_size - 600, 64, 64) #64 was first value

    
    
    
    floor = [Factory_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Factory_S(0, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 1, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 2, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 3, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 4, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 5, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 6, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 7, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 8, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 8, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 9, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 9, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 10, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 10, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 11, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 11, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 12, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 12, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 13, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 13, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 14, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 14, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 15, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 15, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 15, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 16, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 16, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 16, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 17, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 17, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 17, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 18, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 18, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 18, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 19, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 19, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 19, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 20, HEIGHT - block_size * 1, block_size),
               Factory_D2(block_size * 20, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 20, HEIGHT - block_size * 3, block_size),
               Factory_S(block_size * 20, HEIGHT - block_size * 4, block_size),
               Factory_D(block_size * 24, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 24, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 25, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 25, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 26, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 26, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 27, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 27, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 28, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 29, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 30, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 31, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 32, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 33, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 37, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 37, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 38, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 38, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 39, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 39, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 40, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 40, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 41, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 41, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 41, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 42, HEIGHT - block_size * 1, block_size),
               Factory_D2(block_size * 42, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 42, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 43, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 43, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 43, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 44, HEIGHT - block_size * 1, block_size),
               Factory_D(block_size * 44, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 44, HEIGHT - block_size * 3, block_size),
               Factory_D(block_size * 45, HEIGHT - block_size * 1, block_size),
               Factory_D2(block_size * 45, HEIGHT - block_size * 2, block_size),
               Factory_S(block_size * 45, HEIGHT - block_size * 3, block_size),
               Factory_D2(block_size * 51, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 51, HEIGHT - block_size * 2, block_size),
               Factory_D2(block_size * 52, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 52, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 53, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 53, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 54, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 54, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 55, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 55, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 56, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 56, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 57, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 57, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 58, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 58, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 59, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 59, HEIGHT - block_size * 2, block_size),
               Factory_D(block_size * 60, HEIGHT - block_size * 1, block_size),
               Factory_S(block_size * 60, HEIGHT - block_size * 2, block_size), fplatform, fplatform2, conveyoR, conveyoR2,
               conveyoR3, conveyoR4, conveyoR5, conveyoL, conveyoL2, conveyoL3, Robear, Robear2, UFO, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fplatform.loop(VEL, "right")
        fplatform2.loop(VEL, "idle")
        conveyoR.loop()
        conveyoR2.loop()
        conveyoR3.loop()
        conveyoR4.loop()
        conveyoR5.loop()
        conveyoL.loop()
        conveyoL2.loop()
        conveyoL3.loop()
        handle_move(player, objects)
        Robear.loop(FPS, ENEMY_VEL, objects)
        Robear2.loop(FPS, ENEMY_VEL, objects)
        UFO.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()





#====================================WORLD 4================================================
def Ruins_level1A(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Ruins V1.2.3.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)

    shyguy2 = Enemy(820, 672, ENEMY_VEL, 16, 16)
    
    enemies = [shyguy, shyguy2]

    
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()

    goalpost = Goal(8000, HEIGHT - block_size - 128, 64, 64) #64 was first value
    
    door = door_portal(1800, HEIGHT - block_size - 170, 35, 37)
    
    
    
    
    floor = [Ruins_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Ruins_S(0, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 1, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 2, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 3, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 4, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 5, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 6, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 7, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 8, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 9, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 10, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 11, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 12, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 13, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 14, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 15, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 16, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 17, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 18, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 19, HEIGHT - block_size * 2, block_size),
               Ruins_D(block_size * 20, HEIGHT - block_size * 1, block_size),
               Ruins_S(block_size * 20, HEIGHT - block_size * 2, block_size),fire, fire2, shyguy, shyguy2, door, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        handle_move(player, objects)
        shyguy.loop(FPS, ENEMY_VEL, objects)
        shyguy2.loop(FPS, ENEMY_VEL, objects)
        door.loop()
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR


        if door.open == True:
            cooldowner = 5
            while cooldowner != 0:
                print("pee pee")
                cooldowner -= 1

                if cooldowner == 0:
                    Ruins_level1B(window, LEVEL_CLEAR, LEVEL, lives)





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()








def Ruins_level1B(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Ruins V1.2.3.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    
    enemies = []

    
    

    goalpost = Goal(8000, HEIGHT - block_size - 128, 64, 64) #64 was first value
    
    door = door_portal(1800, HEIGHT - block_size - 170, 35, 37)
    
    
    
    
    floor = [Ruins_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Ruins_S(0, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 1, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 2, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 3, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 4, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 5, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 6, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 7, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 8, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 9, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 10, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 11, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 12, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 13, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 14, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 15, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 16, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 17, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 18, HEIGHT - block_size * 2, block_size),
               Ruins_S(block_size * 19, HEIGHT - block_size * 2, block_size),
               Ruins_D(block_size * 20, HEIGHT - block_size * 1, block_size),
               Ruins_S(block_size * 20, HEIGHT - block_size * 2, block_size), door, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        
        handle_move(player, objects)
        
        door.loop()
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, enemies)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR


        if door.open == True:
            cooldowner = 5
            while cooldowner != 0:
                print("pee pee")
                cooldowner -= 1

                if cooldowner == 0:
                    Ruins_level1C(window, LEVEL_CLEAR, LEVEL, lives)





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()















            

                
            



        






                
           
    

#====================================WORLD 5================================================
def World5_level1(window, LEVEL_CLEAR, LEVEL, lives): #drawing test
    clock = pygame.time.Clock()
    background, bg_image = get_background("Factory bg5 2.png")
    #Background_music("")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MOBIL 1.mp3")
    pygame.mixer.music.play(1)
    
    
    
    block_size = 96

    player = Player(100, 100, 50, 50, lives)

    shyguy = Enemy(620, 672, ENEMY_VEL, 16, 16)

    shyguy2 = Enemy(820, 672, ENEMY_VEL, 16, 16)

    
    fire = Fire(115, HEIGHT - block_size - 123, 32, 64) #64 was first value
    fire.on()
    fire2 = Fire(415, HEIGHT - block_size - 410, 32, 64) #64 was first value
    fire2.on()

    goalpost = Goal(1550, HEIGHT - block_size - 128, 64, 64) #64 was first value
    fire.on()
    
    
    
    floor = [Grass_D(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)] #drawing level tiles test
    objects = [*floor, Grass_S(0, HEIGHT - block_size * 2, block_size),
               Grass_D2(block_size * 3, HEIGHT - block_size * 4, block_size),
               Cave_D2(block_size * 4, HEIGHT - block_size * 4, block_size),
               Cave_D(block_size * 5, HEIGHT - block_size * 4, block_size),
               Cave_S(block_size * 6, HEIGHT - block_size * 5, block_size),
               Factory_D2(block_size * 9, HEIGHT - block_size * 5, block_size),
               Factory_D(block_size * 10, HEIGHT - block_size * 5, block_size),
               Factory_S(block_size * 14, HEIGHT - block_size * 3, block_size),
               Ruins_D2(block_size * 15, HEIGHT - block_size * 3, block_size),
               Ruins_D(block_size * 15, HEIGHT - block_size * 3, block_size),
               Ruins_S(block_size * 15, HEIGHT - block_size * 3, block_size),fire, fire2, shyguy, shyguy2, goalpost]

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
                    Player_Sounds("p_jump")



        player.loop(FPS)
        #shyguy.loop(FPS, ENEMY_VEL)
        fire.loop()
        fire2.loop()
        handle_move(player, objects)
        shyguy.loop(FPS, ENEMY_VEL, objects)
        shyguy2.loop(FPS, ENEMY_VEL, objects)
        draw(window, background, bg_image, player, objects, offset_x, bullets)
        bullets.update(bullets, shyguy)
        bullets.draw(window, offset_x)

        
        

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
            

        if player.rect.y >= 1200:
            player.HP = 0




        if player.HP <= 0:
            pygame.mixer.music.pause()
            Player_Sounds("p_death")
            window.fill("black")
            pygame.display.flip() #steps: cut to black -> cooldown + "you died" -> retry subprogram -> back into level (start)

            if lives == 0:
                game_over()

            else:
                retry(1, lives) #level_number, lives

            #retry(1, lives)
            #game_over()
                
            return LEVEL_CLEAR





        if player.rect.x > goalpost.rect.x: #level complete stuff
            LEVEL_CLEAR = True

            if LEVEL_CLEAR == True:
                Player_Sounds("p_win")
                print("Wahoo!")
                #LEVEL += 1
                print("Level =", LEVEL)
                pygame.mixer.music.pause()

                return LEVEL, LEVEL_CLEAR



            

                
            



        

    pygame.quit()
    quit()


#=================================================================================================
#                                     Main Game Loop
#=================================================================================================


def MAIN_MENU():
    clock = pygame.time.Clock()
    background, bg_image = get_background("menu_bg_test.png")
    #Background_music("MOBIL")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "MKWii Main Menu.mp3")
    pygame.mixer.music.play(1)
    

    

    Start_BUTTON = Button("Start", 350, 200, 150, 100) #create button
    Title_BUTTON = Button("Title", 350, 500, 150, 100)
    
    button_list = [Start_BUTTON, Title_BUTTON] #add button instance here

    run = True

    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        MOUSE = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        for event in events:
            for btn in button_list:
                btn.handle_event(event) #deals with button actions for every button

            

        
        draw_menu(window, background, bg_image, button_list) #draws menu assets
        


    pygame.quit()
    quit()



def TITLE_SCREEN():
    clock = pygame.time.Clock()
    background, bg_image = get_background("menu_bg_test2.png")
    #Background_music("MOBIL")

    filename = ""

    song_path = os.path.join("Assets", "Sounds", "Level_Sounds", filename)

    pygame.mixer.music.load(song_path + "NSMBWii Title Theme.mp3")
    pygame.mixer.music.play(1)
    

    

    Test_BUTTON = Button("Test", 400, 400, 150, 100) #create button
    
    button_list = [Test_BUTTON] #add button instance here

    run = True

    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        MOUSE = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        for event in events:
            for btn in button_list:
                btn.handle_event(event) #deals with button actions for every button
                break
            break

            

            

        
        draw_menu(window, background, bg_image, button_list) #draws menu assets
        


    pygame.quit()
    quit()
            



def retry(stage, lives):
    clock = pygame.time.Clock()
    background, bg_image = get_background("you_died.png")
    #Background_music("MOBIL")

    
    level_num = stage
    #lives_rem = lives
    cooldown = 450

    button_list = [] #add button instance here
    draw_menu(window, background, bg_image, button_list) #draws menu assets
    
    lives -= 1

    if cooldown > 0:
        for x in range(cooldown):
            cooldown -= 1
            print("poopyman")
            
            if cooldown == 0:
                if level_num == 1:
                   main2(window, LEVEL_CLEAR, LEVEL, lives)

                elif level_num == 2:
                   main3(window, LEVEL_CLEAR, LEVEL, lives)

    #draw_menu(window, background, bg_image, button_list) #draws menu assets


def game_over():
    clock = pygame.time.Clock()
    background, bg_image = get_background("game_over.png")
    #Background_music("MOBIL")

    cooldown = 500

    button_list = [] #add button instance here


    draw_menu(window, background, bg_image, button_list) #draws menu assets

    if cooldown > 0:
        for x in range(cooldown):
            cooldown -= 1
            print("poopyman")

        #TITLE_SCREEN()
            exit()




def level_transition():
    clock = pygame.time.Clock()
    background, bg_image = get_background("level_transition.png")
    #Background_music("MOBIL")

    cooldown = 300

    button_list = [] #add button instance here


    draw_menu(window, background, bg_image, button_list) #draws menu assets

    while cooldown > 0:
        for x in range(cooldown):
            cooldown -= 1
            print("poopyman")

        break




    
    
    
    

    
        

    
        


    

#TITLE_SCREEN()    
#MAIN_MENU()
#main4(window, LEVEL_CLEAR, LEVEL, lives)
    
#Grass_level1(window, LEVEL_CLEAR, LEVEL, lives)
#Cave_level1(window, LEVEL_CLEAR, LEVEL, lives)
#Factory_level1B(window, LEVEL_CLEAR, LEVEL, lives)
Ruins_level1A(window, LEVEL_CLEAR, LEVEL, lives)

if LEVEL == 1:
    main2(window, LEVEL_CLEAR, LEVEL, lives)
    #if LEVEL_CLEAR == True:
    LEVEL_CLEAR = False
    #window.fill("black")
    #pygame.display.flip()
    level_transition()
    LEVEL += 1

    #elif LEVEL_CLEAR == False:
    #   retry = input("RETRY? ")
    #  if retry == "y":
    #     main2(window, LEVEL_CLEAR, LEVEL)

    #  else:
    #     exit()
        
        
    

if LEVEL == 2:
    main3(window, LEVEL_CLEAR, LEVEL, lives)
    LEVEL_CLEAR = False
    window.fill("black")
    pygame.display.flip()
    LEVEL += 1
    


#if __name__ == "__main__":
#    main2(window)
