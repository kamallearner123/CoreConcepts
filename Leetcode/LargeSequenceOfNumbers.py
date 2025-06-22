

def get_largest_sequence(nums):
    sols = [1]*len(nums) # Memoization
    print(sols)

    for i in range(len(nums)-1,-1,-1):
        print(nums[i])
        
        maxi = sols[i]
        for j in range(i+1,len(nums)):
            print(" j = ", j)
            if nums[j]>nums[i]:
                if sols[j]+1>maxi:
                    maxi = sols[j]+1
                    sols[i] = maxi
        print(f" For index {i}, maxi is {sols[i]}")

get_largest_sequence([1,2,3,4,5,0,6,7,-1,4,2,11,20,12,21,21,21,22])
