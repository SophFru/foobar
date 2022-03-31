'''
The solution I submitted

Approach: Starting from the left of s, create a substring
on each iteration, add a letter from s to the substring
compare this substring to all possible slices of the same length in s
if the substring matches all slices and the slices collectivly exhaust s, 
    return the number of slices
if s is iterated through with no solution
    return 1, there is no solution
'''

def solution(s):
    sub = ''
    for letter in s:
        sub += letter
        sliceLength = len(sub)
        if len(s) % len(sub) == 0:
            numSlices = int(len(s) / len(sub))
            slices = [s[i * sliceLength:i * sliceLength + sliceLength] for i in range(numSlices)]
            matches = 0
            for cake in slices:
                if not cake == sub:
                    break
                matches += 1
            if matches == numSlices:
                return numSlices
    return 1 #failure