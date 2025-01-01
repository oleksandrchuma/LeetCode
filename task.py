import sys
sys.stdin = open("input.txt")

import math

def distanceToRect(rect, p): 
  dx = max(rect[0][0] - p[0], 0, p[0] - rect[1][0])
  dy = max(rect[0][1] - p[1], 0, p[1] - rect[1][1])
  return math.sqrt(dx*dx + dy*dy)

def sumDistance(arr, index):
    return sum(arr[i] * 2 * abs(i - index) for i in range(len(arr)))

def isPrime(x):
    if (x <= 1):
        return False
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

import re
from datetime import datetime
import calendar
import sys 

def get_code(r, c):
    return chr(ord('a') + (ord(r) - ord('a') + ord(c) - ord('a')) % 26)

consonant_letters = set("bcdfghjklmnpqrstvwxyz")

def starts_with_consonant(word):
    return word.lower()[0] in consonant_letters

import math
while (True):
    try:    
        n = int(input())
        for i in range(n):
            joao = 0
            maria = 0
            for i in range(3):
                score, distance = map(int, input().split())
                joao += score * distance
            for i in range(3):
                score, distance = map(int, input().split())
                maria += score * distance
            if (joao > maria):
                print("JOAO")
            else:
                print("MARIA")        
        
    except EOFError:
        break

 
