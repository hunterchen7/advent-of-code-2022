f = open('day1_input.txt', 'r')
lines = f.readlines()

curr_max_sums = [0, 0, 0]
curr_sum = 0

for i in lines:
  if i == '\n':
    if curr_sum > min(curr_max_sums):
      curr_max_sums[0] = curr_sum
      curr_max_sums.sort()
    curr_sum = 0
  else:
    curr_sum += int(i.strip())

print(sum(curr_max_sums))  
