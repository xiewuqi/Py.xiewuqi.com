# -*- coding:UTF-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):        # 定义函数，print_all（f）
    print(f.read())
	
def rewind(f):           # 倒回
    f.seek(0)
	
def print_a_line(line_count, f):   # 传递行，阅读行
    print(line_count, f.readline())

current_file = open(input_file)   

print("First let's print the whole file:\n")

print_all(current_file)          # 阅读函数  

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)