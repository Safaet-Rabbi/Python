class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        mySet=set(allowed)
        for word in words:
            if set(word).issubset(mySet):
                count+=1
        return count
        