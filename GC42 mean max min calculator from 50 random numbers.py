import random
nums = []
for x in range(50):
    nums.append(random.randint(0, 100))

def mean(list_):
    avg = sum(list_) / 50
    return avg

print(nums)

print("max is", max(nums))
print("min is", min(nums))
print("mean is", mean(nums))
