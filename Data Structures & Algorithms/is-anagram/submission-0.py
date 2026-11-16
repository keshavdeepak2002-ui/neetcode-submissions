class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track = dict()

        for char in s:
            track[char] = track.get(char, 0) + 1
        
        for char in t:
            if char not in track: # extra letter found in t, invalid
                return False
            
            track[char] -= 1

            if track[char] == 0:
                del track[char]
        
        if track: # extra letter(s) found in s, invalid
            return False
        
        return True