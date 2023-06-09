#!/usr/bin/python3

# Link - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # If input array is empty immediately return empty answer
        
        if len(digits) == 0:
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return #Backtrack
            
            # Get the letters that the current digit maps t, and loop through them
            possible_letters = letters[digits[index]]
            
            for letter in possible_letters:
                
                # Add the letter to our current path
                path.append(letter)
                
                # Move on to the next digit
                backtrack(index+1, path)
                
                # Backtrack by removing the letter before moving on to the next
                path.pop()
                
        # Initiate backtracking with an empty path and starting index of 0
        
        combinations = []
        backtrack(0, [])
        return combinations
                
        