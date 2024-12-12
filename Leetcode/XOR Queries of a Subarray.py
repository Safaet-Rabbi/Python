class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        px=[0]*(len(arr)+1)
        a=[]
        for i in range(len(arr)):
            px[i+1]=px[i]^arr[i]
        for j in queries:
            a.append(px[j[1]+1]^px[j[0]])
        return a