class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        
        for row in box:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '#':
                    row[j], row[empty] = row[empty], row[j]
                    empty -= 1
                elif row[j] == '*':
                    empty = j - 1
        
        return [[box[m - 1 - i][j] for i in range(m)] for j in range(n)]