import pygame

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __int__(self, image_name, speed = 1):
        #调用父类的初始化方法
        super.__init__()
        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #在屏幕垂直方向移动
        self.rect.y += self.speed
