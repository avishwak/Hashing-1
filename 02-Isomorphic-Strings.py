# Problem2: Isomorphic Strings (https://leetcode.com/problems/isomorphic-strings/)
# Time Complexity: O(N) where N is the length of the strings.
# Space Complexity: O(1) under ASCII constraint
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No
# Your code here along with comments explaining your approach
# 1. Create a hashmap to store the mapping of characters from string s to string t.
# 2. Create a set to store the characters already mapped in string t.
# 3. Iterate through both strings simultaneously and check the mapping conditions.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tSet = set()
        for cs, ct in zip(s, t):
            if cs in sMap:
                if sMap[cs] != ct:
                    return False
            else: 
                if ct in tSet:
                    return False

            sMap[cs] = ct
            tSet.add(ct)

        return True