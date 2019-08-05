nums = [-1,0,1,2,-1,-4,-2,-3,3]

def threeSum(nums):
  nums.sort()
  arr = []
  for i in range(len(nums)):
    diff = 0-nums[i]
    self.helper(diff, nums[i+1:], arr)
    print(arr,'============================')
            
def helper(self, diff, sub_nums, arr):
  maximum = len(sub_nums)-1
  minimum = 0
        
  while (maximum != minimum):
    print(sub_nums)
    print('min ', minimum)
    print('max ', maximum)
    s = sub_nums[minimum]+sub_nums[maximum]
    if s==diff:
      arr.append([-1*diff, sub_nums[minimum], sub_nums[maximum]])
      minimum+=1
      maximum-=1
    elif s < diff:
      minimum+=1
    else:
      maximum-=1
            
        
            
        
