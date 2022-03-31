# I used my notes on dynamic programming from my college algorithms course to solve this problem

def solution(l):
    if len(l) < 3:
        return 0
    count = 0
    doubles = [0 for i in range(len(l))]
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                doubles[i] += 1
                count += doubles[j]
    return count
