
"""!LEETCODE STARTED!
(offfline class)
question no.2169(count opration to obtain zero)
question no.9(palindrome)
question no. ?
(online class)
question no. 575(distribute candies)
question no.2273(remove Anagrams)
question no.389"""
##question 2357
"""
nums=[]
count=0
while True:
    minimum=float('inf')
    for num in nums:
        if num>0 and num<minimum:
            minimum=num

    if minimum==float('inf'):
        break
    for i in range(len(nums)):
        if nums[i]>0:
            nums[i]-=minimum
    count+=1
return count"""

"""#645
freq={}
ans=[]
nums=[1,2,2,4]
freq={}
for num in nums:
    freq[num]=freq.get(num,0)+1
for num,count in freq.items():
    if count==2:
        ans.append(num)
        break
n=len(nums)
for i in range(1,n+1):
##2nd approch
# class Solution:
#     def findErrorNums(self, nums: list[int]) -> list[int]:
#         count = 0
#         l2 = []
#         miss = 0
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 count += 1
#                 miss = nums[i] +1
#         if count > 0:
#             l2.append(nums[i])
#             l2.append(miss)
#             return l2 
##3rd approch
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         duplicate = 0
#         missing = 0

#         for i in range(1, len(nums) + 1):
#             if nums.count(i) == 2:
#                 duplicate = i
#             elif nums.count(i) == 0:
#                 missing = i
#         return [duplicate, missing]  """


"""frequency"""
# n=[1,2,2,3,3,4,4,5,5,5,5,6,7]
# freq={}
# for i in n:
#     freq[i]=freq.get(i,0)+1  #dictionary.get(key, default_value)
# print(freq)
#When a number appears for the first time, .get() returns 0.
#When it appears again, .get() returns its existing frequency.
#That's the entire logic!
# n=[1,2,3,3,4,4,5,5,5,6,6]
# freq={}
# for i in n:
#     freq[i]=freq.get(i,0)+1
# print(freq)

# n = [1, 2, 2, 3]
# freq = {}
# for i in n:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
# print(freq)

""""""