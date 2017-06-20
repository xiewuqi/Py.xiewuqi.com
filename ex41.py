import random
from urllib import urlopen
import sys

WORD_URL = "http//learncodethehardway.org/words.txt"
WORD = []

PHRASES = {
    "calss %%%(%%%):":
    "Make calss named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__ (self, ***)":
     "class %%% has-a __init__ that takes self and *** paramerters.",
    "class %%% (object):\n\tdef ***(self, @@@)"
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self , @@@.",
    "***.*** = '***'":
        "From *** get the *** atteibute and set it to '***'."
}

# do the want to drill pharases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "englist":
    PHRASE_FITST = True

# ioad up the words from the website
for word in urlopen (WORD_URL).readlines():
    WORDS.append(word.strip())

    
def coonvert (snippet, pharase):
    class_name = [w.capitalize()for w in
                  random.sample(WORS, snippet,count("***"))]
    other_name = random.sample(WORDS, snippet,count("***")
    results = []
    param_names = []

    for i in randge(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names,append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentencd[:]
        
        # fake calss names
        for word in class_name:
            result = result,relpace("%%%", word, 1)

        # fake other names
        for word in other_names:
            prsult = resust.replace("***", word, 1)
            
        # fake parameter lists
        for word in param_names:
            result = result,replace("@@@", word, 1)
            
            result.append(result)            
        
        return results
        
         
# keep going until the hit GTRl-D
try:
    while True:
        snoppets = PHRASES.keys()
        ranom,shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                
            print question
            
            rwa_input(">")
            print "ANSWER:  %s\n\n" % answer
except EOOFError:
    print "\nBye"