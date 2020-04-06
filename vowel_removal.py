# 1. Remove Vowels From String

'''
    1. Restate Problem
        - Question is asking if given a string, remove all the vowels from that string 'a,e,i,o,u' and then return the string without the vowels
    2. Ask Clarifying Questions
        - How large is the string?
        - Is there other data types as well besides the string?
        - If there is multiple vowels within the string, do I remove all of them?
        - Will the string only contain just lowercase letters? All uppercase? A mixture of both?
    3. State Assumptions
        - Assume the string given is all lowercase letters
        - The given string does not contain any other data types
        - For now I can assume the string is smaller than 1000 letters
        - Most likely an O(n) solution, it doesn't seem that we need to have multiple for loops
    4. Brainstorm Solutions
        - Easiest way would be a for loop, and look for all occurrences of the vowels, then join the string after
        - Make a temp variable that holds the vowels, then push the vowels into the array once found
        - Replace all the vowels with an empty string. then return S
    5. Think Out Loud
        - Doesn't seem that we need to think about space complexity, this is more centered around how fast the code outputs a result
    6. Explain Rationale
    7. Discuss Tradeoffs
    8. Suggest Improvements

    Code Below!
'''



class Solution:
    # Brute Force, using replace() function
    def removeVowels(self, S: str) -> str:
        '''
            Here I'm using the built-in replace function for a string, which will replace 
            all instances of vowels with an empty string one by one. This will be O(n)
        '''
        S = S.replace("e", "")
        S = S.replace("a", "")
        S = S.replace("i", "")
        S = S.replace("o", "")
        S = S.replace("u", "")
        return S
    
    # Easier solution, 
    def removeVowels2(self, S: str) -> str:
        '''
        Using an object to hold  and then checking if the string contains the vowels object
        '''
        vowel_set = set('aeiou') # Created a new set to hold the vowels
        string = "" # This will be used to hold the string without the vowels
        for character in S: # Created index named character to use in for loop
            if character not in vowel_set: # Checks if each string character is not in the vowel set
                string += character  # If not found, add this character to the string
            return string # returns the string
    

