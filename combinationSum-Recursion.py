Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
        if candidates == None or len(candidates) == 0:
            return []
        self.result = []
        self.recurse(candidates, target , 0, 0, [])
        return self.result
        
    def recurse(self,candidates,target,sums,index,temp):
        if sums == target:
            self.result.append(temp)
            return
        if sums >target or index>=len(candidates)  :
            return
        #dnt choose
        self.recurse(candidates,target,sums,index+1,list(temp))
        temp.append(candidates[index])
        #choose
        self.recurse(candidates,target,sums+candidates[index],index,list(temp))
        
