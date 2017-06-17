# -*- coding: utf-8 -*-
# create a mapping of state to abbreviation
states = {
     'Oregon': 'OR', # 俄勒冈州
     'Florida': 'FL', # 佛罗里达州
     'California': 'CA', # 加利福尼亚州
     'New York' : 'NY', # 纽约
     'Michigan': 'MI'   # 密歇根州 
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco', # 旧金山
    'MI': 'Detroit',  # 底特律
    'FL': 'Jacksonville' # 杰克逊维尔
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10 
print "NY state has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do ti by using the state then cities dict  嵌套式应用
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation  无序排列
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s " % (abbrev, city) 
    
# now do both at the same time  xxx.get('dx', 变量名)
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
