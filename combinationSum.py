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



class Solution(object):
    def combinationSum(self, candidates, target):
        #edge Case
        if candidates == None or len(candidates) == 0:
            return []
        self.result = []
        self.backtrack(candidates,target,0,0,[])
        return self.result
    def backtrack(self,candidates,target,sums,index,temp):
        #Base Case
        if (sums == target):
            self.result.append(list(temp))
            return 
        if sums > target:
            return
        for i in range(index,len(candidates)):
            #action
            temp.append(candidates[i])
            #recurse
            self.backtrack(candidates,target,sums+candidates[i],i,temp)
            #backtrack
            temp.pop()
        
obj = Solution()
print(obj.combinationSum([2,3,6,7],7))
