# n=3, output: [[1,2,3],[8,9,4],[7,6,5]]

class Solution:
    def generateMatrix(self, n):
        x, y, count = 0, 0, 0
        for element in elements:
            struct[x][y] = element
            visited.add((x,y))
            x_next = x + dirct[count][0]
            y_next = y + dirct[count][1]
            if 0 <= x_next < n and 0 <= y_next < n and (x_next, y_next) not in visited:
                x, y = x_next, y_next
            else:
                count = (count+1)%4
                x, y =  x + dirct[count][0], y + dirct[count][1]

n = 5
struct = [[0 for k in range(n)] for k in range(n)]
elements = [i + 1 for i in range(n*n)]

right = [0, 1]
dowm = [1, 0]
left = [0, -1]
up = [-1, 0]

dirct = [right, dowm, left, up]
visited = set()

myclass = Solution()
myclass.generateMatrix(n)
print (struct)

