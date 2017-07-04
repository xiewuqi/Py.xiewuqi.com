# -*- coding:utf-8 -*- 

def scan(stuff):
    sentence = []
    direcitons = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'bcak']
    verbs = ['go', 'stop', 'kill', 'eat']
    stops = ['the', 'in', 'of', 'form', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']
    numbers = [3, 91234 , 1234]
    errors = ['IAS', 'ASDFADFASDF']
    words = stuff.split()
    
for word in words:
        try:
            intword = int(word)
            sentence.append(('number',int(word)))
        except ValueError:
            if word in directions:
                sentence.append(('direction',word))
            elif word in verbs:
                sentence.append(('verb',word))
            elif word in stops:
                sentence.append(('stop',word))
            elif word in nouns:
                sentence.append(('noun',word))
            elif word in errors:
                sentence.append(('error',word))        
            else:
                sentence.append(('unkown',word))
    return sentence


print scan("go north")
print scan("kill the princess")
print scan("eat the bear")
print scan("open the door and smack the bear in the nose")
print scan("open 1234 door")   
   
"""
    def __init__(self, sentence,  ):
        pass
    
    def directions:
        
        
    def verbs:
        pass
        
    def stops:
        pass
    
    def nouns:
        pass
        
    def numbers:
        pass
        
    def errors:
        pass
        
        
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
"""