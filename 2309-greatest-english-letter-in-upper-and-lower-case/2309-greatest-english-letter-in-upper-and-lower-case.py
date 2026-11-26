class Solution:
    def greatestLetter(self, s: str) -> str:
        ans=""
        upper_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letter="abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            upper=upper_letter[i]
            lower=lower_letter[i]
            if upper in s and lower in s:
                if ans<upper:
                    ans=upper
        return ans        