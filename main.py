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
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 4],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

mobs = []

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

# Дисплей атаки
at1 = mod.Actor("at1", topleft=(50, 100))
at_disp_1 = mod.Actor("at2", topleft=(80, 280))
at_disp_2 = mod.Actor("at2", topleft=(230, 280))
left3 = mod.Actor("left3", topleft=(250, 150)) # картинка chara


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
level = 1
q = 0

enemies = []
def enemies_random():
    # Рандомим врагов
    global level
    if (1 <= level) and (level <= 3):
        for i in range(5):
            x = random.randint(1, len(my_map[0]) - 2)
            y = random.randint(1, len(my_map) - 2)

            if (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs:
                while (x == 1 and y == 1) or my_map[y][x] == 0 or [y, x] in mobs:
                    x = random.randint(1, len(my_map[0]) - 2)
                    y = random.randint(1, len(my_map) - 2)

            enemy1 = mod.Actor('enemy', topleft=(x * cell.width, y * cell.height))
            # enemy1.row = x  # х врага
            # enemy1.column = y  # y врага
            enemy1.health = 50 # enemy.health = 50  # здоровье врага
            enemy1.attack = 15 # enemy.attack = 15  # атака врага
            enemies.append(enemy1)  # добавляем врага в список

            mobs.append([y, x])  # добавляем координаты в список мобов


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
            # # плита, через которую char должен переходить на другой level
            elif my_map[i][j] == 4:
                cell4.left = cell.width * j
                cell4.top = cell.height * i
                cell4.draw()

def draw():
    # Режим игры
    if mode == 'game':
        draw_map()

        for enemy in enemies:
            enemy.draw()
        mod.screen.draw.text('HP:' + str(char.health), center=(cell.width * size_w - cell.width / 2, 10), color='white',
                             fontsize=16)
        mod.screen.draw.text('AP:' + str(char.attack), center=(cell.width * size_w - cell.width / 2, 25), color='white',
                             fontsize=16)
        mod.screen.draw.text('Level:' + str(level), topleft=(10, 10), color='white', fontsize=16)
        char.draw()
        light.draw()
    elif mode == 'attack':
        enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке
        at1.draw()
        at_disp_1.draw()
        at_disp_2.draw()
        if (1 <= level) and (level <= 3): # от level'a будет зависеть отрисовка врагов на дисплее
            enemy12.draw()
        left3.draw()
        mod.screen.draw.text("Press Q to Back", topleft=(240, 320), color="white", fontsize=25)
        mod.screen.draw.text("Press E to Attack", topleft=(80, 320), color="red", fontsize=25)
        mod.screen.draw.text(str(char.health), topleft=(260, 280), color="white", fontsize=25)
        mod.screen.draw.text(str(char.attack), topleft=(330, 280), color="white", fontsize=25)
        mod.screen.draw.text(str(enemies[enemy_index].health), topleft=(110, 280), color="white", fontsize=25)
        mod.screen.draw.text(str(enemies[enemy_index].attack), topleft=(180, 280), color="white", fontsize=25)



def on_key_down(key):
    global mode, enemy, i, j, level

    old_i = char.i
    old_j = char.j

    # Полноэкранный режим
    # if key == keys.F:
    #     screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    # elif key == keys.W:
    #     screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))



    # if mod.keyboard.d and mode == 'game':
    #     if my_map[char.i][char.j + 1] != 0:
    #         char.j += 1
    #     char.x = cell.width * char.j
    #     char.image = "stand"
    # elif mod.keyboard.a and mode == 'game':
    #     if my_map[char.i][char.j - 1] != 0:
    #         char.j -= 1
    #     char.x = cell.width * char.j
    #     char.image = "left"
    # elif mod.keyboard.w and mode == 'game':
    #     if my_map[char.i - 1][char.j] != 0:
    #         char.i -= 1
    #     char.y = cell.height * char.i
    # elif mod.keyboard.s and mode == 'game':
    #     if my_map[char.i + 1][char.j] != 0:
    #         char.i += 1
    #     char.y = cell.height * char.i

    enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке

    if enemy_index != -1:  # если есть пересечения хоть с одним из врагов
        mode = 'attack' # ПЕРЕКЛЮЧАЛКА В АТАКУ
        not light.draw()
        enemy = enemies[enemy_index] # в enemy сохраняем Actor врага

        if enemy.health <= 0 and mode == "attack": # Жизнь врага <0 ?
            enemies.pop(enemy_index) # удаляем его из списка по номеру
            light.draw()
            mode = 'game' # ПЕРЕКЛЮЧАЛКА В ИГРУ

        if mod.keyboard.e and mode == 'attack':
            enemy.health -= char.attack  # Уменьшаем здоровье врага
            char.health -= enemy.attack  # Уменьшаем свое здоровье

        if mod.keyboard.q and mode == 'attack':
            if char.x + 100 != 700:
                char.x += 100
                light.x += 100
            else:
                char.x -= 100
                light.x -= 100
            mode = 'game'

    if mod.keyboard.e and enemies == []: # Переход на другой level
        level += 1
        draw_map()
        char.pos = cell.width, cell.height
        enemies_random()

def update(dt):
    global q
    if not mod.keyboard.d and not mod.keyboard.s and not mod.keyboard.a and not mod.keyboard.w:
        if char.image == 'stand1' or char.image == 'right1' or char.image == 'right2' or char.image == 'up1':
            char.image = 'stand1'
        else:
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
        char.x += 15
        light.x += 15
        if char.x >= 700 - 50:
            char.x = 700 - 75

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
        char.x -= 15
        light.x -= 15
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

        char.y -= 15
        light.y -= 15
        if char.y <= 50:
            char.y = 50
            light.y = 75

    if mod.keyboard.s and mode == 'game':
        if char.image == "stand1" or char.image == "right1" or char.image == "right2":
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
        else:
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
        char.y += 15
        light.y += 15
        if char.y >= 700 - 50:
            char.y = 700 - 50
            light.y = 700 - 75
enemies_random()
pgzrun.go()