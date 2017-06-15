# -*- coding:UTF-8 -*-

print "You enter a dark room with two doors. Do you ge through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eathing a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
	
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

# 附加练习，感觉脑洞好大		
elif door == "3":
    print "你来到一片森林，看到了一只小动物。"
    print "动物是什么呢？" 
    print "1. 猪"
    print "2. 狗"
    print "3. 鸡"
    
    dongwu = raw_input("> ")
    
    if dongwu == "1" or dongwu == "2":
        print " 恭喜你，错了"	
    else:
        print " (⊙o⊙)哦，对了"
	
	
else:
    print "You stumble around and fall on a knife and die. Good job!"