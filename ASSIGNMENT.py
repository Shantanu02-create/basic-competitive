# write a program to check two strings are anagrams or not using loop:
# s1=input("Enter first string: ")
# s2=input("Enter second string: ")
# s11=s1.split()
# s22=s2.split()
# if (len(s11)!=len(s22)) or s11.sort()!=s22.sort():
#     print("The strings are not anagrams.")
# else:
#     print("The strings are anagrams.")

# write a program to chaech if given string is palindrome or not using loop:
# s=input("Enter a string: ")
# reversed_s=""
# for i in range(len(s)-1,-1,-1):
#     reversed_s+=s[i]
# if s==reversed_s:
#     print("The string is a palindrome.")

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # No solution found