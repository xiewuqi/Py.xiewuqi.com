# -*- coding: utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "What there's not 10 things in that list, let's fix  that." # 该列表中没有10件事情，我们来解决这个问题。

stuff = ten_things.split(' ') # 把ten_things 进行切片
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # 如果stuff列表等于10停止循环
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)  # len 显示列表位置

print "There we go: ", stuff

print "Let's do some things whit stuff."

print stuff[1]
print stuff[-2] # whoa!fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!  打开 ‘ ’ 里面的内容
print '#'.join(stuff[3:5]) # super stellar!  