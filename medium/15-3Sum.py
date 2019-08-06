nums = [-1,0,1,2,-1,-4,-2,-3,3]
#sorted: [-4, -3, -2, -1, -1, 0, 1, 2, 3]

def threeSum(nums):
  nums.sort()
  print('sorted:', nums)
  print('******************************************************')
  arr = []
  for i in range(len(nums)-1):
    diff = 0-nums[i]
    if nums[:i].count(nums[i])==0:
      helper(diff, nums[i+1:], arr)
    #print('arr:', arr)
    #print('=================================================')
  return arr
            
def helper(diff, sub_nums, arr):
  maximum = len(sub_nums)-1
  minimum = 0
  #print('diff:',diff)
  while (maximum > minimum):
    #print('sub_nums:', sub_nums, '  min:', minimum, '  max:', maximum)
    s = sub_nums[minimum]+sub_nums[maximum]
    if s==diff:
      tmp = [-1*diff, sub_nums[minimum], sub_nums[maximum]]
      if tmp not in arr:
        arr.append(tmp)
      minimum+=1
      maximum-=1
    elif s < diff:
      minimum+=1
    else:
      maximum-=1


print(threeSum(nums))
            
        
