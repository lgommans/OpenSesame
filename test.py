#!/usr/bin/env python3

from open_sesame import OpenSesame
import os, time

f = open("/tmp/test", "wb")
f.write(b"One  two three 1 2 3\r\n4\r5\n6\n7\r\n8 \t\t29\na line with some words!\n")
f.write(b"asdfasdfasdfasdf " * (1000 * 1000))
f.close()
print('Wrote 16MB testdata')

f = OpenSesame("/tmp/test")
One_space = f.bytes(4)
two = f.readUntil([" "])
three = f.word()
_1 = f.int()
_2 = f.number()
_3 = f.string()
_4 = f.word()
_5 = f.word()
_6 = f.int()
_7 = f.int()
_8 = f.int()
_29 = f.int()
line = f.line()

#print(One_space, two, three, _1, _2, _3, _4, _5, _6, _7, _8, _29)

if One_space != b"One ":
    raise Exception()

if two != b"two":
    raise Exception()

if three != b"three":
    raise Exception()

if _1 != 1 or type(_1) != int:
    raise Exception()

if _2 != 2.0 or type(_2) != float:
    raise Exception()

if _3 != b"3":
    raise Exception()

if _4 != b"4":
    raise Exception()

if _5 != b"5":
    raise Exception()

if _6 != 6:
    raise Exception()

if _7 != 7:
    raise Exception()

if _8 != 8:
    raise Exception()

if _29 != 29:
    raise Exception()

if line != b"a line with some words!":
    raise Exception()

print("Passed tests")

print("Starting read benchmark")
t = time.time()
for i in range(0, 1000 * 1000):
    f.word()
tt = time.time() - t # time taken
print("Time to read 1 million words: {} seconds".format(round(tt * 100) / 100))
print("{} 000 words per second".format(round(1000 / tt)))

os.unlink('/tmp/test')

