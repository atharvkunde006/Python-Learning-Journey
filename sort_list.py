nums=[5,3,8,4,2]
for i in range(len(nums)):
    for j in range(0,len(nums)-i-1):
       if nums[j]>nums[j+1]:
           nums[i],nums[j+1]=[j+1],nums[j]
print(nums)