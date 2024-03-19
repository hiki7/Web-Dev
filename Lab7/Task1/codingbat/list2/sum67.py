def sum67(nums):
    sum_val = 0
    in_section = False
    
    for num in nums:
        if num == 6:
            in_section = True
            continue
        elif num == 7 and in_section:
            in_section = False
            continue
        elif not in_section:
            sum_val += num
            
    return sum_val
