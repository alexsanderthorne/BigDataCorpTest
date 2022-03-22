def PalindromicSubstring(strParam, j, k):
  
  count = 0

  while(j >= 0 and k < len(strParam)):
    if strParam[j] != strParam[k]:
      break
    print(strParam[j: k + 1])
    count += 1

    j -= 1
    k += 1
  
  return count

def find(strParam):
  count = 0
  for i in range(0, len(strParam)):
    count += PalindromicSubstring(strParam, i - 1, i + 1)
    count += PalindromicSubstring(strParam, i, i + 1)

  return count

print(find(input()))


