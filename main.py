nums = 66699996666
nums = str(nums)
t =len(nums)
x = nums.find('6')
nums = nums[:x] + "9" + nums[x+1:]
print(nums)





