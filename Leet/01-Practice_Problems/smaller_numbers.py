# 2. How Many Numbers Are Smaller Than the Current Number

'''
    1. Restate Problem
        - Given an array of integers, for each number within the array, state how many numbers within the array is smaller than then number.
    2. Ask Clarifying Questions
        - Are their any negative numbers?
        - Is this array sorted?
        - Is there any float numbers, i.e is there any numbers that contain a decimal?
        - Are there re-occuring numbers within the array?
        - How large or small is this array?
        - Can we state the number of items within the array that are smaller, or do I need to print all number smaller?
    3. State Assumptions
        - This array is already sorted
        - We can assume there is no negative numbers within this array
        - There can we multiples of the same number, which we will just return 0
        - The range of the numbers is 1 - 100
    4. Brainstorm Solution
        - We can record the number of the instances inside a dictionary if number has not appeared before, then return the corrseponding index
        - Count each number and sum their prefix and return 
    7. Discuss Tradeoffs
        - First solution will take time: 0(nlogn) with space complexity: O(1)
        - Second solution will take O(n) with space: O(1)
        - Both solutions will take about the same amount of space but the second solution will be quicker
    8. Suggest Improvements
'''

# Easier Solution: Using a dicitonary to record index
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {} # Created an empty dictionary
        for index, num in enumerate(sorted(nums)): # Creates a counter for nums and returns it as an object
            indices.setdefault(num, index) # setdefault sets the key as the index number from the dictionary object
        return [indices[num] for num in nums]

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        result = [] # creates an empty array
        temp_numbers = nums.copy() # creates a new copied set of the nums
        temp_numbers.sort() # Sorts the copied object set
        for i in temp_numbers: # for loop to sort through 
            result.append(temp_numbers.index(i))
        return result