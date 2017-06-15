# -*- coding:UTF-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count                      # sheeses  奶酪
    print "You have %d boxes of crackers!" % boxes_of_crackers       # crackers 饼干
    print "Man that's enough for a party!"                           # 人是足够的一个聚会！
    print "Get a blanket. \n"                                        # 得到一张毯子
	
	
print "We can just give the function numbers directly:"              # 我们可以直接给出函数数：
cheese_and_crackers(20, 30)
	
	
print "OR, we can use variables from ou script:"                     # OR，我们可以使用ou脚本中的变量
amount_of_cheese = 10
amount_of_crackers = 50
	
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
	
	
print "We can even do math inside too:"                              # 我们甚至可以在里面做数学：
cheese_and_crackers(10 + 20, 5 + 6)
	
	
print "And we can combine the two, variables and math:"              # 我们可以结合两个，变量和数学：
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  