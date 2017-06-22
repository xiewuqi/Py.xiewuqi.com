# -*- coding:UTF-8 -*-
from sys import argv

script, filename = argv

print (f"We're going to erase {filenmae}")         # 我们去看 文件
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you want that, hit RETURN.")

input ("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")    # 我们去第几行

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write(line1)                                  # 将文件写入第一行 下面类推
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()
