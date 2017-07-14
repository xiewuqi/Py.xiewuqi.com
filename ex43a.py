
# coding:utf-8

from sys import exit   

# 0和1是退出代码。exit(0) 意味着干净的出口没有任何错误/问题.exit(1) 意味着有一些问题/错误/问题，这就是程序退出的原因。

from random import randint

def death():
    quips = ["你死了。你在这有点糟糕",
             "干得漂亮，你死了，愚蠢的人类",
             "失败者",
             "我有只小狗很擅长这个"
    ]
    print(quips[randint(0,len(quips)-1)])
    exit(1)


def central_corridor():
    print("来自Percal25号行星的哥顿人入侵并破坏了你的飞船")
    print("你的全体船员已经阵亡，你是最后的幸存者")
    print("任务是从武器库中拿到中子自毁炸弹")
    print("把它放在舰桥上，在你进入一个。。后炸毁飞船")
    print("逃生仓")
    print("\n")
    print("你正奔跑在中央走廊到武器库的路上")
    print("这时一个哥顿人跳出来，红皮肤，黑牙齿，邪恶的服装")
    print("怨恨充斥着他的身体，他正在挡在武器库的门外，好像正准备扔出炸弹炸死你")

    action = input("> ")

    if action == "shoot!":

        print("快速拔出你的枪并朝哥顿人开火")
        print("他灵活的移动让你失去了目标，你的激光枪击中了他的服装，这")
        print("让他整个燃烧起来")    
        print("这让他非常愤怒，不停的揍你的脸，直到")
        print("你死了，然后他吃了你")
        return "death"
    elif action == "dodge!":
        print("像一个世界级拳击手，你躲闪")
        print("哥顿人的枪射穿了你的头，然后把你吃了")
        return "death"
    elif action == "tell a joke":
        print("哥顿人喜欢听笑话")
        print("你给他讲了个非常搞笑的笑话，趁他不注意，你爆了他的头")
        print("穿过了武器库的门")    
        return "laser_weapon_armory"
    else:
        print("别想了")
        return 'central_corridor'

def laser_weapon_armory():
    print("你打了个洞进入武器库")
    print("这里死静死静的，好像埋伏着好多哥顿人")
    print("你发现了中子炸弹，但是它被密码锁锁着")
    print("你需要代码才能打开")
    print("如果输错10次，密码锁将永远锁着")
    print("提示：代码是3个数字")
    code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
    guess = raw_input("[keypad]> ")

    guesses = 0

    while guess != code and guesses < 10:
        print("BZZZZEDDD!")
        guesses += 1
        guess = raw_input("[keypad]> ")

    if guess == code:
        print("锁打开了，飘荡出白色的气体")
        print("你带着中子弹跑得越来越快")
        print("你必须把中子弹放在舰桥正确的位置")
        return "the_bridge"
    else:
        print("你最后一次听到了滴滴声")
        print("锁永久锁定了")
        print("你决定静静的坐着，最终哥顿人炸掉了飞船，你挂了")
        return "death"

def the_bridge():
    print("你带着中子弹突然出现在舰桥")
    print("惊动了5个哥顿人")
    print("他们正试图控制飞船，他们每个人都穿着一套丑陋的服装")
    print("他们还没有拿出武器，因为他们看到你手上正拿着一个已经启动的炸弹，他们不想看着它爆炸")

    action = raw_input("> ")
    if action == "throw the bomb":
        print("恐慌中，你把炸弹扔向了哥顿人")
        print("这时一个哥顿人从背后把你射杀，你倒地的时候看见一个哥顿人正在解除炸弹")


        return "death"

    elif action == "slowly place the bomb":
        print("你指着手中的炸弹，哥顿人被吓到了，他们举起手开始惊慌，")
        print("你慢慢地移动到门口，小心的把炸弹放到地上")
        print("你把门锁住，哥顿人出不来。炸弹放置好了，你跑向逃生仓")
        return "escape_pod"

    else:
        print("DOES NOT COMPUTE")
        return "the_bridge"


def escape_pod():
    print("你冲向逃生仓，争取整个船爆炸前，")
    print("似乎船上没有其他哥顿人，你一路很顺利")
    print("你来到逃生仓，这里有5个仓位，你要选择一个")
    print("你选择哪一个？")

    good_pod = randint(1, 5)
    guess = raw_input("[pod #]> ")


    if int(guess) != good_pod:
        print("你跳进 %s 号逃生仓，按下了弹出按钮" % guess)
        print("逃生仓发生了爆炸")
        print("你挂了")

        return "death"

    else:

        print("你跳进 %s 号逃生仓，按下了弹出按钮" % guess)
        print("你赢了")

        exit(0)

ROOMS = {
    'death':death,
    'central_corridor':central_corridor,
    'laser_weapon_armory':laser_weapon_armory,
    'the_bridge':the_bridge,
    'escape_pod':escape_pod
}



def runner(map, start):
    next = start
    while True:
        room = map[next]
        print("\n-----------")
        next = room()



runner(ROOMS, 'central_corridor')

'''
这个游戏其实是一个小版本的有限状态机FSM
wiki FSM
有限状态机（英语：finite-state machine，缩写：FSM）又称有限状态自动机，简称状态机，是表示有限个状态以及在这些状态之间的转移和动作等行为的数学模型。
'''
 