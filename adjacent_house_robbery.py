
def max_rub(nums):
    if (len(nums)==1):
        return nums[0]
    if(len(nums)==2):
        return max(nums[0], nums[1])
    if(len(nums)==3):
        return max(nums[0]+nums[2], nums[1])
    
def main_function(nums):
    temp_list = []
    prev_max = max_rub(nums[0:2])
    new_max = max_rub(nums[0:3])
    for i in range(3,len(nums)):
        temp_list.append(prev_max)
        temp_list.append(nums[i-1])
        temp_list.append(nums[i])
        prev_max = new_max
        new_max = max_rub(temp_list)
        temp_list = []
    return max(prev_max, new_max)



nums = [2,8,4,2,5,1]
print(main_function(nums))
