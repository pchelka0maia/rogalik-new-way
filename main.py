import pgzrun
import random
import pygame
import sys
import os
import time

mod = sys.modules['__main__']

my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
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
        cell0.health = 30
        cells.append(cell0)
        cells_mobs.append([y, x])

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
    global prise, money
    # screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    a = 0
    # Режим игры
    if mode == 'game':
        draw_map()

        for cell0 in cells:
            cell0.draw()

        for enemy in enemies:
            enemy.draw()
        level1.draw()
        char.draw()
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

    # cell0_index = char.collidelist(cells)
    # if cell0_index != -1:
    #     if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
    #             char.x -= 1
    #     elif char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
    #             char.x += 1
    #     elif char.image == 'up1' or char.image == 'up2':
    #             char.y += 1


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
            # if char.x + 100 != 700:
            #     char.x += 100
            #     light.x += 100
            # else:
            #     char.x -= 100
            #     light.x -= 100
            mode = 'game'

    # level mode
    if char.colliderect(level1):
        mode = 'level'
    if mod.keyboard.q and mode == 'level':
        mode = 'game'
        if char.image == char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
            char.x = level1.x - 80
            light.x = level1.x - 55
        if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
            char.x = level1.x + 25
            light.x = level1.x + 50
        if char.image == 'up1' or char.image == 'up2':
            char.y = level1.y + 25
            light.y = level1.y + 50
        if char.image == 'down1' or char.image == 'down2':
            char.y = level1.y - 80
            light.y = level1.y - 55

    if mod.keyboard.e and mode == 'level': # Переход на другой level
        level += 1



def update(dt):
    global q, cell0, cells_mobs, mode
    # cell0_index = char.collidelist(cells)
    # if cell0_index != -1:
    #     if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
    #             char.x -= 5
    #     elif char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
    #             char.x += 1
    #     elif char.image == 'up1' or char.image == 'up2':
    #             char.y += 1

    # Проверяем пересечение с врагом, если да, то режим атаки
    if char.collidelist(enemies) != -1:
            mode = 'attack'

    if not mod.keyboard.d and not mod.keyboard.s and not mod.keyboard.a and not mod.keyboard.w:
        if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2':
            char.image = 'stand1'
        if char.image == 'left1' or char.image == 'left2' or char.image == 'left3':
            char.image = 'left3'
    if mod.keyboard.d and mode == 'game':
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

if 1 <= level <= 3:
    enemies_random(5)
elif 4 <= level <= 5:
    enemies_random(8)
elif 6 <= level <= 7:
    enemies_random(8)
elif 8 <= level <= 10:
    enemies_random(10)
cell_random()
level_random()
pgzrun.go()