#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
# 
# Author: Matthew Dudley
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List = []
        for num in range(1, n+1):
            if ((num % 3 == 0) and (num % 5 == 0)):
                List.append("FizzBuzz")
            elif (num % 3 == 0):
                List.append("Fizz")
            elif (num % 5 == 0):
                List.append("Buzz")
            else:
                List.append(str(num))

        return List