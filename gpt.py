import sys
sys.stdin = open("input.txt")

def find_min_difference(N, assignments):
    total_difficulty = sum(assignments)
    half = total_difficulty // 2 + 1
    # Create a 2D list to store intermediate results for dynamic programming
    next = set()
    next.add(0)
    dp = set()

    for i in range(1, N + 1):
        dp |= next
        for v in dp:
            if v + assignments[i - 1] <= half:
                next.add(v+assignments[i-1]) 

    min_difference = total_difficulty
    for j in range(total_difficulty // 2, -1, -1):
        if j in next:
            min_difference = total_difficulty - 2 * j
            break

    return min_difference


while True:
    try:
        N = int(input())
        assignments = list(map(int, input().split()))

        min_difference = find_min_difference(N, assignments)
        print(min_difference)
    except EOFError:
        break
