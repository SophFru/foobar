'''
    After submiting my solution, I realized I could make it a few lines shorter.
'''

def solution(s):
    slice_len = 0
    for i in range(int(len(s) / 2)):
        slice_len += 1
        if len(s) % slice_len == 0:
            num_slices = int(len(s) / slice_len)
            slices = [s[i * slice_len:i * slice_len + slice_len] for i in range(num_slices)]
            if s.count(slices[0]) == num_slices:
                return num_slices
    return 1 #failure