import pgzrun
import sys
import random

mod = sys.modules['__main__']

my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 0],
          [0, 1, 2, 1, 0, 2, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 3, 1, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 0]
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

mobs = []

cell = 50
size_w = len(my_map[0])
size_h = len(my_map)
WIDTH = cell * size_w
HEIGHT = cell * size_h
TITLE = "Roguelike"
FPS = 30

cell = mod.Actor("border")
cell1 = mod.Actor("floor")
cell2 = mod.Actor("bones")
cell3 = mod.Actor("crack")

char = mod.Actor("stand", topleft=(cell.width, cell.height), anchor=('left', 'top'))
char.health = 100
char.attack = 25
char.i = 1
char.j = 1

# Рандомим врагов
enemies = []
for i in range(15):
    x = random.randint(1, len(my_map[0]) - 2)
    y = random.randint(1, len(my_map) - 2)

    if my_map[y][x] == 0 or [y, x] in mobs:
        while my_map[y][x] == 0 or [y, x] in mobs:
            x = random.randint(1, len(my_map[0]) - 2)
            y = random.randint(1, len(my_map) - 2)

    enemy = mod.Actor('enemy', topleft=(x * cell.width, y * cell.height))
    enemy.row = x  # х врага
    enemy.column = y  # y врага
    enemy.health = 50  # здоровье врага
    enemy.attack = 15  # атака врага
    enemies.append(enemy)  # добавляем врага в список

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


def draw():
    draw_map()
    for enemy in enemies:
        enemy.draw()
    mod.screen.draw.text('HP:' + str(char.health), center=(cell.width * size_w - cell.width / 2, 10), color='white',
                         fontsize=16)
    mod.screen.draw.text('AP:' + str(char.attack), center=(cell.width * size_w - cell.width / 2, 25), color='white',
                         fontsize=16)
    char.draw()


def on_key_down(key):
    old_i = char.i
    old_j = char.j

    if mod.keyboard.right:
        if my_map[char.i][char.j + 1] != 0:
            char.j += 1
        char.x = cell.width * char.j
        char.image = "stand"
    elif mod.keyboard.left:
        if my_map[char.i][char.j - 1] != 0:
            char.j -= 1
        char.x = cell.width * char.j
        char.image = "left"
    elif mod.keyboard.up:
        if my_map[char.i - 1][char.j] != 0:
            char.i -= 1
        char.y = cell.height * char.i
    elif mod.keyboard.down:
        if my_map[char.i + 1][char.j] != 0:
            char.i += 1
        char.y = cell.height * char.i

    enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке

    if enemy_index != -1:  # если есть пересечения хоть с одним из врагов
        char.i = old_i
        char.y = cell.height * char.i

        char.j = old_j
        char.x = cell.width * char.j

        enemy = enemies[enemy_index]  # в enemy сохраняем Actor врага
        enemy.health -= char.attack  # Уменьшаем здоровье врага
        char.health -= enemy.attack  # Уменьшаем свое здоровье
        if enemy.health <= 0:  # Жизнь врага <0 ?
            enemies.pop(enemy_index)  # удаляем его из списка по номеру


pgzrun.go()