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

import sys
class Graph:
    def __init__(self, num_vertices):
        self.graph = {}
        for i in range(num_vertices):
            self.add_vertex(i)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = dict()

    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex in self.graph and end_vertex in self.graph:
            if end_vertex in self.graph[start_vertex]:
                self.graph[start_vertex][end_vertex] += weight
            else:
                self.graph[start_vertex][end_vertex] = weight

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []
        
    def get_shortest_way(self, start, end):
        #unvisited = set()
        #unvisited.update(i for i in range(len(self.graph)))

        bestway = [sys.maxsize]*(len(self.graph))
        bestway[start] = 0
        j = start
        #while (True):
        for j in range(len(self.graph)):
            for i, weight in self.get_neighbors(j).items():
                if (bestway[j] + weight < bestway[i]):
                    bestway[i] = bestway[j] + weight
        """
            unvisited.remove(j)
            if (j == end):
                break
            else: 
                j = min(unvisited, key=lambda x: bestway[x])
                if bestway[j] == sys.maxsize:
                    break
        """
        return bestway[end]

while True:
    try:    
        n = int(input())
        g = Graph(n*2 + 2)
        e1, e2 = map(int, input().split())

        g.add_edge(0, 1, e1)
        g.add_edge(0, 2, e2)
        up = [int(num) for num in input().split()]
        down = [int(num) for num in input().split()]
        g.add_edge(0, 1, up[0])
        g.add_edge(0, 2, down[0])

        for i in range(1,n):
            g.add_edge(i*2-1, i*2+1, up[i])
            g.add_edge(i*2, i*2+1, up[i])
            g.add_edge(i*2, i*2+2, down[i])
            g.add_edge(i*2-1, i*2+2, down[i])

        if (n > 1):
            odd = [int(num) for num in input().split()]
            even = [int(num) for num in input().split()]
            for i in range(n-1):
                g.add_edge(i*2 + 1, i*2 + 4, odd[i])
                g.add_edge(i*2 + 2, i*2 + 3, even[i])

        x1, x2 = map(int, input().split())
        g.add_edge(n*2-1, n*2+1, x1)
        g.add_edge(n*2, n*2+1, x2)

        print(g.get_shortest_way(0, n*2+1))
    except EOFError:
        break
    except Exception as e:
        print("An exception occurred:", str(e))
        break