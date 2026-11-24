class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        n=len(s)
        for i in range(n):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    d=j-i-1
                    given_d=ord(s[i])-ord("a")
                    if d!=distance[given_d]:
                        return False
        return True
        