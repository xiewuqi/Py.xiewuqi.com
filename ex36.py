# -*- coding: utf-8 -*-
from sys import exit

def deng_room():
    print("你碰见了灯神")
    print("他让你许一个愿望")
    
    next = input(">") 
    if next == "出口在哪":
        chukou_room()
        
        
    elif next == "给我一个美女":
        print("不在权限范围之内，886")
    else:
        print("好吧，你饿死在这个房间！")
        
def chukou_room():
    print('我送你到出口')
    print('----------')    
    print("你到了出口")

def kong_room():
    print("这个房间看起来空无一物")
    
def sitou_room():
    print("好吧，你掉了下去，摔了个稀巴烂。")

def dead(why):
    print(hy, "好可怜")
    
def start():
    print("""
> 哦，你不小心踩入了一个陷阱
······
许久，你从昏迷中醒来。
发现自己在一个幽暗的小屋，四周个有一扇门。
你准备去那扇门呢？ """)

    next = input(">")
    if next == "左边":
	    deng_room()
    elif next == "右边":
	    chukou_room()
    elif next == "上边":
        kong_room()
    elif next == "下边":
        sitou_room()  
    else:
	    dead("好吧，你饿死在这个房间！")



    
start()    
