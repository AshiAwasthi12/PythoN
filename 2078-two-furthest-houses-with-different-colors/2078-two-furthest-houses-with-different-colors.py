class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        ans=0
        n=len(colors)
        for i in range(n):
            for j in range(i+1,n):
                if colors[i]!=colors[j]:
                    distance=j-i
                    if distance>ans:
                        ans=distance
        return ans
        