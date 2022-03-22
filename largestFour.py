def LargestFour(arr):

  n = 4
  sum = 0

  arr.sort()
  
  print(arr[-n:])
  
  for i in range(len(arr)):
    sum = sum + arr[i]

  return sum

print(LargestFour(input()))