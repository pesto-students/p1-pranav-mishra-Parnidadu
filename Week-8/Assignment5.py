class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0]*(n+1)
        
        for trustee, trusted in trust:
            trust_count[trusted]+=1
            trust_count[trustee]-=1
            
        for person in range(1,n+1):
            if trust_count[person]==n-1:
                return person
        return -1
        