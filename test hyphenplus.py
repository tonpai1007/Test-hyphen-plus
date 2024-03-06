#from pongpun teppanom
def cansum(nums,target):
    seen=set()
    for num in nums:
        complement = target-num
        if complement in seen:
            return True
        seen.add(num)
    return False

nums = list(map(int,input("enter number").split()))
target = int(input("enter target"))
print(cansum(nums,target))  
