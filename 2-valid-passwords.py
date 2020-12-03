# Challenge 1
# Get the number of valid passwords
# Where key_char occurs between minN and maxN inclusive
with open('data/2.txt') as f:
  nValid = 0
  for x in f:
    password = x.split()[-1]
    key_char = x.split()[1][:-1]
    minN = int(x.split('-')[0])
    maxN = int(x.split('-')[1].split()[0])

    key_char_count = password.count(key_char)
    if key_char_count <= maxN and key_char_count >= minN:
      nValid += 1

  print(nValid)

# Challenge 2
# Get the number of valid passwords
# Where key_char occurs in index idx1 or idx2, but not both
with open('data/2.txt') as f:
  nValid = 0
  for x in f:
    password = x.split()[-1]
    key_char = x.split()[1][:-1]
    idx1 = int(x.split('-')[0])
    idx2 = int(x.split('-')[1].split()[0])

    # != is equivalent to xor
    if (password[idx1-1] == key_char) != (password[idx2-1] == key_char):
      nValid += 1

  print(nValid)
