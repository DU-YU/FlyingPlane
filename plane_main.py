import pygame
from plane_sprites import *
import sys
sys.setrecursionlimit(1000000000)
class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        #1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        #3. 调用私有方法。精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = Background("./飞机大战素材/background.png")

        self.back_group = pygame.sprite.Group(bg1)



    def start_game(self):
        print("游戏开始...")

        while True:
            #1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2. 事件监听
            self.__event_handler()
            #3. 碰撞检测
            self.__check_collide()
            #4. 更新/绘制精灵组
            self.__update_sprites()
            #5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            #监听用户点击退出按钮
            if event.type == pygame.QUIT:
                #使用类名调用静态方法
                PlaneGame.__game_over()

    def __check_collide(self):
        pass
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()