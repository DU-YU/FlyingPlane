import pygame
from plane_sprites import *
import sys
sys.setrecursionlimit(100000000)
pygame.init()

# 创建游戏窗口,480*700
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1 加载图像数据
bg = pygame.image.load("./飞机大战素材/background.png")

# 2 blit 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄飞机
hero = pygame.image.load("./飞机大战素材/hero.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 100, 68)

#创建敌机精灵
enemy = GameSprite("./飞机大战素材/img-plane_1.png")
#创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环 ->>>>>>意味着游戏的正式开始
while True:
    clock.tick(60)
    # 捕获事件,事件监听
    for event in pygame.event.get():

        # 判断游戏是否点击了退出按钮
        if event.type == pygame.QUIT:
            print("游戏退出。。。")
            #quit卸载所有模块
            pygame.quit()

            exit()
    # 2. 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 836

    # 3.调用blit方法绘制图像,先绘制游戏背景，这样每次绘制后会复制上一次的飞机，从而实现飞机的行动
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    #让精灵组调用2个方法
    #update.让组中所有的精灵更新位置
    enemy_group.update()

    #draw 在screen上绘制所有的精灵
    enemy_group.draw(screen)


    # 4. 调用update方法更新显示
    pygame.display.update()


pygame.quit()