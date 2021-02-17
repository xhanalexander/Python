import cv2
import sys
import math
import numpy
import emoji
import ctypes
from os import system       #(from) using namespace c++
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

system("title " + "Luas Segitiga")

def title():
    print("\n\t******** Luas Segitiga ********")

def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print('(+++)\t Hasil nilai tersebut adalah =', int(luas))

title()
print("")
x = int(input(">>\t Masukkan nilai Alas..."))
y = int(input(">>\t Masukkan nilai Tinggi..."))

luas_segitiga(x, y)
input("\n\t Click Anywhere to Continue...")
system('cls')