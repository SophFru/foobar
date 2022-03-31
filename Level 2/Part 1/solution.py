# I used insertion sort and preprocessing to solve this challenge

def solution(l):
    def compareVersions(key, other):
        k = key.split('.')
        o = other.split('.')
        #major
        if k[0] != o[0]:
            return int(k[0]) < int(o[0])
        else:
            #minor
            if not (len(k) >=2 and len(o) >=2):
                #checked first to avoid out of bounds exception
                return len(k) < len(o) 
            else:
                if k[1] != o[1]:
                    return int(k[1]) < int(o[1])
                else:
                    #revision
                    if not (len(k) >=3 and len(o) >=3):
                        return len(k) < len(o)
                    else:
                        return int(k[2]) < int(o[2])

    #insertion sort
    for i in range(1, len(l)):
        curr = l[i]
        j = i - 1
        while j>= 0 and compareVersions(curr, l[j]):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = curr

    return l