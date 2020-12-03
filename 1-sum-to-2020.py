with open('data/1.txt') as f:
  nums = [int(l) for l in f]

# Challenge 1
# Find two numbers in the list that sum to 2020
# Return their product
for x in nums:
  if (2020-x) in nums:
    print(x*(2020-x))
    break

# Challenge 2
# Find three numbers in the list that sum to 2020
# Return their product
for x in nums:
  for y in nums:
    if (2020-x-y) in nums:
      print(x*y*(2020-x-y))
      break
