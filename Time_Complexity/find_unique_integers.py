'''
2. Find N Unique Integers Sum up to Zero

Example 1:
    Input: n = 5
    Output: [-7,-1,1,3,4]
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4]

Example 2:
    Input: n = 3
    Output: [-1,0,1]

Example 3:
    Input: n = 1
    Output: [0]

Time Complexity: O(n)
'''
class Solution:
    def sumZero(self, n):
        result = []
        num = -n + 1
        for _ in range(n):
            result.append(num)
            num += 2
        return result

