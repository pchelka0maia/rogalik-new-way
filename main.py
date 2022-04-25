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
          [0, 1, 1, 1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

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

at1 = mod.Actor("at1", topleft=(50, 100))
at_disp_1 = mod.Actor("at2", topleft=(80, 280))
at_disp_2 = mod.Actor("at2", topleft=(230, 280))
en = mod.Actor("en", topleft=(100, 150))
ch = mod.Actor("ch", topleft=(250, 150))

# Char
char = mod.Actor("stand", topleft=(cell.width, cell.height), anchor=('left', 'top'))
char.health = 100
char.attack = 50
char.i = 1
char.j = 1

# Enemy
enemy = 0
enemy1 = mod.Actor("enemy", topleft=(-100, -100))

# Переменные
mode = 'game'
level = 1
a = 1
a1 = 15
a2 = 0
a3 = 0
health = 0


h = 1
h1 = 50
h2 = 0
h3 = 0

enemies = []
# Рандомим врагов
if level == 1:
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
    elif mode == 'attack':
        enemy_index = char.collidelist(enemies)  # Получаем номер врага в списке
        at1.draw()
        at_disp_1.draw()
        at_disp_2.draw()
        enemies[enemy_index].draw()
        ch.draw()
        mod.screen.draw.text("Press B to Back", topleft=(250, 300), color="white", fontsize=25)
        mod.screen.draw.text(str(char.health), topleft=(250, 280), color="white", fontsize=25)
        mod.screen.draw.text(str(char.attack), topleft=(320, 280), color="white", fontsize=25)
        mod.screen.draw.text(str(enemies[enemy_index].health), topleft=(100, 280), color="white", fontsize=25)
        mod.screen.draw.text(str(enemies[enemy_index].attack), topleft=(170, 280), color="white", fontsize=25)



def on_key_down(key):
    global mode, enemy, a, a1, a2, a3, h, h1, h2, h3

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
        mode = 'attack' # ПЕРЕКЛЮЧАЛКА В АТАКУ

        enemy = enemies[enemy_index] # в enemy сохраняем Actor врага

        if enemy.health <= 0 and mode == "attack":  # Жизнь врага <0 ?
            enemies.pop(enemy_index) # удаляем его из списка по номеру
            mode = 'game' # ПЕРЕКЛЮЧАЛКА В ИГРУ

        if mod.keyboard.x and mode=='attack':
            enemy.health -= char.attack  # Уменьшаем здоровье врага
            char.health -= enemy.attack  # Уменьшаем свое здоровье
        
        if mod.keyboard.b and mode == 'attack':
            mode = 'game'


pgzrun.go()