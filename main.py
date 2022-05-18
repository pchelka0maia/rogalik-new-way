import pgzrun
import random
import pygame
import sys
import os
import time

mod = sys.modules['__main__']

my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



cell = 50
size_w = len(my_map[0])
size_h = len(my_map)
WIDTH = cell * size_w
HEIGHT = cell * size_h
TITLE = "Roguelike"
FPS = 30

# Actors
cell = mod.Actor("border")
cell1 = mod.Actor("floor")
cell2 = mod.Actor("bones")
cell3 = mod.Actor("crack")
cell4 = mod.Actor("bones")
fireball1 = mod.Actor("fireball1", center=(900, 900))
fireball2 = mod.Actor("fireball2", center=(900, 900))
level_hod = mod.Actor("level_hod", topleft=(175, 150))
level1 = mod.Actor("level1", topleft=(-50, -50), anchor=('left', 'top'))
bomb = mod.Actor("bomb", topleft=(-50, -50), anchor=('left', 'top'))

# Дисплей атаки
at1 = mod.Actor("menu_at", topleft=(175, 150))
ded = mod.Actor("ded12", topleft=(175, 150))
at2 = mod.Actor("menu_at_z", topleft=(175, 150))

# Дисплей меню
menu = mod.Actor("menu1", topleft=(175, 150))


# Char

char = mod.Actor("stand1", topleft=(cell.width, cell.height), anchor=('left', 'top'))
char.health = 100
char.attack = 50
char.i = 1
char.j = 1

light = mod.Actor("light2", center=(75, 75))
 # Enemy
enemy12 = mod.Actor("enemy12", topleft=(100, 150)) # картинка enemy
# enemy = 0
# enemy1 = mod.Actor("enemy", topleft=(-100, -100))

# Переменные
mode = 'game'
money = 0
level = 1
prise = 0
q = 0
w = 0
w1 = True
e = 0
d = 0
d_r =0
# Списки
mobs = []
cells_mobs = []


enemies = []
def enemies_random(N):
    # Рандомим врагов
    global level
    a = 0
    if 1 <= level <= 5:
        for i in range(N):
            x = random.randint(1, len(my_map[0]) - 2)
            y = random.randint(1, len(my_map) - 2)

            if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                    x = random.randint(1, len(my_map[0]) - 2)
                    y = random.randint(1, len(my_map) - 2)
            a = random.randint(1, 3)
            if a == 1:
                enemy = mod.Actor('enemy_g1', topleft=(x * cell.width, y * cell.height))
                enemy.health = 50 # enemy.health = 50  # здоровье врага
                enemy.attack = 15 # enemy.attack = 15  # атака врага
                enemies.append(enemy)  # добавляем врага в список
            elif a == 2:
                enemy = mod.Actor('enemy_g2', topleft=(x * cell.width, y * cell.height))
                enemy.health = 100 # enemy.health = 50  # здоровье врага
                enemy.attack = 20 # enemy.attack = 15  # атака врага
                enemies.append(enemy)  # добавляем врага в список
            else:
                enemy = mod.Actor('enemy_g3', topleft=(x * cell.width, y * cell.height))
                enemy.health = 150 # enemy.health = 50  # здоровье врага
                enemy.attack = 10 # enemy.attack = 15  # атака врага
                enemies.append(enemy)  # добавляем врага в список
            mobs.append([y, x])  # добавляем координаты в список мобов

    if 6 <= level <= 7:
        for i in range(N):
            x = random.randint(1, len(my_map[0]) - 2)
            y = random.randint(1, len(my_map) - 2)

            if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                    x = random.randint(1, len(my_map[0]) - 2)
                    y = random.randint(1, len(my_map) - 2)
            a = random.randint(1, 3)
            if a == 1:
                enemy = mod.Actor('enemy_g1', topleft=(x * cell.width, y * cell.height))
                enemy.health = 75 # здоровье врага
                enemy.attack = 20 # атака врага
                enemies.append(enemy)  # добавляем врага в список
            elif a == 2:
                enemy = mod.Actor('enemy_g2', topleft=(x * cell.width, y * cell.height))
                enemy.health = 125 # здоровье врага
                enemy.attack = 25 # атака врага
                enemies.append(enemy)  # добавляем врага в список
            else:
                enemy = mod.Actor('enemy_g3', topleft=(x * cell.width, y * cell.height))
                enemy.health = 175 # здоровье врага
                enemy.attack = 15 # атака врага
                enemies.append(enemy)  # добавляем врага в список
            mobs.append([y, x])  # добавляем координаты в список мобов

    if 8 <= level <= 10:
        for i in range(N):
            x = random.randint(1, len(my_map[0]) - 2)
            y = random.randint(1, len(my_map) - 2)

            if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                    x = random.randint(1, len(my_map[0]) - 2)
                    y = random.randint(1, len(my_map) - 2)
            a = random.randint(1, 3)
            if a == 1:
                enemy = mod.Actor('enemy_g1', topleft=(x * cell.width, y * cell.height))
                enemy.health = 100 # здоровье врага
                enemy.attack = 25 # атака врага
                enemies.append(enemy)  # добавляем врага в список
            elif a == 2:
                enemy = mod.Actor('enemy_g2', topleft=(x * cell.width, y * cell.height))
                enemy.health = 150 # здоровье врага
                enemy.attack = 30 # атака врага
                enemies.append(enemy)  # добавляем врага в список
            else:
                enemy = mod.Actor('enemy_g3', topleft=(x * cell.width, y * cell.height))
                enemy.health = 200 # здоровье врага
                enemy.attack = 20 # атака врага
                enemies.append(enemy)  # добавляем врага в список
            mobs.append([y, x])  # добавляем координаты в список мобов

cells = []

def cell_random():
    for i in range(30):
        x = random.randint(1, len(my_map[0]) - 2)
        y = random.randint(1, len(my_map) - 2)

        if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
            while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                x = random.randint(1, len(my_map[0]) - 2)
                y = random.randint(1, len(my_map) - 2)
        cell0 = mod.Actor('border', topleft=(x * cell.width, y * cell.height))
        cells.append(cell0)
        cells_mobs.append([y, x])

bones = []

def bones_random(N):
    for i in range(N):
        x = random.randint(1, len(my_map[0]) - 2)
        y = random.randint(1, len(my_map) - 2)

        if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
            while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                x = random.randint(1, len(my_map[0]) - 2)
                y = random.randint(1, len(my_map) - 2)
        bone = mod.Actor('bones', topleft=(x * cell.width, y * cell.height))
        bones.append(bone)
        mobs.append([y, x])

cracks = []

def cracks_random(N):
    for i in range(N):
        x = random.randint(1, len(my_map[0]) - 2)
        y = random.randint(1, len(my_map) - 2)

        if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
            while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
                x = random.randint(1, len(my_map[0]) - 2)
                y = random.randint(1, len(my_map) - 2)
        crack = mod.Actor('crack', topleft=(x * cell.width, y * cell.height))
        cracks.append(crack)
        mobs.append([y, x])

def level_random():
    x = random.randint(1, len(my_map[0]) - 2)
    y = random.randint(1, len(my_map) - 2)

    if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
        while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs or [y, x] in cells_mobs:
            x = random.randint(1, len(my_map[0]) - 2)
            y = random.randint(1, len(my_map) - 2)
    level1.pos = (x * cell.width, y * cell.height)

def draw_map():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width * j
                cell.top = cell.height * i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width * j
                cell1.top = cell.height * i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width * j
                cell2.top = cell.height * i
                cell2.draw()
            elif my_map[i][j] == 3:
                cell3.left = cell.width * j
                cell3.top = cell.height * i
                cell3.draw()

def draw():
    global prise, money, d, level
    # screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    a = 0
    # Режим игры
    if mode == 'game':
        draw_map()

        for cell0 in cells:
            cell0.draw()

        for enemy in enemies:
            enemy.draw()

        for bone in bones:
            bone.draw()

        for crack in cracks:
            crack.draw()
        level1.draw()
        char.draw()
        bomb.draw()
        light.draw()

        mod.screen.draw.text('HP:' + str(char.health), topright=(cell.width * size_w - 5, 10), color='white',
                             fontsize=16)
        mod.screen.draw.text('AP:' + str(char.attack), topright=(cell.width * size_w - 5, 25), color='white',
                             fontsize=16)
        mod.screen.draw.text('Money:' + str(char.attack), topright=(cell.width * size_w - 5, 40), color='white',
                             fontsize=16)
        mod.screen.draw.text('Level:' + str(level), center=(375, 20), color='white', fontsize=16)

    elif mode == 'attack':
        enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке
        at1.draw()
        ded.draw()
        at2.draw()
        fireball1.draw()
        fireball2.draw()
        mod.screen.draw.text("Press Q to Back", topleft=(400, 460), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text("Press E to Attack", topleft=(200, 460), color="#8B0000", fontsize=25)
        mod.screen.draw.text(str(char.health), topleft=(175+290, 150+225), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text(str(char.attack), topleft=(175+290, 150+255), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text(str(enemies[enemy_index].health), topleft=(260, 150+225), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text(str(enemies[enemy_index].attack), topleft=(260, 150+255), color="#E0FFFF", fontsize=25)


    elif mode == "prise":
        # enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке
        if 1 <= level <= 3:
            prise = 15
            money = 30
        elif 4 <= level <= 5:
            prise = 20
            money = 50
        elif 6 <= level <= 7:
            prise = 25
            money = 75
        elif 8 <= level <= 10:
            prise = 40
            money = 100
        at1.draw()
        ded.draw()
        at2.draw()
        mod.screen.draw.text("Press E to Take a prise", topleft=(200, 460), color="#8B0000", fontsize=25)
        mod.screen.draw.text(str(char.health), topleft=(175+290, 150+225), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text(str(char.attack), topleft=(175+290, 150+255), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text('---', topleft=(260, 150+225), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text('---', topleft=(260, 150+255), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text("Prise:", topleft=(200, 200), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text("HP:", topleft=(200, 230), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text("Money:", topleft=(200, 260), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text(str(prise), topleft=(240, 230), color="#E0FFFF", fontsize=25)
        mod.screen.draw.text(str(money), topleft=(270, 260), color="#E0FFFF", fontsize=25)

    elif mode == 'level':
        level_hod.draw()
        mod.screen.draw.text("Press E for next Level", topleft=(200, 460), color="#8B0000", fontsize=25)
        mod.screen.draw.text("Next Level ?", topleft=(175+50, 150+50), color="#E0FFFF", fontsize=25)

    elif mode == "menu":
        menu.draw()

    if d == 1:
        if 1 <= level <= 3:
            if d_r == 1:
                mod.screen.draw.text("I'm feel good", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
            else:
                mod.screen.draw.text("Let's work", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 4 <= level <= 5:
            if d_r == 1:
                mod.screen.draw.text("Monsters...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
            else:
                mod.screen.draw.text("Scary... but I'm fine", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 6 <= level <= 7:
            if d_r == 1:
                mod.screen.draw.text("I have goosebumps...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
            elif d_r == 2:
                mod.screen.draw.text("I feel uneasy...", topleft=(char.x - 10, char.y - 20), color='white',
                                     fontsize=16)
            else:
                mod.screen.draw.text("Well...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 8 <= level <= 10:
            if d_r == 1:
                mod.screen.draw.text("I just wanna leave this place", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
            elif d_r == 2:
                mod.screen.draw.text("Too many bones...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
            elif d_r == 3:
                mod.screen.draw.text("I feel sick...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
            elif d_r == 4:
                mod.screen.draw.text("How many are there?..", topleft=(char.x - 10, char.y - 20), color='white',
                                     fontsize=16)
            else:
                mod.screen.draw.text("...", topleft=(char.x - 10, char.y - 20), color='white',
                                     fontsize=16)

    if d == 2:
        if 1 <= level <= 3:
            mod.screen.draw.text("The hatch I need", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 4 <= level <= 5:
            mod.screen.draw.text("Another hatch", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 6 <= level <= 7:
            mod.screen.draw.text("Jast go down", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 8 <= level <= 9:
            mod.screen.draw.text("Left a little", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        else:
            mod.screen.draw.text("The end", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)

    if d == 3:
        if 1 <= level <= 3:
            mod.screen.draw.text("It's someone bones", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 4 <= level <= 5:
            mod.screen.draw.text("It's monster's bones... Probably", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 6 <= level <= 7:
            mod.screen.draw.text("I think it isn't monster's...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 8 <= level <= 9:
            mod.screen.draw.text("Too many bones...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)

    if d == 4:
        if 1 <= level <= 3:
            mod.screen.draw.text("It's just a blot", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 4 <= level <= 5:
            mod.screen.draw.text("Okey. It isn't blot...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 6 <= level <= 7:
            mod.screen.draw.text("Looks like blood...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)
        elif 8 <= level <= 9:
            mod.screen.draw.text("...", topleft=(char.x - 10, char.y - 20), color='white', fontsize=16)


def on_key_down(key):
    global mode, enemy, i, j, level

    old_i = char.x
    old_j = char.y
    if mod.keyboard.o:
        mode = 'menu'
    # Полноэкранный режим
    if mod.keyboard.l:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif mod.keyboard.k:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))


    enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке

    if mod.keyboard.e and mode == 'prise':
        char.health += int(prise)
        light.draw()
        mode = 'game'  # ПЕРЕКЛЮЧАЛКА В ИГРУ

    if enemy_index != -1:# если есть пересечения хоть с одним из врагов 
        # Это делаем, если пересечения с врагами есть!
        mode = 'attack' # ПЕРЕКЛЮЧАЛКА В АТАКУ
        not light.draw()
        enemy = enemies[enemy_index] # в enemy сохраняем Actor врага

        if enemy.health <= 0 and mode == "attack": # Жизнь врага <0 ?
            enemies.pop(enemy_index) # удаляем его из списка по номеру
            mode = 'prise'

        if mod.keyboard.e and mode == 'attack':
            fireball1.pos=(475, 240)
            animate(fireball1, pos=(-30, 240), tween='decelerate', duration=2)
            enemy.health -= char.attack  # Уменьшаем здоровье врага
            fireball2.pos=(275, 240)
            animate(fireball2, pos=(800, 240), tween='decelerate', duration=2)
            char.health -= enemy.attack  # Уменьшаем свое здоровье


        if mod.keyboard.q and mode == 'attack':
            mode = "game"
            if char.image == char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
                char.x -= 10
                light.x -= 10               
            if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
                char.x += 10
                light.x += 10
            if char.image == 'up1' or char.image == 'up2':
                char.y += 10
                light.y += 10
            if char.image == 'down1' or char.image == 'down2':
                char.y -= 10
                light.y -= 10
            mode = 'game'

    # level mode

    if mod.keyboard.q and mode == 'level':
        mode = 'game'
        if char.image == char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
            char.x -= 10
            light.x -= 10
        if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
            char.x += 10
            light.x += 10
        if char.image == 'up1' or char.image == 'up2':
            char.y += 10
            light.y += 10
        if char.image == 'down1' or char.image == 'down2':
            char.y -= 10
            light.y -= 10

    if mod.keyboard.e and mode == 'level': # Переход на другой level
        level += 1

    # # bombs
    # if mod.keyboard.b and mode == 'game':
    #     if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
    #         bomb.draw()
    #         bomb.pos = (char.x, char.y)
    #         animate(bomb, pos=(char.x + 100, char.y), tween='linear', duration=2)
    #     if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
    #         bomb.draw()
    #         bomb.pos = (char.x, char.y)
    #         animate(bomb, pos=(char.x - 100, char.y), tween='linear', duration=2)
    #     if char.image == 'up1' or char.image == 'up2':
    #         bomb.draw()
    #         bomb.pos = (char.x, char.y)
    #         animate(bomb, pos=(char.x, char.y - 100), tween='linear', duration=2)
    #     if char.image == 'down1' or char.image == 'down2':
    #         bomb.draw()
    #         bomb.pos = (char.x, char.y)
    #         animate(bomb, pos=(char.x, char.y + 100), tween='linear', duration=2)


def update(dt):
    global q, cell0, cells_mobs, mode, d, d_r

    if char.collidelist(bones) != -1:
        d = 3

    if char.collidelist(cracks) != -1:
        d = 4
    # Проверяем пересечение с врагом, если да, то режим атаки
    if char.collidelist(enemies) != -1:
            mode = 'attack'
    if char.colliderect(level1):
            mode = 'level'

    if not mod.keyboard.d and not mod.keyboard.s and not mod.keyboard.a and not mod.keyboard.w:
        if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
            char.image = 'stand1'
        if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
            char.image = 'left3'
    if mod.keyboard.d and mode == 'game':
        d = 0
        if q == 0:
            char.image = "stand1"
            time.sleep(0.1)
            q += 1
        elif q == 1:
            char.image = 'right1'
            time.sleep(0.1)
            q += 1
        elif q == 2:
            char.image = 'right2'
            time.sleep(0.1)
            q -= 2
        
        char.x += 10
        light.x += 10
        
        if char.collidelist(cells) != -1:
            char.x -= 10
            light.x -= 10

        if char.x >= 700 - 50:
            char.x = 700 - 50
            light.x = 700 - 25

    if mod.keyboard.a and mode == 'game':
        d = 0
        if q == 0:
            char.image = "left1"
            time.sleep(0.1)
            q += 1
        elif q == 1:
            char.image = 'left2'
            time.sleep(0.1)
            q += 1
        elif q == 2:
            char.image = 'left3'
            time.sleep(0.1)
            q -= 2
        char.x -= 10
        light.x -= 10

        if char.collidelist(cells) != -1:
            char.x += 10
            light.x += 10

        if char.x <= 50:
            char.x = 50
            light.x = 75

    if mod.keyboard.w and mode == 'game':
        d = 0
        if q == 0:
            char.image = "up1"
            time.sleep(0.1)
            q += 1
        elif q == 1:
            char.image = 'up2'
            time.sleep(0.1)
            q += 1
        elif q == 2:
            char.image = 'up1'
            time.sleep(0.1)
            q -= 2

        char.y -= 10
        light.y -= 10

        if char.collidelist(cells) != -1:
            char.y += 10
            light.y += 10

        if char.y <= 50:
            char.y = 50
            light.y = 75

    if mod.keyboard.s and mode == 'game':
        d = 0
        if q == 0:
            char.image = "down1"
            time.sleep(0.1)
            q += 1
        elif q == 1:
            char.image = 'down2'
            time.sleep(0.1)
            q += 1
        elif q == 2:
            char.image = 'down1'
            time.sleep(0.1)
            q -= 2

        char.y += 10
        light.y += 10

        if char.collidelist(cells) != -1:
            char.y -= 10
            light.y -= 10

        if char.y >= 550 - 50:
            char.y = 550 - 50
            light.y = 550 - 25


    # Проверяем пересечение со стеной, если да, то уничтожаем стену
    if bomb.collidelist(cells) != -1:
        cells.pop(bomb.collidelist(cells))

    # bombs
    if mod.keyboard.b and mode == 'game':
        if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
            bomb.pos = (char.x, char.y)
            animate(bomb, pos=(char.x + 50, char.y), tween='linear', duration=0.5)


        if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
            bomb.pos = (char.x, char.y)
            animate(bomb, pos=(char.x - 50, char.y), tween='linear', duration=0.5)

        if char.image == 'up1' or char.image == 'up2':
            bomb.pos = (char.x, char.y)
            animate(bomb, pos=(char.x, char.y - 50), tween='linear', duration=0.5)

        if char.image == 'down1' or char.image == 'down2':
            bomb.pos = (char.x, char.y)
            animate(bomb, pos=(char.x, char.y + 50), tween='linear', duration=0.5)

def on_mouse_down(pos):
    global d, d_r
    if char.collidepoint(pos) and (1 <= level <= 5):
        d_r = random.randint(1, 2)
        d = 1
    if char.collidepoint(pos) and (6 <= level <= 7):
        d_r = random.randint(1, 3)
        d = 1
    if char.collidepoint(pos) and (8 <= level <= 10):
        d_r = random.randint(1, 8)
        d = 1
    if level1.collidepoint(pos):
        d = 2




if 1 <= level <= 3:
    enemies_random(5)
elif 4 <= level <= 5:
    enemies_random(8)
elif 6 <= level <= 7:
    enemies_random(8)
elif 8 <= level <= 10:
    enemies_random(10)

cell_random()

if 1 <= level <= 3:
    bones_random(1)
elif 4 <= level <= 5:
    bones_random(4)
elif 6 <= level <= 7:
    bones_random(5)
elif 8 <= level <= 10:
    bones_random(7)

if 1 <= level <= 3:
    cracks_random(2)
elif 4 <= level <= 5:
    cracks_random(3)
elif 6 <= level <= 7:
    cracks_random(4)
elif 8 <= level <= 10:
    cracks_random(6)

level_random()
pgzrun.go()