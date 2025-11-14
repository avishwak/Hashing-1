# Problem1: Group Anagrams (https://leetcode.com/problems/group-anagrams/)
# Time Complexity: O(N * KlogK) where N is the number of strings and K is the maximum length of a string in the list.
# Space Complexity: O(N) for the output list and the hashmap.   
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No
# 
# Your code here along with comments explaining your approach 
# 1. Create a hashmap to store the sorted string as key and list of anagrams as value. 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []

        groups = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
            
        return list(groups.values())
    
# Problem2: Group Anagrams (https://leetcode.com/problems/group-anagrams/)
# Time Complexity: O(N * K) where N is the number of strings and K is the maximum length of a string in the list.
# Space Complexity: O(N) for the output list and the hashmap.   
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No
# Your code here along with comments explaining your approach 
# 1. Create a hashmap to store the product of primes as key and list of anagrams as value. 
# 2. Each character is mapped to a prime number. The product of these primes will be unique for each set of anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _PRIMES = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
        ]

        groups = {}  # key: prime product, value: list of words
        for s in strs:
            prod = 1
            for ch in s:
                prod *= _PRIMES[ord(ch) - ord('a')]
            if prod in groups:
                groups[prod].append(s)
            else:
                groups[prod] = [s]
        return list(groups.values())