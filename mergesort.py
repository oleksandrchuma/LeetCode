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

def check_pattern(input_string):
    pattern = r'^[A-Z]{3}-\d{4}$'
    return re.match(pattern, input_string) is not None

def format_int(x):
    if (x >= 0):
        s = ('0'*10 + str(x))[-10:]
    else:
        s = '-' + ('0'*9 + str(abs(x)))[-9:]
    return s 
def sign(a):
    return "" if a >= 0 else "-"

from datetime import datetime
import math

# Merge two sorted sublists `A[low … mid]` and `A[mid+1 … high]`
def merge(A, aux, low, mid, high):
    global dic 
    k = i = low
    j = mid + 1
    inversionCount = 0
 
    # while there are elements in the left and right runs
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            for w in range(mid-i+1):
                inversionCount += dic[A[i+w]]
            inversionCount += (mid-i+1)*dic[A[j]]
            j = j + 1
            
        k = k + 1
 
    # copy remaining elements
    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
 
    ''' no need to copy the second half (since the remaining items
        are already in their correct position in the temporary array) '''
 
    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = aux[i]
 
    return inversionCount
 
 
# Sort list `A[low…high]` using auxiliary list `aux`
def mergesort(A, aux, low, high):
 
    # base case
    if high <= low:        # if run size <= 1
        return 0
 
    # find midpoint
    mid = low + ((high - low) >> 1)
    inversionCount = 0
 
    # recursively split runs into two halves until run size <= 1,
    # then merges them and return up the call chain
 
    inversionCount += mergesort(A, aux, low, mid)       # split/merge left half
    inversionCount += mergesort(A, aux, mid + 1, high)  # split/merge right half
    inversionCount += merge(A, aux, low, mid, high)     # merge the two half runs
 
    return inversionCount
 
while (True):
    try:
        n = int(input())
        A = [int(num) for num in input().split()]
        weight = [int(num) for num in input().split()]
        dic = dict()
        for i in range(n):
            dic[A[i]] = weight[i]
        aux = A.copy()
        print(mergesort(A, aux, 0, len(A) - 1))
    except EOFError:
        break

 
