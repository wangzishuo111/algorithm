#[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]] shuchu:2
#wall = [[1],[1],[1]] shuchu:3
import sys

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
wall = [[1],[1],[1]]
height = len(wall)
width = sum(wall[0])

if width <=1:
    print('break')
    print height
    sys.exit()

gaps = []
for row in wall:
    gap = [0]*width
    for i in range(len(row)):
        gap[sum(row[:i])] = 1
    gap[0] = 0
    gaps.append(gap)

ret_list = [0]*width
for ele in gaps:
    for i in range(len(ele)):
        ret_list[i] = ret_list[i] + ele[i]
ret_list = ret_list[1:]

ret  = height - max(ret_list)
print ret
