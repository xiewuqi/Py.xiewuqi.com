from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {script}, I'm the {user_name} script.")
print("I'd like do ask you a few questions.")
print(f"Do you like me {user_name} ?")
likes = input(prompt)

print(f"Where do you live {user_name}?") 
lives = input(prompt)

print("What kind of computer do you hvav?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""" )