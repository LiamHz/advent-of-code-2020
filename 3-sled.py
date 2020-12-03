# Challenge 1
# Moving right 3, down 1
# with the terrain repeating horizontally
# how many trees (#) will you hit?
with open('data/3.txt') as f:
  pos = 0
  nTrees = 0
  next(f) # Skip first row
  for r in f:
    # Using % (len(f)-1) causes pos to loop around
    pos = (pos + 3) % (len(r)-1)
    if r[pos] == '#':
      nTrees += 1

  print(nTrees)

# Challenge 2
# Get number of trees (#) collided with for each of
# the [dy, dx] slope pairs, and return their product
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
nTrees = [0] * len(slopes)

for i in range(len(slopes)):
  with open('data/3.txt') as f:
    pos = 0
    dy = slopes[i][1]
    next(f) # Skip first row
    for r in f:
      # Downward slope
      dy -= 1
      if dy > 0:
        continue
      if dy == 0:
        dy = slopes[i][1]

      # Using % (len(f)-1) causes pos to loop around
      pos = (pos + slopes[i][0]) % (len(r)-1)
      if r[pos] == '#':
        nTrees[i] += 1

prod = 1
for x in nTrees:
  prod *= x
print(prod)
