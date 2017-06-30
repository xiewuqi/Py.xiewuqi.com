# -*- coding: uft-8 -*- 

# play a game
   
   
"""

你的 class 应该使用 “camel case（驼峰式大小写）”，
你的 __init__不应该做太多的事情，这会让 class 变得难以使用。
函数应该使用 “underscore format（下划线隔词）”，所以你可以写my_awesome_hair

"""
# 导入
from  sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        pass
        
# 引擎        
class Engine(object):

    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        
class Death(Scene):
    quips = ["你死了，大灰狼吃了你的脑浆",
             "如果她更聪明，你的妈妈会自豪",
             "这样一个垃圾",
             "我有一只小狗，比你做的还好。"
    ]

    def enter(self):
        print(Death.quips
        

# 小红帽家
class RedHoodHome(Scene):

    def enter(self):
        pass
# 森林      
class Forest(Scene):
    
    def enter(self):
        pass
# 外婆家
class ﻿GrandmotherHome(Scene):

    def enter(self):
        passH

# 卧室
class room(Scene):

    def enter(self):
        pass
        
# 地图     
class Map(object):
    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
        
a_map = Map('RedHoodHome')
a_game = Engine(a_map)
a_game.play()




