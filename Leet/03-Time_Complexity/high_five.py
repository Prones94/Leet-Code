'''
1. High Five
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
    The average of the student with id = 1 is 87.
    The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

Time Complexity: O(2n + m + log n) --> O(n)
'''
class Solution(object):
    def highFive(self, items):
        grades = sorted(items, key=lambda x:x[1]) # sort by grades, sort is O(nlogn)
        student_grades = {}
        result = []
        for id_grade in grades: # O(n)
            student_grades[id_grade[0]] = student_grades.get(id_grade[0], []) + [id_grade[1]]
        for k,v in student_grades.items(): # O(m)
            average = int(sum(v[-5:])/5)
            result.append([k, average])
        return sorted(result, key=lambda x:x[0])

    