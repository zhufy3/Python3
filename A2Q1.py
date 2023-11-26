import sys
import math
import copy
import random

next_line, next_ctr, next_incr = 1, 1, 1

def incr_next_line():
    global next_line, next_ctr, next_incr
    next_line += next_incr
    next_ctr += 1
    if next_ctr == 10:
        next_incr *= 10
        next_ctr = 1

next_line, next_ctr, next_incr = 1, 1, 1

def incr_next_line():
    global next_line, next_ctr, next_incr
    next_line += next_incr
    next_ctr += 1
    if next_ctr == 10:
        next_incr *= 10
        next_ctr = 1

#----------------------------------------------------------------
# use randomized selection to quickly find the smallest index, with p=0 and r=len(A)-1
def randomized_partition(A,low,high):
    pivot_index = random.randint(low,high)
    pivot = A[pivot_index]
    A[high],A[pivot_index] = A[pivot_index],A[high]
    i = low-1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1
    

def randomized_select(A,low,high,i):
    if low==high:
        return A[high]
    mid = randomized_partition(A,low,high)
    k = mid-low+1
    if k==i:
        return A[mid]
    if i<k:
        return randomized_select(A,low,mid-1,i)
    else:
        return randomized_select(A,mid+1,high,i-k)
#----------------------------------------------------------------   
    

line_ctr = 0
count = [int(s) for s in sys.stdin.readline().split()]
n=len(count)
time = [math.floor(2400/i) for i in count]
def process(record):
    global time
    global count
    global line_ctr
    global n
    for i in range(1234):
        line_ctr += 1
        if line_ctr == next_line:
            min_time = randomized_select(copy.deepcopy(time),0,n-1,1)
#             min_time = min(time)
            idx = time.index(min_time)
            if int(record[1])> min_time:
                print(line_ctr, idx, min_time,count[idx])
                incr_next_line()
                time[idx]+=math.floor(2400/count[idx])
            min_time = randomized_select(copy.deepcopy(time),0,n-1,1)
#             min_time = min(time)
            if int(record[1])== min_time:
                record[1] = str(int(record[1])+1)
            elif int(record[1])< min_time:
                if (record[0] == 'check-in') and (len(record) == 4):
                    count[int(record[3])]+=int(record[2])
                elif record[0] == 'check-in':
                    count[int(record[3])]+=int(record[2])
                    count[int(record[4])]-=int(record[2])
                else:
                    count[int(record[3])]-=int(record[2])
                break

for line in sys.stdin.readlines():
    process(line.strip().split())
print('finally')
time_sorted = sorted([(r, i) for i, r in enumerate(time)], reverse = False)
for i in range(n):
    print(time_sorted[i][1],time_sorted[i][0],count[time_sorted[i][1]])
# print last update for all locations
