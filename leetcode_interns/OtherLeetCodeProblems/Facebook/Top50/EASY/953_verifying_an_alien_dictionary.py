#!/usr/bin/python3

# https://leetcode.com/problems/verifying-an-alien-dictionary/



"""
Time Complexity - O(N^2)
Space Complexity - O(N)
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_map = {c:i for i,c in enumerate(order)}
        print(order_map)
        
        
        for i in range(len(words)-1):
            
            
            for j in range(len(words[i])):
                
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    
                    break
        return True